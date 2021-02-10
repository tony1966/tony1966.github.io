<?php
//啟動 session 功能
session_start();
if (!isset($_SESSION["vaccine_admin_account"])) { //未登入回首頁
  header("Location: index.htm");
  }
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
//刪除資料
$SQL="UPDATE `vaccine` SET name='".$_REQUEST["name"]."',".
     "phone='".$_REQUEST["phone"]."',".
     "age='".$_REQUEST["age"]."',".
     "gender='".$_REQUEST["gender"]."' ".
     "WHERE id='".$_REQUEST["id"]."'"; 
//echo $SQL;
$RS=$conn->query($SQL);
header("Location: vaccine_subject_list.php");
$RS=NULL;
$conn=NULL;
?>