import unittest
import sys

sys.path.append(r"C:\Users\asisrann\Desktop\DDE\workspace\python\schoolapp\school_lib")
import school_lib

def main():
    FILENAME = "SCHOOL_MASTER_FILE.MSR"
    s_records = school_lib.get_file_records_as_list_04(FILENAME)
    print len(s_records[1:])
    print s_records[1]

    student_records = []
    for line in s_records[1:]:
        s_record = school_lib.parse_and_provide_student_data_as_tuple(line)
        student_records.append(s_record)

    print student_records


    s_dict = {}

    for record in student_records:
        roll_no = record[0]
        name = record[1]
        total_marks = sum(record[3])
        s_dict[roll_no] = (name, total_marks)

    print "==" * 30
    for k, v in s_dict.iteritems():
        print k, " == ", v

    print "==" * 30

    '''custom sorting'''
    print "custom sorting based on key"

    for k in sorted(map(int, s_dict.keys())):
        print k, " ===> ", s_dict[str(k)]

if __name__ == "__main__":
    main()