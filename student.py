"""Collect a user's variables and puts them on the screen"""
def main():
    student = get_student()
<<<<<<< HEAD
    print(f"{student['name']} from {student['house']}")
=======
    print(f"{student["name"]} from {student["house"]}")
>>>>>>> 1c0fac76861f1e3b6c2da0f00fc3e5469c5d0f8c

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student
    

if __name__ == "__main__":
    main()