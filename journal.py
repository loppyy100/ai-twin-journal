
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


choice = input ("add or read ?  ")
if choice == "add":
    add_entry()
else :
    read_entries()






 

