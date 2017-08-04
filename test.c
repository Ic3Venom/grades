#include <stdio.h>
#include <stdlib.h>

#define FILE_GRADES "grades.txt"
#define FILE_COURSES "courses.txt"

void main()
{
    FILE *file = fopen(FILE_GRADES, "r");

    char arr[] = "woweee";
    char x[] = "!";


    printf("%s", strcat(arr, x));

}