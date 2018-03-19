"""
Intro to Python Lab 1, Task 4

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Lab Preparation page.
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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers: 
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message: 
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def find_telemarketers(text_records, call_records):
    """
    Find telemarketers.
    :param text_records: Text records.
    :param call_records: Call records.
    :return: list of telemarketers numbers
    """
    call_from = []
    call_to = []
    for call in call_records:
        if call[0] not in call_from:
            call_from.append(call[0])
        if call[1] not in call_to:
            call_to.append(call[1])

    text_from = []
    text_to = []
    for text in text_records:
        if text[0] not in text_from:
            text_from.append(text[0])
        if text[1] not in text_to:
            text_from.append(text[1])

    telemarketers = []
    for ret in call_from:
        if ret not in call_to:
            if ret not in text_from:
                if ret not in text_to:
                    telemarketers.append(ret)

    return sorted(telemarketers)


print("These numbers could be telemarketers: ")
for telemarketer in find_telemarketers(texts, calls):
    print(telemarketer)

