<?php
require_once("db.php");

// Fetch all appointments
$result = $conn->query("
    SELECT a.id, u.name AS patient_name, a.appointment_date, a.appointment_time, a.reason 
    FROM appointments a
    JOIN users u ON a.patient_id = u.id
    ORDER BY a.appointment_date DESC
");

echo "<h1>Manage Appointments</h1>";
echo "<table border='1' cellpadding='10'>";
echo "<tr><th>ID</th><th>Patient Name</th><th>Date</th><th>Time</th><th>Reason</th><th>Action</th></tr>";

while ($row = $result->fetch_assoc()) {
    echo "<tr>";
    echo "<td>" . $row['id'] . "</td>";
    echo "<td>" . $row['patient_name'] . "</td>";
    echo "<td>" . $row['appointment_date'] . "</td>";
    echo "<td>" . $row['appointment_time'] . "</td>";
    echo "<td>" . $row['reason'] . "</td>";
    echo "<td>
            <a href='delete_appointment.php?id=" . $row['id'] . "' onclick=\"return confirm('Are you sure?')\">Delete</a>
          </td>";
    echo "</tr>";
}

echo "</table>";
?>