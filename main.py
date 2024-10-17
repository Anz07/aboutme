import requests
import raducord as du
from colorama import Fore, init
import time, os
import re as r
import threading
import tls_client
from datetime import datetime
from pystyle import Write, Colors
import dotenv

dotenv.load_dotenv()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

green = Fore.GREEN
red = Fore.RED
cyan = Fore.LIGHTCYAN_EX
reset = Fore.RESET

auto_verify = dotenv.get_key(dotenv_path=".env", key_to_get="AUTO_VERIFY")
password_pyc = dotenv.get_key(dotenv_path=".env", key_to_get="PASSWORD")
headless_option = 'N'

def ambilwaktu():
    date = datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee

def tronzip():
    response = requests.get('http://ip-api.com/json/?fields=query')
    if response.status_code == 200:
        ip = response.json()['query']
        return ip
    
def getNegaraTronz():
    response = requests.get(f'http://ip-api.com/json/{tronzip()}?fields=countryCode')
    if response.status_code == 200:
        CountryID = response.json()['countryCode']
        return CountryID

class mailworktronz:
    def dapatemailtronz(self):
        while True:
            try:
                email = requests.post('https://api.internal.temp-mail.io/api/v3/email/new', json={"min_name_length": 7, "max_name_length": 7}).json()['email']
                return email
            except Exception as e:
                print('Failed to get Email')
        
    def verifyemailtronz(self, mail):
        ulangi_teros = 0
        while True:
            try:
                if ulangi_teros >= 20:
                    return None
                response = requests.get(f"https://api.internal.temp-mail.io/api/v3/email/{mail}/messages")
                json = response.json()
                ulangi_teros += 1
                if len(json) > 0:
                    for message in json:
                        if 'payco' in str(message).lower():
                            html = message['body_html']
                            middleLink = html.split('https://id.payco.com/emailAuth.nhn?m=')[1].split('%3D')[0]
                            finalLink = 'https://id.payco.com/emailAuth.nhn?m=' + middleLink + '%3D'
                            return finalLink
                time.sleep(1)
            except Exception as e:
                print(e)
                ulangi_teros += 1

class tronzspdmsi:
    def selentronz(self):
        katasanditronz = f'{password_pyc}'
        mailah = mailworktronz()
        service = Service(executable_path="chromedriver.exe")

        chrome_options = Options()
        chrome_options.add_argument("--disable-logging")
        chrome_options.add_argument("--log-level=3")
        if headless_option == 'Y':
            chrome_options.add_argument("--headless")
        elif headless_option == 'y':
            chrome_options.add_argument("--headless")
        else:
            None

        driver = webdriver.Chrome(service=service)
        driver.get("https://id.payco.com/join.nhn?serviceProviderCode=PAY&inflowKey=www&userLocale=ko_KR&nextURL=https%3A%2F%2Fwww.payco.com%2FafterLogin.nhn")
        print()
        Write.Print(f'[ {ambilwaktu()} |  TASK CREATED  | {tronzip()} ({getNegaraTronz()}) ]\n', Colors.yellow_to_red, interval=0.0000)
        WebDriverWait(driver, 3).until(
           EC.presence_of_element_located((By.ID, "checkboxAll"))
         )

        accept = driver.find_element(By.ID, "checkboxAll")
        accept.click()
        confirmaccept = driver.find_element(By.ID, "confirmButton")
        confirmaccept.click()
        time.sleep(2)

        anothermethod = driver.find_element(By.ID, "selectOtherMethod")
        anothermethod.click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "popupCancelButton"))
         )
        emailsahajatronz = driver.find_element(By.ID, "popupCancelButton")
        emailsahajatronz.click()

        mail = mailah.dapatemailtronz()
        masukkanemailsir = driver.find_element(By.ID, "emailId")
        masukkanemailsir.clear()
        masukkanemailsir.send_keys(mail)

        masukpwjir = driver.find_element(By.ID, "password")
        masukpwjir.clear()
        masukpwjir.send_keys(katasanditronz)
        time.sleep(2)

        confirmdata = driver.find_element(By.ID, "confirmButton")
        confirmdata.click()
        time.sleep(3)
        cobaverify = mailah.verifyemailtronz(mail)
        cobaverify

        Write.Print(f"""
[ + ]  -  Email: {mail}
[ + ]  -  Password: {katasanditronz}
[ + ]  -  Verify URL: {cobaverify[:20]}****\n""", Colors.yellow_to_red, interval=0.0000)
        print(Fore.RED + "*If Your Auto-Verify On, Please Dont Exit or Turn Off Your Computer!")
        print()

        time.sleep(0.5)

        if auto_verify == 'Y':
            driver.get(f'{cobaverify}')
            time.sleep(2)
        elif auto_verify == 'y':
            driver.get(f'{cobaverify}')
            time.sleep(2)
        else:
            None

        driver.quit()
        with open("result.txt", "a+", encoding="utf-8") as f:
            f.write(f'{mail} | {katasanditronz} | {ambilwaktu()}')
        with open("verify-link.txt", "a+", encoding="utf-8") as a:
            a.write(f'{mail} | {cobaverify}')
        Write.Print(f'[ {ambilwaktu()} |  TASK SAVED  | result.txt | verify-link.txt]', Colors.yellow_to_red, interval=0.0000)

    def thread(self, jumlah):
        try:
            threads = []
            count = 0

            while count < int(jumlah):
                thread = threading.Thread(target=self.selentronz)
                threads.append(thread)
                thread.start()
                count += 1

                for thread in threads:
                    thread.join()
        except KeyboardInterrupt:
            pass

    def uibiarcakeptronz(self):
        du.Console.clear()
        du.Console.title(f"TronzPaycoV2 Free Version | Telegram: @tronzbg | Detected Password: {password_pyc} | Auto-Verify: {auto_verify}")
        Write.Print('[ ! ]  :  This Tools Are Credited To @tronzbg In Telegram\n', Colors.green_to_white, interval=0.0000)
        time.sleep(2)
        du.Console.clear()
        Write.Print('[ ! ]  :  Selling Other Premium Tools, Please DM Me On Telegram\n', Colors.green_to_white, interval=0.0000)
        time.sleep(2)
        du.Console.clear()
        Write.Print('[ ! ]  :  Please Read All README.txt, THX!\n', Colors.green_to_white, interval=0.0000)
        time.sleep(2)
        du.Console.clear()
        Write.Print('[ X ]  -  Welcome To Dashboard!\n', Colors.yellow_to_red, interval=0.0000)
        amount = Write.Input('[ # ]  -  How Many Account You Want: ', Colors.yellow_to_red, interval=0.0000)
        tronz.thread(amount)

tronz = tronzspdmsi()
tronz.uibiarcakeptronz()