def main():
    with open("books/frankenstein.txt") as f: #Open the novel from the file location in 'read mode'. The 'with' ensures the file is closed when exited.

        file_contents = f.read() #Reads the novel contents of 'frankenstein.txt' into the string 'file_contents'.

    num_words = get_num_words(file_contents) # Pass the file contents to get_num_words
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")  # Print the word count - printing this first so its easier to see!

    input("\nPress Enter to view the Character Count:\n") # Prompt user to press 'Enter' to continue to stop the scroll of an eternity to the top of the novel to see 'word count'.
  
    # Processes the 'file_contents' into lowercase.
    lowered_string = file_contents.lower() # Converts the string to lowercase
    # Count characters
    char_counts = count_characters(lowered_string)

    # Sort characters by count in descending order
    sorted_char_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_char_counts:
        print(f"The '{char}' character was found {count} times")
    print(f"--- End report ---")
    
    input("\nPress Enter to view the novel contents:\n")
    print(file_contents)
    
def get_num_words(text): 
    words = text.split()
    return len(words)

#define the 'count_characters function.
def count_characters(text):
    character_counts = {} 
    #Iterate through each character in the string. The string being the novel.
    for char in text: # If character is already in the dictionary....
        if char.isalpha():  # Check if the character is an alphabet letter
            if char in character_counts:
                character_counts[char] += 1  # increase the character count by 1
            else:
                character_counts[char] = 1  # Set the count of the character to 1.
    return character_counts

# This ensures the main function is called only when this script is run directly.
if __name__ == "__main__":
    main()