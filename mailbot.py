from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

# os drivers sao usados para a interação do selenium com o browser
# input de usuario = //*[@id="identifierId"]
# botao proximo usuario = //*[@id="identifierNext"]
# input de senha = //*[@id="password"]
# botao proximo senha = //*[@id="passwordNext"]

class mail_bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\pryst\OneDrive\Documentos\chromedriver.exe')

    def login(self):
        driver = self.driver
        driver.get('https://mail.google.com/')
        time.sleep(1)

        userInput = driver.find_element_by_xpath("//*[@id='identifierId']")
        userInput.clear()
        userInput.send_keys(self.username)

        nextButton = driver.find_element_by_xpath("//*[@id='identifierNext']")
        nextButton.click()
        time.sleep(1)

        passwordInput = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
        passwordInput.clear()
        passwordInput.send_keys(self.password)
    
        nextButton = driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/div[2]")  
        nextButton.click()
        

    def clean_mailbox(self):
        driver = self.driver
        time.sleep(1)

        delete_button = driver.find_element_by_xpath("//*[@id=':4']/div/div[1]/div[1]/div/div/div[2]/div[3]")
        time.sleep(5)
        element_content = driver.find_element_by_xpath("//*[@id=':ep']/div/div[2]/div").text
        time.sleep(5)
        check_box = driver.find_element_by_xpath("//*[@id=':1w']/div[1]/span")

        number_emails = int(element_content.replace('.', ''))
        while(number_emails > 0):
            check_box.click()
            time.sleep(2)
            delete_button.click()
            number_emails -= 10
            time.sleep(5)
        else:
            print("Voce nao tem mais emails")
        
email = input("Digite seu email: ")
password = input("Digite sua senha: ")

nesquinho = mail_bot(email, password)
nesquinho.login()
nesquinho.clean_mailbox()