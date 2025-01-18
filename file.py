#hello
#hello world


# 1. Create an empty dictionary called dog
dog = {}
print(dog)

# 2. Add name, color, breed, legs, age to the dog dictionary
dog["name"]="Max"
dog["color"]="Black"
dog["breed"]="German Shepherd"
dog["legs"]=4
dog["age"]=5
print(dog.values())

# 3. Create a student dictionary and add first_name, last_name, age, skills, country, city and address as keys for the dictionary
student = {
    "first_name" : "John",
    "last_name" : "Trump",
    "age" : 25,
    "skills" : ["Python", "Java", "C++"],
    "country" : "USA",
    "city" : "New York",
    "address" : "123 Main St"
}

# 4. Get the length of the student dictionary

print(len(student))

# 5. Get the value of skills and check the data type, it should be a list
print(student["skills"])


# 6. Modify the skills values by adding one or two skills
student["skills"].append("HTML")
student["skills"].append("CSS")
print(student["skills"])

# 7. Get the dictionary keys as a list
print(student.keys())

# 8. Get the dictionary values as a list