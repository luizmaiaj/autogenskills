from langchain_community.tools import DuckDuckGoSearchResults
import re                                                                          

"""
This Python script uses the DuckDuckGo Search tool from the langchain_community.tools package to perform an internet search.
The search results are parsed using a regular expression and displayed in a structured format.
"""

def internet_search(query):
    search_tool = DuckDuckGoSearchResults()
    results = search_tool.run(tool_input={'query': query})

    # Regular expression pattern to extract snippet, title, and link
    pattern = r"\[snippet: (.*?), title: (.*?), link: (.*?)\]"

    # Use re.findall to find all matches according to the pattern
    groups = re.findall(pattern, results, re.DOTALL)

    # Convert the matches into a structured format
    return [
        {"snippet": snippet.strip(), "title": title.strip(), "link": link.strip()}
        for snippet, title, link in groups
    ]


def main():
    query = "best openai api compatible models"
                                                                              
    results = ddg_search(query)

    # Display the parsed groups
    for i, group in enumerate(results, 1):
        print(f"Result {i}:")
        print(f"Summary: {group['snippet']}")
        print(f"Title: {group['title']}")
        print(f"Link: {group['link']}\n")

if __name__ == "__main__":
    main()