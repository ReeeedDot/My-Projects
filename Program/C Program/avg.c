#include<stdio.h>
#include<conio.h>
   int main()
     {
       
        float a,b,avg;
        printf("Enter the First Number: ");
        scanf("%f", &a);
        printf("Enter the Second Number: ");
        scanf("%f",&b);
        avg= (a+b)/2;
        printf(" the average of total no: %.2f",avg);
        return 0;
     }
