# PART 1 : List

age_list = [18,19,20,21,22]
name_list = ["Ajith","Rahul","Akshay","Manu","Renju"]

print("Initial Age List:", age_list)
print("Initial Name List:", name_list)

name_list.append("Yazhini")
print("\nAfter appending 'Yazhini':", name_list)

age_list.insert(2, 30)
print("After inserting 30 at index 2:", age_list)

name_list.remove("Yazhini")
print("After removing 'Yazhini':", name_list)

popped_value = age_list.pop()
print(f"Popped value: {popped_value} |  age_list now:",age_list)

age_list.sort(reverse=True)
print("age_list sorted descending:", age_list)

print("Max age:", max(age_list))
print("Min age:", min(age_list))
print("Sum of ages:", sum(age_list))

print("\n-- Accessing name list --")
print("First element:", name_list[0])
print("Last element:", name_list[-1])
print("Elements index 2 to 4:", name_list[2:5])
print("Reversed name_list:", name_list[::-1])

# Part 2 : Dictionary

student_marks = {
    
    "Ajith": 60,
    "Rahul": 75,
    "Akshay": 95,
    "Manu": 55,
    "Renju": 98
}
print("student_marks:", student_marks)

print("\nAkshay's marks:", student_marks["Akshay"])

student_marks["janani"] = 80
print("After adding 'janani':", student_marks)

student_marks["Rahul"] = 82
print("After updating Rahul's marks:", student_marks)

print("\nkeys:", student_marks.keys())
print("values:", student_marks.values())
print("items:", student_marks.items())

# Part 3 : Sets

my_set = {'a','e','i','o','u','a','a','i'}
print("my_set:", my_set)
# Explanation: Sets automatically remove duplicates, so 'a' and 'i' appear only once

print("\nAttempting my_set[4] = 's' ...")
try:
    my_set[4] = 's'
except TypeError as e:
    print("Error found:", e)
# Explanation: Sets do not support indexing or assignment and thus show an error when trying to assign a value to an index.

set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}
print("\nset1:", set1)
print("set2:", set2)

print("Union of set1 and set2:", set1 | set2)
print("Intersection of set1 and set2:", set1 & set2)

# Part 4 : Operators and Conditional Statements

score = float(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score. Please enter a score between 0 and 10.")
elif score > 7:
    print("Above Average:")
elif 4 <= score <= 7:
    print("Average:")
else:
    print("Below Average:")

if score < 0 or score > 10:
    print("Invalid score. Please enter a score between 0 and 10.")
elif score > 7:
    print("Above Average:Excellent work! Keep it up.")
elif 4 <= score <= 7:
    print("Average: Good effort! You can improve with more practice.")
else:
    print("Below Average: Need to improve your performance.")