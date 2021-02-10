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
    <style>
      table {
          color: black;
          background: #fff;
          border: 1px solid #b4b4b4;
          padding: 0;
          margin-top:10px;
          width: 100%;
          -webkit-border-radius: 8px;
          }
      table tr td {
          color: #666;
          border-bottom: 1px solid #b4b4b4;
          border-right: 1px solid #b4b4b4;
          padding: 5px 5px 5px 5px;
          background-image: -webkit-linear-gradient(top, #fdfdfd, #eee);
          }
      table tr:first-child td {
          border-top: 1px solid #b4b4b4;
          }
      table tr td:last-child {
          border-right: none;
          }
      table tr:last-child td {
          border-bottom: none;
          }
    </style>
  </head>
  <body>
    <!-- 第一頁頁面 -->
    <section data-role="page" id="page1">
      <header data-role="header" data-position="fixed">
        <a href="vaccine_admin.php" data-role="button" data-icon="back" data-mini="true"  data-ajax="false">返回</a>
        <h1>受試者列表</h1>
      </header>
      <article data-role="content">
        <table>
          <thead>
            <tr>
              <th>姓名</th>
              <th>電話</th>
              <th>年齡</th>
              <th>性別</th>
              <th>編輯</th>
            </tr>
          </thead>
          <tbody>
<?php
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
//讀取受試者資料表
$SQL="SELECT * FROM `vaccine` ORDER BY rdate DESC"; 
$RS=$conn->query($SQL);
$row=$RS->fetch(); 
//迭代整個資料集
while(!empty($row)) {
?>
            <tr>
              <td style="word-break: break-all"><? echo $row["name"] ?></td>
              <td><? echo $row["phone"] ?></td>
              <td><? echo $row["age"] ?></td>
              <td style="text-align: center"><? echo $row["gender"] ?></td>
              <td style="text-align: center">
                <a href="vaccine_subject_edit.php?id=<?php echo $row["id"] ?>" data-role="button" data-icon="edit" data-iconpos="notext" data-mini="true"  data-ajax="false">編輯</a>
              </td>
            </tr>
<?php
  $row=$RS->fetch();
  }
$conn=NULL;
?>
          </tbody>
        </table>
      </article>
      <footer data-role="footer" data-position="fixed">
        <h3>小狐狸事務所 07-1234567</h3>
      </footer>
    </section>
  </body>
</html>