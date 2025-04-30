from stats import *

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        return f.read()

def main():
    text = get_book_text("./books/frankenstein.txt")
    report_start = """============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt..."""
    num_words = count_num_words(text)
    report_words = f"""----------- Word Count ----------
    Found {num_words} total words"""
    report_characters = f"""--------- Character Count -------"""
    characters = count_num_characters(text)
    sorted_characters = sorted_num_characters(characters)
    report_char_count = []
    for char in sorted_characters:
        report_char_count.append(f"""{char["char"]}: {char["count"]}""")
    report_char_count = "\n".join(report_char_count)
    report_end = """============= END ==============="""
    print(report_start, report_words, report_characters, report_char_count, report_end, sep="\n")
if __name__ == "__main__":
    main()