#include <stdio.h>

int main() {
    int a,i;
    int p;
    p=scanf("%d", &a);
    if (p==0 || a<=0)
    {
        printf("wrong input");
        return 0;
    }
    for (i = 0; i <a; ++i)
  {
    printf("Hello World\n");
  }

    return 0;
}
