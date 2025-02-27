from user import User
from card import Card

alex = User("Alex")
mark = User("Mark")
marta = User("Marta")

alex.sayName()
alex.setAge(33)
alex.sayAge()

card = Card("4353 1223 6547 9806", "11/28", "Alex F")

alex.addCard(card)
alex.getCard().pay(1000)

