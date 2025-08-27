filename= input("Enter the input file name: ")
try:

    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n")
        print(file.read)
except FileNotFoundError:
    print("Error: The file was not found.")

except PermissionError:
    print("Error: You don't have permission to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

