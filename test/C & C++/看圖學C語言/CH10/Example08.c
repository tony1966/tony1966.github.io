/* �ϥΰ}�C�W�٨��o������ */
#include <stdio.h>

int main() 
{
     /* �ŧitests�}�C�M���w��� */
	int tests[5] = { 71, 83, 67, 49, 59 }; 
    int *ptr, *ptr1;  /* �ŧi���V��ƪ������ܼ�ptr, ptr1 */
 
    ptr = tests;    /* �N�����ܼƫ��V�}�C��1�Ӥ��� */
    ptr1 = &tests[0];   /* �N�����ܼƫ��V�}�C����1�Ӥ��� */

    printf("tests[0]���� = %d\n", tests[0]);
    printf("tests[0]����} = %p\n", ptr1);
    printf("tests���� = %p\n", tests);   
    printf("*ptr���� = %d\n", *ptr);  
    printf("*ptr1���� = %d\n", *ptr1);  
    
    return 0;
}

