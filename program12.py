'''
Katellyn Hyker
Chapter 4 Project 12
Write a program that asks for a filename and prints to the terminal a report of the wages paid to the employees for the given period
Report should be in tabular format with a header consisting of name, hours, and wages.

'''
data_file = input("Enter the name of the txt file: ").strip(" ")
#input_file = "program12Data.txt"
print('%5s%10s%15s' % ('Name', 'Hours', 'Total Pay'))
with open(data_file, 'r') as reader:
    for line in reader:
        dataList = line.strip().split()
        name = str(dataList[0])
        hours = int(dataList[1])
        payRate = float(dataList[2])
        totalPay = hours * payRate
        print('%-15s%-10d%-10d' % (name, hours, totalPay))