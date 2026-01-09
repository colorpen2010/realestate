import sys

password = 12345
if sys.argv[1] == "user":
    import user
elif sys.argv[1] == "admin":
    input_password = int(input("ведите пароль: "))
    if input_password == password:
        import admin
    else:
        print("неверный пароль")
