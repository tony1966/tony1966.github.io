/* �ϥΫ��Ч���ܼƭ� */
#include <stdio.h>

int main() 
{
    int score = 85;  /* �ŧi�ܼ� */  
    int *ptr;        /* �ŧi�����ܼ�ptr�x�sint�ܼƦ�} */

    ptr = &score;    /* ���w�����ܼ�ptr���ȬO�ܼ�score����} */

    printf("�ܼ�score���� = %d\n", score);
    printf("�ܼ�score����} = %p\n", &score);
    printf("*ptr���� = %d\n", *ptr);

    *ptr = 60;       /* ���*ptr���� */
    
    printf("���*ptr���Ȧ���60\n"); 
    printf("�ܼ�score���� = %d\n", score);
    printf("*ptr���� = %d\n", *ptr);

    return 0;
}

