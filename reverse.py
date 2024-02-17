def print_reverse(string):
    if len(string) == 0:
        return  # Base case: an empty string

    # Print the last character
    print(string[-1], end='')

    # Recursive call with the substring excluding the last character
    print_reverse(string[:-1])

# Example usage
input_string = "Hello, World!"
print_reverse(input_string)
