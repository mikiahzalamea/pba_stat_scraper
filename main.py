from bs4 import BeautifulSoup
import requests
import pandas as pd

#Get the link and response
response = requests.get("https://pba.ph/stats")

#Parse it using bs4
soup = BeautifulSoup(response.text, "html.parser")

#Find where exactly to grab the PBA Stats and the id
table = soup.find("table", id = "record-table")

#Put all the headers (th) into a new variable
headers = table.find_all("th")
statTitles = []

#Append each variable to the list statTitles
for i in headers:
    statTitle = i.text
    statTitles.append(statTitle)

#Put the statTitles into a DataFrame
df = pd.DataFrame(columns = statTitles)

#Put all the data under stats into a variable
rows = table.find_all("tr")

#Append each variable into the list row
for i in rows [1:]:
    data = i.find_all("td")
    row = [tr.text for tr in data]
    #Get the length of the columns then append the data in the row list to the DataFrame
    l = len(df)
    df.loc[l] = row

print(df)

#Turn the DataFrame into CSV using pandas
df.to_csv("PBA_Player_Stats_2023.csv")


