import requests
from bs4 import BeautifulSoup
import time
import urllib

main_URL = 'https://internshala.com/internships/web%20development-internship-in-delhi'
html = requests.get(main_URL)
if(html.status_code == 200):
  soup = BeautifulSoup(html.content, "html.parser")
  list_of_link_containers = soup.find_all(class_='company')
  fs = open("links/internshala_links_to_description.txt", 'w')

  #read all the links from the tags with class company and save them into the file.
  for individual_link_container in list_of_link_containers: 
      fs.write(individual_link_container.h4.a.get('href') + " \n")
  fs.close()
  
  #read every link from the links file and request that page parse it then find the requirements
  fs = open("links/internshala_links_to_description.txt", 'r')
  file_content = fs.readlines()
  
  for line in file_content:
      url = "https://internshala.com" + line
      url = url.strip(' \n') #removing linefeed from the line as it is creating malfunctioning url
      #print(repr(url))
      description_page_html = requests.get(url)
      if(description_page_html.status_code == 200):
          soup = BeautifulSoup(description_page_html.content, "html.parser")
          #gs = open("html.txt", 'w')
          #gs.write(soup.prettify())
          try:
             requirement_string_container = soup.find(id="skillNames")
             requirement_string = ' '.join(requirement_string_container.find_all(text=True, recursive=False))
             print(requirement_string)
             
          except:
              print("no requirements")
              
          time.sleep(2)



