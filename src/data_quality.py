
import csv

file_path = "data/raw/retail_sales.csv"

missing_count = 0
duplicate_count = 0
invalid_count = 0

seen_records = set()

with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # 1. Missing Values Check
        for column, value in row.items():
            if value is None or not value.strip():
                missing_count += 1

        # 2. Duplicate Records Check
        record = tuple(row.items())

        if record in seen_records:
            duplicate_count += 1
        else:
            seen_records.add(record)

        # 3. Invalid Quantity and Price Check
        try:
            quantity = float(row["quantity"])
            price = float(row["price"])

            if quantity < 0 or price < 0:
                invalid_count += 1

        except (ValueError, TypeError):
            invalid_count += 1

print("\n===== DATA QUALITY REPORT =====")
print("Missing Values:", missing_count)
print("Duplicate Records:", duplicate_count)
print("Invalid Records:", invalid_count)
print("================================")
