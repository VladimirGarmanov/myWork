import random

word_pairs = {
    "яблоко": "apple",
    "кот": "cat",
    "дом": "house",
    "солнце": "sun",
    "вода": "water",
}

def play_game(words, language):
    score = 0
    incorrect_first_attempt = []
    incorrect_second_attempt = []
    current_words = dict(words)

    while current_words:
        word = random.choice(list(current_words.keys()))
        correct_translation = current_words[word].lower()
        user_translation = input(f"{word.capitalize()} ({language.capitalize()}): ").lower()

        if user_translation == correct_translation:
            if user_translation in incorrect_first_attempt:
                print(f"Правильно! +1 балл.")
                score += 1
                incorrect_first_attempt.remove(user_translation)
            elif user_translation in incorrect_second_attempt:
                print("Вы правильно ответили, но не начисляем баллы за это слово.")
            else:
                print(f"Правильно! +2 балла.")
                score += 2
            del current_words[word]
        else:
            print(f"Неправильно. Правильный ответ: {correct_translation}. 0 баллов.")
            if current_words[word] in incorrect_first_attempt:
                incorrect_second_attempt.append(correct_translation)
                incorrect_first_attempt.remove(correct_translation)
            else:
                incorrect_first_attempt.append(correct_translation)

    total_points = len(words) * 2
    percentage = (score / total_points) * 100
    print(f"\nИгра завершена. Вы набрали {score} баллов из {total_points} возможных ({percentage:.2f}%).")

language_choice = input("Выберите язык для тренировки (русский/английский): ").lower()

if language_choice == "русский":
    play_game(word_pairs, "русский")
elif language_choice == "английский":
    reversed_word_pairs = {v: k for k, v in word_pairs.items()}
    play_game(reversed_word_pairs, "английский")
else:
    print("Выбран неверный язык.")
