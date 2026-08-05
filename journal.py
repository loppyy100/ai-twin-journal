import json
import os
from datetime import date
import ollama


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
 try:
    with open ("journal.json",  "r")  as f:
        entries = json.load(f)
 except FileNotFoundError:
    print(" no journal entries yet , do you want to add")
    return
 except json.JSONDecodeError:
    print(" journal file is corrupted , do you want to fix it ?")
    return
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


def chat_with_twin():
    # 1. read all the journal entries
    with open("journal.json", "r") as f:
        entries = json.load(f)

    # 2. glue entries into one text block
    journal_text = ""
    for entry in entries:
        journal_text += entry.get("date", "no date") + ": " + entry["text"] + "\n"

    # 3. ask what you want to know
    question = input("Ask your twin about your life: ")

    # 4. send to Qwen and print the answer
    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {"role": "system", "content": "You are Tobi's personal AI twin. Here is his journal:\n" + journal_text},
            {"role": "user", "content": question},
        ]
    )
    print(response["message"]["content"])



def search_entries ():
    word = input(" what are you searching for ?       ")

    with open("journal.json", "r") as f:
     entries = json.load(f)

    found = False
    for entry in entries:
        if word.lower() in entry["text"].lower():
            print(entry["date"] + ": " + entry["text"])
            found = True
    if not found:
        print("no entries found for this search term")




while True:
    choice = input("add  read  date  chat  search  or  quit?  ")
    if choice == "add":
        add_entry()
    elif choice == "read":
        read_entries()
    elif choice == "date":
        read_by_date()
    elif choice == "chat":
        chat_with_twin()
    elif choice == "search":
        search_entries()
    elif choice == "quit":
        print("bye Tobi!  have a great day!")
        break
    else:
        print("unknown command — try again")
