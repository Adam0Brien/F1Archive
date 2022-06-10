import requests
import lxml.etree as etree



year = input("What year?: ")
round = input("What round?: ")
r = requests.get("http://ergast.com/api/f1/"+year+"/"+round)
f = open('data.xml', 'a')

f.truncate(0)
f.write(r.text)




x = etree.parse('data.xml')
print(etree.tostring(x, pretty_print=True))

if __name__ == '__main__':
    print()
