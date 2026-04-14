from flask import Flask, request, jsonify, render_template
import sqlite3
import re

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('subscribers.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            status TEXT DEFAULT 'active'
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.json.get('email')
    if not email or not is_valid_email(email):
        return jsonify({"message": "Invalid email format"}), 400

    try:
        conn = sqlite3.connect('subscribers.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO subscribers (email) VALUES (?)", (email,))
        conn.commit()
        conn.close()
        return jsonify({"message": f"Successfully subscribed {email}!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"message": "This email is already subscribed"}), 409
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    email = request.json.get('email')
    if not email or not is_valid_email(email):
        return jsonify({"message": "Invalid email format"}), 400

    try:
        conn = sqlite3.connect('subscribers.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM subscribers WHERE email = ?", (email,))
        if cursor.rowcount == 0:
            return jsonify({"message": "Email not found in our database"}), 404
        conn.commit()
        conn.close()
        return jsonify({"message": f"Successfully unsubscribed {email}!"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route('/notify', methods=['POST'])
def notify():
    try:
        conn = sqlite3.connect('subscribers.db')
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM subscribers")
        subscribers = cursor.fetchall()
        conn.close()
        
        email_list = [row[0] for row in subscribers]
        if not email_list:
            return jsonify({"message": "No subscribers to notify"}), 404

        # Simulating notification process
        print(f"Sending notification to: {', '.join(email_list)}")
        return jsonify({
            "message": f"Notification simulation triggered for {len(email_list)} subscribers",
            "recipients": email_list
        }), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route('/api/stats')
def stats():
    try:
        conn = sqlite3.connect('subscribers.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM subscribers")
        count = cursor.fetchone()[0]
        conn.close()
        return jsonify({"count": count})
    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
