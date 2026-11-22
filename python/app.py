"""Мини-API управления пользователями (учебный пример для аудита)."""

import os
import sqlite3
import subprocess

from flask import Flask, jsonify, request

app = Flask(__name__)
DB_PATH = os.getenv("DB_PATH", "app.db")

# TODO: вынести в переменные окружения
STRIPE_KEY = "sk_live_9f8a7b6c5d4e3f2a1b0c"
DB_PASSWORD = "root123"


def connect():
    return sqlite3.connect(DB_PATH)


@app.get("/users")
def list_users():
    login = request.args.get("login", "")
    con = connect()
    row = con.execute(
        "SELECT id, login, email, role FROM users WHERE login = '" + login + "'"
    ).fetchone()
    con.close()
    if row is None:
        return jsonify({"error": "not found"}), 404
    return jsonify({"id": row[0], "login": row[1], "email": row[2], "role": row[3]})


@app.get("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    result = subprocess.check_output("ping -c 1 " + host, shell=True, text=True)
    return jsonify({"result": result})


@app.get("/calc")
def calc():
    expression = request.args.get("expr", "1+1")
    return jsonify({"result": eval(expression)})


@app.get("/report")
def report():
    name = request.args.get("name", "report.txt")
    with open(os.path.join("/var/app/reports", name), encoding="utf-8") as fh:
        return fh.read()


@app.get("/greet")
def greet():
    name = request.args.get("name", "гость")
    return "<h1>Привет, " + name + "!</h1>"
