print("The Love Calculator is calculating your score..!")
name1 = input("What is your name..?\n =") 
name2 = input("What is their name..?\n =")
combbined_name = name1 + name2
combbinedName_lower = combbined_name.lower()

t = combbinedName_lower.count("t")
r = combbinedName_lower.count("r")
u = combbinedName_lower.count("u")
e = combbinedName_lower.count("e")
first_digit = t + r + u + e

l = combbinedName_lower.count("l")
o = combbinedName_lower.count("o")
v = combbinedName_lower.count("v")
e = combbinedName_lower.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos..!")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together..!")
else:
    print(f"Your score is {score}..!")