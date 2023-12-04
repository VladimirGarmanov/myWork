
import random

word_pairs = {'дом': 'house', 'солнце': 'sun', 'книга': 'book', 'стол': 'table', 'вода': 'water'}

language_choice = 'ru'

score = 0
shown_words = list(word_pairs.keys())

for i in range(len(shown_words)):

    current_word = random.choice(shown_words)

    user_translation = input(f"Переведите слово '{current_word}': ").lower()



    if user_translation == word_pairs[current_word]:
        print("Правильно!")
        score += 2
        shown_words.remove(current_word)
    else:
        print(f"Неправильно. Правильный ответ: {word_pairs[current_word]}")
        score += 0
        shown_words.remove(current_word)

percentage = (score / (len(word_pairs) * 2)) * 100
print(f"\nВы закончили тренировку! Набрано баллов: {score}/10, процент правильных ответов: {percentage}%.")