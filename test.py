#!/usr/bin/env python3
"""
⚠️ This script is intentionally vulnerable.
Use only for testing SAST / SonarQube scanners.
"""

import os
import subprocess
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# ❌ Hardcoded secret (sensitive information exposure)
API_KEY = "12345-SECRET-KEY"


# ❌ SQL Injection Vulnerability
def get_user(username):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()

    # Vulnerable: unsanitized string concatenation
    query = f"SELECT * FROM users WHERE username = '{username}'"
    print("Executing query:", query)

    result = cur.execute(query).fetchall()
    conn.close()
    return result


# ❌ Command Injection Vulnerability
def ping_host(host):
    # Vulnerable: user-controlled command
    cmd = f"ping -c 1 {host}"
    return subprocess.check_output(cmd, shell=True).decode()


# ❌ Path Traversal Vulnerability
def read_file(filename):
    # Completely unvalidated path from user
    with open(filename, "r") as f:
        return f.read()


# ❌ Flask route with multiple vulnerabilities
@app.route("/user")
def user_route():
    username = request.args.get("name", "")
    return {"data": get_user(username)}


@app.route("/ping")
def ping_route():
    host = request.args.get("host", "")
    return {"result": ping_host(host)}


@app.route("/file")
def file_route():
    filename = request.args.get("path", "")
    return {"content": read_file(filename)}


# ❌ Weak crypto (MD5)
import hashlib
def weak_hash(data):
    return hashlib.md5(data.encode()).hexdigest()


@app.route("/hash")
def hash_route():
    data = request.args.get("data", "")
    return {"md5": weak_hash(data)}


# ❌ Insecure random (predictable tokens)
import random
def generate_token():
    return str(random.random())


@app.route("/token")
def token_route():
    return {"token": generate_token()}


# ❌ Unsafe eval
@app.route("/calc")
def calc_route():
    expr = request.args.get("expr", "1+1")
    return {"result": eval(expr)}  # DO NOT DO THIS IN REAL APPS


if __name__ == "__main__":
    # ❌ Debug mode + public host exposure
    app.run(host="0.0.0.0", port=5000, debug=True)
