# Car Parking System - API Payload Documentation

This document outlines the available REST API endpoints for the Car Parking System, including their request methods, URL paths, and payload structures.

## Base URL
`http://<your-domain>/api/`

---

## 1. Parking Slots

### List Parking Slots
Retrieve a list of all parking slots.
- **Method**: `GET`
- **URL**: `/api/slots/`
- **Query Parameters**:
  - `car_type`: Filter by car type (`small`, `medium`, `large`).
  - `available`: Filter by availability (`true`).
- **Response**: List of parking slot objects.

### Create Parking Slot
Create a new parking slot.
- **Method**: `POST`
- **URL**: `/api/slots/`
- **Request Payload**:
```json
{
  "slot_number": "A-101",
  "car_type": "small",
  "hourly_rate": 20.00
}
```

### Retrieve / Update / Delete Slot
Specific operations on a single slot.
- **Method**: `GET` / `PUT` / `PATCH` / `DELETE`
- **URL**: `/api/slots/<id>/`
- **Update Payload (PUT/PATCH)**:
```json
{
  "slot_number": "A-101",
  "car_type": "small",
  "hourly_rate": 25.00
}
```

---

## 2. Car Parking (Check-in)

### List Parking Sessions
Retrieve historical and active parking sessions.
- **Method**: `GET`
- **URL**: `/api/parking/`
- **Query Parameters**:
  - `status`: Filter by status (`parked`, `exited`).
- **Response**: List of parking session objects.

### Car Check-in (Create Session)
Records a car entering a parking slot.
- **Method**: `POST`
- **URL**: `/api/parking/`
- **Request Payload**:
```json
{
  "car_brand": "Toyota",
  "car_model": "Camry",
  "car_number": "MH-12-AB-1234",
  "car_type": "medium",
  "parking_slot": 1
}
```
> [!IMPORTANT]
> The `parking_slot` must be the ID of an available slot that matches the `car_type`.

### Retrieve / Update / Delete Session
- **Method**: `GET` / `PUT` / `PATCH` / `DELETE`
- **URL**: `/api/parking/<id>/`

---

## 3. Car Parking Checkout

### Car Checkout
Processes the exit of a car and calculates the final charge.
- **Method**: `POST`
- **URL**: `/api/parking/<id>/checkout/`
- **Request Payload**: (Empty)
```json
{}
```
- **Response**:
```json
{
  "message": "Car 'MH-12-AB-1234' has exited successfully.",
  "session": {
    "id": 1,
    "car_number": "MH-12-AB-1234",
    "incoming_time": "2024-04-11T10:00:00Z",
    "outgoing_time": "2024-04-11T12:00:00Z",
    "status": "exited",
    "status_display": "Exited",
    "amount_charged": "40.00",
    ...
  }
}
```

---

## Data Enums

### Car Types
- `small`
- `medium`
- `large`

### Session Status
- `parked`: Car is currently in the slot.
- `exited`: Car has checked out and paid.
