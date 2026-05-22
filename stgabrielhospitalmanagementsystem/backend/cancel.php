<?php
session_start();
require_once("db.php");

$id = $_GET['id'];

$conn->query("DELETE FROM appointments WHERE id = $id");

header("Location: view.php");
exit();
?>