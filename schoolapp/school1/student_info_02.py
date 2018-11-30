"""student application

accept student data and display data
"""

def get_student_info():
    global student_name, roll_number, school_name, class_name, marks
    student_name = raw_input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    school_name = raw_input("Enter school name: ")
    class_name = input("Enter your class name(1 to 12): ")
    marks = raw_input("Enter 6 subject marks separated by comma: ")

def display_student_data():
    print "student_name: ", student_name
    print "roll_number: ", roll_number
    print "school_name: ", school_name
    print "class_name: ", class_name
    print "marks: ", marks

if __name__ == "__main__":
    get_student_info()
    display_student_data()