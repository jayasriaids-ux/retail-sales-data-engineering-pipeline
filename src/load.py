import csv
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "processed" / "retail_sales_transformed.csv"
db_path = BASE_DIR / "data" / "retail_sales.db"

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

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

try:
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = [
            (
                int(row["order_id"]),
                row["order_date"],
                row["product_name"],
                row["category"],
                int(row["quantity"]),
                float(row["price"]),
                row["region"],
                float(row["revenue"])
            )
            for row in reader
        ]

    cursor.execute("DELETE FROM retail_sales")

    cursor.executemany("""
        INSERT INTO retail_sales
        (order_id, order_date, product_name, category, quantity, price, region, total_sales)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, rows)

    connection.commit()
    print("Data loaded successfully!")
    print("Total records loaded:", len(rows))
    print("Database location:", db_path)

except (FileNotFoundError, KeyError, ValueError) as error:
    connection.rollback()
    print("ERROR:", error)

finally:
    connection.close()