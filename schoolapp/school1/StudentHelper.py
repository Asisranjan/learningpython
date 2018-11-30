""" student application

This applications accept students data and displays it
"""

import datetime
import calendar

class StudentHelper:
    students_data = []
    def StudentHelper(self):
        print "student helper"

    def accept(self):
        student_name = raw_input("Enter Student name : ")
        gender = raw_input("Enter gender: ")

        student_tuple = (student_name, gender)
        self.students_data.append(student_tuple)

    def dumpData(self):
        print "Dump student raw_inputs.."
        name = raw_input("Enter your name : ")
        nokia_id = raw_input("Enter Nokia id : ")
        today = datetime.datetime.today()
        file_name = name + "_" + str(nokia_id) + "_" + str(today.day) + "_" + calendar.month_name[
            today.month] + "_" + str(today.year) + ".txt"
        print file_name
        f = open(file_name, "w")
        f.write("student_name, gender\n")

        for student in self.students_data:
            f.write(student[0] + ", " + student[1] + "\n")

        f.close()


if __name__ == "__main__":
    sh = StudentHelper();
    i = 0
    total_student  = 1
    while i < total_student:
        sh.accept();
        i = i + 1

    sh.dumpData()