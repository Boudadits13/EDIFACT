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

1. Clone the repository to your local machine.

`
Install the required Python packages.
pip install flask
pip install psycopg2
Set up a PostgreSQL database and import your data using a tool like pgAdmin.```
`
`##Usage`

1.Run the Flask application.
python app.py
