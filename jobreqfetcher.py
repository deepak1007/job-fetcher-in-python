import requests
from bs4 import BeautifulSoup

html = requests.get('https://internshala.com/internships/web%20development-internship-in-delhi')
if(html.status_code == 200):
  soup = BeautifulSoup(html.content, "html.parser")
  list_of_link_containers = soup.find_all(class_='company')
  fs = open("links/internshala_links_to_description.txt", 'w')
  for individual_link_container in list_of_link_containers:
      fs.writelines(individual_link_container.h4.a.get('href'))

  fs.close()    