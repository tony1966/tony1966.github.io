/* 建立與使用字串指標 */
#include <stdio.h>

int main() 
{
    /* 字元陣列宣告 */
    char str[15] = "This is a pen.";  
    char str1[15] = "hello! world";
    char *ptr, *ptr1;           /* 宣告字串指標 */
    
    ptr = str;                  /* 指標ptr指向字串str */
    ptr1 = "This is an apple."; /* 指向字串常數 */

    /* 顯示字串內容 */
    printf("str字串 = \"%s\"\n", str);
    printf("str1字串 = \"%s\"\n", str1);
    printf("ptr = \"%s\"\n", ptr);
    printf("ptr1 = \"%s\"\n", ptr1);
    
    ptr1 = str1;    /* 字串指標ptr1改指向str1字串 */
    
    printf("更改後ptr1 = \"%s\"\n", ptr1);  /* 顯示字串內容 */

    return 0;
}

