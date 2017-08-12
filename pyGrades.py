"""
    Python version of the Grades program
"""

import pandas
import pickle
from difflib import get_close_matches


class Course:
    courses = []

    def __init__(self, name, weighted=False):
            self.categories = []
            self.name = name
            self.weighted = weighted

    def addCategory(self, key, weight=None):
        self.categories.append({key: {"Weight": weight}})

    def addGrade(self, category, title, score, maxScore):
        percent = "{0:.2%}".format((score/maxScore))
        self.categories.append(
            {title: [score, maxScore, percent]}
        )

    def findCourse(userInput):
        courseNames = []

        for course in Course.courses:
            courseNames.append(course.name)

        if userInput in [x.lower() for x in courseNames]:
            for course in Course.courses:
                if course.name.lower() is userInput.lower():
                    return course
        elif len(get_close_matches(userInput,
                [x.lower() for x in courseNames])) > 0:

            print("Unknown course {0}".format(userInput))
            print("Did you mean to type one of these courses?")

            for i, j in enumerate(
                    get_close_matches(userInput, 
                        [x.lower() for x in courseNames], 5)):
                print("{0}: {1}".format(i+1, j))

            return None
        else:
            print("The course name '{0}' does not exist. Try again"
                  .format(userInput))
            return None

    def findCategory(userInput):
        userInput = userInput.lower()
        keys = []

        for i in self.categories:
            keys.append(i.lower())

        if category in self.categories:
            return self.categories[category]
        elif len(get_close_matches(userInput, self.categories.keys(), 5)) > 0:
            print("Unknown category {0}".format(category))
            print("Did you mean to type one of these categories?")

            for i, j in enumerate(
                    get_close_matches(userInput, self.categories.keys(), 5)):
                print("{0}: {1}".format(i+1, j))

            return None
        else:
            print("The word '{0}' does not exist. Try again".format(userInput))
            return None

    def __str__(self):
        return "{}{}\n{:>12}{}\n{:>12}{}\n{:>12}{}" \
               .format(self.name, ".__str__(): ",  # remove this format later
                       "Name: ", self.name,
                       "Weighted? ", self.weighted,
                       "Categories: ", self.categories)


def main():
    Course.courses.append(Course("CS38"))
    Course.courses[0].addCategory("Tests", 50)
    Course.courses[0].addGrade("Tests", "test1", 100, 100)
    Course.courses[0].addCategory("Quizzes", 20)
    Course.courses[0].addGrade("Quizzes", "popquiz1", 20, 22)
    Course.courses[0].addCategory("Homework", 10)
    Course.courses[0].addGrade("Homework", "assignment1", 10, 10)

    validCategory = None
    while validCategory is None:
        print("What course do you want to know about?")
        userInput = input(">>> ")
        validCategory = Course.findCourse(userInput.lower())

    print(validCategory.__str__())
if __name__ == '__main__':
    main()
