import os

file_name = os.open('test_data.txt', os.O_RDWR)
os.write(file_name, b'I am overwriting this file 123')
os.close(file_name)
