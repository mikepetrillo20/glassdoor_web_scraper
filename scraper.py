from bs4 import BeautifulSoup
import requests
import csv


page = 1
base_url = f'https://www.glassdoor.com/Job/raleigh-software-engineer-jobs-SRCH_IL.0,7_IC1138960_KO8,25_IP{page}.htm?jobType=fulltime&fromAge=30&radius=0&cityId=1138960&sgocId=7'
header = {'user-agent': 'Mozilla/5.0'}

url = requests.get(base_url, headers=header).text
soup = BeautifulSoup(url, 'lxml')


for container in soup.find_all('div', class_='jobContainer'):

    company = container.find('div', class_='jobInfoItem').text
    job_title = container.find_all('a', class_='jobLink jobInfoItem jobTitle')[1].text        
    location = container.find('span', class_='subtle loc').text
    salary = container.find('span', class_='salaryText').text
    posted_days = container.find('span', class_='minor').text

    print(f'Company: {company}')
    print(f'Job Title: {job_title}')
    print(f'Location: {location}')
    print(f'Salary: {salary}')
    print(f'Days Posted: {posted_days}')
    print()

    # TODO: add some try except to catch postings that dont have salary

