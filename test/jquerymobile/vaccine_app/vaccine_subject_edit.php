<?php
//啟動 session 功能
session_start();
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
      <header data-role="header" data-position="fixed">
        <a href="vaccine_subject_list.php" data-role="button" data-icon="back" data-mini="true" data-ajax="false">返回</a>
        <h1 style="white-space: nowrap">編輯受試者資料</h1>
      </header>
      <article data-role="content">
<?php
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
//讀取受試者資料表
$SQL="SELECT * FROM `vaccine` WHERE id='".$_REQUEST["id"]."'"; 
$RS=$conn->query($SQL);
$row=$RS->fetch(); 
if(!empty($row)) {
?>
        <form id="edit_form" method="post" data-ajax="false">  
          <div data-role="fieldcontain">
            <label for="name">姓名 :</label>
            <input type="text" id="name" name="name" value="<?php echo $row["name"] ?>">
          </div>
          <div data-role="fieldcontain">
            <label for="phone">電話 :</label>
            <input type="tel" id="phone" name="phone" value="<?php echo $row["phone"] ?>">
          </div>
          <div data-role="fieldcontain">
            <label for="age">年齡 :</label>
            <input type="number" id="age" name="age" min="0" max="100" value="<?php echo $row["age"] ?>">
          </div>
          <fieldset data-role="controlgroup" data-type="horizontal">
            <legend>性別 :</legend>
            <div data-role="fieldcontain">
              <label for="gender-1">男</label>
              <input type="radio" name="gender" id="gender-1" value="男"<?php if ($row["gender"]=="男") {echo " checked";} ?>>
              <label for="gender-2">女</label>
              <input type="radio" name="gender" id="gender-2" value="女"<?php if ($row["gender"]=="女") {echo " checked";} ?>>
            </div>
          </fieldset>
          <div data-role="fieldcontain">
            <button id="update_btn" data-icon="edit">更新</button>
            <button id="delete_btn" data-icon="delete">刪除</button>
          </div>
          <input type="hidden" name="id" value="<?php echo $row["id"] ?>">
        </form>
<?php
  }
else { //id 不存在
?>
        <h3>資料不存在</h3>
        <a href="vaccine_subject_list.php" data-role="button" data-icon="back">返回列表</a>
<?php    
  }
$RS=NULL;
$conn=NULL;
?>
      </article>
      <footer data-role="footer" data-position="fixed">
        <h3>小狐狸事務所 07-1234567</h3>
      </footer>
    </section>
    <script>
      function trim(s){ 
        return (s || '').replace(/^\s+|\s+$/g, ''); 
        }
      $(document).ready(function() {
        $("#update_btn").on("click", function(e) { 
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
          else {
            $("#edit_form").attr("action", 'vaccine_subject_update.php');
            this.form.submit();
            }
          });
        $("#delete_btn").on("click", function(e) { 
          e.preventDefault();
          if (!confirm("確定要刪除這筆資料嗎?")) {return;}
          else {
            $("#edit_form").attr("action", 'vaccine_subject_delete.php');
            this.form.submit();
            }
          });
        });
    </script>
  </body>
</html>