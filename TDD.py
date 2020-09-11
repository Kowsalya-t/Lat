import unittest
import os
import sys
import string

TEST_FAILED = 0
def test_file_created():
    if os.path.exists(os.path.dirname(sys.argv[0])+'/csv_file_parsed.csv') == True:
        print("File created ok..")
    else:
        TEST_FAILED = TEST_FAILED + 1
        print("No file created")

def test_file_empty():
    if os.stat(os.path.dirname(sys.argv[0])+'/csv_file_parsed.csv').st_size != 0:
        print("File not empty ok ..")
    else:
        TEST_FAILED = TEST_FAILED + 1
        print("File empty")

def test_record_lengths():
    if os.stat(os.path.dirname(sys.argv[0]) + '/csv_file_parsed.csv').st_size != 0:
        file1 = open(os.path.dirname(sys.argv[0]) + '/csv_file_parsed.csv', 'r')
        Lines = file1.readlines()
        count = 0
        for line in Lines:
            if count != 0 and count % 2 == 0 and  line.count(",") == 9 :
                print("ok ..")
            else:
                if count % 2 == 0 and count != 0:
                    print ("Test Failed, Check no of columns in record " + str(count))
                    TEST_FAILED = TEST_FAILED + 1

            count = count +1

def tdd():
    test_file_created()
    test_file_empty()
    test_record_lengths()
    
    if TEST_FAILED > 0:
        print("Test Failed")
    else:
        print("Test Passed")

if __name__ == "__main__":
    tdd()