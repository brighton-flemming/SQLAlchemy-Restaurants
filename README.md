# SQLAlchemy-Restaurants


![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4%2B-green)
![SQLite](https://img.shields.io/badge/SQLite-3.x-blue)

This project demonstrates the use of SQLAlchemy to model a restaurant review system. It includes three main models: `Customer`, `Review`, and `Restaurant`. The project allows you to create, manage, and query restaurant reviews and related data.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Creating Sample Data](#creating-sample-data)
  - [Querying Data](#querying-data)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create and manage customer records.
- Create and manage restaurant records.
- Create and manage reviews, associating them with customers and restaurants.
- Calculate and display average ratings for each restaurant.
- Find the fanciest restaurant based on price.
- Retrieve all reviews for a specific restaurant.
- Retrieve customer data and their favorite restaurant.
- And more!

## Getting Started

### Prerequisites

To run this project, you need to have the following installed on your system:

- Python 3.7+
- SQLAlchemy 1.4+
- SQLite 3.x

### Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/brighton-flemming/SQLAlchemy-Restaurants.git
- Navigate to the project directory:
cd SQLAlchemy-Restaurants

- Create a virtual environment (optional but recommended):
python -m venv venv

-Activate the virtual environment (if you created one):
On Windows:
.\venv\Scripts\activate

On macOS and Linux:
source venv/bin/activate

-Install the project dependencies:

pip install -r requirements.txt
# Usage
Running the Application
To run the application, you can execute the main.py script:
python3 main.py

# Creating Sample Data
You can create sample data to populate the database with customers, restaurants, and reviews. Uncomment the following lines in the main.py script:

- Uncomment the following line if you want to recreate the database and create sample data
- Base.metadata.drop_all(engine)
- Base.metadata.create_all(engine)
- create_sample_data(session)
Then, run the script to create the sample data:
python main.py
# Querying Data
The main.py script demonstrates various database operations, including querying data. You can use this script to interact with the database and retrieve information about customers, restaurants, reviews, and more.

Here are some example queries you can perform:

- Find a customer by name.
- Get the fanciest restaurant.
- Get all reviews for a specific restaurant.
- Calculate and display average ratings for each restaurant.

# Project Structure
The project directory structure is organized as follows:

project_directory/
├── main.py
├── models/
│   ├── __init__.py
│   ├── customer.py
│   ├── review.py
│   └── restaurant.py
└── README.md
main.py: The main script to run the application and interact with the database.
models/: A directory containing the SQLAlchemy model classes for Customer, Review, and Restaurant.
README.md: This documentation file.
Contributing
Contributions are welcome! Feel free to open issues, submit pull requests, or provide suggestions for improvements.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

