import json
from csv import DictReader
from files import CSV_FILE
from files import JSON_FILE, JSON_FILE_W

result = []


with open(JSON_FILE, "r") as f:
    users = json.load(f)
    for user in users:
        result.append({
            "name": user["name"],
            "gender": user["gender"],
            "age": int(user["age"]),
            "books": []

        })

with open(CSV_FILE, newline='') as f:
    reader = DictReader(f)
    i = 0
    for row in reader:
        result[i % len(result)]['books'].append({
            "title": row["Title"],
            "author": row["Author"],
            "pages": int(row["Pages"]),
            "genre": row["Genre"]
        })

        i += 1

        with open(JSON_FILE_W, "w") as f:
            s = json.dumps(result, indent=4)
            f.write(s)
