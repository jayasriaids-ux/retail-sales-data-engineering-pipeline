# Retail Sales Data Engineering Pipeline

## 📌 Project Overview

This project demonstrates an end-to-end **ETL (Extract, Transform, Load) pipeline** built using Python, SQL, and SQLite.

The pipeline extracts retail sales data from a CSV file, transforms the data by calculating revenue, loads the processed records into a SQLite database, and runs SQL queries to analyze sales performance.

## 🎯 Project Objectives

- Build a basic ETL pipeline using Python.
- Clean and transform retail sales data.
- Calculate revenue for each sales record.
- Store processed data in a SQLite database.
- Analyze sales data using SQL queries.

## 🛠️ Technologies Used

- **Python** — Data extraction and transformation
- **SQL** — Data analysis and querying
- **SQLite** — Database storage
- **CSV** — Source and processed data format
- **Git & GitHub** — Version control and project hosting

## 🔄 ETL Pipeline Architecture

```text
Raw Retail Sales CSV
         |
         v
     Extraction
         |
         v
    Transformation
         |
         v
 Processed Sales CSV
         |
         v
   SQLite Database
         |
         v
     SQL Analysis
         |
         v
  Sales Insights
```

## 📂 Project Structure

```text
retail-sales-data-engineering-pipeline/
│
├── data/
│   ├── raw/
│   │   └── retail_sales.csv
│   └── processed/
│       └── retail_sales_transformed.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── analysis.sql
│   └── run_analysis.py
│
├── .gitignore
└── README.md
```

## ⚙️ How to Run the Project

### Prerequisites

- Python 3.9 or later
- Git

SQLite is available through Python's built-in `sqlite3` module.

### Step 1: Clone the repository

```bash
git clone https://github.com/jayasriaids-ux/retail-sales-data-engineering-pipeline.git
cd retail-sales-data-engineering-pipeline
```

### Step 2: Extract the data

```bash
python src/extract.py
```

### Step 3: Transform the data

```bash
python src/transform.py
```

### Step 4: Load the data into SQLite

```bash
python src/load.py
```

### Step 5: Run SQL analysis

```bash
python src/run_analysis.py
```

## 📊 Key Features

- CSV data extraction
- Data transformation using Python
- Revenue calculation
- SQLite database loading
- SQL-based sales analysis
- Reproducible pipeline execution

## 📚 Skills Demonstrated

Python | SQL | ETL | SQLite | Data Transformation | CSV Processing | Git | GitHub

## 👩‍💻 Author

**Jayasri R**

Aspiring Data Engineer

[GitHub Profile](https://github.com/jayasriaids-ux)
