import requests


def check_site(site):
    try:
        r = requests.get(site)
        print("O utilizador tem acesso ao website!")
    except requests.exceptions.RequestException as err:
        print("O utilizador não tem acesso ao website!")


check_site('https://www.iefp.pt/')