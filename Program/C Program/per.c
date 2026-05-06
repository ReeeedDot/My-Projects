#include<stdio.h>
#include<conio.h>
   int main()
     {
       
        float hindi,eng,math,sci,com;
        float per;

        printf("Enter five subjects marks: ");
        scanf("%f%f%f%f%f",&hindi,&eng,&math,&sci,&com);
        per=(hindi+eng+math+sci+com)/5.0;
        printf("Percentage of total marks obtained : %.2f",per);
        return 0;
     }
