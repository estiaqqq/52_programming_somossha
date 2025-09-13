import os


def make_a_file(file_name):
    # Define the directory path
    directory_path = "D:/52_programming_somossha/"  # Replace with your actual path
    # file_name = "problem_02.py"

    # Construct the full file path
    full_file_path = os.path.join(directory_path, file_name)

    # Ensure the directory exists (optional, but good practice)
    # If the directory doesn't exist, this will create it.
    os.makedirs(directory_path, exist_ok=True)

    # Create and open the file in write mode ('w')
    # 'w' mode will create the file if it doesn't exist, or overwrite it if it does.
    # Use 'a' for append mode if you want to add content without overwriting.
    try:
        with open(full_file_path, "w") as f:
            f.write("This is some content for the new file.")
        print(f"File '{file_name}' created successfully at '{directory_path}'.")
    except IOError as e:
        print(f"Error creating file: {e}")


print("Calling func")
# make_a_file("file_name_one.py")
i = 0
file_name_str = "problem_"
file_extention = ".py"
number_of_files = 2
while (i < number_of_files):

    # make_a_file(file_name_str + i + file_extention)
    file_name_for_argumet = file_name_str + str(i) + file_extention
    make_a_file(file_name_for_argumet)
    i = i + 1
