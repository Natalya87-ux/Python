from user import User
from card import Card


alex = User("Alex")


alex.sayName()
alex.sayAge()
alex.setAge(33)

card = Card("1234 5678 9112 3456", "11/28", "Alex F")
card.pay(1000)
