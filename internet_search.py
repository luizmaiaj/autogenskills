from bs4 import BeautifulSoup
import requests

# from langchain_community.tools import DuckDuckGoSearchRun
# search_tool = DuckDuckGoSearchRun()

def ddg_search(query):
    url = f'https://duckduckgo.com/html/?q={query}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    for result in soup.find_all('a', class_='result__a'):
        
        title = result.get_text()
        link = result['href']
        
        results.append({
                'title': title,
                'url': link
            })
        
    return results

def main():
    query = "best openai api compatible models"

    print(ddg_search(query))

if __name__ == "__main__":
    main()
