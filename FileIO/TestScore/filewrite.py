import os

f = open("./myfile.txt", "a")
f.write("test\n")
#with open("myfile.txt", "a") as f:
 #   f.write("test\n")

print(os.getcwd())

f.close()