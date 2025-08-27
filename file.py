def modify_file(input_file, output_file):
    try:
        with open(input_file, "r") as infile:
            lines = infile.readlines()

        # Modification: Add line numbers and uppercase the content
        modified_lines = [f"{i+1}: {line.upper()}" for i, line in enumerate(lines)]

        with open(output_file, "w") as outfile:
            outfile.writelines(modified_lines)

        print(f"Modified content written to '{output_file}'")

    except FileNotFoundError:
        print("Error: The input file does not exist.")
    except PermissionError:
        print("Error: You don’t have permission to access the file.")
    except Exception as e:
        print(f"Unexpected error: {e}")
