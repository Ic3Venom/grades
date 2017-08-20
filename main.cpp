#include <iostream>

#define CATEGORIES  3
#define TASKS_MAX   5

int     total           (int scores[][TASKS_MAX], int section);
float   average         (int scores[][TASKS_MAX], int section);
float   weightCalculate (int realTotal, int highTotal, int weight);

void main()
{
    int scoresMax[CATEGORIES][TASKS_MAX]= {{60,36,54,48,54},{50,50,50,50,50},{100,100,100,100,100}};
    int scoresAct[CATEGORIES][TASKS_MAX]= {{57,46,54,48,54},{48,46,50,48,50},{91,95,100,85,98}};
    int weight[CATEGORIES]= {20, 30, 50};

    int scoresMaxTotal[CATEGORIES]{};
    int scoresActTotal[CATEGORIES]{};

    for (int i= 0; i < CATEGORIES; i++)
    {
        scoresMaxTotal[i] = total(scoresMax, i);
        scoresActTotal[i] = total(scoresAct, i);
    }

    {
        static float thing{0};
        for (int i= 0; i < CATEGORIES; i++)
        {
            thing += weightCalculate(scoresActTotal[i], scoresMaxTotal[i], weight[i]);
        }
        std::cout << thing *100<< std::endl;
    }
}
/*
UNFINISHED; plans to allow grades to be put into files
void fileRead(int scoresHigh[][TASKS_MAX]) {}
*/
int total(int scores[][TASKS_MAX], int section)
{
    int scoresTotal{0};

    for (int i= 0; i < TASKS_MAX; i++)
    {
        scoresTotal += scores[section][i];
    }

    return scoresTotal;
}

float weightCalculate(int realTotal, int highTotal, int weight)
{
    return  (static_cast<float>(realTotal)/ static_cast<float>(highTotal)) *
            (static_cast<float>(weight)   / 100);
}
