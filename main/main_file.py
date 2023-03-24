from bs4 import BeautifulSoup
import re
import os
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import time






folder_path = './text_only'           #    <--     ##############################################################################

files_list=os.listdir(folder_path)

# counter=1

for filename in files_list:
    html_file_path = os.path.join(folder_path, filename)

    try:
        with open(html_file_path, 'r') as f:

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

            with open('./question.txt', 'w') as f:
                f.write(question_data)

            with open('./answer.txt', 'w') as f:
                f.write(answer_data)

    except:

        with open('./counter.txt', 'r') as f:
            counter=f.read()

        counter=int(counter)

        source_file_path = html_file_path
        destination_path = f'./dump1/data_file{counter}.html'

        shutil.copy2(source_file_path, destination_path)
        counter += 1

        counter=str(counter)

        with open('./counter.txt', 'w') as f:
            f.write(counter)
        continue



#############################################################################################################################

    try:

        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1\\")
        driver = webdriver.Chrome(options=options)
        # driver = uc.Chrome(options=options)

        driver.get('https://quillbot.com')
        # driver.minimize_window()
        time.sleep(0.5)

        input_file_path="./answer.txt"
        with open(input_file_path, 'r') as f:
            content = f.read()

        driver.find_element(By.ID,"inputText").send_keys(content)
        # time.sleep(1)

        driver.find_element(By.XPATH, '//button/parent::div[@class="MuiGrid-root css-rfnosa"]').click()
        time.sleep(10)

        paraphrased_text = driver.find_element(By.XPATH, '//div[@id="outputText"]')

        # print(paraphrased_text.text)

        output_file_path="./parapharased.txt"
        with open(output_file_path, 'w') as f:
            f.write(paraphrased_text.text)

        driver.quit()

    except:
            with open('./counter.txt', 'r') as f:
                counter=f.read()

                counter=int(counter)

                source_file_path = html_file_path
                destination_path = f'./dump2/data_file{counter}.html'

                shutil.copy2(source_file_path, destination_path)
                counter += 1

                counter=str(counter)

                with open('./counter.txt', 'w') as f:
                    f.write(counter)
            continue


###############################################################################################################################

    with open('./counter.txt', 'r') as f:
        counter=f.read()

    counter=int(counter)

    new_file_path=f'./main_files/data_file{counter}.txt'

    with open('./question.txt', 'r') as f:
        data_question=f.read()

    with open('./parapharased.txt', 'r') as f:
        data_answer=f.read()

    with open(new_file_path, 'w') as f:
        f.write(data_question)
        f.write("\n")
        f.write(data_answer)

    counter += 1

    counter=str(counter)

    with open('./counter.txt', 'w') as f:
        f.write(counter)
