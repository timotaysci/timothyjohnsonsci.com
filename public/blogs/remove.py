import os

directory_path = os.getcwd()

# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)

    # Check if the item is a file (not a subdirectory)
    if os.path.isfile(file_path):
        # Read the file into memory
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Rewrite the file, excluding lines starting with "tags"
        with open(file_path, 'w') as file:
            for line in lines:
                if not line.startswith("tags"):
                    file.write(line)
