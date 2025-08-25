import xml.etree.ElementTree as ET

tree = ET.parse('StudentInfo.xml')
root = tree.getroot()

print("Student Details:\n")
for student in root.findall('student'):
    category = student.get('category')
    name = student.find('name').text
    studentno = student.find('studentno').text
    department = student.find('department').text
    year = student.find('year').text
    bloodgroup = student.find('bloodgroup').text

    print(f"Category: {category}")
    print(f"Name: {name}")
    print(f"Student No: {studentno}")
    print(f"Department: {department}")
    print(f"Year: {year}")
    print(f"Blood Group: {bloodgroup}")
    print()
