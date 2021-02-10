<?php
//啟動 session 功能
session_start();
//設定台北時間
date_default_timezone_set("Asia/Taipei");
if (!isset($_SESSION["vaccine_admin_account"])) { //未登入回首頁
  header("Location: index.htm");
  }
?>
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
      <header data-role="header">
        <a href="index.htm" data-icon="home" data-ajax="false">回首頁</a>
        <h1>系統管理</h1>
        <a href="logout.php" class="ui-btn-right" data-icon="power" data-ajax="false">登出</a>
      </header>
      <article data-role="content">
        <a href="vaccine_subject_list.php" data-role="button" data-icon="user" data-ajax="false">受試者列表</a>
        <a href="#" data-role="button" data-icon="action" data-ajax="false">匯出受試者</a>
        <a href="#" data-role="button" data-icon="gear" data-ajax="false">系統設定</a>
      </article>
      <footer data-role="footer" data-position="fixed">
        <h3>小狐狸事務所 07-1234567</h3>
      </footer>
    </section>
    <script>
      $(document).ready(function() {
        $("#ok_btn").on("click", function(e) { 
          e.preventDefault();
          var name=trim($("#name").val());
          var phone=trim($("#phone").val());
          var age=trim($("#age").val());
          var gender=$("[name=gender]:radio:checked").val();
          if (name=="" ||  phone=="" || age=="" || gender==undefined) {
            alert("每一個欄位都必須填寫");
            return;
            }
          var msg="姓名 : " + name + "\n" + 
                  "電話 : " + phone + "\n" +  
                  "年齡 : " + age + "\n" + 
                  "性別 : " + gender + "\n" +
                  "以上資料正確嗎? ";
          if (!confirm(msg)) {return;}
          else {this.form.submit();}
          });
        $("#login_btn").on("click", function(e) { 
          e.preventDefault();
          var account=trim($("#account").val());
          var password=trim($("#password").val());
          if (account=="" || password=="") {
            alert("請輸入帳號與密碼");
            return;
            }
          this.form.submit();
          });
        });
    </script>
  </body>
</html>