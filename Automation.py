import re

inputfile="input.txt"
outputfile="emails.txt"

with open(inputfile,"r") as file:
    content=file.read()

emails=re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

uniqueemails=set(emails)

with open(outputfile,"w") as file:
    for email in uniqueemails:
        file.write(email+"\n")

print("Email extraction completed successfully.")
