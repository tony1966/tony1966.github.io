<!DOCTYPE html>
<html>
  <head>
    <title></title>
    <meta charset="utf-8">
    <meta http-equiv="cache-control" content="no-cache">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <link href="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-1.11.1.min.js"></script>
    <script src="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
  </head>
  <body>
    <!-- 第一頁頁面 -->
    <section data-role="page" id="page1">
      <header data-role="header">
        <h1>換頁傳送 data 測試</h1>
      </header>
      <article data-role="content">
<?php
echo "name:".$_REQUEST["name"]."<br>".
     "msg:".$_REQUEST["msg"];
?>
      </article>
      <footer data-role="footer">
        <h3>頁尾</h3>
      </footer>
    </section>
  </body>
</html>