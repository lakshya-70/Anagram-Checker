# 39th github project --> Anagram Checker
print('----------Anagram Checker----------')
def is_anagram(a, b):
    clean = lambda s: sorted(s.lower().replace(" ", ""))
    return clean(a) == clean(b)


def main():
    word1 = input("First word: ").strip()
    word2 = input("Second word: ").strip()

    if not word1 or not word2:
        print("Both words are required.")
        return

    if is_anagram(word1, word2):
        print(f'"{word1}" and "{word2}" are anagrams.')
    else:
        print(f'"{word1}" and "{word2}" are not anagrams.')



main()