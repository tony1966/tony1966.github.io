<?php
header('Content-Type: text/html;charset=UTF-8');
$host="mysql.hostinger.co.uk"; 
$username="u137801098_test"; 
$password="a5572056"; 
$database="u137801098_test"; 
$conn=mysql_connect($host, $username, $password); 
mysql_query("SET NAMES 'utf8'"); 
mysql_select_db($database, $conn); 
$SQL="SELECT pid FROM `pid_valid_date`"; 
$result=mysql_query($SQL, $conn); 
$arr=array(); 
for ($i=0; $i < mysql_numrows($result); $i++) { 
     $row=mysql_fetch_array($result); 
     $option="<option value='".$row["pid"]."'>".$row["pid"]."</option>";
     $arr[$i]=$option; 
     } 
echo implode("\n", $arr);  
?>