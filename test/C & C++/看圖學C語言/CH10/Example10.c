/* �b��ƨϥΫ��ШӶǻ��}�C�Ѽ� */
#include <stdio.h>
#define LENGTH  5           /* �w�q�`�� */

int total(int *, int);    /* ��ƭ쫬�ŧi */

/* �bmain()��ƩI�stotal()��� */ 
int main() 
{
    int i;              /* �ŧi�ܼ� */  
    int result;

    int tests[LENGTH];  /* �ŧi��ư}�C�A�x�sLENGTH�Ӥ��� */

    for ( i = 0; i < LENGTH; i++ )  /* for�j���J���Z */
    {
        printf("�п�J��%d��ǥͪ����Z => ", (i+1)); 
        scanf("%d", &tests[i]);
    }

    result = total(tests, LENGTH);       /* �I�s��� */ 

    printf("���Z�`��: %d\n", result);    /* ����`�� */
    
    return 0;
}

/* total()��ƪ��w�q */
int total(int *t, int len)
{
    int i;
    int sum = 0;

    for ( i = 0; i < len; i++ )  /* for�j��p���`�� */
        sum = sum + *(t+i); 

    return sum;
}

