import re


# This function is to verify if a user name is correct

def verify_user_name(user_name):
    return 'The user name is correct' if re.match("[a-z0-9-_]+$", user_name) else 'The user name is incorrect'


print(verify_user_name("escar_999"))
print(verify_user_name("hello_1345"))
print(verify_user_name("bad"))


# This function is to verify if a user password is correct

def verify_password(password):
    return 'The password is correct' if re.match("[a-zA-Z0-9]{8,16}$", password) else 'The password is incorrect'


print(verify_password("helloH11"))
print(verify_password("Not"))
print(verify_password("Yes00IsValid"))


# This function is to verify if a email is correct

def verify_email(email):
    return 'The email is correct' if re.match("^([a-zA-Z]+[-/_0-9]*)@[a-z0-9-]+(.[a-z0-9-]+)*([a-z]{1,2})$",
                                              email) else 'The email is incorrect'


print(verify_email("anything@domain.com.bo"))
print(verify_email("anything@domain.com.bo3"))
print(verify_email("escarlita_555@gmail.com"))
print(verify_email("this is bad "))
