import os
def clearing():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
#выбор: Вход или регистрация
cycle = True
while cycle == True:

    print("Log in or Registration? ")
    
    #ввод ответа и возможный выбор
    statusIn_1 = input("").strip()  
    
    clearing()
    
    #после выбора
    if statusIn_1.lower() in ["log in", "login"]: 
        login = input("Login: ")
        password = input("Password: ")
        
        clearing()
            
        print(f"Login: {login} \nPassword: {password} \nRight?")
        answer = input("").strip().lower() 
        
        if answer == "yes":  
            print("Log in completed.")
            clearing()
        else:
            print("Login cancelled.")
            continue  
            
    elif statusIn_1.lower() in ["registration", "register"]:  
        new_login = input("Create Login: ")
        new_password = input("Create Password: ")
        new_password_repeat = input("Repeat Password: ")
        
        clearing()
            
        if new_password_repeat != new_password:
            print("Wrong password. Repeat again.")
            continue  
            
        print(f"Login: {new_login} \nPassword: {new_password} \nAlways remember your password!")
        input("Press Enter to continue...")
        clearing()
            
    else:  
        print("Invalid choice! Please enter 'Log in' or 'Registration'")
        continue  
    
    about = input("Do you want to write something about you? (Yes/No)\n").strip().lower()
    
   
    user_nickname = None
    user_about = None
    user_phone = None
    user_mail = None
    
    while about == "yes":  
        clearing()
            
        print("What do you want to add? ")
        print("0. Exit \n1. Nickname \n2. About me \n3. Number of phone \n4. Your mail \n5. View my information")
        
        choose = input("Your choice: ").strip()
        
        clearing()
        
        if choose == "0":
            break  
            
        elif choose == "1":
            user_nickname = input("Write your new nickname: ")
            clearing()
            print(f"Your new nickname: {user_nickname}")
            input("Press Enter to continue...")
            
        elif choose == "2":
            user_about = input("Write about yourself: ")
            clearing()
            print(f"About you: {user_about}")
            input("Press Enter to continue...")
            
        elif choose == "3":
            user_phone = input("Write your phone number: ")
            clearing()
            print(f"Your phone: {user_phone}")
            input("Press Enter to continue...")
            
        elif choose == "4":
            user_mail = input("Write your email: ")
            clearing()
            print(f"Your email: {user_mail}")
            input("Press Enter to continue...")
            
        elif choose == "5":
            clearing()
            print("=== YOUR INFORMATION ===")
            print(f"Nickname: {user_nickname if user_nickname else 'Not set'}")
            print(f"About: {user_about if user_about else 'Not set'}")
            print(f"Phone: {user_phone if user_phone else 'Not set'}")
            print(f"Email: {user_mail if user_mail else 'Not set'}")
            print("========================")
            input("Press Enter to continue...")
            
        else:
            print("Invalid choice! Please try again.")
            input("Press Enter to continue...")

    exit_choice = input("Do you want to exit? (Yes/No)\n").strip().lower()
    if exit_choice == "yes":
        cycle = False
    else:
        clearing()
            
            #сделать очистку строк через создание функции def
