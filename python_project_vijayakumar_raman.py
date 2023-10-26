from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import urllib.parse
import random
from selenium.common.exceptions import NoSuchElementException, WebDriverException

driver = None
def install():
    global driver
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    except:
        install()
install()

genres_links = []
genres_title = []
def get_genre():
    try:
        driver.get('https://tubitv.com/home')
        wait = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="XVtXO qmpj2"]')))
        driver.find_element(By.XPATH, '//button[@class="XVtXO qmpj2"]').click()
        wait = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="Button__content"]')))
        genres_xpath = driver.find_elements(By.XPATH, '//*[@id="app"]/div[3]/div/div[1]/div/div[2]/div[1]/a')
        for genre in genres_xpath:
            genres_links.append(genre.get_attribute('href'))

        for genre in genres_links:
            genres_title.append(genre[28:])

        df = pd.DataFrame({'Genres': genres_title, 'Links': genres_links})
        print('Please find the list of Genres available on the Tubi TV!')
        print(df['Genres'].to_string(index=False))
    
    except:
        get_genre()

get_genre()

movies = []
def find():
    user_choice = input("Please enter your choice of Genre: ").lower()
    try:
        if user_choice in genres_title:
            driver.get(f'https://tubitv.com/category/{user_choice}')
            wait = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div/a[@class="web-content-tile__title"]')))
            movies_xpath = driver.find_elements(By.XPATH, '//div/a[@class="web-content-tile__title"]')
            for movie in movies_xpath:
                movies.append(movie.text)
            print(f'we found {len(movies)} movies from', user_choice)
            print(f'Please find a random movie from {user_choice}:', random.choice(movies))
            print('\nHope you will enjoy the movie!')
        else:
            print('\n The given choice of genre is not listed on the above so, using search key with your choice to assist you better')
            user = urllib.parse.quote(user_choice)
            driver.get(f'https://tubitv.com/search/{user}')
            wait = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div/a[@class="web-content-tile__title"]')))
            movies_xpath = driver.find_elements(By.XPATH, '//div/a[@class="web-content-tile__title"]')
            for movie in movies_xpath:
                movies.append(movie.text)
            print(f'we found {len(movies)} movies from', user_choice)
            print(f'Please find a random movie from {user_choice}:', random.choice(movies))
            print('\nHope you will enjoy the movie!')
    except NoSuchElementException:
        print("Element not found or No movies found, please try with diffrent choice")
        find()

    except WebDriverException:
        print("An error occurred:", 'TimeoutException, could not find any result, please try with different choice')
        find()

find()
driver.quit()