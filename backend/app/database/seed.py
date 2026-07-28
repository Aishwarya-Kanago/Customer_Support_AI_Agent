from app.database.database import get_connection

orders = [

(1001,"Alice","Laptop",1,1200,"Delivered","Paid","TRK123"),

(1002,"Bob","Shoes",2,180,"Shipped","Paid","TRK124"),

(1003,"Charlie","Keyboard",1,90,"Processing","Pending",""),

(1004,"David","Monitor",1,350,"Cancelled","Refunded",""),

(1005,"Emma","Headphones",1,140,"Delivered","Paid","TRK125"),

(1006,"Sophia","Tablet",1,450,"Shipped","Paid","TRK126"),

(1007,"James","Mouse",2,60,"Processing","Pending",""),

(1008,"Olivia","Smart Watch",1,300,"Delivered","Paid","TRK127"),

(1009,"Noah","Camera",1,900,"Shipped","Paid","TRK128"),

(1010,"Liam","Phone",1,850,"Delivered","Paid","TRK129")

]

conn = get_connection()

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS orders")

cursor.execute("""
CREATE TABLE orders(

order_id INTEGER PRIMARY KEY,

customer_name TEXT,

product TEXT,

quantity INTEGER,

total REAL,

status TEXT,

payment_status TEXT,

tracking_number TEXT

)
""")

cursor.executemany("""

INSERT INTO orders VALUES(?,?,?,?,?,?,?,?)

""",orders)

conn.commit()

conn.close()

print("Sample orders inserted.")