/* ���o���Ы��V�ܼƪ��� */
#include <stdio.h>

int main() 
{
    int score = 85;  /* �ŧi�ܼ� */  
    int *ptr;        /* �ŧi�����ܼ�ptr�x�sint�ܼƦ�} */

    ptr = &score;    /* ���w�����ܼ�ptr���ȬO�ܼ�score����} */

    printf("�ܼ�score���� = %d\n", score);
    printf("�ܼ�score����} = %p\n", &score);
    printf("����ptr���� = %p\n", ptr);
    printf("����ptr����} = %p\n", &ptr);
    printf("*ptr���� = %d\n", *ptr);

    return 0;
}

