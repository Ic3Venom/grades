#include <stdio.h>
#include <stdlib.h>

#define FILE_GRADES "grades.txt"
#define FILE_COURSES "courses.txt"

int totalCourses()
{
    FILE *file = fopen(FILE_GRADES, "r");
    int courseCount = 0;
    int nextChar;

    while ((nextChar = fgetc(file)) != EOF)
    {
        printf("%c ", nextChar);
        if (nextChar == '@')
        {
            courseCount++;
        }
    }

    if (feof(file))
    {
        fclose(file);
        return courseCount;
    }
    else
    {
        printf("Something went wrong when accessing %s!", FILE_GRADES);
        fclose(file);
        exit(1);
    }

}

void main()
{
    printf("%d", totalCourses());

}