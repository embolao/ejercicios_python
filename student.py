"""Collect a user's variables and puts them on the screen"""
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}
    

if __name__ == "__main__":
    main()
