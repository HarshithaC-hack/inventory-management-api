# 🧾 Flask Inventory API

A simple Flask-based inventory tracking API to:

- Add items
- Update quantities
- Trigger alerts when quantity falls below a threshold
![cmd running](./inventory/successful-running.png)
---

## 🔗 API Endpoints

### ➕ Add Item
**POST** `/inventory/add`  
**Body:**
```json
{
  "name": "Notebook",
  "quantity": 30,
  "threshold": 5
}
```
![add item](./inventory/add.png)

---

### 🔁 Update Quantity
**POST** `/inventory/update`  
**Body:**
```json
{
  "name": "Notebook",
  "delta": -27
}
```

![update item](./inventory/update.png)

---

### 📦 Get All Items
**GET** `/inventory/all`  
**Response:**
```json
[
  {
    "alert": true
    "name": "Notebook",
    "quantity": 3,
    "threshold": 5,
    
  }
]
```
![updated items](./inventory/updated-all.png)

## ✍️ Author
Harshitha Chowdappa
