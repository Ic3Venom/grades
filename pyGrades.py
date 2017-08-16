"""
    Python version of the Grades program
"""

import pandas
import pickle
from datetime import datetime
from difflib import get_close_matches


class Grade:
    def __init__(self, title, score, maxScore, date, late=False):
        self.title = title
        self.score = score
        self.maxScore = maxScore
        self.percent = "{:.2%}".format(score/maxScore)
        self.date = date
        self.late = late

    def __str__(self):
        print("{} | {} | {} | {} | {}\n\n".format(
            self.title, self.date, self.score,
            self.maxScore, self.percent))


class Course:
    def __init__(self, name, weighted=False):
            self.categories = []
            self.name = name
            self.weighted = weighted

    def addCategory(self, key, weight=None):
        self.categories.append({key: [(weight)]})

    def addGrade(self, c, t, s, m, d=datetime.now(), l=False):
        key = self.findCategory(c)[1:]
        self.categories[key[0]][key[1]] += [Grade(t, s, m, d, l)]

    def findCategory(self, category):
        for i, j in enumerate(self.categories):
            if str(list(j.keys())[0]).lower() == category.lower():
                return [j, i, list(j.keys())[0]]
        else:
            return None

    def findGrade(self, category, assignment):
        pass

    def isValid(self, category):
        return NotImplementedError

        if self.findCategory(category):
            return NameError

    def __str__(self):
        return "{}{}\n{:>12}{}\n{:>12}{}\n{:>12}{}" \
               .format(self.name, ".__str__(): ",  # remove this format later
                       "Name: ", self.name,
                       "Weighted? ", self.weighted,
                       "Categories: ", self.categories)


def findCourse(courses, courseName):
    for i in courses:
        if i.name.lower() == courseName.lower():
            return i
    else:
        return None


def main():
    courses = []
    courses.append(Course("CS38", True))
    crs = courses[0]

    crs.addCategory("Tests", 50)
    crs.addGrade("Tests", "test1", 86, 100)
    crs.addCategory("Quizzes", 20)
    crs.addGrade("Quizzes", "popquiz1", 20, 22)
    crs.addCategory("Homework", 10)
    crs.addGrade("Homework", "assignment1", 10, 10)
    crs.findGrade("Homework", "assignment1")
    try:
        crs.addGrade("Homework", "assignment1", 10, 10)
        crs.isValid("Homework")
    except NameError:
        print("Assignment already exists")

    print(findCourse(courses, "CS38"))
    print(crs.findCategory("Tests")[0])
    print("\n\n\n")
    for i in crs.categories:
        for j in i.keys():
            print(i[j][1].__str__())

if __name__ == '__main__':
    main()
