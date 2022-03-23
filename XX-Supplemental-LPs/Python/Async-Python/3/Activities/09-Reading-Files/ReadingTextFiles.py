
# The open() function creates a connection to an external file
# The parameter passed into the function is the relative or absolute path to file to open
diary_txt_file = open("Diary.txt","r")

# Using the .read() function then stringifies the file's contents
diaryText = diary_txt_file.read()
print(diaryText)

# Closing the connection to the external file in order to save memory
diary_txt_file.close()

