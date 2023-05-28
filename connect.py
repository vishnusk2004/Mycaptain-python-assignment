import sqlite3


def connect(dbname):
    conn = sqlite3.connect(dbname)
    conn.execute("CREATE TABLE IF NOT EXISTS AMAZON_DEVICES(MODEL TEXT, RATING INT, DELIVERY_BY TEXT)")
    print("Table created successfully!")
    conn.close()


def insert_into_table(dbname, values):
    conn = sqlite3.connect(dbname)
    print("Inserted into table: " + str(values))
    insert_sql = "INSERT INTO AMAZON_DEVICES(MODEL, RATING,  DELIVERY_BY) VALUES (?, ?, ?)"
    conn.execute(insert_sql, values)
    conn.commit()
    conn.close()


def get_devices_info(dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM AMAZON_DEVICES")
    table_data = cur.fetchall()
    for record in table_data:
        print(record)
        conn.close()
