import requests

def fetch_url_content(url):
    try:
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            return response.text  # Returns the content of the URL as a string
        else:
            return f"Failed to fetch the URL content. Status code: {response.status_code}"
    except requests.RequestException as e:
        return f"An error occurred: {e}"
    
def main():
    # Prompt the user for a URL
    url = input("Please enter a URL to fetch its content: ")
    content = fetch_url_content(url)
    print(content)

if __name__ == "__main__":
    main()