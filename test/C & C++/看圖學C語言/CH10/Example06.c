/* ��ƪ��ǭȰѼƶǻ� */
#include <stdio.h>

void swap(int, int);     /* ��ƭ쫬�ŧi */

int main() 
{
    int x = 15, y = 20;  /* �ŧi�ܼ� */ 
    
    printf("�洫�e x= %d y= %d\n", x, y); 
    
    swap(x, y);          /* �I�sswap()��� */
    
    printf("�洫�� x= %d y= %d\n", x, y); 

    return 0;
}

/* swap()��ƪ��w�q */
void swap(int x, int y) 
{
    int temp;   /* �ŧi�ܼ� */
    temp = x;   /* �洫�ܼƭ� */
    x = y;
    y = temp;   
}
