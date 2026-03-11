# logistics_systems[README.md](https://github.com/user-attachments/files/25913228/README.md)
# 🚚 Logistics & Delivery Tracking System

A menu-driven, role-based logistics management system built with Python.  
Uses text files as a database — no SQL or external libraries required.

---

## 📌 Project Overview

Small and medium logistics companies struggle to track deliveries, manage drivers, monitor fuel costs, and evaluate performance without expensive software. This system provides a low-cost, fully functional logistics management solution built entirely in Python.

---

## 🎯 Objectives

- Automate delivery order assignment and tracking
- Manage drivers and fleet vehicles
- Monitor fuel consumption and operational costs
- Generate performance reports
- Provide role-based access for Admin, Driver, and Manager

---

## 🗂️ Project Structure

```
logistics_system/
│
├── main.py                          ← Entry point, run this file
├── auth.py                          ← Login & authentication system
│
├── modules/
│   ├── order_management.py          ← Add/View/Search/Update/Cancel orders
│   ├── driver_management.py         ← Add/View/Search/Update/Remove drivers
│   ├── vehicle_management.py        ← Add/View/Update/Maintenance vehicles
│   ├── route_assignment.py          ← Assign/Complete/View routes
│   ├── delivery_tracking.py         ← Track and update delivery status
│   ├── fuel_tracking.py             ← Fuel records and cost reports
│   └── reports.py                   ← Driver/Vehicle/Operational reports
│
├── menus/
│   ├── admin_menu.py                ← Admin control panel
│   ├── driver_menu.py               ← Driver portal
│   └── manager_menu.py              ← Manager portal
│
├── database/
│   ├── orders.txt                   ← Order records
│   ├── drivers.txt                  ← Driver records
│   ├── vehicles.txt                 ← Vehicle records
│   ├── routes.txt                   ← Route assignment records
│   ├── fuel_records.txt             ← Fuel usage records
│   └── roles.txt                    ← Login credentials
│
└── diagrams/
    ├── ProcessFlowDiagram.png       ← System process flow
    ├── ER_Diagram.png               ← Entity relationship diagram
    └── ChenNotation_ER.png          ← Chen notation ER diagram
```

---

## ▶️ How to Run

### Requirements
- Python 3.x (no external libraries needed)
- VS Code (recommended) or any Python IDE

### Steps

**1. Clone or download the project folder**

**2. Open terminal in the `logistics_system/` folder**

**3. Run the program:**
```bash
python main.py
```

**4. Login using one of the test credentials below**

---

## 🔐 Login Credentials

| Role | Username | Password |
|------|----------|----------|
| Admin | admin | admin123 |
| Driver | driver001 | pass456 |
| Manager | manager01 | mgr789 |

---

## 📦 Database Structure (Text Files)

All data is stored in plain text files using `|` as a delimiter.

### orders.txt
```
order_id | customer_name | address | contact | order_date | deadline | weight | status
```

### drivers.txt
```
driver_id | name | phone | license | vehicle_id | status | rating
```

### vehicles.txt
```
vehicle_id | type | registration | fuel_type | mileage | status | location
```

### routes.txt
```
route_id | order_id | driver_id | vehicle_id | distance | est_time | status
```

### fuel_records.txt
```
fuel_id | driver_id | vehicle_id | quantity | cost | date | route_id
```

### roles.txt
```
username | password | role
```

---

## 🧩 Modules

### 1. Order Management
| Function | Description |
|----------|-------------|
| Add Order | Creates new delivery order with auto-generated ID |
| View Orders | Displays all orders in formatted table |
| Search Order | Find order by ID or customer name |
| Update Order | Modify address, contact, deadline, or weight |
| Cancel Order | Marks order as Cancelled (cannot cancel Delivered) |

### 2. Driver Management
| Function | Description |
|----------|-------------|
| Add Driver | Register new driver with auto-generated ID |
| View Drivers | Display all drivers with status |
| Search Driver | Find by ID or name |
| Update Driver | Modify phone, license, vehicle, status, rating |
| Remove Driver | Marks driver status as Removed |

### 3. Vehicle Management
| Function | Description |
|----------|-------------|
| Add Vehicle | Register new vehicle with auto-generated ID |
| View Vehicles | Display all vehicles in table |
| Search Vehicle | Find by ID or registration number |
| Update Vehicle | Modify mileage, status, location |
| Maintenance | Mark vehicle as Under Maintenance or Good |

### 4. Route Assignment
| Function | Description |
|----------|-------------|
| Assign Route | Links Order + Driver + Vehicle together |
| View Active | Shows only currently active routes |
| View All | Shows complete route history |
| Complete Route | Marks route done, updates order and driver status |

### 5. Fuel Tracking
| Function | Description |
|----------|-------------|
| Add Fuel Record | Log fuel usage per trip |
| View All Records | Display all fuel records with totals |
| Driver Fuel Report | Per-driver fuel usage and cost summary |
| Monthly Report | Month-wise fuel expense breakdown |

### 6. Reports
| Report | Description |
|--------|-------------|
| Driver Performance | Total routes, completed, failed, success rate |
| Vehicle Performance | Routes used, fuel consumed, total cost |
| Operational Summary | Overall orders, drivers, routes, fuel cost |

---

## 🔒 Role-Based Access

### Admin
- Full access to all 6 modules
- Can add, update, delete all records
- Can view all reports

### Driver
- View only own assigned orders
- Update delivery status (Assigned → Picked Up → Out for Delivery → Delivered)
- Submit own fuel records
- View own performance stats

### Manager
- Assign and monitor routes
- View all orders (read only)
- Access all performance reports

---

## 📊 Delivery Status Flow

```
Pending → Assigned → Picked Up → Out for Delivery → Delivered
                                                    ↓
                                                 Cancelled (if needed)
```

---

## 🔄 System Flow

```
python main.py
      ↓
  Login Portal (auth.py)
      ↓
  Role Check
      ↓
┌─────────────┬──────────────┬───────────────┐
│    ADMIN    │    DRIVER    │    MANAGER    │
│  Full Access│  Own Orders  │ Routes+Reports│
└─────────────┴──────────────┴───────────────┘
```

---



---

## 📁 Diagrams

| Process Flow | 
| ER Diagram |

---

## ⚙️ Status Enumerations

| Entity | Allowed Status Values |
|--------|----------------------|
| Order | Pending, Assigned, Picked Up, Out for Delivery, Delivered, Cancelled |
| Driver | Available, On Duty, Leave, Removed |
| Vehicle | Good, Under Maintenance, Out of Service |
| Route | Active, Completed, Failed |

---

## 🚀 Business Benefits

- Reduced fuel wastage through route tracking
- Improved delivery time with status monitoring
- Better driver accountability via performance reports
- Increased operational visibility for management
- Data-driven decisions through report generation
- Zero cost — no paid software or databases required

---

*Built with Python 3 | CIA Project | Business Analytics*
