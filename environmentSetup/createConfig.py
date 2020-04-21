# coding:utf-8
from selenium import webdriver
import configparser
import os
curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "config.ini")
print(cfgpath)

conf = configparser.ConfigParser()
conf.add_section("amazon")
conf.set("amazon", "url", "https://www.amazon.com/")
conf.set("amazon", "browser", "chrome")
conf.set("amazon", "time_out", "5")
conf.set("amazon", "browser_path", "chromedriver.exe")
conf.set("amazon", "filename", "productList.txt")

items = conf.items("amazon")
print(items)
conf.write(open(cfgpath, "w"))
