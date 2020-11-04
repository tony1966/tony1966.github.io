<?php
header('Content-Type: text/html;charset=UTF-8');
//建立 PDO 連線物件
$dsn="mysql:host=localhost;port=3306;dbname=test"; 
$username="root"; 
$password="mysql"; 
try {$conn=new PDO($dsn, $username, $password);}
catch (PDOException $e) {
  echo "資料庫連線錯誤!";
  die();
  }
//設定資料編碼
$conn->exec("SET CHARACTER SET utf8"); 
//讀取資料表
$SQL="SELECT * FROM `pid_valid_date`"; 
$RS=$conn->query($SQL);
//讀取第一列資料
$row=$RS->fetch(); 
//迭代整個資料集
while(!empty($row)) {
  echo "pid=".$row["pid"]." valid_date=".$row["valid_date"]."<br>";
  $row=$RS->fetch();
  } 
//關閉資料庫連線
$conn=NULL;
?>