
import csv

input_file = "data/raw/retail_sales.csv"
output_file = "data/processed/retail_sales_transformed.csv"
import os

os.makedirs("data/processed", exist_ok=True)

with open(input_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    rows = []

    for row in reader:
        quantity = int(row["quantity"])
        price = float(row["price"])

        revenue = quantity * price

        row["quantity"] = quantity
        row["price"] = price
        row["revenue"] = revenue

        rows.append(row)

with open(output_file, "w", newline="", encoding="utf-8") as file:
    fieldnames = [
        "order_id",
        "order_date",
        "product_name",
        "category",
        "quantity",
        "price",
        "region",
        "revenue",
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Data transformation completed!")
print("Total records processed:", len(rows))
print("Transformed file:", output_file)
