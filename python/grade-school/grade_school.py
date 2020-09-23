from collections import defaultdict


class School(object):
    def __init__(self):
        self.__grades = defaultdict(list)

    def add_student(self, name, grade):
        self.__grades[grade].append(name)
        self.__grades[grade] = sorted(self.__grades[grade])

    def roster(self):
        nums = sorted(self.__grades.keys())
        return [x for i in nums for x in self.__grades[i]]

    def grade(self, grade_number):
        return self.__grades[grade_number]
