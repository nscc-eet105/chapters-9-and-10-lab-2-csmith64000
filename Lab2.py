#Chris Smith
#07/06/2025
#Lab 2 Chapters 9&10


def main():

    print("File Processor")

    file_name = input("Enter the name of the file you wish to process: ")

    try:
        with open(file_name, "r") as f:
            text = f.read()

        words = text.split()
        total_words = len(words)

        capitalized_words = 0
        for word in words:
            if word[0].isupper():
                capitalized_words += 1
        print(f"The file {file_name} contains {total_words} words of which {capitalized_words} of them are capitalized.")

        
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")

main()              



