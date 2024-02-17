def count_words_and_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the content of the file
            content = file.read()

            # Counting words and lines
            word_count = len(content.split())
            line_count = content.count('\n')  # Adding 1 for the last line

            return word_count, line_count

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'sample_text.txt'  # Change this to the path of your text file

result = count_words_and_lines(file_path)

if result:
    word_count, line_count = result
    print(f"Number of words: {word_count}")
    print(f"Number of lines: {line_count}")
