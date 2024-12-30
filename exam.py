from utils import unzip_with_7z

zip_file_path = 'C:\\crash project\\congrats.7z'  # keep as is
dest_path = 'C:\\crash project\\opened file'  # keep as is

find_me = ''  # 2 letters are missing!
secret_password = find_me + 'bcmpda'

# WRITE YOUR CODE BELOW

import string  # Import string module to get all lowercase letters

# Loop through all combinations of two lowercase letters
for first_letter in string.ascii_lowercase:
    for second_letter in string.ascii_lowercase:
        # Construct the password dynamically
        secret_password = first_letter + second_letter + 'bcmpda'

        print(f"Trying password: {secret_password}")  # Debug message

        # Try to unzip the file with the generated password
        if unzip_with_7z(zip_file_path, dest_path, secret_password):
            print(f"Password found: {secret_password}")
            exit(0)  # Exit the script once the correct password is found

print("Password not found.")
