# Coffee Shop OOP Project

This is an object-oriented programming (OOP) project simulating a simple coffee shop ordering system using Python. It models the relationships between Customers, Coffees, and Orders.

## 📁 Project Structure

coffee_shop/
├── customer.py
├── coffee.py
├── order.py
├── Pipfile
├── Pipfile.lock
├── README.md

bash
Copy
Edit

## 📦 Setup and Installation

1. Clone the repository or create the directory:

```bash
mkdir coffee_shop
cd coffee_shop
Initialize a pipenv environment:

bash
Copy
Edit
pipenv install
pipenv shell
pipenv install pytest
🧱 Domain Model
Classes
Customer: Represents a customer with a name (1-15 characters).

Coffee: Represents a coffee type with a name (minimum 3 characters).

Order: Represents an order with a customer, coffee, and price (float between 1.0 and 10.0).

Relationships
A Customer can have many Orders.

A Coffee can have many Orders.

An Order links a Customer and a Coffee.

🛠 Features
Customer
.name - validated property

.orders() - list of the customer’s orders

.coffees() - unique list of coffees the customer has ordered

.create_order(coffee, price) - creates and adds an order

Customer.most_aficionado(coffee) - returns the customer who spent the most on a coffee

Coffee
.name - validated property

.orders() - list of all orders for the coffee

.customers() - unique list of customers who ordered it

.num_orders() - total number of times the coffee has been ordered

.average_price() - average price of the coffee based on orders

Order
.customer - the associated customer (validated)

.coffee - the associated coffee (validated)

.price - price of the order (float between 1.0 and 10.0)

Order.all() - list of all order instances