from selenium import webdriver
from bs4 import BeautifulSoup

def dummy_input():
    return 'Software Engineer', 'Denver CO', 1

def get_input():
    print('Enter Desired Job')
    desired_job = input()

    print('Enter Location')
    location = input()

    print('How many pages to search')
    pages = int(input())

    if pages > 10:
        pages = 10

    return desired_job, location, pages

def main():
    # Initialize Selenium options
    options = webdriver.FirefoxOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')

    # Get input from user
    desired_job, location, num_pages = dummy_input()

    # Start selenium browser
    driver = webdriver.Firefox(options)

    page_sources = []
    page_index = 0
    for i in range(num_pages):
        # If on second page or further
        if i > 0:
            # Add pagination query string
            page_index = i * 10
            driver.get('https://www.indeed.com/jobs?q=' + desired_job + '&l=' + location + '&start=' + str(page_index));
        # If on the first page
        else:
            # Just get the first page of data
            driver.get('https://www.indeed.com/jobs?q=' + desired_job + '&l=' + location);
        # Add page source to list
        page_sources.append(driver.page_source)

    return page_sources

pages = main()
