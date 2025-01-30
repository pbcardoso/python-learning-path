# A program that checks the validity of a password provided by the user.
# The valid password is '1234'. The program prints: ACCESS GRANTED if
# the password is valid and ACCESS DENIED if the password is invalid.

password = input("Enter the password: ")

if password == '1234':
    print("\n\033[32mACCESS GRANTED\033[0m")

else:
    print("\n\033[31mACCESS DENIED\033[0m")
