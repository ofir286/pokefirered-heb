import sys
import os


LETTER_DICTIONARY =\
{
    "א" : "E",
    "ב" : "F",
    "ג" : "G",
    "ד" : "H",
    "ה" : "I",
    "ו" : "J",
    "ז" : "K",
    "ח" : "L",
    "ט" : "M",
    "י" : "N",
    "כ" : "O",
    "ל" : "P",
    "מ" : "Q",
    "נ" : "R",
    "ס" : "S",
    "ע" : "T",
    "פ" : "U",
    "צ" : "V",
    "ק" : "W",
    "ר" : "X",
    "ש" : "Y",
    "ת" : "Z",
    "ן" : "a",
    "ם" : "b",
    "ץ" : "c",
    "ף" : "d",
    "ך" : "e"
}
SEP = "###Translated###"


def main():

    # Make sure a path is given.
    if len(sys.argv) >= 2:
        path = sys.argv[1]
        file_paths = []

        # Handle dirs as well as files.
        if os.path.isdir(path):
            files = os.listdir(path)
            file_paths =[os.path.join(path, single_file) for single_file in files]
        else:
            file_paths.append(path)

        for file_path in file_paths:
            with open(file_path , "r", encoding="utf-8") as f:
                original_lines = f.read().splitlines()

            # Make sure this is a file we need to translate.
            if SEP not in original_lines:
                continue

            # Get only the hebrew.
            original_lines = original_lines[original_lines.index(SEP)+1:]
            translated_file_path = "_translated.".join(file_path.split("."))
            translated_lines = ""

            # Replace all letters with the correct values.
            for line in original_lines:
                for letter in LETTER_DICTIONARY:
                    if letter in line:
                        line = line.replace(letter, LETTER_DICTIONARY[letter])

                # Reverse the line because hebrew is RTL language.
                line = line[::-1]
                translated_lines += line + "\n"
            with open(translated_file_path, "w", encoding="utf-8") as f:
                f.write(translated_lines)
    else:
        text = input("Enter text to translate:\n> ")
        for letter in LETTER_DICTIONARY:
            if letter in text:
                text = text.replace(letter, LETTER_DICTIONARY[letter])
        text = text[::-1]
        print(text)

    
if __name__ == "__main__":
    main()
