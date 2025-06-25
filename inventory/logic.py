# Core logic for inventory ops
from inventory.db import get_connection

def add_item(data):
    conn = get_connection()
    cursor = conn.cursor()
    
    # Check if item already exists
    cursor.execute("SELECT * FROM inventory WHERE name = ?", (data['name'],))
    existing = cursor.fetchone()

    if existing:
        conn.close()
        return {"status": "Item already exists"}
    
    cursor.execute("INSERT INTO inventory (name, quantity, threshold) VALUES (?, ?, ?)",
                   (data['name'], data['quantity'], data['threshold']))
    conn.commit()
    conn.close()
    return {"status": "Item added"}


def update_item(data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE inventory SET quantity = quantity + ? WHERE name = ?",
                   ((data['delta'], data['name'])))
    conn.commit()
    conn.close()
    return {"status": "Quantity updated"}

def get_all_items():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, quantity, threshold FROM inventory")
    rows = cursor.fetchall()
    conn.close()
    result = []
    for name, qty, threshold in rows:
        result.append({"name": name, "quantity": qty, "threshold": threshold, "alert": qty < threshold})
    return result