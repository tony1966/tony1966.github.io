/* 使用陣列名稱取得元素值 */
#include <stdio.h>

int main() 
{
     /* 宣告tests陣列和指定初值 */
	int tests[5] = { 71, 83, 67, 49, 59 }; 
    int *ptr, *ptr1;  /* 宣告指向整數的指標變數ptr, ptr1 */
 
    ptr = tests;    /* 將指標變數指向陣列第1個元素 */
    ptr1 = &tests[0];   /* 將指標變數指向陣列的第1個元素 */

    printf("tests[0]的值 = %d\n", tests[0]);
    printf("tests[0]的位址 = %p\n", ptr1);
    printf("tests的值 = %p\n", tests);   
    printf("*ptr的值 = %d\n", *ptr);  
    printf("*ptr1的值 = %d\n", *ptr1);  
    
    return 0;
}

