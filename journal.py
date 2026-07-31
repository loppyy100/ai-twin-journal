
import json
import os
from datetime import date


def add_entry():
    text = input("What happened today? ")
    entry = {"date": str(date.today()), "text": text }

    if os.path.exists("journal.json"):
        with open("journal.json", "r") as f:
            entries = json.load(f)
    else:
        entries = []

    entries.append(entry)

    with open("journal.json", "w") as f:
        json.dump(entries, f)



def read_entries():
    with open ("journal.json",  "r")  as f:
        entries = json.load(f)
    for entry in entries:
        print(entry["text"])



def read_by_date():
    wanted = input(" which date  ?   (yyyy-mm-dd)  ")

    with open("journal.json", "r") as f :
        entries = json.load(f)

        found = False
        for entry in entries :
            if entry.get("date") == wanted:
                print(entry["text"])
                found = True
        if not found:
                print("no entry for this date")



choice = input ("add   read   or   date ?  ")
if choice == "add":
    add_entry()
elif choice == "date":
    read_by_date()
else :
    read_entries()

