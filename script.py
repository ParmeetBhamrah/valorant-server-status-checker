import requests as req
from bs4 import BeautifulSoup
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }
try:
    response = req.get("https://istheservicedown.in/problems/valorant", headers=headers)
    response.raise_for_status()   
    soup = BeautifulSoup(response.content, 'html.parser')
    valorant_status = soup.find('p', class_ = "status-title-normal")
    if valorant_status.text.strip().lower() == "no problems detected":
        print("VALORANT servers are working fine!")
    else:
        print("There might be issues with VALORANT servers at the moment.\nTry again later.")
except req.exceptions.ConnectionError:
    print("No internet connection detected.\nPlease check your connection and try again.")
except req.exceptions.HTTPError:
    print("HTTP error occurred.")
except AttributeError:
    print("Failed to retrieve the server status.\nTry again later.")
except Exception as err:
    print(f"An unexpected error has occurred: {err}")