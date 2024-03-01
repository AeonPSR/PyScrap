from bs4 import BeautifulSoup
import requests
import re

# Define headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

# Make a request to the website with headers
# url = 'https://www.espn.co.uk/football/scoreboard'
url = 'https://www.espn.co.uk/football/scoreboard/_/date/20240229'
response = requests.get(url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')
# Find all <ul> elements with class "ScoreboardScoreCell__Competitors"
scoreboard_elements = soup.find_all('ul', class_='ScoreboardScoreCell__Competitors')

# Iterate through each scoreboard element
for scoreboard in scoreboard_elements:
	soupUl = BeautifulSoup(scoreboard.text, 'html.parser')
	print("----------------------------------------")
	pretty = soupUl.prettify()
	pretty = re.sub(r'\([^)]*\)', '', pretty) # Remove parenthesis
	name1 = re.match(r'[^0-9\W_]+(?:[- ][^0-9\W_]+)*', pretty).group()
	pretty = pretty.replace(name1, "")
	score1 = re.match(r'\d+', pretty)
	if score1 is not None:
		score1 = score1.group()
		pretty = pretty[len(score1):]
	name2 = re.match(r'[^0-9\W_]+(?:[- ][^0-9\W_]+)*', pretty).group()
	pretty = pretty.replace(name2, "")
	score2 = re.match(r'\d+', pretty)
	if score1 and score2 is not None:
		score2 = score2.group()
		print(f"{name1} // {name2} - Score {score1} // {score2}")
	else:
		print(f"{name1} // {name2} - Yet to come.")
print("----------------------------------------")
