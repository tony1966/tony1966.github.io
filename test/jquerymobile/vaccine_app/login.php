<?php
//啟動 session 功能
session_start();
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
$account=$_REQUEST["account"];
$password=$_REQUEST["password"];
//echo $account.$password;
$SQL="SELECT * FROM `users` WHERE account='".$account."' ".
     "AND password='".$password."'"; 
$RS=$conn->query($SQL);
if ($RS->rowCount() > 0) { //帳密符合
  $_SESSION["vaccine_admin_account"]=$account;
  header("Location: vaccine_admin.php");
  }
else { //帳密不符
  header("Location: index.htm");
  die();
  } 
$conn=NULL;
?>