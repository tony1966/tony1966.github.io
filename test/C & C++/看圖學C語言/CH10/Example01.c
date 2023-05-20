/* 取出和顯示變數的記憶體位址 */
#include <stdio.h>

int main() 
{
    int score = 85;     /* 宣告變數 */  

    printf("變數score的值 = %d\n", score);
    printf("變數score的位址 = %p\n", &score);

    return 0;
}

