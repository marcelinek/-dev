import re
def validateEmail (email):
    return re.match(r'.+\@.+\..+\..+' and r'.+\@.+\..+', email)

giris_hakki = 3

while giris_hakki > 0:
    giris_hakki -=1
    email = input("Mail adresinizi giriniz:")
    valid = validateEmail(email)

    if valid:
        print("Mail adresiniz doğrudur.")
        break
    else:
        print("Mail adresiniz yanlıştır.")
