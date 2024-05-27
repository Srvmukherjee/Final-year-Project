<?php
$servername = "localhost";
$username = "your_username"; // Your MySQL username
$password = "your_password"; // Your MySQL password
$dbname = "your_database"; // Your MySQL database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve form data
$admin_username = $_POST['admin_username'];
$admin_password = $_POST['admin_password'];

// SQL to insert admin data into the database
$sql = "INSERT INTO admins (admin_username, admin_password) VALUES ('$admin_username', '$admin_password')";

if ($conn->query($sql) === TRUE) {
    echo "New admin created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
