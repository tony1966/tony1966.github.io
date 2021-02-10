<?php
//啟動 session 功能
session_start();
session_destroy(); //刪除 session 檔
header("Location: index.htm");
?>