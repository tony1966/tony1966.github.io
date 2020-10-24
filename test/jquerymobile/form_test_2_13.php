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
        <h1>表單元件測試</h1>
      </header>
      <article data-role="content">
      <?php
        $msg="自動更新 1=".$_REQUEST["auto_update_1"]."<br>".
             "自動更新 2=".$_REQUEST["auto_update_2"]."<br>".
             "自動更新 3=".$_REQUEST["auto_update_3"];
        echo $msg;
      ?>
      </article>
      <footer data-role="footer">
        <h3>頁尾</h3>
      </footer>
    </section>
  </body>
</html>