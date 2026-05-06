import requests
from bs4 import BeautifulSoup

# On simule un navigateur Safari sur Mac pour ne pas être bloqué
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'
}

url = "https://news.ycombinator.com/"
print("--- Tentative de connexion sécurisée ---")

try:
    # On ajoute headers=headers ici
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status() # Vérifie si la page a bien chargé
    
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('span', class_='titleline')
    
    for i, link in enumerate(links[:5], 1):
        print(f"{i}. {link.text}")
        
except Exception as e:
    print(f"Erreur technique : {e}")

url = "https://news.ycombinator.com/"
print("--- Test de Scraping en cours ---")

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('span', class_='titleline')
    
    for i, link in enumerate(links[:5], 1):
        print(f"{i}. {link.text}")
        
except Exception as e:
    print(f"Erreur : {e}")

