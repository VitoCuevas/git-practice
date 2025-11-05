# LinkedIn Learning Python Course by Joe Marini
# Retrieving Internet Data  


import urllib.request       #import urllib.parse
from bs4 import BeautifulSoup #import BeautifulSoup

web_url = urllib.request.urlopen("http://www.example.com")  # Open a web URL
print("Result Code:", web_url.getcode())    # Print the result code
data = web_url.read()                     # Read the data from the URL
#print(data)                    # Print the data retrieved (HTML content)
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(data, 'html.parser') # Create a BeautifulSoup object to parse the HTML
all_text = soup.get_text()  # Extract all text from the HTML content 
print(all_text)            # Print the extracted text
