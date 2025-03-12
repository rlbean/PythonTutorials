#create filename variables
output_file_name = "output.txt"

# Open the file to write to it - overwrite current file
#outfile = open(output_file_name, "w") 

#Open file to write -- add to end -- append
outfile = open(output_file_name, "a")

#writes a string to the file
outfile.write("Hank Jacobson\n")

#outfile.write(lines) #write a list of lines to the file

outfile.close() # close it when you are done

#OR use open with to manage open/close better

with open(output_file_name, "a") as outfile:
    outfile.write("Felix Armstrong \n")
