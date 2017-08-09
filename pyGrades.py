"""
    Python version of the Grades program
"""

import pandas
import pickle


class Course:

    def __init__(self, name, weighted=True):
            self.categories = []
            self.name = name
            self.weighted = weighted

    def addCategory(self, key, value={"Weight": 0}):
        self.categories.update({key: value})

    def addGrade(self, category, title, grade):
        self.categories[category].update({title: grade})

    def findCategory(self, category):
        i = 0
        for j in self.categories:
            i += 1

            if j == category:
                return i

        return -1

    def __str__(self):
        return "Name:       {0}\nWeighted?   {1}\nCategories: {2}" \
               .format(self.name, self.weighted, self.categories)


def main():
    crs = Course("CS38", False)

    print(crs.__str__())


if __name__ == '__main__':
    main()
