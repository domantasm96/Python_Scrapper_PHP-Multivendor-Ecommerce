#!/usr/bin/python3
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import csv
import re
import MySQLdb
import os

DB_NAME = 'Sqli_coursework'
DB_USER = 'root'
DB_PSW = 'test'
HOST = 'test'

LOGIN_URL = 'http://www.fxwebsolution.com//demo/arthi/multivendor/sign-in.php'
SELENIUM_PATH = '/home/domantas/Documents/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'
driver = webdriver.PhantomJS(executable_path=SELENIUM_PATH)

ITERATION_NUM = 70

auth_username = 'tesotest22@gmail.com'
auth_password = 'super1234'

os.system("""mysql -uroot -p'nesakysiu' < database_creation""")
db = MySQLdb.connect(host=HOST, user=DB_USER, passwd=DB_PSW, db=DB_NAME)
cursor = db.cursor()

def login_session():
    driver.get(LOGIN_URL)
    username = driver.find_element_by_id('exampleInputEmail1')
    password = driver.find_element_by_id('exampleInputPassword1')
    username.send_keys(auth_username)
    password.send_keys(auth_password)
    driver.find_element_by_name('loginuser').click()

def remove_spaces(string):
    return re.sub(' {2,}', '_', string)

def seller_view():
    print('SELLER VIEW SCRIPT IS EXECUTED')
    print('TARGET: http://www.fxwebsolution.com//demo/arthi/multivendor/seller-view.php?usid=')
    data_list = []
    user_list = []
    for uid in range(ITERATION_NUM):
        print('Scraping data from {} user'.format(uid))
        is_empty = True
        driver.get('http://www.fxwebsolution.com//demo/arthi/multivendor/seller-view.php?usid='+str(uid))
        soup = BeautifulSoup(driver.page_source, "lxml")
        info = soup.find_all('div', class_='form-group')
        user_list.append(uid)
        for i in info:
            user_info = i.get_text().strip().replace('\n', ':').split(':')
            if len(user_info) > 1:
                user_list.append(user_info[1])
                is_empty = False
            else:
                user_list.append('')

        data_list.append(user_list)
        user_list = []

    return data_list

def shopping_cart():
    print('SHOPPING CART SCRIPT IS EXECUTED')
    print('TARGET: http://www.fxwebsolution.com/demo/arthi/multivendor/shopping-cart.php?cusid=')
    data_list = []
    temp_list = []
    user_data = []
    cuid_list = []
    for cuid in range(ITERATION_NUM):
        print('Scraping data from {} user'.format(cuid))
        driver.get('http://www.fxwebsolution.com/demo/arthi/multivendor/shopping-cart.php?cusid='+str(cuid))
        soup = BeautifulSoup(driver.page_source, "lxml")
        pattern = soup.find('tbody').find_all('tr')
        if len(pattern) < 1:
            continue
        for product in pattern:
            temp_list.append(cuid)
            for i, elements in enumerate(product.find_all('td')):
                if i == 1:
                    continue
                text = remove_spaces(elements.get_text().replace('\n', ' ').replace('\t', '').replace('\xa0','').strip())
                temp_list.append(text)
            
            data_list.append(temp_list)
            temp_list = []
        cuid_list.append(cuid)
    print('SHOPPING CART SCRIPT IS FINISHED')
    return data_list

def my_whishlist():
    print('MY WISHLIST SCRIPT IS EXECUTED')
    print('TARGET: http://www.fxwebsolution.com/demo/arthi/multivendor/my_wishlist.php?fid=')
    user_data = []
    for fid in range(ITERATION_NUM):
        print('Scraping data from {} user'.format(fid))
        driver.get('http://www.fxwebsolution.com/demo/arthi/multivendor/my_wishlist.php?fid='+str(fid))
        soup = BeautifulSoup(driver.page_source, "lxml")
        pattern = soup.find_all('tbody')
        if len(pattern[0]) <  1:
            continue
        for product in pattern:
            temp_list = []
            text = remove_spaces(product.get_text().replace('\n', ' ').replace('\t', '').replace('\xa0','').strip())
            if text == '':
                continue
            text = re.sub('(INR[0-9]+){2}',re.search('INR[0-9]+', text)[0], text)
            temp_list.append(fid)
            for i in text.split('_')[:-1]:
                temp_list.append(i)
            user_data.append(temp_list)
    return user_data

def db_seller_insert():
    column_names = '(user_id,name, email,mobile,company,about_company,ph_no,store_name,cancellation_policy,compnay_url,company_address1,company_address2)'
    format_param = ('%s,' * len(seller_data[0:12]))[:-1]
    for i in range(len(seller_data)):
        seller_list = []
        for data in seller_data[i]:
            seller_list.append(data)
        try:
            cursor.execute("INSERT INTO Seller "+ column_names +" VALUES ("+format_param+")""",seller_list[0:12])
            db.commit()
        except:
            db.rollback()


def db_cart_insert():
    column_names = '(user_id,s_no, product_name,product_rank,product_color,quantity,subtotal,grandtotal)'
    for i in range(len(cart_data)):
        temp = []
        for j in range(len(cart_data[i])-1):
            if(j == 2):
                for values in cart_data[i][j].split('_'):
                    temp.append(values)
            else:
                temp.append(cart_data[i][j])
        format_param = ('%s,' * len(temp))[:-1]
        try:
            cursor.execute("INSERT INTO Cart "+ column_names +" VALUES ("+format_param+")""",temp)
            db.commit()
        except:
            db.rollback()

def db_wishlist_insert():
    column_names = '(user_id, product_name,product_rank,product_price)'
    for i in range(len(wishlist_data)):
        temp = []
        for j in wishlist_data[i]:
            temp.append(j)
        format_param = ('%s,' * len(temp))[:-1]
        try:
            cursor.execute("INSERT INTO Wishlist "+ column_names +" VALUES ("+format_param+")""",temp)
            db.commit()
        except:
            print('ERROR')
            db.rollback()

login_session()
seller_data = seller_view()
cart_data = shopping_cart()
wishlist_data = my_whishlist()
db_seller_insert()
db_cart_insert();
db_wishlist_insert();