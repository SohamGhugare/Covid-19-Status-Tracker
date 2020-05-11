import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('https://news.google.com/covid19/map?hl=en-IN&gl=IN&ceid=IN:en')
soup = BeautifulSoup(page.content, 'html5lib')


# Headings
head = soup.find_all(class_='TSGsib')

# Values 
val = soup.find_all(class_='l3HOY')

# Getting stuff as text (without tags)

headings = [
     head[1].get_text(),
     head[3].get_text(),
     head[4].get_text(),
 ]

values = [
     val[1].get_text(),
     val[3].get_text(),
     val[4].get_text(),
 ]

# Converting into columns using Pandas
covidStat = pd.DataFrame({
    'Worldwide' : headings,
    'Cases' : values,
})
        
print(covidStat)

#covidStat.to_csv('Covid-19 Status')                        ## Remove the comment of this syntax to store this data in a csv file