#include <stdio.h>
#include <limits.h>

#define SIZE 50

int main()
{
   int array[SIZE];
   int i, max, min, size, pos1, pos2;

   printf("Enter size of the array: ");
   scanf("%d", &size);
   printf("Enter elements in the array: ");

   for(i=0; i<size; i++)
   {
       scanf("%d", &array[i]);
   }

   max = array[0];
   min = array[0];

   for(i=1; i<size; i++)
   {
       if(array[i] > max)
       {
           max = array[i];
           pos1 = i + 1;
       }
       if(array[i] < min)
       {
           min = array[i];
           pos2 = i + 1;
       }
   }

   printf("Maximum element = %d is at position %d\n", max, pos1);
   printf("Minimum element = %d is at position %d\n", min, pos2);

   return 0;

}