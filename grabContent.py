import start
import requests
import json

def grabit():
    query = """
        {
            pages{
                single (id: 158) {
                    content
                }
            }
        }
    """

    # API
    api_url = start.api_url
    api_token = start.api_token

    # Headers
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }

    # Formater Payload
    payload = json.dumps({
        "query": query,
    })
    
    print(f"[*] Laster ned fra Wiki.js..")
    response = requests.post(api_url, headers=headers, data=payload)
    data = json.loads(response.text)
    content = data["data"]["pages"]["single"]["content"]

    # Start og stopp ved ``` i informasjonen fra content
    start_index = content.find("```") + 3
    end_index = content.find("```", start_index)
    content = content[start_index:end_index].strip()

    # Skriver til io.txt
    file_path = 'core/io.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    # Respons
    if response.status_code == 200:
        print(f"[*] OK!")
    else:
        print(f"[!] Feilet. Statuskode: {response.status_code}\n-----\n{response.text}")