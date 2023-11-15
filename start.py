from postContent import *
from grabContent import *

api_url = 'https://YOUR-WIKIJS-INSTANCE/graphql'
api_token = '<API-TOKEN-HER>'


if __name__ == "__main__":
    print("\n----------\nWikiUpdater\nAuthor: v3lip\n----------\n")
    grabit()
    postit()