import random
import sys
import time

def note():
    print("<กรอกชื่อไฟล์หรือชื่อไฟล์และนามสกุลไฟล์> & <input name file> ")

def main(file):
    import time
    with open(file, "r") as files:
        passwd = str(files.read())
    check = any(char.isalpha() for char in passwd)
    if check:
        if any(chars.isdigit() for chars in passwd):
            password = ""
            while password != passwd:
                 password= ""
                 for i in range(len(passwd)):
                    number = random.choice("0123456789abcdefghijklmnopqrsuvwyz")
                    password += "".join(number)
                    print("[*] --------Password----------- >> ", password)
            print()
            print("""                

                          ______
                          |    |
                          |    |
    We are Anonymous.     |    |  We are Ligion.
                      ____|    |____
                     |    |    |    |
  We Do not forgive. |    |    |    |  We Do not Forget.
                 ____|    |    |    |____
                |    |              |    |
                |    |              |    |             
                |        Expect Us.      |
                |                        | 
                                    Crack Password __version__ Make fun""")
            print()
            print()
            print("Crack Password Successful & Password is >>>> ",password)
        else:
            password = ""
            while password != passwd:
                 password= ""
                 for i in range(len(passwd)):
                    number = random.choice("abcdefghijklmnopqrstuvwxyz")
                    password += "".join(number)
                    print("[*] --------Password----------- >> ", password)
            print()
            print("""                

                          ______
                          |    |
                          |    |
    We are Anonymous.     |    |  We are Ligion.
                      ____|    |____
                     |    |    |    |
  We Do not forgive. |    |    |    |  We Do not Forget.
                 ____|    |    |    |____
                |    |              |    |
                |    |              |    |             
                |        Expect Us.      |
                |                        | 
                                    Crack Password __version__ Make fun""")
            print()
            print()
            print("Crack Password Successful & Password is >>>> ",password)


    else:
        password = ""
        while password != passwd:
             password= ""
             for i in range(len(passwd)):
                number = random.choice("0123456789")
                password += "".join(number)
                print("[*] ------------Password------------ >> ", password)
        print()
        print("""                

                          ______
                          |    |
                          |    |
    We are Anonymous.     |    |  We are Ligion.
                      ____|    |____
                     |    |    |    |
  We Do not forgive. |    |    |    |  We Do not Forget.
                 ____|    |    |    |____
                |    |              |    |
                |    |              |    |             
                |        Expect Us.      |
                |                        | 
                                    Crack Password __version__ Make fun""")
        print()
        print()
        print("Crack Password Successful & Password is >>>> ",password)
    

if len(sys.argv) != 2:
    note()
else:
    if sys.argv[1][-3:] == "txt":
         main(sys.argv[1])
    else:
        x = sys.argv[1]
        x+= ".txt"
        main(x)

    

