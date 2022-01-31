import datetime
import os

QUESTIONS: list = ["what went good?", "what went bad?", "goals for tomorrow?"]
FILE_NAME: str = "Journal.md"

def fill_in_answers() -> list:
    answers: list = []
    while (answer := input()) != "":
        answers.append(answer)

    return answers

def write_to_file(contents: dict):
    date = datetime.datetime.now()
    with open(FILE_NAME, "a+") as journal:
        if os.path.getsize(FILE_NAME) == 0:
            journal.write(f"# My daily journal\n")

        journal.write(f"##{date.day}/{date.month}/{date.year}\n")

        for question, answers in contents.items():
            journal.write(f"### {question}\n")

            for answer in answers:
                journal.write(f"- {answer}\n")

def main() -> None:
    counter: int = 0
    answ: dict = {}
    for question in QUESTIONS:
        print(question)
        answ[QUESTIONS[counter]] = fill_in_answers()
        counter += 1

    write_to_file(answ)

if __name__ == "__main__":
    main()
