while True:
    # Savol sonini so'rash
    user = input("ismingizni kiriting:")
    count_of_questions = int(input("Savollar sonini kiriting: "))
    questions = []
    # Savollarni kiritish
    user_result = open("result.txt", "x")
    for i in range(1, count_of_questions + 1):
        question_text = input("Savolni kiriting: ")
        current_question = {
            'question': question_text,
            'answers': {},
            'true_answer': ''

        }
        # Javoblarni kiritish
        for answer_key in ['a', 'b', 'c']:
            entered_answer = input(f"{answer_key}: ")
            current_question['answers'][answer_key] = entered_answer

        true_answer = input("To'g'ri javobni tanlang: a/b/c")
        current_question['true_answer'] = true_answer
        questions.append(current_question)

    correct_answers = 0
    for question in questions:
        print("\nSavol:", question['question'])
        for key, value in question['answers'].items():
            print(f"{key}) {value}")
        user_answer = input("To'g'ri javobni tanlang: ")
        if user_answer == question['true_answer']:
            correct_answers += 1

    incorrect_answer = count_of_questions - correct_answers

    print("\nSavollar soni:", count_of_questions, "ta, to'g'ri javoblar", correct_answers, "ta."  "Xato javoblar soni",
          incorrect_answer)
    print("Ishtirokingiz uchun tashakkur!")

    user_result = open("result.txt", "a")
    user_result.write(user + "to'gri javoblar" + correct_answers + "xato javoblar" + incorrect_answer)
    user_statiscks = open("statistika", user_result)

    another_round = input("Yana bir test boshlashni xohlaysizmi? (ha/yo'q): ")
    if another_round.lower() != "ha":
        break
