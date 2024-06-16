# break -> takes loop execution out of loop
# pass -> takes loop execution to start of loop

for counter in range(1, 11):
    if counter == 5:            # condition became true the loop executes again from start
        pass
    else:
        print(counter)

for i in range(1, 31):
    if i % 3 == 0:              # Printing odd values
        print(i)

for i in range(1, 31):
    if i % 3 != 0:              # Printing odd values
        pass
    else:
        print(i)
