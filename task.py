import re


def read_first_sentence(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            # Виділення першого речення
            sentence = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text.strip())[0]
            return sentence
    except FileNotFoundError:
        print(f"Помилка: файл '{file_path}' не знайдений.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None


def sort_words(sentence):
    # Видалення пунктуації
    words = re.findall(r'\b\w+\b', sentence.lower())
    return words


def split_by_language(words):
    ukrainian = []
    english = []
    for word in words:
        if re.match(r'^[а-яА-ЯєЄїЇіІґҐ]+$', word):  # Перевірка на українське слово
            ukrainian.append(word)
        else:  # Перевірка на англійське слово
            english.append(word)
    return sorted(ukrainian), sorted(english)


def main():
    file_path = 'text.txt'  # Замініть на шлях до вашого текстового файлу
    sentence = read_first_sentence(file_path)

    if sentence:
        print(f"Перше речення: {sentence}")
        words = sort_words(sentence)
        ukrainian_words, english_words = split_by_language(words)

        print(f"Українські слова (відсортовані): [{', '.join(ukrainian_words)}", end="]\n")
        print(f"Англійські слова (відсортовані): [{', '.join(english_words)}", end="]\n")
        print(f"Загальна кількість слів: {len(words)}")


if __name__ == "__main__":
    main()
