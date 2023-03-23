import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
site_url = 'https://piter-online.net/'
driver = webdriver.Chrome()
driver.set_window_size(1200, 900)
try:
    driver.get(site_url)
    main_frame = driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div[3]/div[1]/div")
    search_fild = driver.find_element(By.XPATH,
                                      "//*[@id='root']/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div/div[1]/input")
    search_fild.send_keys('Тестовая линия')
    time.sleep(5)
    main_frame.click()
    search_fild.click()
    search_fild.send_keys(Keys.ENTER)
    house_field = driver.find_element(By.XPATH,
                                      "//*[@id='root']/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div/div[1]/input")
    time.sleep(2)
    house_field.send_keys("1")
    time.sleep(3)
    main_frame.click()
    house_field.send_keys(Keys.ENTER)
    select_field = driver.find_element(By.XPATH, "//*[@id='forSelectField']/div[1]/div/div/div/ul/li[1]").click()
    time.sleep(3)
    show_rates_button = driver.find_element(By.XPATH,
                                            "//*[@id='root']/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div")
    show_rates_button.click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[4]/div/div/div/div/div"))).click()

    time.sleep(3)

    connect_button = driver.find_element(By.XPATH,
                                         "//*[@id='root']/div/div[1]/div[4]/div[4]/div[1]/div/div/div[2]/div[1]/div[7]/div/div/div[2]/div[2]/a").click()

    time.sleep(3)

    user_name = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='root']/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[2]/div/div[2]/input")))
    user_name.send_keys('Автотест')

    time.sleep(3)

    user_number = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='root']/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[3]/div/div[2]/input")))
    user_number.send_keys('1111111111')
    time.sleep(5)

    submit_button = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[6]/div"))).click()
    time.sleep(5)

    for i in range(6):
            try:
                if driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div[4]/div/div[2]/div[1]/form"):
                    time.sleep(3)
                    driver.refresh()
                    time.sleep(5)
                    submit_button = driver.find_element(By.XPATH,
                                                        "//*[@id='root']/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[6]/div")

                    user_name = driver.find_element(By.XPATH,
                                                    "//*[@id='root']/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[2]/div/div[2]/input")

                    user_number = driver.find_element(By.XPATH,
                                                      "//*[@id='root']/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[3]/div/div[2]/input")
                    user_name.send_keys("Автотест")
                    user_number.send_keys('1111111111')
                    submit_button.click()
                    time.sleep(5)
            except Exception as E:
                print(E)
except Exception as e:
    print(e)

driver.quit()