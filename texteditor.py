"""Text Editor Demo
This example is using a single line of text.
The purpose is to read some names from a text file,
sort them and write them back (optionally in same file).
"""
democontent = "Carl Chuck Ann Joe Jack Jill Bill Steve Zach Jude Pat Rick"
# Opening the file with context manager
# (it is closed automatically when 'with' is done)
with open('textfile.txt', mode='w') as file:
    # We put the list of names into a file first.
    file.write(democontent)

# Opening the file again in read-only mode:
with open('textfile.txt', mode='r') as file:
    content = file.read()

# Sorting the names
names = sorted(content.split())
print(names)

# Create a new file to put the sorted names
# (optionally you can put them back in the original file)
with open('textfile_sorted.txt', mode='w') as file:
    file.write(' '.join(names))
