#Create an empty dictionary
country_db = {}

#infinite loop...
while True:
    print("1. insert")
    print("2. Display all countries")
    print("3. Display all capitals")
    print("4. Get capital")
    print("5. Delete")
    choice = input("Which one do you want to do? Type the number here: ")
    if choice == "1":
        country = input("Which country do you want to add? ")
        capital = input("What is the capital of that country? ")
        country_db[country] = capital
        print(country_db)
    elif choice == "2":
        print(country_db.keys())
    elif choice == "3":
        print(country_db.values())
    elif choice == "4":
        country = input("Type in a country to get it's capital (only if you have put it in there): ")
        print(country_db[country])
    elif choice == "5":
        delete = input("Type in a country you want to delete from the dictionary: ")
        del(country_db[delete])
    else:
        print("I'm sorry, wrong number")
        break