#This code renames filenames with extension .hpp to .h using a list comprehension

filenames = ["file1.hpp", "file2.cpp", "file3.hpp", "file4.hpp"]

newfilenames = [filename.replace(".hpp", ".h") if filename.endswith(".hpp") else filename for filename in filenames]

print(newfilenames)
