# Search if the word “learning” exists in the file or not.
# Read the file
with open("practice.txt", 'r') as f:
    lines = f.readlines()
    # print(lines)
    # Iterate the file
    for item, index in enumerate(lines, start=1):
        # print(item, index)
        if 'learning' in index:
            print(f"The word 'learning' found on line number {item}")
            f.close()

# 2nd Method we can also do lik this
word = 'Technology'
f = open("industry.csv", 'r')
data_read = f.read()
if (data_read.find(word)) != 0:
    print('Found')
else:
    print('Not found')
f.close()


# By using function also we can achieve this
# Function to find a specific word in a file
def find_word_in_file(file_path, word_to_find):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read all lines of the file
            lines = file.readlines()

            # Iterate through each line
            for line_number, line in enumerate(lines, start=1):
                # Check if the word is in the current line
                if word_to_find in line:
                    print(f"Word '{word_to_find}' found on line {line_number}: {line.strip()}")
                    return  # Exit after finding the first occurrence

            print(f"Word '{word_to_find}' not found in the file.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = "industry.csv"  # Replace with your file's path
word_to_find = "Sales"  # Replace with the word you want to search
find_word_in_file(file_path, word_to_find)

