# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# concatenate the names and create a new variable, remove white spaces with replace, covert to lowercase and print the name back into single string, now we should be ready to count them. 

names = name1.replace(" ","")+ name2.replace(" ","")
names = names.lower()
print(names)
# print(names.count("t"))
# print(names.count("r"))
# print(names.count("u"))
# print(names.count("e"))
# print(names.count("l"))
# print(names.count("o"))
# print(names.count("v"))
# print(names.count("e"))
tally = names.count("t") + names.count("r") + names.count("u") + names.count("e") + names.count("l") + names.count("o") + names.count("v") + names.count("e")

#print(tally)

if tally < 10 or tally > 90:
  print(f"your score is {tally} you two are like coke and mentols together")
elif tally > 40 and tally < 50:
  print(f"your score is {tally} you are alright together")
else:
  print(f"your score is {tally}. meh!")