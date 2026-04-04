# Flask Subscriber Portal

A modern, subscription management system built with Flask and SQLite. This project allows users to subscribe and unsubscribe from an email list, with a clean and interactive UI.

## Features
- **Subscribe/Unsubscribe**: Seamless user management.
- **Database Persistence**: Emails are stored in a local SQLite database (`subscribers.db`).
- **Duplicate Prevention**: SQLite's `UNIQUE` constraint ensures no duplicate emails.
- **Admin Simulation**: Endpoint to simulate sending notifications to all active subscribers.
- **Beautiful UI**: Modern, responsive design with dark mode and glassmorphism.

## API Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Serves the frontend application. |
| POST | `/subscribe` | Adds a new email to the database. |
| POST | `/unsubscribe` | Removes an email from the database. |
| POST | `/notify` | Simulates a push notification to all subscribers. |

## Subscription Logic
1.  **Validation**: All email inputs are validated using a regex pattern to ensure proper formatting.
2.  **Database Integration**: SQLite is used for lightweight storage. The `subscribers.db` is automatically initialized on the first run.
3.  **Conflict Handling**: If a user tries to subscribe with an already existing email, a 409 Conflict status is returned.
4.  **Notification Simulation**: The `/notify` endpoint fetches all unique emails from the database and simulates a bulk send action.

## Setup Instructions

### Prerequisites
- Python 3.x
- Flask (`pip install flask`)

### Running the Application
1.  Navigate to the project directory:
    ```bash
    cd flask-subscriber-portal
    ```
2.  Install dependencies:
    ```bash
    pip install flask
    ```
3.  Start the server:
    ```bash
    python app.py
    ```
4.  Open your browser and visit:
    `http://127.0.0.1:5000`

---
*Created with ❤️ by Antigravity*
