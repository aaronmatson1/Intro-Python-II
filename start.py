from category import Category

class Store:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        output = f"{self.name}" + "\n"
        for i , c in enumerate(self.categories):
            output += " " + str(i+1) + ". " + c + "\n"
        return output

my_store = Store("Aaron's Store", ["food", "beverage", "clothing"])
print(my_store)

selection = 0
while selection != len(my_store.categories)+1:
    selection = input("Select the number of a department")
    try:
        #move casting to int into the try block
        selection = int(selection)
        if selection == len(my_store.categories)+1:
            print("thanks for shopping.")
        elif selection > 0 and selection <= len(my_store.categories):
            print(my_store.categories[selection - 1])
        else:
            print("please select a valid number.")
    except ValueError:
        print("Please enter your choice as a number.")
    # print("The user selected "+ str(selection) )