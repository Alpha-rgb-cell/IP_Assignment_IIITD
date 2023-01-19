import re

# Open the input file and read the data into a list
with open("pages.txt", "r") as f:
    data = [line.strip() for line in f]

# Create a dictionary to store the page data
pages = {}
for line in data:
    # check if the line contains a comma
    if "," not in line:
        continue
    # Extract the URL, init_importance, and text from each line
    url, rest = line.split(",", 1)
    init_importance, text = rest.split(":", 1)
    init_importance = float(init_importance)
    # Extract the URLs referenced in the text
    links = set(re.findall(r"URL\d+", text))
    # Add the page data to the dictionary
    pages[url] = {"init_importance": init_importance, "links": links}

# Compute the overall importance of each page
for url, page in pages.items():
    overall_importance = 0
    for link in page["links"]:
        if link in pages:
            overall_importance += pages[link]["init_importance"] / len(pages[link]["links"])
    page["overall_importance"] = overall_importance

# Find the highest ranking N pages
N = 10
highest_ranking_pages = sorted(pages.items(), key=lambda x: x[1]["overall_importance"], reverse=True)[:N]

# Print the highest ranking N pages
for i, (url, page) in enumerate(highest_ranking_pages):
    print(f"{i+1}. {url}: {page['overall_importance']}")

