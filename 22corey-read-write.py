# File Objects - read and write files
# f = open('file.txt', 'r')  
# print(f.name) # Get the name of the file
# print(f.mode) # Get the mode in which the file was opened

# Let us use context manager
with open('file.txt', 'r') as f:
    print(f.name)
    print(f.mode)
    print(f.readline(), end='') # Read the entire content of the file
    print(f.readline(), end='') # Read the entire content of the file

# Using for loop
print("Uisng for loop")
with open('file.txt', 'r') as f:
    for line in f:
        print(line, end='') # end='' to avoid adding extra new line

# copying file content
with open('file.txt', 'r') as source_file:
    with open('copy_file.txt', 'w') as dest_file:
        for line in source_file:
            dest_file.write(line)
# copying image
with open('sidebar.png', 'rb') as img:
    with open('copy_sidebar.png', 'wb') as copy_img:
        for line in img:
            copy_img.write(line)