from bs4 import BeautifulSoup

with open("index.html","r") as html_file:
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content,'lxml')
    course_cards = soup.find_all("div",class_="card")
    course_obj = {}
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        course_obj[course_name] = course_price
        
        print(f"{course_name} costs {course_price}")

    
    # print(course_obj)
    
  