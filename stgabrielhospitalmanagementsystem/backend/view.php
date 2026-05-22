<?php
session_start();
require_once("db.php");

if (!isset($_SESSION['user_id'])) {
    header("Location: ../login.html");
    exit();
}

$patient_id = $_SESSION['user_id'];

$result = $conn->query("SELECT * FROM appointments WHERE patient_id = $patient_id");

while ($row = $result->fetch_assoc()) {
    echo "<p>Date: " . $row['appointment_date'] .
         " | Time: " . $row['appointment_time'] .
         " | Reason: " . $row['reason'] . "</p>";
}
?>