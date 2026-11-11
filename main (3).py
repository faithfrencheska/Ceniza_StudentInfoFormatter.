# Get student information
first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
section = input("Enter section: ").strip()
favorite_subject = input("Enter favorite subject: ").strip()

# Format student information
full_name = (first_name + " " + last_name).title()
name_code = full_name.upper()
formatted_section = section.upper()
formatted_subject = favorite_subject.title()

# Count characters in full name
character_count = len(full_name)

# Display formatted information
print("\nFormatted Output:")
print("Name:", full_name)
print("Name Code:", name_code)
print("Section:", formatted_section)
print("Favorite Subject:", formatted_subject)
print("Character Count:", character_count)