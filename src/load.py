
import csv
import sqlite3
from pathlib import Path

# Project folder location
BASE_DIR = Path(__file__).resolve().parent.parent

# Input CSV file
file_path = BASE_DIR / "data" / "processed" / "retail_sales_transformed.csv"

# Output database file
db_path = BASE_DIR / "data" / "retail_sales.db"

# Connect to SQLite database
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS retail_sales (
    order_id INTEGER,
    order_date TEXT,
    product_name TEXT,
    category TEXT,
    quantity INTEGER,
    price REAL,
    region TEXT,
    total_sales REAL
)
""")

# Read CSV and load data
try:
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        rows = [
            (
                row["order_id"],
                row["order_date"],
                row["product_name"],
                row["category"],
                int(row["quantity"]),
                float(row["price"]),
                row["region"],
                float(row["total_sales"])
            )
            for row in reader
        ]

    cursor.executemany("""
        INSERT INTO retail_sales
        (order_id, order_date, product_name, category,
         quantity, price, region, total_sales)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, rows)

    connection.commit()
    print("Data loaded successfully!")
    print(f"Total records loaded: {len(rows)}")
    print(f"Database location: {db_path}")

except FileNotFoundError:
    print(f"ERROR: CSV file not found: {file_path}")
    connection.rollback()

except (KeyError, ValueError) as error:
    print(f"ERROR: Check the CSV columns or data: {error}")
    connection.rollback()

finally:
    connection.close()
