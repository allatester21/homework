from smartphone import Smartphone

catalog = [
    Smartphone("iPhone", "11Max", "+79990009900"),
    Smartphone("Poco", "12", "+79887778877"),
    Smartphone("Huawey", "10.5", "+79665556655"),
    Smartphone("Xiaomi", "Lite 11", "+79334443344"),
    Smartphone("Readme", "Note", "+79223331122")
]

for smartphone in catalog:
    print(f"{smartphone.marka} {smartphone.model} {smartphone.number}")
