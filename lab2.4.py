import xml.etree.ElementTree


file = xml.etree.ElementTree.parse("currency.xml")
root = file.getroot()

currency = {}

for valute in root.findall("Valute"):
    name = valute.find("Name").text
    value = float(valute.find("Value").text.replace(",", "."))

    currency[name] = value

print(currency)