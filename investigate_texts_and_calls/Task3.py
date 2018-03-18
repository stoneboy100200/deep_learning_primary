"""
Intro to Python Lab 1, Task 3

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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore. 
Fixed line numbers include parentheses, so Bangalore numbers 
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. 
 - Fixed lines start with an area code enclosed in brackets. The area 
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def get_area_code_and_mobile_prefixes(records):
    """
    Get all of the area codes and mobile prefixes called by people in Bangalore.
    :param records: Call records.
    :return: List of area code and mobile prefixes.
    """
    code = []
    for call in records:
        if call[0][:5] == "(080)":
            if call[1][0] == "(":
                area_code = call[1][1:call[1].index(")")]
                if area_code not in code:
                    code.append(area_code)
            elif call[1].find(" ") != -1:
                if call[1][0] == "7" or call[1][0] == "8" or call[1][0] == "9":
                    mobile_prefixes = call[1][:4]
                    if mobile_prefixes not in code:
                        code.append(mobile_prefixes)

    return code


def get_percentage(records):
    """
    Get percentage of calls from fixed lines in Bangalore are made to fixed lines also in Bangalore.
    :param records: Call records.
    :return: Percentage of calls from fixed lines in Bangalore.
    """
    total = 0
    to_bangalore = 0
    for call in records:
        if call[0][:5] == "(080)":
            total += 1
            if call[1][:5] == "(080)":
                to_bangalore += 1

    percent = '%.2f' % (to_bangalore / total * 100)
    return percent


print("The numbers called by people in Bangalore have codes:")
for item in get_area_code_and_mobile_prefixes(calls):
    print(item)
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".
      format(get_percentage(calls)))
