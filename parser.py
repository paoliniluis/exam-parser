import json

questions = {}
with open('exam1.json') as json_file:
    questions = json.load(json_file)
    with open(r"fileToWrite.txt", "+w") as writer:
        for question in questions:
            question['question'] = question['question'].replace('\n', '')
            concatOfAnswers = ''
            for answer in question['answers']:
                answer = answer.replace('\n', '')
                if '(Correct)' in answer:
                    answer = f'{answer[:len(answer)-13].strip()}\tcorrect\t'
                else:
                    answer = f'{answer.strip()}\tincorrect\t'
                concatOfAnswers = concatOfAnswers + answer
            writer.write(f'{question["type"]}\t{question["question"]}\t{concatOfAnswers}\n')