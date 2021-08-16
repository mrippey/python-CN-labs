'''
Use the countries API https://restcountries.eu/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''

import requests


base_countries_api_url = "https://restcountries.eu/rest/v2"

ask_home_country = input("whats your home country?: ")

ask_current_country = input("where do you currently live?: ")

print()


def make_api_request() -> None:

    home_country = requests.get(base_countries_api_url + f"/name/{ask_home_country}")
    home_country.status_code
    current_country = requests.get(
        base_countries_api_url + f"/name/{ask_current_country}"
    )
    current_country.status_code

    get_country_population(home_country, current_country)


def get_country_population(home_country, current_country) -> requests.Response:

    home_country_result = home_country.json()
    current_country_result = current_country.json()

    for home_pop in home_country_result:
        home_pop_nums = home_pop["population"]

    for current_pop in current_country_result:
        current_pop_nums = current_pop["population"]

    if current_pop_nums > home_pop_nums:
        print(f'{current_pop["name"]} has a larger population')
    else:
        print(f'{home_pop["name"]} has a larger population')

    print()

    get_country_area(home_country_result, current_country_result)
    get_country_names(home_country_result, current_country_result)


def get_country_area(home_country_result, current_country_result) -> requests.Response:

    for home_area in home_country_result:
        home_area_nums = home_area["area"]

    for current_area in current_country_result:
        current_area_nums = current_area["area"]

    print(f"Difference in area: {abs(home_area_nums - current_area_nums)}")
    print()


def get_country_names(home_country_result, current_country_result) -> requests.Response:

    for native_name_home in home_country_result:
        native_cn_name = native_name_home["nativeName"]
        country_capital_home = native_name_home["capital"]

    for native_name_current in current_country_result:
        native_curr_name = native_name_current["nativeName"]
        country_capital_curr = native_name_current["capital"]

    print(
        f"""Home country native name and capital: {native_cn_name}, {country_capital_home}\n 
Current country native name and capital: {native_curr_name}, {country_capital_curr}"""
    )


make_api_request()
