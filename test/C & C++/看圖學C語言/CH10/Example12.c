/* �ϥΫ��йB��ƻs�r�� */
#include <stdio.h>

int main() 
{
    /* �r���}�C�ŧi */
    char str[15] = "This is a pen.";  
    char str1[15];
    char *ptr, *ptr1;         /* �ŧi�r����� */
    int i = 0;
    
    ptr = str;                /* ����ptr���V�r��str */
    ptr1 = str1;              /* ����ptr1���V�r��str1 */
    
    /* �ϥΫ��йB��ƻs�r����while�j�� */
    while ( *ptr != '\0' )   
    {   
        *(ptr1+i) = *ptr++;
        i++;
    }
    *(ptr1+i) = '\0';  /* �[�W�r�굲���r�� */

    /* ��ܦr�ꤺ�e */
    printf("�N�r��str�ƻs��str1: \n");
    printf("str�r�� = \"%s\"\n", str);
    printf("str1�r�� = \"%s\"\n", str1);
    printf("ptr1 = \"%s\"\n", ptr1);

    return 0;
}

