import re
import os

# (x, y, x + w, y + h) in mm. Tuple that contains placement of a value to change
# For example:
box_version = (235, 10, 251, 15)
box_revision = (255, 10, 275, 15)
box_data = (185, 0, 200, 5)
box_machine_name = (185, 20, 275, 27)
box_sheet_number = (195, 10, 228, 15)

# Chose value box you want to replace
box_to_replace = box_machine_name
# New value
replacement_value = 'new value'


def replace_content(match, inside):
    attributes = match.group(1)  # Capture attributes within <text> tag
    return f'<text{attributes}>{inside}</text>'


def check_if_line_exist(box_name, text_data):
    for line in text_data:
        numbers = re.findall(r'\d+\.\d+', line)
        try:
            x, y = float(numbers[0]), float(numbers[1])
        except IndexError:
            pass
        else:
            if box_name[0] <= x <= box_name[2] and box_name[1] <= y <= box_name[3]:
                return line, x, y
    return -1


# Pattern for text lines in xml (sch) file
pattern = r'<text(.*?)>(.*?)</text>'

dir_path = 'data'
directories = os.listdir(dir_path)
print(directories)

for directory in directories:
    path = f'{dir_path}/{directory}'
    files = os.listdir(path)
    print(files)
    for file in files:
        with open(f'{path}/{file}', 'r', encoding='utf-8') as data:
            src_text = data.read()

        plain = src_text.split(r'<plain>')
        plain = plain[1].split(r'</plain>')
        lines = plain[0].splitlines()
        text_lines = []
        for line in lines:
            if line.find('text') != -1:
                text_lines.append(line)

        line, x, y = check_if_line_exist(box_to_replace, text_lines)
        if line == -1:
            print('No line found with giver boundaries.')
        else:
            modified_line = re.sub(pattern, lambda match: replace_content(match, replacement_value), line)
            src_text = src_text.replace(line, modified_line)

        with open(f'{path}/{file}', 'w', encoding='utf-8') as data:
            data.write(src_text)
