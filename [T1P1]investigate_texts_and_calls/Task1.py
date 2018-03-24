"""
Intro to Python Project 1, Task 1

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Project Preparation page.
"""


"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1: 
How many different telephone numbers are there in the records? 
Print a message: 
"There are <count> different telephone numbers in the records."
"""


def get_phone_count(text_records, call_records):
    """
    Get the count of telephone numbers in the records.
    :param text_records: Text records.
    :param call_records: Call records.
    :return: The count of phone number.
    """
    phone_num = []
    for text in text_records:
        if text[0] not in phone_num:
            phone_num.append(text[0])
        if text[1] not in phone_num:
            phone_num.append(text[1])

    for call in call_records:
        if call[0] not in phone_num:
            phone_num.append(call[0])
        if call[1] not in phone_num:
            phone_num.append(call[1])

    return phone_num


print("There are {} different telephone numbers in the records.".format(len(get_phone_count(texts, calls))))
