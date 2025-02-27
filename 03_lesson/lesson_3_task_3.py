from address import Address
from mail import Mailing

address = Address("650056", "Kemerovo", "Volgogradskaya", "150", "15")
address_to = Address("490014", "Moscow", "Lenina", "23", "1")

mail = Mailing(
      to_address=address_to,
      from_address=address,
      cost=1500,
      track="836543975"
)

print(f"Отправление {mail.track} из {mail.from_address.index}, "
      f"{mail.from_address.city}, "
      f"{mail.from_address.street}, - {mail.from_address.flat} в "
      f"{mail.to_address.index}, {mail.to_address.city}, "
      f"{mail.to_address.street}, "
      f"{mail.to_address.house} - {mail.to_address.flat}."
      f"Стоимость {mail.cost} рублей")
