# Odata-service
### Create a Python Virtual Environment using the below commnad
```
virtualenv -p python3 venv

```
### To Activate the virtual enviroment 

```
source venv/bin/activate

```

### clone the project

#### Install the requrements file for the necessary libraries to run the application using the below command
```
pip install -r requirements.txt
```

### To use the create entity service use the below commnd
```
python odata_service.py create_entity

```

whenever the user run the above command, In the command prompt its asks the user to add the inputs for the create entity service.

Below example shows how command interface asks for the user to enter the inputs to use the create entity service

#### Example1

##### Enter the username: jhonwhyte
##### Enter the First Name: Jhon
##### Enter the last name: Whyte
##### Enter the emails: john@example.com john@abc.com
##### Enter the address: 187 Suffolk Ln
##### Enter the City Name: Boise
##### Enter the Country Region: United States
##### Enter the Region: ID

Below data shows the output of the above created entity

```
@odata.context:  https://services.odata.org/TripPinRESTierService/(S(1edjpi2kilekoqynwth4lojw))/$metadata#People/$entity
UserName:        jhonwhyte
FirstName:       Jhon
LastName:        Whyte
MiddleName:      null
Gender:          Male
Age:             null
Emails:          ["john@example.com", "john@abc.com"]
FavoriteFeature: Feature1
Features:        []
AddressInfo:     [{"Address": "187 Suffolk Ln","City": {"Name": "Boise", "CountryRegion": "United States", "Region": "ID" }}]
HomeAddress:     null

```

### To use the search entity service use the below commnd
```
python odata_service.py serach_entity

```
whenever the user run the above command, In the command prompt its asks the user to add the parameter to serach the entity by ising search entitiy service.

Below example shows how command interface asks  the user to enter the parameter to search the entity

#### Example2

##### Enter the Search parameter id: jhonwhyte

Below data shows the output of the above searched parameter

```
@odata.context:  https://services.odata.org/TripPinRESTierService/(S(1edjpi2kilekoqynwth4lojw))/$metadata#People/$entity
UserName:        jhonwhyte
FirstName:       Jhon
LastName:        Whyte
MiddleName:      null
Gender:          Male
Age:             null
Emails:          ["john@example.com", "john@abc.com"]
FavoriteFeature: Feature1
Features:        []
AddressInfo:     [{"Address": "187 Suffolk Ln.","City": {"Name": "Boise", "CountryRegion": "United States", "Region": "ID" }}]
HomeAddress:     null

```

### To use the filter entity service use the below command

```
python odata_service.py filter_entity

```
whenever the user run the above command, In the command prompt its asks the user to add the filter parameter to run the filter entity service.

Below example shows how command interface asks  the user to enter the filter parameter

#### Example3

##### Enter the filter parameter id: Jhon

Below data shows the output of the above searched parameter

```
@odata.context: https://services.odata.org/TripPinRESTierService/(S(1edjpi2kilekoqynwth4lojw))/$metadata#People
value:          [{"UserName": "jhonwhyte", "FirstName": "Jhon", "LastName": "Whyte", "MiddleName": null, "Gender": "Male", "Age": null, "Emails": ["john@example.com", "john@abc.com"], "FavoriteFeature": "Feature1", "Features": [], "AddressInfo": [{"Address": "187 Suffolk Ln", "City": {"Name": "Boise", "CountryRegion": "United States", "Region": "ID"}}], "HomeAddress": null}]
```

