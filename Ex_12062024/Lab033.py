# Loop -> Repeat a block of code multiple times

# For

# Print Hello World 10 times
for i in range(10):
    print("Hello World", i)

# Print Hello World 5 times starting from 5th index to 10th index
for i in range(5, 10):
    print("Hello World", i)

# Range -> range(start, stop, step)

# Print Hello World 5 times starting from 1st index to 10th index with step of 2 - Odd values printing
for i in range(1, 10, 2):       #Here each loop statement is executed with increment of 2
    print("Hello World", i)

# Print Hello World 5 times starting from 1st index to 10th index with step of 2 - Even values printing
for i in range(0, 10, 2):       #Here each loop statement is executed with increment of 2
    print("Hello World", i)