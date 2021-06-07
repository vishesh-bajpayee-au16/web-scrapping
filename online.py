import time
from bs4 import BeautifulSoup
import requests

print("Enter unfamilier skills")
unfamilier_skill = input(">")
print(f"Filtering jobs without {unfamilier_skill}")

def findJobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=web+developer&txtLocation=Indore').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all("li",class_="clearfix job-bx wht-shd-bx")

    for job in jobs:
        published_date = job.find("span",class_ ="sim-posted").span.text
        if "few" in published_date:
            
            skills_rquired = job.find("span",class_="srp-skills").text.replace(" ","")
            if unfamilier_skill not in skills_rquired:
                company_name = job.find("h3",class_="joblist-comp-name").text.replace(" ","")
                more_info = job.header.h2.a['href']
                print(f"\ncompany name: {company_name.strip()}\nskills required: {skills_rquired.strip()}\npublished date: {published_date} ")
                print(more_info)
                
                    
if __name__ == "__main__":
    while True:
        findJobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)