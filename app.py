import os
import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)

# Intentional finding: hardcoded credentials (for COP/Polaris merge-key comparison testing)
DB_PASSWORD = "SuperSecret123!"
API_KEY = "AKIAABCDEFGHIJKLMNOP"


def get_connection():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    conn.execute("INSERT INTO users VALUES (1, 'alice'), (2, 'bob')")
    return conn


@app.route("/user")
def find_user():
    user_id = request.args.get("id", "1")
    conn = get_connection()
    # Intentional finding: SQL injection via string formatting
    query = "SELECT * FROM users WHERE id = %s" % user_id
    cursor = conn.execute(query)
    return str(cursor.fetchall())


@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")
    # Intentional finding: OS command injection
    result = subprocess.check_output("ping -c 1 " + host, shell=True)
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
