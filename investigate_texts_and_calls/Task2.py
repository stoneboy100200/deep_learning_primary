"""
Intro to Python Lab 1, Task 2

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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message: 
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.". 

HINT: Build a dictionary with telephone numbers as keys, and their
total time spent on the phone as the values. You might find it useful
to write a function that takes a key and a value and modifies a 
dictionary. If the key is already in the dictionary, add the value to
the key's existing value. If the key does not already appear in the
dictionary, add it and set its value to be the given value.
"""


def get_longest_time(records):
    """
    Get the longest time on the phone.
    :param records: Call records.
    :return: A dictionary with phone number and time.
    """
    phone_time = {}
    for call in records:
        if call[0] not in phone_time:
            phone_time[call[0]] = int(call[3])
        else:
            phone_time[call[0]] += int(call[3])

        if call[1] not in phone_time:
            phone_time[call[1]] = int(call[3])
        else:
            phone_time[call[1]] += int(call[3])

    max_time = 0
    for time in phone_time:
        if phone_time[time] > max_time:
            phone = {}
            phone[time] = phone_time[time]
            max_time = phone_time[time]
        elif phone_time[time] == max_time and time not in phone:
            phone[time] = phone_time[time]

    return phone


tel_time = get_longest_time(calls)
for tel in tel_time:
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(tel, tel_time[tel]))

