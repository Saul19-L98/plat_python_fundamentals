import os

#Get current directory
cwd = os.getcwd()
print(f"Your current directory is: {cwd}")

#Get all the .txt files
txt_files = [f for f in os.listdir('./reading_files/') if f.endswith('.txt')]
print(".txit files: ", txt_files)

os.rename('./reading_files/tale.txt','reading_files/caperucita.txt')

verify_files = [f for f in os.listdir('./reading_files/') if f.endswith('.txt')]
print(".txit files: ", verify_files)


