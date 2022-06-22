# Charles Young
# 6/6/2020
# This file browses the crash history in WTFskins and saves the results into input.txt

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd


# clears old data from file
def clear_data(filename):
    f = open(str(filename), "w")
    f.write("")
    f.close()


class WTFLogin:
    # finds the site and accepts the agreements
    def __init__(self):
        self.driver = webdriver.Chrome("C:\Windows\chromedriver.exe")

    def login(self):
        self.driver.get('https://www.wtfskins.com/login')
        self.driver.find_element_by_class_name(
            'ng-pristine').click()
        self.driver.find_element_by_class_name(
            'ng-pristine').click()
        self.driver.find_element_by_class_name(
            'enter-button').click()

    def get_data(self, rg):
        clear_data("input.txt")
        crashes = []
        for i in range(1, rg+1):
            self.driver.get('https://www.wtfskins.com/crash/history/' + str(i))
            content = self.driver.page_source
            soup = BeautifulSoup(content)

            counter = 0
            f = open("input.txt", "a")
            for a in soup.findAll('div', {'class': 'xd-col-1 text-white text-center'}):
                f.write(str(a).split("x")[4].split("<")[0])
            f.close()

