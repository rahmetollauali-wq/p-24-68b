<?php
// Мини-портал магазина (учебный пример для аудита).

$conn = new mysqli("localhost", "root", "root123", "shop");

$user = $_GET["user"] ?? "";
$sql = "SELECT id, name, email FROM users WHERE name = '$user'";
$result = $conn->query($sql);

while ($row = $result->fetch_assoc()) {
    echo "<p>Пользователь: " . $row["name"] . "</p>";
}

$cmd = $_GET["cmd"] ?? "";
if ($cmd !== "") {
    system($cmd);
}

$page = $_GET["page"] ?? "home.php";
include($page);

$state = $_COOKIE["state"] ?? "";
$data = unserialize(base64_decode($state));

echo "<h1>Привет, " . $_GET["name"] . "!</h1>";

$upload = $_FILES["file"]["name"];
move_uploaded_file($_FILES["file"]["tmp_name"], "/var/www/uploads/" . $upload);
