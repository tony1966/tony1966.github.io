/* �ϥΫ��йB�� */
#include <stdio.h>

int main() 
{
     /* �ŧitests�}�C�M���w��� */
	int tests[5] = { 71, 83, 67, 49, 59 }; 
    int *ptr, *ptr1;  /* �ŧi���V��ƪ������ܼ�ptr, ptr1 */
 
    ptr = tests;    /* �N�����ܼƫ��V�}�C��1�Ӥ��� */
    ptr1 = &tests[4];   /* �N�����ܼƫ��V�}�C�̫�1�Ӥ��� */

    printf("tests[0]���� = %d\n", tests[0]);
    printf("tests[0]����} = %p\n", ptr1);
    printf("ptr+1���� = %p\n", ptr+1);  
    printf("*(ptr+1)���� = %d\n", *(ptr+1)); 
    printf("ptr+2���� = %p\n", ptr+2);  
    printf("*(ptr+2)���� = %d\n", *(ptr+2)); 	 
    printf("ptr1~ptr������������ = %d\n", ptr1-ptr);  
    
    return 0;
}

