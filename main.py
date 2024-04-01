def main():
    path_to_file = "books/frankenstein.txt"  
    with open(path_to_file) as f:
        file_contents = f.read()
        
    word_count = count_words(file_contents)
    
    letter_counts = count_letters(file_contents)
    sorted_letters = sort_by_count(letter_counts)

    print_report(path_to_file, word_count, sorted_letters)
    

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    text_lower = text.lower()  # Convert text to lowercase
    letter_counts = {}
    for char in text_lower:
        if char.isalpha():  # Check if character is a letter
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts

def sort_by_count(letter_counts):
    sorted_letters = [{'char': char, 'count': count} for char, count in letter_counts.items()]
    sorted_letters.sort(key=lambda x: x['count'], reverse=True)
    return sorted_letters

def print_report(file_path, word_count, sorted_letters):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    print("Character counts:")
    for entry in sorted_letters:
        print(f"The '{entry['char']}' character was found {entry['count']} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()
    
