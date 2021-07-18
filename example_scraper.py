#!/usr/bin/python3

from selenium import webdriver

# fix taken from https://dev.to/t00m/testing-selenium-4-0-0a5-pre-release-with-python-42h7
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# for using special keys like enter, alt, F1
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup as bs

# hidden password entry
import getpass

# colored terminal output
from colorama import Fore


import re as re
import time
import pandas as pd


# additional setup for fix fix taken from https://dev.to/t00m/testing-selenium-4-0-0a5-pre-release-with-python-42h7
options = Options()

# path to firefox profile
options.profile = '/home/cn1d4r14n/.mozilla/firefox/ct8fbiwt.default'

options.headless = False

service = Service('/home/cn1d4r14n/Documents/geckodriver')


driver = webdriver.Firefox(options=options, service=service)



def log_in_to_linkedin():
    # initial get request that takes us to the login page
    driver.get('https://www.linkedin.com/uas/login')
    time.sleep(1)
    print(driver.title)
    assert "LinkedIn" in driver.title
    #USERNAME = input("Enter username: ")
    USERNAME = "cephalopod31956@gmail.com"
    PASSWORD = getpass.getpass(f"Enter password: ")
    # We'll now login using the provided credentials
    email = driver.find_element_by_id("username")
    print(email)
    email.send_keys(USERNAME)
    password = driver.find_element_by_id("password")
    print(password)
    password.send_keys(PASSWORD)
    password.send_keys(Keys.RETURN)
    time.sleep(6)


def global_search() -> None:
    search_box = driver.find_elements_by_class_name("search-global-typeahead__input.always-show-placeholder")
    # take the element out of the list
    search_box = search_box[0]
    print(search_box)
    search_term = input("Input search term: ")
    # clear currently prepopulated or entered text (if any)
    search_box.clear()
    # input new search term and subsequently press enter
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    time.sleep(7)



def main() -> None:
    print("mark0")
    log_in_to_linkedin()
    print("mark1")
    global_search()
    print("mark2")
    driver.quit()
    print("mark3")




if __name__ == "__main__":
    main()






