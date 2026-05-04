file = open('example.txt', 'a')
file.write('Hello, world!\n')
file.close()

file = open('example.txt', 'r')
print(file.read())         # show what we read