# How to connect to an API using Python

# import the library
import requests 
'''
if only on project virtual environment you will type 
    pip install requests
if system wide (full wsl2)
    sudo apt install python3-requests
check version
    python3 -c "import requests; print(requests.__version__)"       
'''


base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    # print(url) # https://pokeapi.co/api/v2//pokemon/pikachu
    response = requests.get(url)
    # print(response) # <Response [200]> - means ok

    if response.status_code == 200:
        pokemon_data = response.json()
        # print(pokemon_data) # large dictionary
        print("\nData is retrieved.\n")
        return pokemon_data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")   

pokemon_name = "Typhlosion"

pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")

