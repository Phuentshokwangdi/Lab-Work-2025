import json

FILE = "students.json"

def load_data():
    # Load JSON data from file
    try:
        with open(FILE, "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}  

def save_data(data):
    # Save JSON data back to file
    with open(FILE, "w") as json_file:
        json.dump(data, json_file, indent=4)


# CRUD Operations
def create_student(student_id, firstname, lastname, department, year):
    data = load_data()
    if student_id in data:
        print(f"Student ID {student_id} already exists!")
        return
    data[student_id] = {
        "firstname": firstname,
        "lastname": lastname,
        "department": department,
        "year": year
    }
    save_data(data)
    print(f"Student {student_id} added successfully!")

def read_students():
    data = load_data()
    if not data:
        print("No students found.")
        return
    for sid, info in data.items():
        print(f"{sid}: {info}")

def update_student(student_id, field, new_value):
    data = load_data()
    if student_id not in data:
        print(f"Student ID {student_id} not found!")
        return
    if field not in data[student_id]:
        print(f"Field '{field}' not valid!")
        return
    data[student_id][field] = new_value
    save_data(data)
    print(f"Student {student_id} updated successfully!")

def delete_student(student_id):
    data = load_data()
    if student_id not in data:
        print(f"Student ID {student_id} not found!")
        return
    del data[student_id]
    save_data(data)
    print(f"Student {student_id} deleted successfully!")

 
if __name__ == "__main__":
    print("****************************************************")
    # CREATE
    create_student("student5", "Karma", "Dawa", "ECE", "1")
    print("****************************************************")
    # READ
    read_students()
    print("****************************************************")
    # UPDATE
    update_student("student2", "year", "1")
    print("****************************************************")
    # DELETE
    delete_student("student4")
    print("****************************************************")
    # Final read
    read_students()
