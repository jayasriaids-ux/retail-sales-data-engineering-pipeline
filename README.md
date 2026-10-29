\# Retail Sales Data Engineering Pipeline



\## 📌 Project Overview



This project demonstrates an end-to-end \*\*ETL (Extract, Transform, Load) pipeline\*\* using Python, SQL, and SQLite.



The pipeline extracts retail sales data from a CSV file, transforms the data by calculating revenue, loads the processed records into a SQLite database, and performs SQL-based analysis.



\## 🎯 Project Objectives



\- Extract retail sales data from CSV files.

\- Transform data using Python.

\- Calculate revenue for each sales record.

\- Load processed data into an SQLite database.

\- Analyze sales data using SQL queries.



\## 🛠️ Technologies Used



\- \*\*Python\*\* – Data extraction and transformation

\- \*\*SQL\*\* – Data analysis

\- \*\*SQLite\*\* – Database management

\- \*\*CSV\*\* – Data storage and processing

\- \*\*Git \& GitHub\*\* – Version control



\## 🔄 ETL Pipeline Architecture



```text

Raw CSV Data

&#x20;    |

&#x20;    v

Extract (extract.py)

&#x20;    |

&#x20;    v

Transform (transform.py)

&#x20;    |

&#x20;    v

Processed CSV Data

&#x20;    |

&#x20;    v

Load into SQLite (load.py)

&#x20;    |

&#x20;    v

SQL Analysis (analysis.sql)

&#x20;    |

&#x20;    v

Sales Insights

```



\## 📂 Project Structure



```text

retail-sales-data-engineering-pipeline/

├── data/

│   ├── raw/

│   │   └── retail\_sales.csv

│   └── processed/

│       └── retail\_sales\_transformed.csv

├── src/

│   ├── extract.py

│   ├── transform.py

│   ├── load.py

│   ├── analysis.sql

│   └── run\_analysis.py

├── .gitignore

└── README.md

```



\## ⚙️ How to Run



\### Prerequisites



\- Python 3.9 or later

\- Git



\### 1. Clone the repository



```bash

git clone https://github.com/jayasriaids-ux/retail-sales-data-engineering-pipeline.git

cd retail-sales-data-engineering-pipeline

```



\### 2. Extract the data



```bash

python src/extract.py

```



\### 3. Transform the data



```bash

python src/transform.py

```



\### 4. Load data into SQLite



```bash

python src/load.py

```



\### 5. Run SQL analysis



```bash

python src/run\_analysis.py

```



\## 📚 Skills Demonstrated



Python | SQL | ETL Pipelines | SQLite | CSV Processing | Data Transformation | Git | GitHub



\## 👩‍💻 Author



\*\*Jayasri R\*\*



Aspiring Data Engineer



