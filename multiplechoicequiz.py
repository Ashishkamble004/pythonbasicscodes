#refer question.py as well for this
from question import Question


question_prompts = [
    "What color are apples?\n(a) Red/Green \n(b) Purple\n(c) Orange \n\n",
    "What color are Bananas?\n(a) Teal \n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"

]

questionsarray =[
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_tests(questionsarray):
    score = 0
    for questionobj in questionsarray:
        answer = input(questionobj.prompt)
        if answer == questionobj.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questionsarray)) + " questions right" )

run_tests(questionsarray)