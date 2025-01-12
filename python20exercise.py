# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
word=['Thirty','Days','Of','Python']
result="Thrirty"+" "+"Days"+" "+"Of"+" "+"Python"
print(result)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
word=['Coding','For','All']
result=' '.join(word)
print(result)

# Declare a variable named company and assign it to an initial value "Coding For All".
company="Coding For All"
print(company)

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
print(company[0:6])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding','Python'))

# Change Python for Everyone to Python for All using the replace method or other methods.
sentence="Python for Everyone"
print(sentence.replace('Everyone','All'))

# Split the string 'Coding For All' using space as the separator (split())
print(company.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))

# What is the character at index 0 in the string Coding For All.
print(company[0])

# What is the last index of the string Coding For All.
print(company[-1])

# What character is at index 10 in "Coding For All" string.
print(company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
name="Python For Everyone"
name=name.split()
acronym=""
for i in name:
    acronym+=i[0].upper()
print(acronym)

# Create an acronym or an abbreviation for the name 'Coding For All'.
name="Coding For All"
name=name.split()
acronym=""
for i in name:
    acronym+=i[0].upper()
print(acronym)

