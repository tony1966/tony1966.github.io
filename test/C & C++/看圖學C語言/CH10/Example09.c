/* 使用指標運算 */
#include <stdio.h>

int main() 
{
     /* 宣告tests陣列和指定初值 */
	int tests[5] = { 71, 83, 67, 49, 59 }; 
    int *ptr, *ptr1;  /* 宣告指向整數的指標變數ptr, ptr1 */
 
    ptr = tests;    /* 將指標變數指向陣列第1個元素 */
    ptr1 = &tests[4];   /* 將指標變數指向陣列最後1個元素 */

    printf("tests[0]的值 = %d\n", tests[0]);
    printf("tests[0]的位址 = %p\n", ptr1);
    printf("ptr+1的值 = %p\n", ptr+1);  
    printf("*(ptr+1)的值 = %d\n", *(ptr+1)); 
    printf("ptr+2的值 = %p\n", ptr+2);  
    printf("*(ptr+2)的值 = %d\n", *(ptr+2)); 	 
    printf("ptr1~ptr之間的元素數 = %d\n", ptr1-ptr);  
    
    return 0;
}

