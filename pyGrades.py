"""
    Python version of the Grades program
"""

import pickle
from datetime import datetime
from difflib import get_close_matches
from os import system


class Grade:
    def __init__(self, name, score, maxScore, date, late=False):
        self.name = name
        self.score = score
        self.maxScore = maxScore
        self.percent = "{:.2%}".format(score/maxScore)
        self.date = date
        self.late = late

    def __str__(self):
        return "{} {} {} {} {} {}".format(
                self.name, self.score, self.maxScore,
                self.percent, self.date, self.late)

    # del/change/get methods removed: Category can just remove/recreate/search


class Category:
    def __init__(self, name, weight=None):
        self.name = name
        self.weight = weight
        self.grades = []

    def __str__(self):
        gradeStr = ""
        for i in self.grades:
            gradeStr += i.__str__()
        return "{} {}".format(
            self.name, self.weight) + gradeStr

    def addGrade(self, name, score, m, d=datetime.now(), l=False):
        if self.verify(name):
            self.grades.append(Grade(name, score, m, d, l))

    def delGrade(self, name):
        for i in self.grades:
            if i.name.lower() == name.lower():
                self.grades.pop(i)

    def verify(self, name):
        for i in self.grades:
            if i.name.lower() == name.lower():
                return False
        else:
            return True


class Course:
    def __init__(self, name, weighted=False):
            self.categories = []
            self.name = name
            self.weighted = weighted

    def __str__(self):
        return "{} {}".format(self.name, self.weighted)

    def addCategory(self, name, weight=None):
        if self.verify(name):
            self.categories.append(Category(name, weight))
            self.getTotalWeight()
        else:
            print("Category {} already exists".format(name))
            # return NameError

    def delCategory(self, name):
        if self.valid(name):
            self.categories.pop(i)
        else:
            print("Category {} does not exist".format(name))
            # return NameError

    def changeWeight(self):
        names = self.getAllNames()

        while(True):
            print("What category do you want to change the weight of?")
            userInput = input(">>> ")

            if userInput.lower() == 'quit':
                system('pause')
                exit(0)
            elif userInput.lower() in [i.lower() for i in names]:
                while(True):
                    print("What would you like to change it to? (Now at {}%)"
                          .format(self.getCategory(userInput).weight))
                    newWeight = input(">>> ").rstrip("%")

                    if newWeight == "quit":
                        system('pause')
                        exit(0)
                    try:
                        self.getCategory(userInput).weight = float(newWeight)
                        return
                    except ValueError:
                        print("'{}' is not a valid input."
                              " Try again or type 'quit'"
                              .format(newWeight))
            elif len(get_close_matches(userInput, names, 1)) > 0:
                print("Unknown category '{}'. Did you mean category '{}'?"
                      .format(
                        userInput, get_close_matches(userInput, names, 1)[0]))

    def getAllNames(self):
        names = []
        for i in self.categories:
            names.append(i.name)

        return names

    def getCategory(self, name):
        for i in self.categories:
            if i.name.lower() == name.lower():
                return i
        else:
            print("Category {} does not exist".format(name))
            # return NameError

    def getTotalWeight(self):
        weight = 0
        for i in self.categories:
            weight += i.weight

        if weight > 100:
            print("This category's total weight exceeds 100% ({}%).\
                  \nDo you want to change the category's weights? (Y/N)"
                  .format(weight))
            userInput = input(">>> ")

            if userInput.lower() in 'yes':  # Intentional: can enter 'ye'
                self.changeWeight()
            else:
                print("Because you do not want to change this class's \
                    category weights, you may not\nice your grade \
                    percentage \ to change.")

    def verify(self, name):
        for i in self.categories:
            if i.name.lower() == name.lower():
                return False
        else:
            return True


def getCourseName(courses):
    names = []
    for i in courses:
        names.append(i.name)

    return names


def findCourse(courses, name):
    for i in courses:
        if i.name.lower() == name.lower():
            return i
    else:
        return NameError


def clearFile():
    with open("grades.bin", "w") as file:
        file.write("")


def read():
    with open("grades.bin", "rb") as file:
        courses = pickle.load(file)

    return courses


def rm(courses, courseName):
    courses.pop(courseName)


def write(courses):
    with open("grades.bin", "wb") as file:
        pickle.dump(courses, file)


def cleanCoursePrint(course) -> None:
    crs = """\
Course Name: {0}
Weighted Course? {1}
Categories:
"""
    category = """\
\tCategory name: {0}
\tWeight: {1}%
\tGrades:
"""
    grade = """\
 \t   {0:<5}Grade name: {1}
\t\tScore: {2}/{3}
\t\tPercent: {4}
\t\tAssigned: {5}
\t\tLate? {6}\
"""

    print(crs.format(course.name, course.weighted))

    for i in course.categories:
        print(category.format(i.name, i.weight))

        for n, j in enumerate(i.grades):
            print(grade.format(n+1, j.name, j.score, j.maxScore, j.score,
                               j.date, j.late))
        else:
            print("")  # Print newline after all grades in category are printed


def main():
    crs1 = Course("CS38", True)
    crs1.addCategory("Tests", 50)
    crs1.getCategory("Tests").addGrade("test1", 86, 100)
    crs1.addCategory("Quizzes", 20)
    crs1.getCategory("Quizzes").addGrade("popquiz1", 20, 22)
    crs1.addCategory("Homework", 10)
    crs1.getCategory("Homework").addGrade("assignment1", 10, 10)

    crs2 = Course("Algebra1", True)
    crs2.addCategory("Tests", 50)
    crs2.addCategory("Quizzes", 20)
    crs2.addCategory("Homework", 10)
    crs2.addCategory("Participation", 10)
    crs2.addCategory("Projects", 10)  # 100 instead of 10
    crs2.getCategory("Tests").addGrade("Chapter 1 Test", 120, 124)
    crs2.getCategory("Tests").addGrade("Chapter 2 Test", 115, 124)

    write([crs1, crs2])
    courses = read()

    cleanCoursePrint(crs1)
    cleanCoursePrint(crs2)

    exit(0)

    '''
    while True:
        print("What would you like to do? (Type 'help' for more info)")
        userInput = input(">>> ")
        parse = userInput.split(" ")

        if parse[0] == "help":
            break
        elif parse[0] == "get":

            break
        elif parse[0] == "find":
            try:
                if findCategory(parse[1]):
                    print( findCategory(parse[1]).__str__() )
                    break
                else:
                    print("You did not supply a category.")
            except NameError:
                print("Category {} does not exist.".format(parse[1]))
        elif parse[0] == "show":
            break
        elif parse[0] == "new":
            print("New )
            break
        else:
            print("Unknown command '{}'. Try again.".format(userInput))

        break'''

if __name__ == '__main__':
    main()
