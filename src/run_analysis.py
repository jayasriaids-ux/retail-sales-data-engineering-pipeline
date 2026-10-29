import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "data" / "retail_sales.db"
sql_path = BASE_DIR / "src" / "analysis.sql"

connection = sqlite3.connect(db_path)

try:
    with open(sql_path, "r", encoding="utf-8") as file:
        sql_script = file.read()

    queries = [q.strip() for q in sql_script.split(";") if q.strip()]

    for query in queries:
        query = "\n".join(
            line for line in query.splitlines()
            if not line.strip().startswith("--")
        ).strip()

        if not query:
            continue

        print("\n" + "=" * 40)
        print("QUERY RESULT")

        cursor = connection.execute(query)

        if cursor.description:
            print(" | ".join(column[0] for column in cursor.description))
            for row in cursor.fetchall():
                print(row)

    print("\nSQL analysis completed successfully!")

except Exception as error:
    print("Error:", error)

finally:
    connection.close()