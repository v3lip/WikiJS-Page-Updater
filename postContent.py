import start
import requests
import json

def create_table_from_file():
    # Leser .txt-fil med leverandører
    print("[*] Leser 'io.txt..'")
    with open('core/io.txt', 'r', encoding='utf-8') as file:
        rows = [line.strip().split(',') for line in file]

    # Sorterer alt alfabetisk
    sorted_rows = sorted(rows, key=lambda x: x[0].lower())

    print("[*] Genererer payload..")
    # Lager headeren
    header = ["Firma", "Produkt", "Navn", "Telefon", "Epost"]
    column_widths = [max(len(row[i]) for row in sorted_rows + [header]) for i in range(len(header))]

    # Formaterer alle rader slik at det blir riktig spacing
    def format_row(row):
        return "|" + "|".join(f"{cell:{column_widths[i]}}" for i, cell in enumerate(row)) + "|"

    # Lager table
    table = format_row(header)
    table += "\n" + format_row(["-" * width for width in column_widths])

    for row in sorted_rows:
        table += "\n" + format_row(row)

    return "Legg til nye leverandører [her](/leverandorer/juks)\n\n---\n" + table



def postit():
    mutation = """
        mutation ($id: Int!, $content: String, $description: String, $editor: String, $isPrivate: Boolean, $isPublished: Boolean, $locale: String, $path: String, $publishEndDate: Date, $publishStartDate: Date, $scriptCss: String, $scriptJs: String, $tags: [String], $title: String) {
            pages {
                update(id: $id, content: $content, description: $description, editor: $editor, isPrivate: $isPrivate, isPublished: $isPublished, locale: $locale, path: $path, publishEndDate: $publishEndDate, publishStartDate: $publishStartDate, scriptCss: $scriptCss, scriptJs: $scriptJs, tags: $tags, title: $title) {
                    responseResult {
                        succeeded
                        errorCode
                        slug
                        message
                        __typename
                    }
                    page {
                        updatedAt
                        __typename
                    }
                __typename
                }
            __typename
            }
        }
    """

    table_content = create_table_from_file()

    # API
    api_url = start.api_url
    api_token = start.api_token

    # Headers
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }

    # Payload Variabler
    variables = {
        "content": f"{table_content}",
        "description": "",
        "editor": "markdown",
        "id": 157,
        "isPrivate": False,
        "isPublished": True,
        "locale": "en",
        "path": "leverandorer",
        "publishEndDate": "",
        "publishStartDate": "",
        "scriptCss": "",
        "scriptJs": "",
        "tags": [],
        "title": "Leverandører",
    }

    # Formater Payload
    payload = json.dumps({
        "query": mutation,
        "variables": variables
    })

    
    # Send payload/variabler
    print("[*] Sender payload til Wiki.js..")
    response = requests.post(api_url, headers=headers, data=payload)

    # Respons
    if response.status_code == 200:
        print(f"[*] Wiki.js er nå oppdatert med siste leverandørinfo!")
    else:
        print(f"[!] Feilet. Feilmelding: {response.status_code}\n-----\n{response.text}")