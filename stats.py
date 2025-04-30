from collections import Counter

def count_num_words(text: str) -> int:
    return len(text.split())

def count_num_characters(text: str) -> int:
    return dict(Counter(text.lower()))

    
def sorted_num_characters(all_chars: dict) -> list[dict]:
    final_chars = []
    for char, count in all_chars.items():
        if char.isalpha():
            final_chars.append({"char": char, "count": count})
    return sorted(final_chars, key=lambda x: x["count"], reverse=True)