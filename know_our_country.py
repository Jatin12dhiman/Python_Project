from random import shuffle4
qus=[
    ("This is name of your country","india"),
    ("This is the capital of your country","newdelhi"),
    ("What is the national flower","Lotus"),
    ("What is the name of your national animal","tiger"),
    ("What is the name of your national anthem","janganman"),
    ("What is the your nationa flag","tiranga")
]
shuffle(qus)
right=0
wrong=0
for question,right_ans in qus:
    ans=input(question + " ")
    if ans.lower() == right_ans:
        right+=1
    else:
        print("No , the right answer is: ",right_ans)
        wrong +=1
print("Congratulation!")
print("You gave",right,"right answer and",wrong,"wrong answer")