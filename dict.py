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
"""
from itertools import count

words = ["apple","banana","apple","orange","banana","apple"]

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] = word_count + 1
    else:
        word_count[word] = 1

print(word_count)