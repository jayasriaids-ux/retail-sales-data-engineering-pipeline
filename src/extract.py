```python
import csv

file_path = "data/raw/retail_sales.csv"

with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```
