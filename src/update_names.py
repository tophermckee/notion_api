import sys
sys.path.append("..")
from src.util import *

with open("../creds.json") as file:
    credentials = json.load(file)

def main():
    headers = {
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Authorization": f"Bearer {credentials['internal_integration_token']}"
    }

    wishlist_items = requests.post(
        url="https://api.notion.com/v1/databases/6449b9f514ae4ba9a0656f47d82fc28b/query",
        json = {
            "filter" : {
                "and": [
                    {
                        "property": "Christmas?",
                        "checkbox": {
                            "equals": True
                        }
                    },
                    {
                        "property": "Purchased",
                        "checkbox": {
                            "equals": False
                        }
                    },
                ]
            }
        },
        headers=headers
    ).json()

    with open('../logs/example.json', 'w') as file:
        json.dump(wishlist_items, file, indent=4)

    for item in wishlist_items['results']:
        
        title = item['properties']['Title']['rich_text'][0]['text']['content']
        author = item['properties']['Author / Publisher / Brand']['rich_text'][0]['text']['content']
        
        if title == title.upper() :
            title = title.title()
        if author == author.upper():
            author = author.title()

        new_title = f"{title} by {author}"
        
        payload = {
            "properties": 
                {
                    "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": new_title,
                                "link": None
                            },
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default"
                            },
                            "plain_text": new_title,
                            "href": None
                        }
                    ]
                },
            }
        }
        update_attempt = requests.patch(url=f"https://api.notion.com/v1/pages/{item['id']}", json=payload, headers=headers).json()
        logging.info(update_attempt)
        print(f"✅ Updated: {new_title}")

if __name__ == '__main__':
    main()