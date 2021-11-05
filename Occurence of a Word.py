String=input("Enter The String: ")
print(len(String))
Character=input("Enter The Character: ")
Count=0
string=String.lower()
for i in range(0,len(string)):
    if (string[i]==Character):
        Count=Count+1
print("Total No. Of Occurrence of ",Character, " In ", String, "Is: ", Count)