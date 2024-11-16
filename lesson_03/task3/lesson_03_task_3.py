from address import Address
from mailing import Mailing

to_address = Address("248000", "г. Калуга", "ул. Кибальчича", "1", "96")
from_address = Address("101000", "г. Москва", "ул. Валовая", "1", "19")


mailing = Mailing(to_address, from_address, 100, "1234567890")

print(mailing)
