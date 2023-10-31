from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Configure the PostgreSQL connection parameters
db_config = {
    "database": "TP3",
    "user": "postgres",
    "password": "root",
    "host": "localhost",
    "port": "5432"
}


def get_db_connection():
    return psycopg2.connect(**db_config)


def generate_edifact_order(order_number, items, date, time):
    edifact_message = f"""UNA:+.? '
UNB+UNOC:3+SenderID+ReceiverID+{date}:{time}+ReferenceNumber'
UNH+MessageReferenceNumber+ORDERS:D:96A:UN'
BGM+220+{order_number}+ORD'
DTM+137:{date}:102'
NAD+BY+BuyerName++++Country'
NAD+SE+SellerName++++Country'
"""
    for i, item in enumerate(items, start=1):
        item_number, ordered_quantity, item_description = item
        edifact_message += f"""LIN+{i}++{item_number}:GTIN'
IMD+A+{item_description}++Description'
QTY+21+{ordered_quantity}+EA'
"""
    edifact_message += """UNS+S'
UNT+12+MessageReferenceNumber'
UNZ+SequenceNumber'
"""
    return edifact_message

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM public."orderitem"')  # Fetch data from the "orderitem" table
        data = cursor.fetchall()
        conn.close()
        return render_template('Orderitem.html', data=data)
    except Exception as e:
        # Handle the error gracefully, e.g., log it
        return f"An error occurred: {str(e)}"


@app.route('/bdd/<int:order_id>')
def bdd_order(order_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"""SELECT "OrderNumber", DATE("OrderDate") AS "OrderDate", CAST("OrderDate" AS TIME) AS "time_part", "ProductId", "Quantity", "ProductName"
FROM public."order" AS a
INNER JOIN public."orderitem" AS b ON "a"."Id" = "b"."OrderId"
INNER JOIN public."product" As p ON "ProductId" = "p"."Id"
WHERE "a"."Id" = %s;
"""
        cursor.execute(query, (order_id,))  # Fetch data for the specified order ID
        data = cursor.fetchall()
        conn.close()
        return render_template('index.html', data=data)
    except Exception as e:
        # Handle the error gracefully, e.g., log it
        return f"An error occurred: {str(e)}"

@app.route('/<int:order_id>')
def afficherEdifact(order_id):
    data = []
    num_rows = 0
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """SELECT "OrderNumber",DATE("OrderDate") AS "OrderDate",CAST("OrderDate" AS TIME) AS "time_part","ProductId","Quantity","ProductName"
FROM public."order" AS a
INNER JOIN public."orderitem" AS b ON "a"."Id" = "b"."OrderId"
INNER JOIN public."product" As p ON "ProductId" = "p"."Id"
where "a"."Id" = %s;
"""
        cursor.execute(query, (order_id,))  # Fetch data for the specified order ID
        data = cursor.fetchall()
        num_rows = cursor.rowcount
        conn.close()
    except Exception as e:
        print(e)
        # Handle the error gracefully here

    if num_rows > 0:
        order_number = data[0][0]
        date = data[0][1]
        time = data[0][2]
        items = []
        for row in data:
            item = row[3], row[4], row[5]
            items.append(item)

        edifact_message = generate_edifact_order(order_number, items, date, time)
        return edifact_message
    else:
        return f"Order with ID {order_id} not found."
if __name__ == '__main__':
    app.run(debug=True)


