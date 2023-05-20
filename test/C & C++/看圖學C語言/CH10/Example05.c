/* 使用指標更改變數值 */
#include <stdio.h>

int main() 
{
    int score = 85;  /* 宣告變數 */  
    int *ptr;        /* 宣告指標變數ptr儲存int變數位址 */

    ptr = &score;    /* 指定指標變數ptr的值是變數score的位址 */

    printf("變數score的值 = %d\n", score);
    printf("變數score的位址 = %p\n", &score);
    printf("*ptr的值 = %d\n", *ptr);

    *ptr = 60;       /* 更改*ptr的值 */
    
    printf("更改*ptr的值成為60\n"); 
    printf("變數score的值 = %d\n", score);
    printf("*ptr的值 = %d\n", *ptr);

    return 0;
}

