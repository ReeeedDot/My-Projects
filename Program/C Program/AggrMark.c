#include<stdio.h>
  int main()
  {
    int num_sub;
    float total_marks=0, aggrigate_marks,percentage;
    printf("Enter the no. of Subject: ");
    scanf("%d",&num_sub);
      //input marks for subject

      for(int i=1;i<=num_sub;i++)
      {
         float marks;
           printf("Enter marks for subject %d:",i);
           scanf("%f",&marks);
           total_marks+=marks;
      }

      //calculate aggregate marks and percentage

      aggrigate_marks=total_marks/num_sub;
      percentage=(total_marks/(num_sub*100))*100;


        printf("Aggrigate marks: %.2f \n",aggrigate_marks);
        printf("percentage: %.2f %% \n",percentage);
        return 0;
  }