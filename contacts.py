contacts = {
    "number" : 4,
    "students":
    [ 
        {"name":"Sara Holderness","email":"sarah@example.com"},
        {"name":"Harry Potter","email":"harry@example.com"},
        {"name":"Herminoe Granger", "email":"hermione@exmaple.com"},
        {"name":"Ron Weasley", "email":"ron@example.com"}
    ]
}

for student in contacts['students']:
    print(student["email"])
