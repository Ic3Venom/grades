/*
    Created by Julian Meyn
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FILE_GRADES "grades.txt"
#define SIZE_SCORE_MIN 0
#define SIZE_SCORE_MAX 100
#define SIZE_CHAR_MAX  127
#define COURSE_START   '@'
#define COURSE_NAME    '$'
#define GRADE_NAME     '&'
#define GRADE_START    '^'
#define CATEGORY_NAME  '<' 
#define CATEGORY_START '>'

void writeGrade(char course[], char category[], float points)
{
    FILE *file = fopen(FILE_GRADES, "a");
    
    if (courseExists(course))
    {
        if (!courseExists(category))
        {
            printf("Could not find course %s in course \"%s\"", category, course);
        }
    }
    
    courseLocation = 
    fseek(file, courseLocation, SEEK_SET);
    fclose(file);
}


void readGrade(char course[])
{
    return;
}



int totalCourses()
{
    FILE *file = fopen(FILE_GRADES, "r");
    char nextChar = 0, 
         courseCount = 0;

    rewind(file);
    while ((nextChar = fgetc(file)) != EOF)
    {
        if (nextChar == COURSE_START)
        {
            courseCount++;
        }
    }
    

    if (feof(file))
    {
        fclose(file);
        return courseCount;
    }
    else if (ferror(file))
    {
        printf("Something went wrong when accessing %s!", FILE_GRADES);
        fclose(file);
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

    rewind(file);
    courseAmount = totalCourses();

}


void update()
{

}


int courseExists(char course[])
{
    FILE *file = fopen(FILE_GRADES, "r");
    char string[SIZE_CHAR_MAX+1] = {0};
    char nextChar, char j = 0; //j could be unsigned
    long i;

    rewind(file);
    while ((nextChar = fgetc(file)) != EOF )
    {   
        i++;

        if (nextChar == COURSE_NAME)
        {
            while ((nextChar = fgetc(file)) != COURSE_NAME)
            {
                string[j] = nextChar;
                j++;
                i++;
            }

            if (strcmp(string, course) == 0)
            {
                fclose(file);
                return i - j; //returning starting offset of course, not end of course name
            }

            j = 0;
        }
    }

    if (feof(file))
    {
        fclose(file);
        return 0;
    }
    else if (ferror(file))
    {
        printf("Something went wrong when accessing %s!", FILE_GRADES);
        fclose(file); //In case the file is open despite not reaching EOF
        exit(1);
    }

}

int categoryExists(char[] course[], char[] category[])
{
    FILE *file;
    int offset = courseExists(course);
    char nextChar;

    if (offset)
    {
        file = fopen(FILE_GRADES, "r");
        fseek(file, offset, SEEK_SET);

        while((nextChar = fgetc(file)) != EOF)
        {
            printf("%c ", nextChar);
        }
        
        if (feof(file))
        {

        }
        else if (ferror(file))
        {

        }
    }
    else
    {
        return 0;
    }
}


int main()
{
    printf(">FILE START\n\n");
    int courseCount = totalCourses();
    char courseNames[SIZE_CHAR_MAX][SIZE_CHAR_MAX] = {0};
    strcpy(courseNames[0], "COURSE 1");

    printf("total courses found in file: %d\n", courseCount);
    printf("Course %s exists? %s", courseNames[0], courseExists(courseNames[0]) ? "true":"false");

    printf("\n\nFILE END<");

    return 0;
}