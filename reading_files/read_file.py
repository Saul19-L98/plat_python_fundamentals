#Read lines in a text file.
"""with open('caperucita.txt','r') as file:
    for lines in file:
        print(lines.strip())"""
        
#Read all the lines in a list
"""with open('caperucita.txt','r') as file:
    lines = file.readlines()
    print(lines)"""

#Add text
"""with open('caperucita.txt','a') as file:
    file.write("\n\nBy:Sam")"""

#Overwrite text
"""with open('caperucita.txt','w') as file:
    file.write("\n\nBy:Sam")"""

#Exercise
with open('caperucita.txt','r') as file:
    count = 0
    for lines in file:
        count = count + 1
    print(f"Amount of lines: {count - 1}")

