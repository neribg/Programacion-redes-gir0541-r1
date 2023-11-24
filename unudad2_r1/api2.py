import requests
url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "application/gzip",
    "X-RapidAPI-Key": "386d45ff01msh448912d7759b49ap1ce128jsncc7d31c478f6",
    "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}
while True:
    user_input = input("Enter a phrase to translate (or type s to quit): ")
    if user_input.lower() == "s" or user_input.lower() == "yes":
        print("Exiting program...")
        break
    
    payload = {
        "source": "es",
        "target": "en",
        "q": user_input
    }
    response = requests.post(url, data=payload, headers=headers)
    json_data = response.json()
    translation = json_data["data"]["translations"][0]["translatedText"]
    print(f"Translated phrase: {translation}\n")