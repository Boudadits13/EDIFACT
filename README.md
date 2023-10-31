### From Boudadi Abdelkader 

## Introduction

The Order Management and EDIFACT Generator is a web application that allows users to manage and view order data stored in a PostgreSQL database. Additionally, the application can generate EDIFACT messages for each order, making it a useful tool for businesses that need to exchange electronic data with trading partners.

## Features

- Display a list of all orders with relevant attributes.
- View specific order details, including order number, date, time, quantity, and total.
- Generate EDIFACT messages for individual orders.
- Seamless integration with a PostgreSQL database.
- Clean and user-friendly interface for easy navigation.

## Requirements

Before using this application, ensure you have the following requirements in place:

- Python 3.x
- Flask
- PostgreSQL
- `psycopg2` Python library (for connecting to the PostgreSQL database)
- Web browser

## Installation

- Clone the repository to your local machine.

`
Install the required Python packages.
pip install flask
pip install psycopg2
Set up a PostgreSQL database and import your data using a tool like pgAdmin.```
`
## Usage
- Run the Flask application.
`python app.py`
- Open a web browser and access http://localhost:5000/ to view a list of all orders.

- Click on a specific order to view its details.

To generate an EDIFACT message for an order, use the following URL format: `http://localhost:5000/{order_id}`. For example, `http://localhost:5000/1` generates the EDIFACT message for order 1.
## Configuration
- You can customize the application's configuration by modifying the appropriate settings in the `app.py` file.
Ensure that you configure the database connection and other parameters to match your environment.

## Database Setup
To set up the database:

-Create a PostgreSQL database.

-Import your data from an SQL file using a tool like pgAdmin.

-Configure the application to connect to your database by updating the db_config dictionary in main.py

## Routes and Endpoints
- `/:` Displays a list of all orders and their relevant attributes.
- `/bdd/{order_id}:` Displays detailed information about a specific order, including order number, date, time, quantity, and total.
- `/{order_id}:` Generates an EDIFACT message for the specified order.

## Generating EDIFACT Messages
- To generate an EDIFACT message for an order, access the URL `http://localhost:5000/{order_id}`.
- For example, `http://localhost:5000/1` generates the EDIFACT message for order 1.

## Contributing
- Contributions to this project are welcome. To contribute:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and submit a pull request.
