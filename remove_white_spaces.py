"""
To remove white spaces we use replace method .replace(" ", "")
"""

#Import the  library 7
from bs4 import BeautifulSoup 

with open("index.html", "r") as html_file:
	content = html_file.read()
	"""If you want to print content run: print(content)"""

	soup = BeautifulSoup(content, "lxml")
	"""The above code makes the element to appear as it is in the website"""
	tag = soup.find("h1")
	tags  = soup.find("h1").text.replace(" ","")
	print(tags)

	







