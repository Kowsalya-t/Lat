import random
import string
import csv
import sys

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def main():
    numOfRecs = input("Enter number of records to generate : ")
    headerList = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10']
    colLengthList = [5, 12, 3, 2, 13, 7, 10, 13, 20, 13]
    fixedLengthFile = open("myFixedLengthFile.txt", "w")
    index = 0
    dataset = []
    dataset.append(headerList)
    while index < int(numOfRecs):
        line = ''
        for i in range(0,10):
            col = get_random_string(colLengthList[i])
            line =  line + " " + col
        fixedLengthFile.write(line)
        fixedLengthFile.write("\n")
        index = index + 1
    fixedLengthFile.close()

    index = 0
    fixedLengthFile = open("myFixedLengthFile.txt","r")
    fixedLenghtFileLine = fixedLengthFile.readlines()

    for record in fixedLenghtFileLine:
        dataset.append(record.split())
    fileOutput = 'csv_file_parsed.csv'
    try:
        with open(fileOutput, 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(dataset)
    except IOError:
        print("I/O error :", sys.exc_info())

if __name__ == "__main__":
    main()

