import requests
from bs4 import BeautifulSoup as BS
import json
import time

url = 'https://thunder.api.overdrive.com/v2/libraries/noble-stoneham/media'
subject = 'fiction'

params = {
    "sortBy": "newlyadded",
    "mediaTypes": "audiobook",
    "format": "audiobook-overdrive,audiobook-overdrive-provisional",
    "perPage": 24,
    "page": 1,
    "truncateDescription": "false",
    # "availability": "available", # only the available audiobooks; can delete to get all
    "subjects": subject,
    "includedFacets": [
        "availability",
        "mediaTypes",
        "formats",
        "maturityLevels",
        "subjects",
        "languages",
        "boolean",
        "addedDates",
        "audiobookDuration",
        "freshStart"
    ]
}

headers = {
    "x-client-id": "dewey",
    "accept": "application/json"
}

page = 1
while page < 101:
    params['page'] = page
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    
    items = data.get('items', [])
    if not items:
        print("No books.")
        break # if no more results
    
    # save progress
    with open(f'{subject} audiobooks.json', 'a') as f:
        json.dump(items, f)

    # stop if website blocks us
    if response.status_code != 200:
        print(f'Error: {response.status_code}')
        break
    
    print(f'Page {page} complete.') # to track progress

    # to prevent overwhelming website
    time.sleep(2)
    page += 1


data = response.json()
# print(json.dumps(data['items'], indent=2)) # makes it look pretty

# metadata() is for title, author, readers, and duration of each item in items

def metadata():
    titles = []
    authors = []
    readers = []
    durations = []
    for (i,item) in enumerate(data.get("items", [])):
        # Add title
        title = item.get("title", "Unknown Title")
        titles.append(title)

        # Add author
        author = item.get('author', 'Unknown Author')
        authors.append(author)

        # Add reader; 'Multiple narrators' if more than one
        narrators = [c['name'] for c in item.get('creators', []) if c['role'] == 'Narrator']
        if len(narrators) == 1:
            readers.append(narrators[0])
        elif len(narrators) > 1:
            readers.append('Multiple narrators')
        else:
            readers.append('')

        # Add duration
        for fmt in item.get("formats", []):
            duration = fmt.get("duration")
            if duration:
                #hours = duration // 3600
                #minutes = (duration % 3600) // 60
                #print(f"{title} - {hours} hr {minutes} min")
                hours = round(int(duration[0:2]) + int(duration[3:5])/60 + int(duration[6:8])/360,2)
                durations.append(hours)
    print(titles)
    print(authors)    
    print(readers)
    print(durations)


# Potential problems:
# - some narrators are "full cast"
# - want to exclude books where there is more than one narrator
# - iterate over 'creators' section in each item, keep counter for how many narrators, while narrators = 1, index <= n, continue
# - if we find another narrator then stops loop