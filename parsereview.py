import requests
import json


def fetch_and_save_json_with_headers(url, headers, filename):
    # Make a GET request to the URL with custom headers
    response = requests.get(url, headers=headers)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse JSON data from the response
        data = response.json()
        # Write the JSON data to a file
        with open(filename, 'w') as file:
            file.write(json.dumps(data, indent=4))
        print(f"Data saved to {filename}")
    else:
        print("Failed to fetch data. Status code:", response.status_code)


# URL from which to fetch the JSON data without the API key in the URL


# Headers including the API key
headers = {
    "Authorization": "Bearer c8986ed2e3764e50bf963f679c07c13068069c22b53ee318b4e1971b23ff274b"
}
ids = [
    "yPrwvd6z5dCHWU8l4b8nyA",
    "0ukhgBeLATOo8b8lDobRGg",
    "3ehyrexo3WcoTy74c2jDKA",
    "ApwmEiStq9aP9-Tf2xfVtA",
    "q43-XtobLPmbkxHmpSvEFA",
    "cZmnKz8AnTVoDLTGbpK_yQ",
    "QHhSs3JJ2k9tJufA4QUtYw",
    "uhIQYIk5LpBlRho9n_D_7g",
    "6wGHem2o7migh4syWmmB8A",
    "O4RxA_zCFBHd_2mrERSiNQ",
    "bCY3Jn1_p9GbCwnDzU-nDA",
    "kzXrQKJpN2JyLd68iwH3hg",
    "UG6_dVkv1I5AV7NS3CG6Kg",
    "6wGHem2o7migh4syWmmB8A",
    "-7Pb_TmSCZ4wUHQKoZD62A",
    "23UWCyB8UnPu-0t-67iEKA",
    "kdcnUiHns8Ni04Vl6VOikQ",
    "LoMpMSfzVd1g-5szne8V3w",
    "CkWEtj4Y8sG-U9x2eoejvw",
    "ZdEohT36LcY3eKh4fJMGRQ",
    "rP90TP7gOMzBFTrKWEEsOw",
    "xakTfx650TBYn3IALjPZDg",
    "RewS023eAFmP9AlOcemXkw",
    "KD3vnYvuHpfC_sYeWkgUTA",
    "3fUs8kbbbDvD_lTE5sOcKQ",
    "RFCibpN2u5pt4eev7gBQXA",
    "KTGOyUdVsd__xSU58vG4Iw",
    "87O_yo8r8IlG7e82-usSiw",
    "RpsYzOuyCoAVKLl-vQL1mw",
    "AiN208ZI9KEsrc3BQucKMw",
    "COgw5a3B_fwmN0BbZObJwg",
    "87O_yo8r8IlG7e82-usSiw",
    "oPoBBnSQlil1SWkX802asA",
    "V6OToDLIwUllf1MbgWw-9w",
    "1_JJaNLnedujQIAu6i10jQ",
    "f2tTzO54v9FNUZaGbIXJFQ",
    "-3q2_EyalvMK9xysWe3DbA",
    "tfGXKEGtiuo4YB3ocK-ywQ",
    "83maS2mCXYZjuwEhozVtLA",
    "D-JjoA77Il97HPfMsUs8Vg",
    "WF4_Nqgdbn_nJHwhXmgfRQ",
    "AiN208ZI9KEsrc3BQucKMw",
    "PuNB8MH5P0gEX9RVXoORcg",
    "-AIX1rem_OF-9Et3p_K9Gg",
    "e1RoEC5uvzXnLXbjuK3ZSg",
    "24--2r1ZEgnmJs5iVVAOgQ",
    "KtI2ZEWm9VE-anUL-H_MaQ",
    "r0JxdG5StcD8eiHF9u01ZQ",
    "WS_3VW9O2CmJMzlI4uxJrA",
    "9x8tQvdczbrNaTsQJWRiCQ",
    "tJGAni_ckCFH1SDmyopG9g",
    "h4d0f2VpgycY5oPBsJowyQ",
    "xPNE432uqWzrN2LNEpW5MA",
    "uIAos8ANK0KDY5Vpy5EHCA",
    "ZqPa0NeZoJiKyQ1TZ8OoJQ",
    "3zI1Ycg-VsFarVA2adIJGg",
    "1b-SIUJttFwlFWTfpp0Xqg",
    "Kcva2t7e6Ukpb5vMvkdc2w",
    "8PcTmvfMShQkdS4qDbyzog",
    "Qe7_nhlFf6WO541A9AAYbw",
]
for i in range(60):
    # Filename where the JSON data will be saved
    filename = f"{i+180}_py.json"
    url = f"https://serpapi.com/search.json?engine=yelp_reviews&place_id={ids[i]}&api_key" \
          f"=c8986ed2e3764e50bf963f679c07c13068069c22b53ee318b4e1971b23ff274b "
    fetch_and_save_json_with_headers(url, headers, filename)
