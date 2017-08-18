"""
    Python version of the Grades program
"""

import pandas
import pickle
from datetime import datetime
from difflib import get_close_matches


class Grade:
    def __init__(self, name, score, maxScore, date, late=False):
        self.name = name
        self.score = score
        self.maxScore = maxScore
        self.percent = "{:.2%}".format(score/maxScore)
        self.date = date
        self.late = late

    def __str__(self):
        return("Name: {}; Score: {}; Max Score: {}; Date: {}; Late? {}".format(
            self.name, self.date, self.score,
            self.maxScore, self.percent))


class Category:
    def __init__(self, name, weight=None):
        self.name = name
        self.weight = weight
        self.grades = []

    def verify(self, name):
        for i in self.grades:
            if i.name.lower() == name.lower():
                return False
        else:
            return True

    def addGrade(self, name, score, m, d=datetime.now(), l=False):
        if self.verify(name):
            self.grades.append(Grade(name, score, m, d, l))

    def delGrade(self, name):
        for i in self.grades:
            if i.name.lower() == name.lower():
                self.grades.pop(i)

    def __str__(self):
        return ("Name: {}; Weight: {}% \n{}".format(
            self.name, self.weight, [i.__str__() for i in self.grades]))


class Course:
    def __init__(self, name, weighted=False):
            self.categories = []
            self.name = name
            self.weighted = weighted

    def getCategory(self, name):
        for i in self.categories:
            if i.name.lower() == name.lower():
                return i
        else:
            print("Category {} does not exist".format(name))
            # return NameError

    def addCategory(self, name, weight=None):
        if self.verify(name):
            self.categories.append(Category(name, weight))
        else:
            print("Category {} already exists".format(name))
            # return NameError

    def delCategory(self, name):
        if self.valid(name):
            self.categories.pop(i)
        else:
            print("Category {} does not exist".format(name))
            # return NameError

    def verify(self, name):
        for i in self.categories:
            if i.name.lower() == name.lower():
                return False
        else:
            return True

    def __str__(self):
        return "{}{}\n{:>12}{}\n{:>12}{}\n" \
               .format(self.name, ".__str__(): ",  # remove this format later
                       "Name: ", self.name,
                       "Weighted? ", self.weighted)


def findCourse(courses, name):
    for i in courses:
        if i.name.lower() == name.lower():
            return i
    else:
        print("Course {} does not exist".format(name))
        # return NameError


def main():
    courses = []
    courses.append(Course("CS38", True))
    crs = courses[0]

    crs.addCategory("Tests", 50)
    crs.getCategory("Tests").addGrade("test1", 86, 100)
    crs.addCategory("Quizzes", 20)
    crs.getCategory("Quizzes").addGrade("popquiz1", 20, 22)
    crs.addCategory("Homework", 10)
    crs.getCategory("Homework").addGrade("assignment1", 10, 10)

    for i in crs.categories:
        print(i.__str__())

if __name__ == '__main__':
    main()
