# coding=gbk
import pickle
import requests
import time
import pandas as pd
import random
from lxml import etree
from io import BytesIO
import jieba
import numpy as np
from PIL import Image

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")

options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
# options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
driver = webdriver.Chrome(executable_path='D:\\how to\\Python3\\chromedriver.exe')
# driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()

driver.get('https://gccaa.us.oracle.com/')
# driver.get('https://login.oracle.com/mysso/signon.jsp')
time.sleep(5)
'''driver.add_cookie({'_gcl_au':'1.1.1339188789.1568104678',
'ELOQUA':'GUID=95F2BE52D8844C3CBF532A35E4E23E8D',
'lastBreakOn':'false',
'lastLoginType':'Until',
'lastLoginUntil':'16:30',
'OHS-gccaa.us.oracle.com-80':	'76C8198E277B5831B23B99ADEB4BD933FDE4E340C06EA7C83F490A300037826B38F0FFF1F562480CC45597C9ADEC0D8A98D28F22DAC63038534904638748E3298954DDB82E1D84A2D680DF4A39FE75E36DAA5A03D2BE16B2CA75FFE84F0176051B9056BC36DE4254BAC332C5D4059D06EAA306FC9410AFE30EF19AE8D2289E7CB18833B1399DF234CD903F6ACB638A11D13ACAF25E60FFBD5E6C1568D3BAD7B450E2C76196E70D0744E722261A07501820FAD64C7C45927CB98A81963CD9BF6E169D4437491D95A37FAFFB7196471B75602501478F8CE1F2F7A16361FC8F82A29A0151DE142D4BA31DE58640A50F2896~',
'ORA_ML3_SITE'	:'Internal',
'ORA_UCM_INFO':	'3~B0F9E9061966440BE040548C2C7051D8~Rock~Dong~rock.dong@oracle.com',
'ORASSO_AUTH_HINT':	'v1.0~20191127093140',
'PSCUser':	'rock.dong@oracle.com',
'releaseSeen':	'6'})'''

driver.add_cookie({'name': 'PSCUser',
                   'value': 'rock.dong@oracle.com',
                   'path': '/'})
USER_NAME='xxx'
PASSWORD='xxx'

driver.find_element_by_id('sso_username').send_keys('USER_NAME')
driver.find_element_by_id("ssopassword").send_keys('PASSWORD')
#driver.implicitly_wait(20)

#python_button = driver.find_element_by_xpath("//input[@value='登录']")
python_button = driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/form/div[2]/span/input")
python_button.click()
time.sleep(10)
# click radio button
# python_button = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
# python_button.click()

# type text
# text_area = driver.find_element_by_id('textarea')
# text_area.send_keys("print('Hello World')")

# click submit button
# submit_button = driver.find_elements_by_xpath('//*[@id="editor"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td[3]/input')[0]
# submit_button.click()

python_button = driver.find_element_by_id('logMeInBut')
python_button.click()
