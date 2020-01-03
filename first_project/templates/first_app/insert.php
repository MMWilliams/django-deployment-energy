<?php

$email = $_POST['email'];
$phone_number = $_POST['phone_number'];

if (!empty($email) || (!empty($phone_number)) {
  $host = "MWILLIAMS.mysql.pythonanywhere-services.com";
  $dbusername = "MWILLIAMS";
  $dbpassword = "Skateg215";
  $dbname = "first_database";
  // Create connection
  $conn = new mysqli ($host, $dbusername, $dbpassword, $dbname);

  if (mysqli_connect_error()){
  die('Connect Error ('. mysqli_connect_errno() .') '. mysqli_connect_error());
  }else{
  $sql = "INSERT INTO account (email)
  values ('$email','$phone_number)";
  if ($conn->query($sql)){
  echo "New record is inserted sucessfully";
  }
  else{
  echo "Error: ". $sql ."
  ". $conn->error;
  }
  $conn->close();
  }
  }
  else{
  echo "Phone number should not be empty";
  die();
  }
  }
  else{
  echo "Email should not be empty";
  die();
  }



} else {
  echo "All fields are required";
  die();
}

?>
