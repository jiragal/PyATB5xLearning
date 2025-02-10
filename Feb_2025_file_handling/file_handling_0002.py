#Python program to read character by character from a file

def read_file_character_by_character(filepath):
    try:
        with open(filepath, mode='r') as file:
            while True:
                char = file.read(1)   # read by character
                if not char:
                    break
                print(char)
    except FileNotFoundError:
        print(f"Error: File not found at{filepath}")

    except Exception as e:
        print(f"An error occured{e}")


#Medthod is calling and passing file
read_file_character_by_character("GFG.txt")
