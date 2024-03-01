import requests
from bs4 import BeautifulSoup

"""
This script fetches the content of a given URL using the requests library.
It uses BeautifulSoup to parse the HTML content and extracts all paragraphs and headings, which it then prints out.
The script prompts the user for a URL to fetch its content.
"""

def fetch_url_content(url):                                                                                     
    response = requests.get(url)                                                                                  
    soup = BeautifulSoup(response.content, 'html.parser')                                                         
                                                                                                                
    return "\n\n".join([f"{element.name.upper()}: {element.text.strip()}" for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])])
                                                                                                                
def main():
    url = input("Please enter a URL to fetch its content: ")
    content = fetch_url_content(url)
    print(content)

if __name__ == "__main__":
    main()