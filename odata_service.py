import fire
import requests


class OdataService(object):
    def search_entity(self):
        search_id = input("Enter the Search parameter id: ")
        url = "https://services.odata.org/TripPinRESTierService/(S(ebte4tgtnsponxq0kowrl2yg))/People('{}')".format(search_id)
        response = requests.get(url)
        data = response.json()
        return data

    def filter_entity(self):
        filter_id = input("Enter the filter parameter id: ")
        url = "https://services.odata.org/TripPinRESTierService/(S(ebte4tgtnsponxq0kowrl2yg))/People?$filter=FirstName eq '{}'".format(filter_id)
        response = requests.get(url)
        data = response.json()
        return data

    def create_entity(self):
        username = input("Enter the username: ")
        first_name = input("Enter the First Name: ")
        last_name = input("Enter the last name: ")
        emails = list(map(str, input("Enter the emails: ").split()))
        address = input("Enter the address: ")
        city_name = input("Enter the City Name: ")
        country_region = input("Enter the Country Region: ")
        region = input("Enter the Region: ")
        data={
		    "UserName":username,
		    "FirstName":first_name,
		    "LastName":last_name,
		    "Emails":emails,
		    "AddressInfo": [
		    {
		      "Address":address ,
		      "City": {
			"Name": city_name,
			"CountryRegion": country_region,
			"Region": region
		      }
		    }
		    ]
 	     }
        url = "https://services.odata.org/TripPinRESTierService/(S(ebte4tgtnsponxq0kowrl2yg))/People"
        response = requests.post(url, json=data)
        data = response.json()
        return data

if __name__ == '__main__':
    fire.Fire(OdataService)

