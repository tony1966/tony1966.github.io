/* ㄧ计肚把计肚患 */
#include <stdio.h>

void swap(int, int);     /* ㄧ计 */

int main() 
{
    int x = 15, y = 20;  /* 跑计 */ 
    
    printf("ユ传玡 x= %d y= %d\n", x, y); 
    
    swap(x, y);          /* ㊣swap()ㄧ计 */
    
    printf("ユ传 x= %d y= %d\n", x, y); 

    return 0;
}

/* swap()ㄧ计﹚竡 */
void swap(int x, int y) 
{
    int temp;   /* 跑计 */
    temp = x;   /* ユ传跑计 */
    x = y;
    y = temp;   
}
