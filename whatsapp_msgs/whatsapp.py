"""
Send messages on whatsapp using python: Automate whatsapp messages

pip install pywhatkit
"""

import pywhatkit
# log in to whatsapp manually on browser before running the code

# how to send messages to contact
phone_no = input("Enter phone number: ")

# add phone no, text, hour and minutes into parenthesis
#pywhatkit.sendwhatmsg(phone_no, "Test", 7, 20)

# to close tab after delivering message after 2secs, set the tab_close = True
pywhatkit.sendwhatmsg(phone_no, "Test", 7, 20, 15, True, 2)


# to send messages to group
group_id = input("Enter group id: ")
pywhatkit.sendwhatmsg_to_group("group_id", "Test_group", 7, 31)






