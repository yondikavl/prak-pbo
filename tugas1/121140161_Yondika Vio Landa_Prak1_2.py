i = 0
while i < 3:
    usern = input("Username anda: ")
    passw = input("Password anda: ")
    if usern == "informatika" and passw == "12345678":
        print("Berhasil login!")
        break
    else:
        i += 1
        if i == 3:
            print("Username atau password salah, Akun diblokir!")
        else:
            print("Username atau password salah coba lagi")
