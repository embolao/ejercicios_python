"""Collect a user's variables and puts them on the screen"""
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house) #Return tuple 

if __name__ == "__main__":
    main()