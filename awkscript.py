import os

# Define a sample text file to work with
filename = "example.txt"
with open(filename, "w") as f:
    f.write("Hello, world!\n")
    f.write("This is a sample text file.\n")
    f.write("It contains multiple lines of text.\n")
    f.write("We will use awk, sed, and grep to process this file.\n")

# Use awk to print the second field of each line
awk_command = "awk '{print $2}' " + filename
os.system(awk_command)

# Use sed to replace "multiple" with "many"
sed_command = "sed -i 's/multiple/many/g' " + filename
os.system(sed_command)

# Use grep to find all lines containing the word "sample"
grep_command = "grep 'sample' " + filename
os.system(grep_command)

