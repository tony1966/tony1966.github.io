/* 在函數使用指標來傳遞陣列參數 */
#include <stdio.h>
#define LENGTH  5           /* 定義常數 */

int total(int *, int);    /* 函數原型宣告 */

/* 在main()函數呼叫total()函數 */ 
int main() 
{
    int i;              /* 宣告變數 */  
    int result;

    int tests[LENGTH];  /* 宣告整數陣列，儲存LENGTH個元素 */

    for ( i = 0; i < LENGTH; i++ )  /* for迴圈輸入成績 */
    {
        printf("請輸入第%d位學生的成績 => ", (i+1)); 
        scanf("%d", &tests[i]);
    }

    result = total(tests, LENGTH);       /* 呼叫函數 */ 

    printf("成績總分: %d\n", result);    /* 顯示總分 */
    
    return 0;
}

/* total()函數的定義 */
int total(int *t, int len)
{
    int i;
    int sum = 0;

    for ( i = 0; i < len; i++ )  /* for迴圈計算總分 */
        sum = sum + *(t+i); 

    return sum;
}

