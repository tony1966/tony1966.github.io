/* �������ܼƪ���}�� */
#include <stdio.h>

int main() 
{
    int score = 85;  /* �ŧi�ܼ� */  
    int score1 = 72;
    int *ptr;        /* �ŧi�����ܼ�ptr�x�sint�ܼƦ�} */

    ptr = &score;    /* ���w�����ܼ�ptr���ȬO�ܼ�score����} */

    printf("�ܼ�score���� = %d\n", score);
    printf("�ܼ�score����} = %p\n", &score);
    printf("����ptr���� = %p\n", ptr);
    printf("*ptr���� = %d\n", *ptr);
    
    ptr = &score1;    /* ���w�����ܼ�ptr���ȬO�ܼ�score1����} */

    printf("�ܼ�score1���� = %d\n", score1);
    printf("�ܼ�score1����} = %p\n", &score1);
    printf("������ptr���� = %p\n", ptr);
    printf("*ptr���� = %d\n", *ptr);

    return 0;
}

