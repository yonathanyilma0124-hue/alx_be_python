def display_menu():
    print("\n Shopping list manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
def main():
    shopping_list = []
    while True:
        display_menu()
        choice= input("Enter your choice: ").strip()
        
        if choice == "1":
            item = input("Enter the item  to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f" '{item}' is added to your Shopping list")
            else:
                print(f"item name can not be empty")
        elif choice == "2":
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
        
                print(f" '{item}' is removed from your Shopping List")
            else:
                print(f" '{item}' is not found in your Shopping List")
        elif choice == "3":
            if shopping_list:
                print("\nYour Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is currently empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
