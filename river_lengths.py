# filename: river_lengths.py
import skills
# Search the web for top 5 longest rivers in africa and their lengths
search_query = "top 5 longest rivers in africa"
results = skills.search_startpage(search_query)
# Parse the search results to extract the required information
table_data = []
for result in results:
    if "length:" in result:
        river, length = result.split(":")[0].strip(), int(result.split(":")[1].strip().replace(",", ""))
        table_data.append([river, length])
# Print the markdown table
print("# Top 5 Longest Rivers in Africa")
print("| River        | Length (km) |")
print("|--------------|-------------|")
for data in table_data:
    print(f"| {data[0]}      | {data[1]}       |")