/*
    Created by Julian Meyn
*/

#include <stdio.h>
#include <stdlib.h>

#define FILE_GRADES "grades.txt"
#define FILE_COURSES "courses.txt"
#define MAX 100
#define MIN 0
#define ARR_SIZE 50
#define COURSE_SENTINEL '@'
#define NAME_SENTINEL '$'

void writeGrade(char course[], char category[], float points)
{
    FILE *file = fopen(FILE_GRADES, "a");
    fclose(file);
}


void readGrade(char course[])
{
}



int totalCourses()
{
    FILE *file = fopen(FILE_GRADES, "r");
    int nextChar, courseCount = 0;
    
    while ((nextChar = fgetc(file)) != EOF)
    {
        if (nextChar == COURSE_SENTINEL)
        {
            courseCount++;
        }
    }
    if (feof(file))
    {
        return courseCount;
    }
    else
    {
        printf("Something went wrong when accessing %s!", FILE_GRADES);
        exit(1);
    }

}

void calculateGrade(char course[])
{
    FILE *file = fopen(FILE_GRADES, "r");

}


void calculateAllGrades()
{
    FILE *file = fopen(FILE_GRADES, "r");
    int i = 0, courseAmount = 0;
    int beginLine, endLine;
    char findSentinel;

    courseAmount = totalCourses();

}


void update()
{

}


int courseExists(char course[])
{
    FILE *file = fopen(FILE_GRADES, "r");
    char string[ARR_SIZE] = {0};

    while (fscanf(file, "%s", &string) != EOF) {
        if (strcmp(string, strcat(NAME_SENTINEL, course)) == 0)
        {
            return 1;
        }
    }
    if (feof(file))
    {
        return 0;
    }
    else 
    {
        printf("Something went wrong when accessing %s!", FILE_GRADES);
        exit(1);
    }

}


int main()
{
    printf("FILE START\n");
    int courseCount = totalCourses();
    char courseNames[ARR_SIZE][ARR_SIZE] = {0};

    printf("%s\n", FILE_GRADES);
    printf("%d\n", &courseCount);
    printf("%d", courseExists("$COURSE"));


    printf("\nFILE END");

    return 0;
}