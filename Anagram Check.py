word1=input("Enter 1st Word: ")
word2=input("Enter 2nd Word: ")
def Main(a,b):
    word1=sorted(a)
    word2=sorted(b)
    if word1==word2:
        return True
    else :
        return False
if Main(word1,word2):
    print("Its A ANAGRAM")
else:
    print("Its Not A ANAGRAM")