import test
## Data Types


#number
num = 10
# +, -, *, /, %


#string
name = "Matt"

print(num)
print(name)

#boolean
result = True

#lists
students = ["Amy", "Thomas", "Nathalie", "Saneeta"]

# {
#     0:"Amy",
#     1:"Thomas"
# }

print(len(students))

students.append("Matt")

students.pop()

print(students)

print(students[1])

#dictionaries

bad_guy = {
    'health': 500,
    'name': "Ka'Thar",
    'attack': 'Mace Smash'
}
# name = 'attack'

print(bad_guy['name'])

bad_guy["attack"] = 'Mace Super Smash'

print(bad_guy['attack'])

#loops/conditionals

students = ["Amy", "Thomas", "Nathalie", "Saneeta"]

post = {
    'poster': "Odion",
    "content": "omg this python class won't end!!",
    'post_date': '07/07/20'
}

count = 0

for whatever in post:
    count+=1
    print(f"Object attr: {whatever}, Object value: {post[whatever]}")
    print(count)

# for(let i =0; i<250; i++){
# }

for i in range(0, 100, 1):
    print(f"This is the index: {i}, this is the value: {students[i]}")

def print_name_return_ten(name):
    print(name)
    if name == "Ka'Thar":
        return "You have run into the boss"
    elif name == "Michael":
        return "Oh no... run"
    else:
        return 10


print(print_name_return_ten("Kyle"))