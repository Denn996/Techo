<?php
session_start();
include "db.php";

if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    $name     = trim($_POST['name']);
    $email    = trim($_POST['email']);
    $password = trim($_POST['password']);
    $confirm  = trim($_POST['confirm_password']);

    // Check password match
    if ($password !== $confirm) {
        echo "<script>
                alert('Passwords do not match!');
                window.history.back();
              </script>";
        exit();
    }

    // Hash password
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);

   // If email does not exist, proceed with insertion
if ($stmt->num_rows == 0) {
    $stmt->close(); // Close the previous check statement

    // Prepare the INSERT statement
    $insert_query = "INSERT INTO users (name, email, password) VALUES (?, ?, ?)";
    $insert_stmt = $conn->prepare($insert_query);
    
    // Bind parameters (s = string)
    $insert_stmt->bind_param("sss", $name, $email, $hashed_password);

    if ($insert_stmt->execute()) {
        echo "<script>
                alert('Registration successful! Please login.');
                window.location.href = '../login.html';
              </script>";
    } else {
        echo "Error: " . $insert_stmt->error;
    }
    
    $insert_stmt->close();
} else {
    // This handles the 'Email already exists' case from your line 30
    echo "<script>
            alert('Email is already registered!');
            window.history.back();
          </script>";
}
    $stmt->close();

    // Insert user
    $stmt = $conn->prepare("INSERT INTO users (name, email, password) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $name, $email, $hashed_password);

    if ($stmt->execute()) {
        $stmt->close();
        $conn->close();

        header("Location: ../login.html");
        exit();
    } else {
        echo "Error: " . $conn->error;
    }

    $stmt->close();
    $conn->close();
}
?>