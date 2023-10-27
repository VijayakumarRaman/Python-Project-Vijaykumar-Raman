# Movie picker project made by Vijayakumar Raman
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import random
from selenium.common.exceptions import WebDriverException
from time import sleep

driver = None
user_choice = ''
choice = ''
movies = []
home = '//div[3]/a[@target="_self"]'
movie_xpath = '//article/div/a[@target="_self"]'
search = '//input[@id="searchBar"]'
error = 0

def install():
    global driver
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service, options=chrome_options)
        driver.maximize_window()
    except:
        install()

def user():
    global choice, user_choice
    while not user_choice:
        user_choice = input("Please enter your choice of Genre: ").lower()
    choice = user_choice +' movies'

def get_movie():
    global movies, user_choice, error

    try:
        driver.get('https://www.hotstar.com/in/explore')
        wait = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, home)))

        driver.find_element(By.XPATH, search).send_keys(choice)
        sleep(3)
        titles = driver.find_elements(By.XPATH, movie_xpath)
        movies_link = []

        for title in titles:
            movies_link.append(title.get_attribute('href'))

        for movie in movies_link:
            if 'https://www.hotstar.com/in/movies/' in movie:
                movies.append(movie[34:-11])

        df = pd.DataFrame({'Movies': movies})
        df['Movies'] = df['Movies'].str.replace('-', ' ')
        count = len(movies)
        print(f'\nWe found {count} movies for', user_choice)
        print('Please find the movie list below')
        print(df['Movies'].to_string(index=False))

        movies = df['Movies'].to_list()

        print('\nI would recommend you to watch:', random.choice(movies))
        print('\nHope you will enjoy the movie!')
    
    except WebDriverException:
        error = error+1
        print('\nAn error occurd on the website, please wait we will reload the page')
        if error<4:
            get_movie()
        else:
            print('\nmaximum of 3 attempts were failed, please restart the program')
            sleep(5)
    except:
        print('\nNo results found, please try again with different choice of genre')
        user_choice = ''
        user()
        get_movie()


install()
user()
get_movie()
driver.quit()