"""This is the school function library module

This module contains common set of functions across school application
"""

__version__ = "1.0.0"

def get_student_info():
    """This function accept the student info from the user"""
    student_name = raw_input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    school_name = raw_input("Enter school name: ")
    class_name = input("Enter your class name(1 to 12): ")
    marks = raw_input("Enter 6 subject marks separated by comma: ")

    return (student_name, roll_number, school_name, class_name, marks)

def display_student_data(student_name, roll_number, school_name, class_name, marks):
    """This function displays the given students info"""
    print "student_name: ", student_name
    print "roll_number: ", roll_number
    print "school_name: ", school_name
    print "class_name: ", class_name
    print "marks: ", marks


def get_totoal_marks_01(*marks):
    """Calculate and return total marks"""
    total = 0
    for mark in marks:
        total = total + mark
    return total

def get_totoal_marks_02(*marks):
    """Calculate and return total marks"""
    return sum(marks)

def get_max_marks(*marks):
    """Return maximum marks"""
    return max(marks)

def is_student_passed(min_pass_mark,*marks):
    """return true if all marks above or equal to min pass mark"""
    for mark in marks:
        if mark < min_pass_mark:
            return False
    return True

def is_student_failed(min_pass_mark,*marks):
    """return true if all marks above or equal to min pass mark"""
    for mark in marks:
        if mark < min_pass_mark:
            return True
    return False

def get_avg_mark(*marks):
    """return average marks"""
    return sum(marks)/len(marks)

def parse_and_provide_student_data_as_tuple(student_record):
    """This parses the given line and return as tuple.

    sample data: 1101, Manohar Sharma, M, 60, 66, 67, 99, 62, 71
    """

    student_data_list = student_record.split(",")
    roll_no = student_data_list[0]
    s_name = student_data_list[1].strip()
    s_gender = student_data_list[2].strip()
    marks = map(int, student_data_list[3:])

    return (roll_no, s_name, s_gender, marks)

def display_student_data_02(roll_number, s_name, s_gender, marks):
    """This function displays the given students info"""
    print "student_name: ", s_name
    print "roll_number: ", roll_number
    print "school_name: ", s_gender
    print "marks: ", marks

def get_file_records_as_list_01(filename):
    """Take file name as input and return list of contents"""
    f = open(filename)
    result = []

    for line in f:
        result.append(line)
    f.close()
    return result

def get_file_records_as_list_02(filename):
    """Take file name as input and return list of contents"""
    f = open(filename)
    result = f.readlines()
    f.close()
    return result

def get_file_records_as_list_03(filename):
    """Take file name as input and return list of contents"""
    f = open(filename)
    result = []

    while True:
        line = f.readline()
        result.append(line)
        if len(line) == 0:
            break

    f.close()
    return result

def get_file_records_as_list_04(filename):
    """Take file name as input and return list of contents"""
    with open(filename) as f:
        return f.readlines();


if __name__ == "__main__":
    print get_totoal_marks_01(10, 20, 30)
    print get_totoal_marks_02(10, 20, 30)