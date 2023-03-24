from bs4 import BeautifulSoup
import re
import os
import shutil




with open('./abc.html', 'r',encoding="utf-8") as f:

    content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    text=soup.get_text(separator='\n', strip=True)

    question=re.search(r"Question",text)
    question_position=question.start()

    answer=re.search(r"Answer",text)
    answer_position=answer.start()



    question_data=text[question_position:answer_position]
    answer_data=text[answer_position:]

    match=re.findall(r"Total answers posted by the expert is: \d*",text)
    answer_data=answer_data.replace(match[0],"")
    answer_data=str(answer_data)

    with open('./question.txt', 'w', encoding='utf-8') as f:
        f.write(question_data)

    with open('./answer.txt', 'w', encoding='utf-8') as f:
        f.write(answer_data)

# question=re.search(r"Question",text)
# question_position=question.start()

# answer=re.search(r"Answer",text)
# answer_position=answer.start()



# question_data=text[question_position:answer_position]
# answer_data=text[answer_position:]

# remove_text=text[0:start]
# text=text.replace(remove_text,"")

# match=re.findall(r"Total answers posted by the expert is: \d*",text)
# answer_data=answer_data.replace(match[0],"")

# with open('./question.txt', 'w') as f:
#     f.write(question_data)

# with open('./answer.txt', 'w') as f:
#     f.write(answer_data)


