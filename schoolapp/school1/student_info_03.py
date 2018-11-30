"""student application

accept student data and display data
"""

class Student(object):
    """Student"""
    school_name = "christ"

    def __init__(self):
        print "student constructor called"

    def get_student_info(self):
        """Display Student Info"""
        self.student_name = raw_input("Enter student name: ")
        self.roll_number = input("Enter roll number: ")
        self.school_name = raw_input("Enter school name: ")
        self.class_name = input("Enter your class name(1 to 12): ")
        self.marks = raw_input("Enter 6 subject marks separated by comma: ")

    def display_student_data(self):
        """Display Student data"""
        print "student_name: ", self.student_name
        print "roll_number: ", self.roll_number
        print "school_name: ", self.school_name, " ==> ", Student.school_name
        print "class_name: ", self.class_name
        print "marks: ", self.marks

    @classmethod
    def get_school_name(cls):
        """Get school name"""
        return cls.school_name

    @staticmethod
    def display_average_number(n1, n2, n3):
        """Display average number"""
        avg = (n1 + n2 + n3) / 3
        print "average of 3 numbers: {}, {}, {} is {}".format(n1, n2, n3, avg)
        print "average of 3 numbers: %d, %d, %d is %d" % (n1, n2, n3, avg)

if __name__ == "__main__":
    Student.display_average_number(10, 20, 30)