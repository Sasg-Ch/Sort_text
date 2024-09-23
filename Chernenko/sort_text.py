import re

def get_priority(text):
    if re.search('[а-яі]', text,flags=re.IGNORECASE):
        return 1,text
    if re.search('[a-z]', text,flags=re.IGNORECASE):
        return 2,text
    return 3,text

def f_sentence_text(text):
    selected_words = []
    for word in text:
        selected_words.append(word)
        if re.search(r'[.!?]', word):
            break
    fisrt_sentence = ' '.join(selected_words)
    return fisrt_sentence

try:
    with open('example_text.txt',"r") as file:
        text = file.read()
except FileNotFoundError:
    print("Файл не знайдено.")
except PermissionError:
    print("Недостатньо прав для доступу до файлу.")

words_file = text.split()

f_sentence = f_sentence_text(words_file)

text_words = re.sub(r'[.,]','',text).split()
text_words.sort(key=get_priority)
text_words_str = ' '.join(text_words)

count_words = 0
for word in text_words:
    count_words += 1

print(f'Перше речення: {f_sentence}\nВідсортовані слова A-я, A-z: {text_words_str}\nКількість слів: {count_words}')