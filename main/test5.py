from bs4 import BeautifulSoup
import re
import os
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import time
import random
import pickle

# <--     ##############################################################################
folder_path = 'main\\text_only'

files_list = os.listdir(folder_path)

# counter=1

for filename in files_list:
    html_file_path = os.path.join(folder_path, filename)

    try:
        with open(html_file_path, 'r', encoding="utf-8") as f:

            content = f.read()

            soup = BeautifulSoup(content, 'html.parser')

            text = soup.get_text(separator='\n', strip=True)

            question = re.search(r"Question", text)
            question_position = question.start()

            answer = re.search(r"Answer", text)
            answer_position = answer.start()

            question_data = text[question_position:answer_position]
            answer_data = text[answer_position:]

            match = re.findall(
                r"Total answers posted by the expert is: \d*", text)
            answer_data = answer_data.replace(match[0], "")

            with open('question.txt', 'w', encoding='utf-8') as f:
                f.write(question_data)

            with open('answer.txt', 'w', encoding='utf-8') as f:
                f.write(answer_data)

    except:

        with open('main\\counter.txt', 'r') as f:
            counter = f.read()

        counter = int(counter)

        source_file_path = html_file_path
        destination_path = f'main\\dump1\\data_file{counter}.html'

        shutil.copy2(source_file_path, destination_path)
        counter += 1

        counter = str(counter)

        with open('main\\counter.txt', 'w') as f:
            f.write(counter)
        continue


#############################################################################################################################

    try:
        file = open('answer.txt', 'r')
        read_data = file.read()
        per_word1 = read_data.split()
        if(len(per_word1)>100 and len(per_word1)<120):
            options = webdriver.ChromeOptions()
            options.add_argument("--user-data-dir=C:\\Users\\Omen\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 4")
            # options.add_argument("--window-size=100,100")
            driver = webdriver.Chrome(options=options)
        
        elif(len(per_word1)>70 and len(per_word1)<=100):
            options = webdriver.ChromeOptions()
            options.add_argument("--user-data-dir=C:\\Users\\Omen\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
            # options.add_argument("--window-size=100,100")
            driver = webdriver.Chrome(options=options)
        
        elif(len(per_word1)>50 and len(per_word1)<=70):
            options = webdriver.ChromeOptions()
            options.add_argument("--user-data-dir=C:\\Users\\Omen\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 4")
            # options.add_argument("--window-size=100,100")
            driver = webdriver.Chrome(options=options)



        elif(len(per_word1)>20 and len(per_word1)<=50):
            options = webdriver.ChromeOptions()
            options.add_argument(("--user-data-dir=C:\\Users\\Omen\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1") or ("--user-data-dir=C:\\Users\\Omen\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2"))
            # options.add_argument("--window-size=100,100")
            driver = webdriver.Chrome(options=options)

        elif(len(per_word1)>=0 and len(per_word1)<=20):
            options = webdriver.ChromeOptions()
            options.add_argument("--user-data-dir=C:\\Users\\Omen\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3")
            # options.add_argument("--window-size=100,100")
            driver = webdriver.Chrome(options=options)

        elif(len(per_word1)>=120):
            options = webdriver.ChromeOptions()
            options.add_argument("--user-data-dir=C:\\Users\\Omen\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Default")
            # options.add_argument("--window-size=100,100")
            driver = webdriver.Chrome(options=options)

        else:
            options = webdriver.ChromeOptions()
            options.add_argument("--user-data-dir=C:\\Users\\Omen\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
            # options.add_argument("--window-size=100,100")
            driver = webdriver.Chrome(options=options)

        input_file_path = "answer.txt"
        file = open(input_file_path, 'r')
        read_data = file.read()
        per_word = read_data.split()
        driver.get('https://quillbot.com/')
            # time.sleep(0.5)

        with open(input_file_path, 'r') as f:
                    content = f.read()

        driver.find_element(By.ID, "inputText").send_keys(content)
        time.sleep(1)

        driver.find_element(By.XPATH, '//button/parent::div[@class="MuiGrid-root css-rfnosa"]').click()
        time.sleep(8)

        paraphrased_text = driver.find_element(
                By.XPATH, '//div[@id="outputText"]')

                # print(paraphrased_text.text)

        output_file_path = "main\\parapharased.txt"
        with open(output_file_path, 'w') as f:
                    f.write(paraphrased_text.text)

        # if(counter%6==0):
        driver.close()
        # driver.get('https://quillbot.com/')

    except:
        with open('main\\counter.txt', 'r') as f:
            counter = f.read()

            counter = int(counter)

            source_file_path = html_file_path
            destination_path = f'main\\dump2\\data_file{counter}.html'

            shutil.copy2(source_file_path, destination_path)
            counter += 1

            counter = str(counter)

            with open('main\\counter.txt', 'w') as f:
                f.write(counter)
        continue


###############################################################################################################################

    with open('main\\counter.txt', 'r') as f:
        counter = f.read()

    counter = int(counter)

    new_file_path = f'main\\main_files\\data_file{counter}.txt'

    with open('main\\question.txt', 'r') as f:
        data_question = f.read()

    with open('main\\parapharased.txt', 'r') as f:
        data_answer = f.read()

    with open(new_file_path, 'w') as f:
        f.write(data_question)
        f.write("\n")
        f.write(data_answer)

    counter += 1

    counter = str(counter)

    with open('main\\counter.txt', 'w') as f:
        f.write(counter)

    random_number = random.randint(1, 5)
    time.sleep(random_number)
