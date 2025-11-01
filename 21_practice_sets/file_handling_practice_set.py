# 1 . 
    # Create a text file notes.txt using Python and write "Learning Python is fun!" into it.
    # Open notes.txt, read its content, and print it to the console.

# with open("note.txt","r") as f:
#     print(f.read())


# 2 . 
    # Write a program that writes three lines of text to a file tasks.txt.
    # Open tasks.txt in append mode and add a new line "Task Completed!".
    # Read the file and print all lines as a list using readlines().

# with open("task.txt","w") as f:
#     f.write("hello mister john i hope you are doing well there in chennai \n")
#     f.write("I am also doing fine here in Raipur\n")
#     f.write("Hope to meet you soon\n")

# with open("task.txt","a") as f:
#     f.write("i almost forgot to tell you that i will be visiting chennai for a meeting soon take care")


# with open("task.txt","r") as f:
#     for i in f.readlines():
#         print(i)


# 3. 
    # Use the os module to:
    #     Print the current working directory
    #     List all files and folders in the current directory
    #     Create a new folder my_folder
    # Use the shutil module to:
    #     Copy a file from one folder to another
    #     Move a file to a new folder 
    #     Delete a file (careful: irreversible!)


import os
import shutil

# print(a:= os.getcwd())
# print(os.listdir(a))
# os.mkdir("my_folder")

# shutil.copy("task.txt", "my_folder/task.txt")
# shutil.move("task.txt", "my_folder/task.txt")
# shutil.rmtree("my_folder")

# 4. Write a small script count_lines.py that takes a filename as input and prints how many lines are in the file.

# Write a command-line utility search_word.py that takes two arguments:

#     A filename
#     A word to search and prints how many times the word appears in the file.


import sys

# def count_lines(filename):
#     with open(filename) as f:
#         return len(f.readlines())


# if __name__ == "__main__":
#     filename = sys.argv[1]
#     num_lines = count_lines(filename)
#     print(f"there are {num_lines} lines in {filename}")


# def search_word(filename,word):
#     with open(filename) as f:
#         l = f.read().split(" ")
#         return l.count(word)


# if __name__ == "__main__":
#     filename = sys.argv[1]
#     word = sys.argv[2]
#     num_word = search_word(filename,word)
#     print(f"there are {num_word} occurences of '{word}' in {filename}")


# Bonus : 


    # Write a program that reads a file and creates another file with all words converted to uppercase.
    # Create a script that deletes all .tmp files from the current directory using os and os.remove().
    # Write a Python command-line tool that takes a folder name and prints the total size of all files inside it (use os.path.getsize()).


# def upper_copy(filename):
#     with open(filename,"r") as f:
#         text = f.read()

#     upper = text.upper()
#     with open(f"upper_copy_{filename}.txt","w") as f:
#         f.write(upper)

# upper_copy("note.txt")

# Create a script that deletes all .tmp files from the current directory using os and os.remove().

# files = os.listdir()

# for file in files:
#     if file.endswith("txt"):
#         os.remove(file)
#         print(f"{file} has been removed")



# Write a Python command-line tool that takes a folder name and prints the total size of all files inside it (use os.path.getsize()).

def get_size(filename):
    size = os.path.getsize(filename)
    return size

if __name__ == "__main__":
    filename = sys.argv[1]
    filesize = get_size(filename)
    print(f"size of file {filename} is {filesize} bytes")







