from Address import Address
from Mailing import Mailing

to_address = Address(141865, 'Лобня', 'Ленина', '30', '25')
from_address = Address(156458, 'Дмитров', 'Промышленная', '65','158')
mailing=Mailing (to_address, from_address, '750', 'DM00585')

print (f'Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.sity}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartament}'
       f' в {mailing.to_address.index}, {mailing.to_address.sity}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartament}. Стоимость {mailing.cost}')