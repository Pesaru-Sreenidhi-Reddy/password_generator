import random

print("Welcome to password generator")
print("==============================")
n = int(input("Enter password length: ").strip())
charSet={
'upCase':"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
'lowCase' : "abcdefghijklmnopqrstuvwxyz",
'specialChars': "\'\\!@#$%^&*+-_<>?~`",
'nums':"1234567890"
}
pwdCnt= int(input("How many passwords do you need? ").strip())
upCaseResp = input("Do you want to include upper case letters in password?(y/n) ").strip().lower()
lowCaseResp = input("Do you want to include lower case letters in password?(y/n) ").strip().lower()
specialCharsResp = input("Do you want to include special characters in password?(y/n) ").strip().lower()
numsResp = input("Do you want to include numbers in password?(y/n) ").strip().lower()
password = ""
selectedSets=[]
if upCaseResp == "y":
    selectedSets.append('upCase')
if lowCaseResp == "y":
    selectedSets.append('lowCase')
if specialCharsResp == "y":
    selectedSets.append('specialChars')
if numsResp == "y":
    selectedSets.append('nums')
if not selectedSets:
    print("Please enter 'y' for at least once to get the password.")
else:
    print("\nGenerated Passwords List:")
    for _ in range(pwdCnt):
        for Set in selectedSets:
            password += random.choice(charSet[Set])
        for _ in range(n-len(selectedSets)):
            randChar =random.choice(selectedSets)
            password += random.choice(charSet[randChar])
        pwdAsList = list(password)
        random.shuffle(pwdAsList)
        password= ''.join(pwdAsList)
        print(password.strip())
        password=""

