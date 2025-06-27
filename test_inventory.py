import pytest
from inventory.logic import add_item, update_item, get_all_items
from inventory.db import init_db, get_connection

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Fresh DB before each test
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS inventory")
    conn.commit()
    init_db()
    yield
    conn.close()

def test_add_item():
    data = {"name": "Test Item", "quantity": 5, "threshold": 10}
    result = add_item(data)
    assert result["status"] == "Item added"
    assert result["alert"] is True  # Because 5 < 10

def test_duplicate_add():
    data = {"name": "ItemX", "quantity": 1, "threshold": 5}
    add_item(data)
    result = add_item(data)
    assert result["status"] == "Item already exists"

def test_update_item():
    add_item({"name": "ItemY", "quantity": 10, "threshold": 3})
    result = update_item({"name": "ItemY", "delta": -5})
    assert result["status"] == "Quantity updated"

def test_get_all_items():
    add_item({"name": "ItemZ", "quantity": 3, "threshold": 5})
    items = get_all_items()
    assert len(items) == 1
    assert items[0]["name"] == "ItemZ"
    assert items[0]["alert"] is True
