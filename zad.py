def menu():
    print("Menu:")
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")
    print("6")
    print("7")
    choice= int(input("Enter choice: "))
    if choice==1:
        print("one")
    elif choice==2:
        print("2")
    elif choice==3:
        print("3")
    elif choice==4:
        print("4")
    elif choice==5:
        print("5")
    elif choice==6:
        print("6")
    elif choice==7:
        print("7")
        exit()
    else:
        print("Invalid choice")
    menu()
menu()
