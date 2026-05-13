import sqlite3
import pandas as pd

conn = sqlite3.connect(
    r"C:\Users\19ayu\Documents\invoice_data\data\inventory(1).db"
)

tables = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table'",
    conn
)

print(tables)

conn.close()