#Q1: READ FILE,MODIFY IT, WRITE IN NEW FILE
#Open file and read it's contents
with open('PYTHON ASSIGNMENTS/File_Handling/Movies.pdf','r') as infile:
    movies = infile.read()

#Modify movies' list by making everything uppercase
modified_list = movies.upper() 

#create a new file and write modified content
with open('Movies-list.pdf','w') as outfile:
    outfile.write(modified_list)



#Q2: ERROR HANDLING
filename = 'PYTHON ASSIGNMENTS/File_Handling/' + input('Enter the name of the file you want to read: ')
try:
    with open(filename,'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File doesn't exist.\nEnter a valid filename")

