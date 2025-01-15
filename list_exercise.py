# 1. Declare an empty list
lst=[]
print(lst)

# 2. Declare a list with more than 5 items
lst=[1,2,3,4,5,6]
print(lst)

# 3. Find the length of your list
print(len(lst))

# 4. Get the first item, the middle item and the last item of the list
print(lst[0:6:2])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=["Isrer",25,5.8,"Single","123 Main St"]
print(mixed_data_types)

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(it_companies)

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
print(it_companies[0],it_companies[3],it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies[1]="YouTube"
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append("Twitter")
it_companies.append("LinkedIn")
it_companies.append("Instagram")
it_companies.append("Google")
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(3,"TikTok")
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[-1]=it_companies[-1].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;  '
print('#;'.join(it_companies))

# 15. Check if a certain company exists in the it_companies list.
print("IBM" in it_companies)

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)


# 18. Slice out the first 3 companies from the list
print(it_companies[0:3])

# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])

# 20. Slice out the middle IT company or companies from the list
print(it_companies[3:6])

# 21. Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# 22. Remove first IT companies from the list
it_companies.pop(0)
print(it_companies)

# 23. Remove middle IT companies from the list
print(len(it_companies))
del it_companies[4:6]
print(it_companies)



# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
front_end=["HTML", "CSS", "JS", "React", "Redux"]
back_end=["Node","Express", "MongoDB"]
full_stack=front_end+back_end
print(full_stack)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack
full_stack_copy=full_stack.copy()
print(full_stack_copy)



