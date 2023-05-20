/* 宣告指標變數來儲存其他變數的位址 */
#include <stdio.h>

int main() 
{
    int score = 85;  /* 宣告變數 */  
    int *ptr;        /* 宣告指標變數ptr儲存int變數位址 */

    ptr = &score;    /* 指定指標變數ptr的值是變數score的位址 */

    printf("變數score的值 = %d\n", score);
    printf("變數score的位址 = %p\n", &score);
    printf("指標ptr的值 = %p\n", ptr);
    printf("指標ptr的位址 = %p\n", &ptr);

    return 0;
}

