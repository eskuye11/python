quizs = [
    ['1. what is the capital of US?\n a) Dallas \n b) Atlanta \n c) washington\n\nYour Answer : ', 'c'],
    ['2. when was the Us Constitution signed? \n a) 1998 \n b) 1787 \n c) 2020\n\nYour Answer : ', 'b'],
    ['3. who is the president of the US? \n a) Obama \n b) biden \n c) trump\n\nYour Anser : ', 'c'],
    ['4. how often president elect in US? \n a) 2 years \n b) 4 years \n c) 6 years\n\nYour Anser : ', 'b'],
    ['5. how many states in US? \n a) 52 \n b) 49 \n c) 50\n\nYour Anser : ', 'c']
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question[0])
        if answer.lower() == question[1]:
            score += 1
        else:
            print(f"\x1b[31mSorry!, The Correct answer was ' {question[1].upper()}' \x1b[00m \n ")
    greet = {0: 'VERY SORRY !', 1: 'Too Bad !', 2: 'Not Good', 3: 'Need Word', 4: 'Nice Word', 5: 'Congratulation !'}
    print(f"\n\n \033[1:32m   {greet[score]}, You got {score * 20}/{len(questions) * 20} Correct. \033[00m \n")


if __name__ == '__main__':
    run_test(quizs)