from selenium import webdriver
import dataset
import random

DB = dataset.connect("sqlite:///./mydb.db")
NAME_TABLE = DB["JAPANESE_NAME"]
NAME_NUM_IN_1PAGE = 100

TARGET_SITE_URL = "http://www.gaoshukai.com/lab/0003/"
CHROME_DRIVER_PATH = "./chromedriver.exe"

def insert_1page(driver):
    for i in range(1, NAME_NUM_IN_1PAGE+1):
        first_name = driver.find_element_by_xpath("//*[@id='main']/ul/li[%d]/ruby[1]/rb" % i).text
        last_name = driver.find_element_by_xpath("//*[@id='main']/ul/li[%d]/ruby[2]/rb" % i).text
        first_name_kana = driver.find_element_by_xpath("//*[@id='main']/ul/li[%d]/ruby[1]/rt" % i).text
        last_name_kana = driver.find_element_by_xpath("//*[@id='main']/ul/li[%d]/ruby[2]/rt" % i).text

        new_data = dict(
            first_name=first_name,
            last_name=last_name,
            first_name_kana=first_name_kana,
            last_name_kana=last_name_kana
        )
        NAME_TABLE.insert(new_data)

    recs = NAME_TABLE.find(order_by="-id", _limit=1)
    for rec in recs:
        print(rec)


def main():
    try:
        driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        for i in range(100):
            driver.get(TARGET_SITE_URL)
            insert_1page(driver)

    finally:
        driver.quit()


if __name__ == '__main__':
    main()
