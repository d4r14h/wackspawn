from faker import Faker
from faker.providers import internet


faker = Faker()
name = faker.name()
address = faker.address()
faker.add_provider(internet)
ipPriv = faker.ipv4_private()
ipPub = faker.ipv4_public()
cc = faker.credit_card_full()
print(f'Name: {name}')
print(f'Address: {address}')
print(f'Private IP: {ipPriv}')
print(f'Public IP: {ipPub}')
print(f'Credit Card Info: {cc}')
