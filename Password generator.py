import random
def password_generator(length,all):
    passwd="".join(random.sample(all,length))
    return passwd
char="QWERTYUIOPASDFGHJKLMNBVCXZqwertyuioplkjhgfdsazxcvbnm"
numbers="1234567890"
special_characters="@#$()"
all=char+numbers+special_characters
length=int(input("Enter length of a password you want:"))
if length<8:
    print("minimum length of a password should be 8")
else:
    print("Your generated password is :",password_generator(length,all))