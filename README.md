# django-data-api
> Created by Nicholas Ramsay

Front-end built with Vue.JS

Back-end/REST API built with Django Rest Framework

## Adding data to api
This was executed in the django shell
```py
    from data.models import Person
    import csv

    with open('./MOCK_DATA.csv') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i > 0:
                p = Person(
                    first_name = row[1], 
                    last_name = row[2], 
                    email = row[3], 
                    gender = row[4], 
                    ip_address = row[5], 
                    country = row[6], 
                    age = int(row[7])
                )
                p.save()
```