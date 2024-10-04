# This program finds all words in a document that begin with any letter from the given arguments. It outputs the document with the matched words highlighted in ALL-CAPS.
# usage format: python3 highlight.py filename.txt A B C [...]

import sys
import re

ARGS = sys.argv
EXTRA_CHARS = 'äÄöÖüÜßåÅ'
REPLACEMENT_CHARS = ['‽', '‰', '‸', '‡', '¤', '¬']

def show_help():
    print("Usage: python highlight.py <filename> [<A> ...]")

def highlight_words_by_starting_letter(input_text, letters):

    search_letters = ''
    for letter in letters:
        search_letters += letter.lower()
        search_letters += letter.upper()

    pattern = r'\b[' + search_letters + r'][A-Za-z]*'
    output_text = re.sub(pattern, lambda match: match.group(0).upper(), input_text)

    return output_text


def run():

    if len(ARGS) < 2:
        print("Too few arguments.")
        show_help()
        return

    file = open(ARGS[1])
    text = ''
    for line in file:
        text += line

    # Check args
    for i, arg in enumerate(ARGS):
        if i > 2:
            if len(arg) > 1:
                print("Arguments after the filename should be individual alphabetic characters (a-z) or (A-Z)")
                return

            exp = r'[a-zA-Z' + EXTRA_CHARS + r']'
            if not re.match(exp, arg):
                print("Arguments after the filename should be individual alphabetic characters (a-z) or (A-Z)")
                return

    highlighted_text = highlight_words_by_starting_letter(text, ARGS[2:])
    print(highlighted_text)

# Run
run()
