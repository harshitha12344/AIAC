# Python code to generate institutional email IDs

def generate_email(name):
    parts = name.strip().split(',')
    if len(parts) != 2:
        return None
    first_name = parts[0].strip()
    last_name = parts[1].strip()
    if not first_name or not last_name:
        return None
    email = f"{first_name[0].lower()}{last_name.lower()}@sru.edu.in"
    return email

student_names = input("Enter student names (format: first,last), separated by semicolons: ")
names_list = student_names.split(';')

for name in names_list:
    email = generate_email(name)
    if email:
        print(email)
    else:
        print(f"Invalid input format for: {name}")