a  = open("sample2.txt","a")

name = input("enter the name:")
age = input("enter the age:")

a.write("\nname")
a.write(name)
a.write("\nage")
a.write(age)


a.close()