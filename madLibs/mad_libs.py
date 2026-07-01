# importing libraries
import re
from pathlib import Path
# getting user inputs
input_1 = input('Enter a adjective: ')
input_2 = input('Enter a noun: ')
input_3 = input('Enter a verb: ')
input_4 = input('Enter a 2_noun: ')
# creating a dictionary of replacements
replacements = {'ADJECTIVE': input_1, 'NOUN': input_2, 'VERB': input_3, '2_NOUN': input_4}
# reading the text file and replacing the placeholders with user inputs
file = Path(r'C:\Users\Dell\Desktop\python_practice_projects\madLibs\text_file.txt')
content = file.read_text()   # this will give the content of the file as a string
# creating a regex pattern to match the placeholders in the text file
pattern = re.compile('|'.join(map(re.escape, replacements.keys())))
updated_content = pattern.sub(lambda match: replacements[match.group(0)], content)
# printing the updated content
print(updated_content)
# writing the updated content to a new text file
with open(r'C:\Users\Dell\Desktop\python_practice_projects\madLibs\updated_text_file.txt', 'w', encoding='UTF-8') as file_obj:
    file_obj.write(updated_content)