<?php
// Database connection
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "Userid";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get username and password from the form
$username = $_POST['username'];
$password = $_POST['password'];

// Query to check if the username and password exist in the database
$sql = "SELECT * FROM users WHERE username='$username' AND password='$password'";
$result = $conn->query($sql);

// Check if there is a match
if ($result->num_rows > 0) {
    // Username and password are correct, redirect to admin dashboard or another page
    header("Location: admin_dashboard.php");
    exit();
} else {
    // Username and/or password are incorrect, redirect back to login page
    header("Location: login.html");
    exit();
}

$conn->close();
?>
