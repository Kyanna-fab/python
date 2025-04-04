"""
students = {"Alice":85,
            "Bob":78,
            "Charlie":92
            }

print(students["Charlie"])
students["David"] =88

students["Bob"] = 82
del students["Alice"]
print(students)

for x,y in students.items():
    print(x,y)

for x in students.keys():
    print(x)

for x in students.values():
    print(x)

words = ["apple","banana","apple","orange","banana","apple"]

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word] = 1

print(word_count)


key = ["name", "age", "city"]
value = ["Alice", 25, "New York"]

mydict = dict(zip(key, value))

print(mydict)


students = {
        "Alice": {"age": 20,"marks": {"Math": 85, "Science": 90}},
        "Bob": {"age": 22, "marks": {"Math": 78, "Science": 85}}
    }

print(students["Bob"]["marks"]['Science'])
students["Alice"]["marks"]["History"] = 80


print(students)


squares = {x: x**2 for x in range(1, 6)}

for x in range(1,6):
    x = x**2
    print(x)
"""

prices = {"apple": 100, "banana": 50, "cherry": 75}

increased = {}

for x in prices.values():
    x = x * 1.10
    print(int(x))



