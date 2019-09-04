"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
import os

script_dir = os.path.dirname(__file__)
rel_path = "foo.txt"
abs_file_path = os.path.join(script_dir, rel_path)

print(script_dir)
print(f'absolute path {abs_file_path}')

# with open(abs_file_path) as f:
#     read_data = f.read()
#     print(read_data)


f = open(abs_file_path, 'r')

for i in f:
    print(i, end='')

f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
import os

script_dir = os.path.dirname(__file__)
rel_path = "bar.txt"
abs_file_path = os.path.join(script_dir, rel_path)

print(script_dir)
print(f'absolute path {abs_file_path}')

listFile = ['line1', 'line2','line3']

f = open(abs_file_path, 'w')

for i in listFile:
    f.write(i+'\n')

f.close()

f = open(abs_file_path, 'r')

for i in f:
    print(i, end='')

f.close()