<!DOCTYPE html>
<html>
  <head>
    <title></title>
    <meta charset="utf-8">
    <meta http-equiv="cache-control" content="no-cache">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <script src="https://code.jquery.com/jquery-1.11.1.min.js"></script>
    <script src="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
    <link href="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css" rel="stylesheet">
  </head>
  <body>
    <!-- 第一頁頁面 -->
    <section data-role="page" id="page1">
      <header data-role="header" data-position="fixed">
        <h1 style="white-space: nowrap">疫苗臨床試驗登記</h1>
      </header>
      <article data-role="content">
<?php
//設定台北時間
date_default_timezone_set("Asia/Taipei");
//建立 PDO 連線物件
$dsn="mysql:host=mysql.hostinger.co.uk;port=3306;dbname=u137801098_test"; 
$username="u137801098_test"; 
$password="a5572056"; 
try {$conn=new PDO($dsn, $username, $password);}
catch (PDOException $e) {
  echo "資料庫連線錯誤!";
  die();
  }
//設定資料編碼
$conn->exec("SET CHARACTER SET utf8"); 
//取得傳遞之參數
$name=$_REQUEST["name"];
$phone=$_REQUEST["phone"];
$age=$_REQUEST["age"];
$gender=$_REQUEST["gender"];
//檢查是否已登記過
$SQL="SELECT * FROM `vaccine` WHERE name='".$name."' AND phone='".
      $phone."' AND age='".$age."'"; 
$RS=$conn->query($SQL);
if ($RS->rowCount() > 0) { //已登記過
?>
        <h3>您已登記過了, 勿重複登記!</h3>
<?php
  }
else { //未曾登記 -> 新增紀錄 
  $SQL="INSERT INTO `vaccine`(name,phone,age,gender,rdate) VALUES('".
       $name."','".$phone."','".$age."','".$gender."','".date("Y-m-d H:i:s")."')"; 
  $RS=$conn->query($SQL);
  if ($RS->rowCount() > 0) { //新增成功
?>
        <h3>已完成登記, 將有專人與您聯絡!</h3>
<?php
    }
  else { //新增失敗
?>
        <h3>系統異常, 請稍後再試試!</h3>
<?
    } 
  }
$conn=NULL;
?>

        <a href="index.htm" data-role="button" data-ajax="false">回登記頁面</a>
      </article>
      <footer data-role="footer" data-position="fixed">
        <h3>小狐狸事務所 07-1234567</h3>
      </footer>
    </section>
  </body>
</html>