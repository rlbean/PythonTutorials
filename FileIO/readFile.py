# grab access to the file name -- relative path ./info/data.txt
input_file_name = "data.txt"

infile = open(input_file_name, "r") # open file to read contents
print(infile.readline())
#infile.read() -- whole file
#infile.readline() -- one line at the time
#infile.readlines() - to read each line of code

#Print all of he languages line by line
for line in infile:
    print(line)

infile.close() # close it at the end so that we save resources