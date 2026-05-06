#include<stdio.h>
  int main()
   {
    float distance_meters,distance_inches,distance_feet,distance_centimeters,distance_kilometers;
       printf("Enter the distance in kilometers: ");
       scanf("%f",&distance_kilometers);

           distance_feet=distance_kilometers*3280.84;
           distance_inches=distance_kilometers*39370.08;
           distance_centimeters=distance_kilometers*100000;
           distance_meters=distance_kilometers*1000;

        printf("Distance in feet: %.2f\n",distance_feet);
        printf("Distance in inches: %.2f\n",distance_inches);
        printf("Distance in centimeters: %.2f\n",distance_centimeters);
        printf("Distance in meters: %.2f\n",distance_meters);

        return 0;
   }