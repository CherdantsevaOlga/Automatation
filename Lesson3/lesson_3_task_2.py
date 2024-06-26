from smartphone import Smartphone
catalog=[]

phone_1=Smartphone('Apple', '15', '+79655552233')
phone_2=Smartphone('Samsung', 'Galaxy', '+79034568955')
phone_3=Smartphone('Xiaomi', 'A5', '+79661536593')
phone_4=Smartphone('POCO', 'F6 Pro', '+79056578997')
phone_5=Smartphone('Realme', 'GT 6T', '+79096531133')

catalog.append(phone_1)
catalog.append(phone_2)
catalog.append(phone_3)
catalog.append(phone_4)
catalog.append(phone_5)

for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.number}')
