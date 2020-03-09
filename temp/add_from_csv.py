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