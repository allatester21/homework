from address import Address
from mail import Mailing


mail = Mailing("Moscow", "Kemerovo", 1500, "836543975")
address = Address("650056", "Kemerovo", "Volgogradskaya", "150", "15")
address_to = Address("490014", "Moscow", "Lenina", "23", "1")

print(f"Отправление {mail.track} из {address.index}, {address.city}, "
      f"{address.street}, - {address.flat} в "
      f"{address_to.index}, {address_to.city}, {address_to.street}, "
      f"{address_to.house} - {address_to.flat}."
      f"Стоимость {mail.cost} рублей")
