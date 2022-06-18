

f = open("newfile.txt", "w")

f.write("Introduction to Python")

f = open("newfile.txt", "r")
print(f.read())
f.close()

f = open("newfile.txt", "a")

f.write("\nPython Intermediate")
f = open("newfile.txt", "r")
print(f.read())
f.close()