# Python-Project-Vijaykumar-Raman
Libraries used: selenium, webdriver_manager, pandas, random and time
Code Explanation:
1. Created a recursive function to install Chrome browser without any error blocker.
2. Made the webdriver invisible to make the user interact only with interpreter.
3. Created a function to get the genre from user wihtout any NULL value.
4. Created a recursive function to get the movies list using the user input.
5. The webdriver will go to https://www.hotstar.com/in/explore and search the user input keyword to fetch movies.
6. Once the movies fetched it will print all the movies line by line (used pandas to print the movies as a column with string values)
7. Used random to get a random choice from the fetched list and printed as a suggested movie.
8. If there are no result on the search, used recursive on the execption to get different keyword from user and search again.
9. Like wise if there are any issues in loading the website I have used recursive in WebDriverException to attempt the website loading with max limit of 3.
10. Once the suggestion completed, the program will end.
