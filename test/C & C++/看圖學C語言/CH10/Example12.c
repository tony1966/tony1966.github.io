/* 使用指標運算複製字串 */
#include <stdio.h>

int main() 
{
    /* 字元陣列宣告 */
    char str[15] = "This is a pen.";  
    char str1[15];
    char *ptr, *ptr1;         /* 宣告字串指標 */
    int i = 0;
    
    ptr = str;                /* 指標ptr指向字串str */
    ptr1 = str1;              /* 指標ptr1指向字串str1 */
    
    /* 使用指標運算複製字元的while迴圈 */
    while ( *ptr != '\0' )   
    {   
        *(ptr1+i) = *ptr++;
        i++;
    }
    *(ptr1+i) = '\0';  /* 加上字串結束字元 */

    /* 顯示字串內容 */
    printf("將字串str複製到str1: \n");
    printf("str字串 = \"%s\"\n", str);
    printf("str1字串 = \"%s\"\n", str1);
    printf("ptr1 = \"%s\"\n", ptr1);

    return 0;
}

