names = input("Enter the names:")
count = 0
for i in names:
    for j in i:
        if j == "a":
            count = count + 1
print(count)
