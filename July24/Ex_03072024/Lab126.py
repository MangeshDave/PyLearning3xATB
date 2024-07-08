# File IO

with open('Dummy_File.txt', 'r') as file:
    print(file.read())

with open('C:/Users/ADMIN$/PycharmProjects/PyLearning3xATB/July24/Ex_01072024/Demo_File_FileIO.txt', 'r') as file1:
    print(file1.read())

with open(r'C:\Users\ADMIN$\PycharmProjects\PyLearning3xATB\July24\Ex_01072024\Demo_File_FileIO.txt', 'r') as file2:
    print(file2.read())

with open(r'C:\\Users\\ADMIN$\\PycharmProjects\\PyLearning3xATB\\July24/Ex_01072024\\Demo_File_FileIO.txt', 'r') as file3:
    print(file3.read())

