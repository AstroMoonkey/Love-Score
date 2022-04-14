# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# concatenate the names and create a new variable, remove white spaces with replace, covert to lowercase and print the name back into single string, now we should be ready to count them. 

names = name1.replace(" ","")+ name2.replace(" ","")
names = names.lower()
# print(type(names))
true = str(names.count("t") + names.count("r") + names.count("u") + names.count("e"))
love = str(names.count("l") + names.count("o") + names.count("v") + names.count("e"))
tally = true + love
# print(type(tally))
tally = int(tally)
if tally < 10 or tally > 90: # **less than 10** or **greater than 90**
  print(f"Your score is {tally}, you go together like coke and mentos.")
elif tally > 40 and tally < 50: # **between 40** and **50**
  print(f"Your score is {tally}, you are alright together.")
else:
  print(f"Your score is {tally}.")