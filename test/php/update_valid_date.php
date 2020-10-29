<?php
header('Content-Type: text/html;charset=UTF-8');
$host="mysql.hostinger.co.uk"; 
$username="u137801098_test"; 
$password="a5572056"; 
$database="u137801098_test"; 
$conn=mysql_connect($host, $username, $password); 
mysql_query("SET NAMES 'utf8'"); 
mysql_select_db($database, $conn); 
$SQL="UPDATE `pid_valid_date` SET valid_date='".$_REQUEST["valid_date"]."' ".
     "WHERE pid='".$_REQUEST["pid"]."'"; 
$result=mysql_query($SQL, $conn);  
if (mysqli_error($conn)) {$msg="NG";}
else {$msg="OK";}
echo $msg; 
?>