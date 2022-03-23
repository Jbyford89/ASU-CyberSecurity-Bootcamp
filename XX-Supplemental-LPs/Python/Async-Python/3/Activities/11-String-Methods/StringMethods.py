
# The open() function creates a connection to an external file
# The parameter passed into the function is the relative or absolute path to file to open
diary_txt_file = open("Diary.txt","r")

# Using the .read() function then stringifies the file's contents
diaryText = diary_txt_file.read()

# Since the file is now a string, it can be modified and worked with using some string functions
# The split() function breaks a string apart into a list based upon common words/characters that appear in the original string
diarySplit = diaryText.split(" ")

# Since the string was split on spaces, individual words will now be printed when referenced
print(diarySplit[0])
print(diarySplit[1])
print(diarySplit[2])
print(diarySplit[3])
print("-----------")

# The find() function will navigate through some text, determine whether or not the string passed into it is contained within, and return the index of that string
print(diaryText.find("malarkey"))

# This can be exceptionally useful when checking to see if a file contains some specific keywords
if diaryText.find("malarkey") > -1:
    print("Malarkey found!")

if diaryText.find("juice") > -1:
    print("Juice found")

print("-----------")

# Closing the connection to the external file in order to save memory
diary_txt_file.close()

