import random
import string
import csv
import sys

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def generate_fixed_file(numOfRecs,colLengthList,fixedLengthFileName):
    index = 0
    fixedLengthFile = open(fixedLengthFileName, "w")
    while index < int(numOfRecs):
        line = ''
        for i in range(0,10):
            col = get_random_string(colLengthList[i])
            line =  line + " " + col
        fixedLengthFile.write(line)
        fixedLengthFile.write("\n")
        index = index + 1
    fixedLengthFile.close()

def generate_csv_file(dataset,fixedLengthFileName,csvFileName):
    index = 0
    fixedLengthFile = open(fixedLengthFileName, "r")
    fixedLenghtFileLine = fixedLengthFile.readlines()

    for record in fixedLenghtFileLine:
        dataset.append(record.split())
    fileOutput = csvFileName
    try:
        with open(fileOutput, 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(dataset)
    except IOError:
        print("I/O error :", sys.exc_info())

def main():
    numOfRecs = input("Enter number of records to generate : ")

    #Define Header and column length
    headerList = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10']
    colLengthList = [5, 12, 3, 2, 13, 7, 10, 13, 20, 13]

    dataset = []
    dataset.append(headerList)
    fixedLengthFileName = "myFixedLengthFile.txt"
    csvFileName = 'csv_file_parsed.csv'

    generate_fixed_file(numOfRecs,colLengthList,fixedLengthFileName )
    generate_csv_file(dataset,fixedLengthFileName,csvFileName)

if __name__ == "__main__":
    main()