import re
regex_email= '^[a-zA-z]+\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
email=input("enter email address:")
if(re.search(regex_email,email)):
    print("email address is valid")
else:
    print("please enter valid email address!")