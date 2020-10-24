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
        $msg="設定日期時間=".$_REQUEST["set_datetime_local"];
        echo $msg;
      ?>
      </article>
      <footer data-role="footer">
        <h3>頁尾</h3>
      </footer>
    </section>
  </body>
</html>