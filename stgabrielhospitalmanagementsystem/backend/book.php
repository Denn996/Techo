<?php
session_start();
require_once("db.php");

if (!isset($_SESSION['user_id'])) {
    header("Location: ../login.html");
    exit();
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $patient_id = $_SESSION['user_id'];
    $date = $_POST['date'];
    $time = $_POST['time'];
    $reason = $_POST['reason'];

    $stmt = $conn->prepare("INSERT INTO appointments (patient_id, appointment_date, appointment_time, reason) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("isss", $patient_id, $date, $time, $reason);

    if ($stmt->execute()) {
        echo "Appointment booked successfully!";
    } else {
        echo "Booking failed.";
    }
}
?>