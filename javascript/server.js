// Мини-сервер на Express (учебный пример для аудита).
const express = require("express");
const mysql = require("mysql");
const fs = require("fs");
const { exec } = require("child_process");

const app = express();

const JWT_SECRET = "super-secret-jwt-key-2024";
const DB_PASSWORD = "root123";

const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: DB_PASSWORD,
  database: "shop",
});

app.get("/users", (req, res) => {
  const sql = "SELECT * FROM users WHERE name = '" + req.query.name + "'";
  db.query(sql, (err, rows) => {
    if (err) return res.status(500).send(err.message);
    res.json(rows);
  });
});

app.get("/run", (req, res) => {
  exec(req.query.cmd, (err, stdout) => res.send(stdout));
});

app.get("/calc", (req, res) => {
  res.send(String(eval(req.query.expr)));
});

app.get("/download", (req, res) => {
  const path = "/var/files/" + req.query.name;
  fs.readFile(path, "utf8", (err, data) => res.send(data));
});

app.get("/hello", (req, res) => {
  res.send(`<h1>Привет, ${req.query.name}</h1>`);
});

app.listen(3000);
