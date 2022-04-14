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




