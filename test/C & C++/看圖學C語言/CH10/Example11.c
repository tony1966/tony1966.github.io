/* �إ߻P�ϥΦr����� */
#include <stdio.h>

int main() 
{
    /* �r���}�C�ŧi */
    char str[15] = "This is a pen.";  
    char str1[15] = "hello! world";
    char *ptr, *ptr1;           /* �ŧi�r����� */
    
    ptr = str;                  /* ����ptr���V�r��str */
    ptr1 = "This is an apple."; /* ���V�r��`�� */

    /* ��ܦr�ꤺ�e */
    printf("str�r�� = \"%s\"\n", str);
    printf("str1�r�� = \"%s\"\n", str1);
    printf("ptr = \"%s\"\n", ptr);
    printf("ptr1 = \"%s\"\n", ptr1);
    
    ptr1 = str1;    /* �r�����ptr1����Vstr1�r�� */
    
    printf("����ptr1 = \"%s\"\n", ptr1);  /* ��ܦr�ꤺ�e */

    return 0;
}

