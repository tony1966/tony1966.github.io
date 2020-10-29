<?php
header('Content-Type: text/html;charset=UTF-8');
$host="mysql.hostinger.co.uk"; 
$username="u137801098_test"; 
$password="a5572056"; 
$database="u137801098_test"; 
$conn=mysql_connect($host, $username, $password); 
mysql_query("SET NAMES 'utf8'"); 
mysql_select_db($database, $conn); 
$SQL="SELECT * FROM `pid_valid_date` WHERE pid='".$_REQUEST["pid"]."'"; 
$result=mysql_query($SQL, $conn);  
$row=mysql_fetch_array($result); 
echo $row["valid_date"]; 
?>