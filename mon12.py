import os
from selenium import webdriver
import time
import random
import smtplib

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def load_driver():
    options = webdriver.FirefoxOptions()

    # enable trace level for debugging
    options.log.level = "trace"

    options.add_argument("-remote-debugging-port=9224")
    options.add_argument("-headless")
    options.add_argument("-disable-gpu")
    options.add_argument("-no-sandbox")

    binary = FirefoxBinary(os.environ.get('FIREFOX_BIN'))

    firefox_driver = webdriver.Firefox(
        firefox_binary=binary,
        executable_path=os.environ.get('GECKODRIVER_PATH'),
        options=options)

    return firefox_driver

for h in range(1):
    for x in range(5):

        driver = load_driver()
        list1 = [
            "756944937",
            "762889738",
            "787657284",
            "762889151",
            "100214956"

        ]
        sele = list1[x]
        list2 = [
            "7856",
            "4236",
            "4311",
            "0963",
            "0852"
        ]

        pos = list2[x]

        driver.get("https://mobile.betlion.ke/Login/login")
        time.sleep(5)

        username2 = driver.find_element_by_id("userMobile")
        password2 = driver.find_element_by_id("userPass")
        # 0770244721
        username2.send_keys(sele)
        password2.send_keys(pos)
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/button/span").click()
        time.sleep(10)

        driver.get("https://pick5.betlion.ke/predictions")
        time.sleep(10)
        t = time.localtime()
        z = time.strftime("%M", t)
        if z == "08" or z == "09" or z == "18" or z == "19" or z == "28" or z == "29" or z == "38" or z == "39" or z == "48" or z == "49" or z==z == "58" or z == "59":
            # print("wait")
            time.sleep(140)
            driver.get("https://pick5.betlion.ke/predictions")
            time.sleep(10)

        driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/button").click()
        time.sleep(3)
        # GET POINTS , POSITION REMAINING
        remn = driver.find_element_by_xpath('//*[@id="root"]/div/header/div[1]/div[1]').text

        time.sleep(1)
        poin = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/a/div[1]/span[2]').text

        time.sleep(1)
        post = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/a/div[2]/span[2]').text

        bn1 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[2]/div[2]/button[1]')
        bn2 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[2]/div[4]/button[1]')
        bn3 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[3]/div[2]/button[1]')
        bn4 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[3]/div[4]/button[1]')
        bn5 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[4]/div[2]/button[1]')
        bn6 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[4]/div[4]/button[1]')
        bn7 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[5]/div[2]/button[1]')
        bn8 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[5]/div[4]/button[1]')
        bn9 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[6]/div[2]/button[1]')
        bn10 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[6]/div[4]/button[1]')

        scores = ["10", "20", "21", "00", "11", "01", "02", "12"]

        score1 = random.choice(scores)
        time.sleep(6)

        if score1 == "10":
            bn1.click()
            print(score1)

        if score1 == "20":
            bn1.click()
            bn1.click()
            print(score1)

        if score1 == "21":
            bn1.click()
            bn1.click()
            bn2.click()
            print(score1)

        if score1 == "11":
            bn1.click()
            bn2.click()
            print(score1)

        if score1 == "01":
            bn2.click()
            print(score1)

        if score1 == "02":
            bn2.click()
            bn2.click()
            print(score1)

        if score1 == "12":
            bn1.click()
            bn2.click()
            bn2.click()
            print(score1)

            # SCORES 2
        time.sleep(5)
        score2 = random.choice(scores)

        if score2 == "10":
            bn3.click()
            print(score2)

        if score2 == "20":
            bn3.click()
            bn3.click()
            print(score2)

        if score2 == "21":
            bn3.click()
            bn3.click()
            bn4.click()
            print(score2)

        if score2 == "11":
            bn3.click()
            bn4.click()
            print(score2)

        if score2 == "01":
            bn4.click()
            print(score2)

        if score2 == "02":
            bn4.click()
            bn4.click()
            print(score2)

        if score2 == "12":
            bn3.click()
            bn4.click()
            bn4.click()
            print(score2)

            # SCORES 3
        time.sleep(2)
        score3 = random.choice(scores)

        if score3 == "10":
            bn5.click()
            print(score3)

        if score3 == "20":
            bn5.click()
            bn5.click()
            print(score3)

        if score3 == "21":

            bn5.click()
            bn5.click()
            bn6.click()
            print(score3)

        if score3 == "11":
            bn5.click()
            bn6.click()
            print(score3)

        if score3 == "01":
            bn6.click()
            print(score3)

        if score3 == "02":
            bn6.click()
            bn6.click()
            print(score3)

        if score3 == "12":
            bn5.click()
            bn6.click()
            bn6.click()
            print(score3)

            # SCORES 4
        time.sleep(2)
        score4 = random.choice(scores)

        if score4 == "10":
            bn7.click()
            print(score4)

        if score4 == "20":
            bn7.click()
            bn7.click()
            print(score4)

        if score4 == "21":
            bn7.click()
            bn7.click()
            bn8.click()
            print(score4)

        if score4 == "11":
            bn7.click()
            bn8.click()
            print(score4)

        if score4 == "01":
            bn8.click()
            print(score4)

        if score4 == "02":
            bn8.click()
            bn8.click()
            print(score4)

        if score4 == "12":
            bn7.click()
            bn8.click()
            bn8.click()
            print(score4)

            # SCORES 5
        time.sleep(2)
        score5 = random.choice(scores)

        if score5 == "10":
            bn9.click()
            print(score5)

        if score5 == "20":
            bn9.click()
            bn9.click()
            print(score5)

        if score5 == "21":
            bn9.click()
            bn9.click()
            bn10.click()
            print(score5)

        if score5 == "11":
            bn9.click()
            bn10.click()
            print(score5)

        if score5 == "01":
            bn10.click()
            print(score5)

        if score5 == "02":
            bn10.click()
            bn10.click()
            print(score5)

        if score5 == "12":
            bn9.click()
            bn10.click()
            bn10.click()
            print(score5)

        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[7]/button").click()
        time.sleep(10)
        # rem = driver.find_element_by_xpath('//*[@id="root"]/div/header/div[1]/div[1]')
        # res = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/a/div[1]/span[2]')

        print(x, ".", sele, "-", score1, score2, score3, score4, score5)
        # SEND TO MAIL
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('charlesnganda001@gmail.com', 'emalison8181!')
        senda = "charlesnganda001@gmail.com"

        mtu = "charlesnganda001@gmail.com"
        p = '['
        b = ']'
        x = '-'
        gf = p + post + b + poin + x + remn
        server.sendmail(senda, mtu, gf)
        time.sleep(20)
        driver.close()

