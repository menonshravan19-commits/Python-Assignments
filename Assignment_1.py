string1 = "Hello "
string2 = input("Enter your Name")
concatenated = string1 + string2
print(concatenated)

string3 = ", Welcome to Python programming"
concatenated = concatenated + string3
print(concatenated)

start = concatenated.find("Python")
print(concatenated[0])

start = concatenated.find("Python")
print(concatenated[-1])

start = concatenated.find("Python")
print(concatenated[:5])

start = concatenated.find("Python")
print(concatenated[-11:])

start = concatenated.find("Python")
print(concatenated[::-1])

start = concatenated.find("Python")
print(concatenated[start:start+6])

strM = "Python beginner tutorial"
print(strM.upper())

strM = "Python beginner tutorial"
print(strM.lower())

strM = "Python beginner tutorial"
lower_str = strM.lower()
print(lower_str.capitalize())

strM = "Python beginner tutorial"
print(strM.count("t"))

strM = "Python beginner tutorial"
print(strM.replace("Python", "Machine Learning"))

tuple1 = (10,20,30)
tuple2 = (40,50,60)

t_combine = tuple1 + tuple2
print(t_combine)

t_repeat = t_combine * 3
print(t_repeat)

print(t_combine[2])

print(t_combine[:3])

print(t_combine[-3:])

