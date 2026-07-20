import json

def add_entry():
    text = input("what happened today ? :  ")
    entry = {"text": text}
    with open ("journal.json" , "w") as f:
        json.dump(entry , f)
add_entry()