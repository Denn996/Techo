<?php
require_once("db.php");

// Fetch all patients
$result = $conn->query("SELECT id, name, email, created_at FROM users ORDER BY id DESC");

echo "<h1>Manage Patients</h1>";
echo "<table border='1' cellpadding='10'>";
echo "<tr><th>ID</th><th>Name</th><th>Email</th><th>Registered At</th><th>Action</th></tr>";

while ($row = $result->fetch_assoc()) {
    echo "<tr>";
    echo "<td>" . $row['id'] . "</td>";
    echo "<td>" . $row['name'] . "</td>";
    echo "<td>" . $row['email'] . "</td>";
    echo "<td>" . $row['created_at'] . "</td>";
    echo "<td>
            <a href='delete_patient.php?id=" . $row['id'] . "' onclick=\"return confirm('Are you sure?')\">Delete</a>
          </td>";
    echo "</tr>";
}

echo "</table>";
?>