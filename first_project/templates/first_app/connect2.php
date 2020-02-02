<?php
$servername = "MWILLIAMS.mysql.pythonanywhere-services.com";
$username = "MWILLIAMS";
$password = "Skateg215";
$dbname = "first_database";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO account (email)
VALUES ('john@example.com')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
