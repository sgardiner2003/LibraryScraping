from bs4 import BeautifulSoup
"""
import os
print(os.listdir())


with open("test.html", 'r', encoding="utf8") as html_file:
    content = html_file.read()
    # print(content) # checking that file was read successfully
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify()) # prettify seems to just indent the code
    sections_html_tags = soup.find_all('h2') # soup.find() just gives first instance and stops
    print(sections_html_tags)

    # everything below here is from the video, doesn't work with my html file
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        print(course.h5) # gives all h5 elements of this html block
        course_name = course.h5.text # gives the course names from these html blocks
        course_price = course.a.text.split()[-1] # gives price for each course
        # ^ 'split' turns string into list where spaces are commas, [-1] chooses the last list element (which is price)
        print(f'{course_name} costs {course_price}') # final output: dynamic string that says course name and price for each course


    for section in sections_html_tags:
        print(section)
"""

import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=Python&txtKeywords=Python%2C&txtLocation=').text # get website html
# print(html_text) # without .text -- successful! (Response [200] means success in web speak)
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx") # start with one job (find) then move to find_all

"""
job = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx") # start with one job (find) then move to find_all
company_name = job.find('h3', class_ = "joblist-comp-name").text.replace(' ','') # gets rid of white space
    skills = job.find('div', class_ = "more-skills-sections").text # replace doesn't do anything here
    published_date = job.find('span', class_ = "sim-posted").text

    print(f'''
    Company Name: {company_name}
    Skills required: {skills}
    ''')
# indented all of this, then put "for job in jobs:" on top, to create the for loop!
"""

for job in jobs:
    published_date = job.find('span', class_ = "sim-posted").text.strip()
    print(published_date)
    if published_date in ('Posted 2 days ago',
                          '1 day ago',
                          'few days ago',
                          '2 days ago',
                          '3 days ago',
                          '4 days ago',
                          '5 days ago',
                          '6 days ago'):
        company_name = job.find('h3', class_ = "joblist-comp-name").text.replace(' ','') # gets rid of white space
        skills = job.find('div', class_ = "more-skills-sections").text # replace doesn't do anything here
        print(f'''
        Company Name: {company_name}
        Skills required: {skills}
        ''')
        print('')