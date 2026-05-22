<?php
require_once("db.php");

$users = $conn->query("SELECT COUNT(*) AS total_users FROM users");
$appointments = $conn->query("SELECT COUNT(*) AS total_appointments FROM appointments");
$messages = $conn->query("SELECT COUNT(*) AS total_messages FROM messages");

$user_count = $users->fetch_assoc()['total_users'];
$app_count  = $appointments->fetch_assoc()['total_appointments'];
$msg_count  = $messages->fetch_assoc()['total_messages'];

echo "<h1>Admin Dashboard</h1>";
echo "<p>Total Patients: $user_count</p>";
echo "<p>Total Appointments: $app_count</p>";
echo "<p>Total Messages: $msg_count</p>";
?>