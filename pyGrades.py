"""
    Python version of the Grades program
"""

import pandas
import pickle
from difflib import get_close_matches


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
        if category in self.categories:
            return self.categories[category]
        elif len(get_close_matches(category, self.categories.keys(), 5)) > 0:
            print("Unknown category {0}".format(category))
            print("Did you mean to type one of these words?")

            for i, j in enumerate(
                    get_close_matches(category, self.categories.keys(), 5)):
                print("{0}: {1}".format(i+1, j))

            return None
        else:
            print("The word '{0}' does not exist. Try again".format(category))
            return None

    def __str__(self):
        return "{}{}\n{:>12}{}\n{:>12}{}\n{:>12}{}" \
               .format(self.name, ".__str__(): ",  # remove this format later
                       "Name: ", self.name,
                       "Weighted? ", self.weighted,
                       "Categories: ", self.categories)


def main():
    crs = Course("CS38", False)

    print(crs.__str__())


if __name__ == '__main__':
    main()
