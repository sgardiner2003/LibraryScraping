import requests
from bs4 import BeautifulSoup as BS
import creds
import json
import time

url = 'https://thunder.api.overdrive.com/v2/libraries/noble-stoneham/media'

params = {
    "sortBy": "newlyadded",
    "mediaTypes": "audiobook",
    "format": "audiobook-overdrive,audiobook-overdrive-provisional",
    "perPage": 24,
    "page": 1,
    "truncateDescription": "false",
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
while True:
    params['page'] = page
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    
    items = data.get('items', [])
    if not items:
        break  # No more results
    
    # process items here
    with open('audiobooks.json', 'a')
    
    time.sleep(2)
    page += 1


data = response.json()
# print(json.dumps(data['items'], indent=2)) # makes it look pretty

# Print title and duration

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

"""


login_url = ('https://the-internet.herokuapp.com/authenticate')
secure_url = ('https://the-internet.herokuapp.com/secure')

payload = {
    'username': creds.username,
    'password': creds.password
}

# r = requests.post(login_url, data = payload) # gets us to secure area

with requests.session() as s:
    s.post(login_url, data=payload)
    r = s.get(secure_url).text
    soup = BS(r, 'lxml')
    print(soup.prettify())

### Libby attempt #1

login_url = ('https://sentry.libbyapp.com/auth/link/327')
secure_url = ('https://thunder.api.overdrive.com/v2/libraries/noble-stoneham/media?sortBy=newlyadded&format=ebook-overdrive,ebook-media-do,ebook-overdrive-provisional,audiobook-overdrive,audiobook-overdrive-provisional,magazine-overdrive&perPage=0&includedFacets=availability&includedFacets=mediaTypes&includedFacets=formats&includedFacets=maturityLevels&includedFacets=subjects&includedFacets=languages&includedFacets=boolean&includedFacets=addedDates&includedFacets=audiobookDuration&includedFacets=freshStart&x-client-id=dewey')
secure_url2 = ('https://libbyapp.com/library/noble')

payload = {
    'ils': creds.ils,
    'username': creds.username
}

with requests.session() as s:
    s.post(login_url, data = payload)
    r = s.get(secure_url2).text
    soup = BS(r,'lxml')
    #with open('test3', 'w') as test:
    #    test.write(r)
    print(soup.prettify())

# Turns out that Libby uses javascript, so I have to use the API to get the actual html data
# (which is hidden in a json file?)
# Also, I don't need a library card to access this data somehow.
"""