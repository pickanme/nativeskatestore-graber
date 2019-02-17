import pyodbc
from io import StringIO
from urllib.request import urlopen

from lxml import etree

# Specifying the ODBC driver, server name, database, etc. directly
cnxn = pyodbc.connect('DRIVER={/usr/local/lib/libsqlite3odbc.so};'
                      'Database=../resources/nativeskatestore.sqlite;'
                      'LongNames=0;Timeout=1000;NoTXN=0;'
                      'SyncPragma=NORMAL;StepAPI=0;')
# Python 3.x
cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
cnxn.setencoding(encoding='utf-8')
# Create a cursor from the connection
cursor = cnxn.cursor()

host = "https://www.nativeskatestore.co.uk"

def main():
    # specify the url
    sk_link = host+"/skateboards-c7"
    sh_link = host+"/skate-shoes-c1"
    cl_link = host+"/skate-clothing-c9"
    ac_link = host+"/accessories-c3"
    # specify db names
    sk_db = "skateboards"
    sh_db = "shoes"
    cl_db = "clothing"
    ac_db = "accessories"

    print("-----------------------------------------------------------")
    print("Skateboards")
    print("Page number 1")
    print_products(sk_link, sk_db)
    for i in range(2,47,1):
        print("Page number ", i)
        print_products(sk_link + "?page=" + str(i), sk_db)
    print("-----------------------------------------------------------")
    print("Shoes")
    print("Page number 1")
    print_products(sh_link, sh_db)
    for i in range(2, 13, 1):
        print("Page number ", i)
        print_products(sh_link + "?page=" + str(i), sh_db)
    print("-----------------------------------------------------------")
    print("Clothing")
    print("Page number 1")
    print_products(cl_link, cl_db)
    for i in range(2, 83, 1):
        print("Page number ", i)
        print_products(cl_link + "?page=" + str(i), cl_db)
    print("-----------------------------------------------------------")
    print("Accessories")
    print("Page number 1")
    print_products(ac_link, ac_db)
    for i in range(2, 14, 1):
        print("Page number ", i)
        print_products(ac_link + "?page=" + str(i), ac_db)

def print_products(link, db_name):
    data = urlopen(link).read()  # bytes
    body = data.decode('utf-8')

    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(body), parser)

    links = tree.xpath('//div[contains(@class,"product__details__title")]'
                       '/a')
    prices = tree.xpath('//div[@class="product__details__prices"]'
                        '/span[contains(@class, "product__details__prices__price")]'
                        '/span'
                        '/span[@class="product-content__price--inc"]'
                        '/span[@class="GBP"]')
    images = tree.xpath('//div[@class="product__image"]'
                        '/a'
                        '/img')

    for i in range(len(links)):
        cursor.execute("insert  into "+db_name+"(title, price, prod_link, img_link)"
                       "values (?, ?, ?, ?)",
                       links[i].attrib.get('title'),
                       prices[i].text,
                       host + links[i].attrib.get('href'),
                       host + images[i].attrib.get('data-src'))
        cursor.commit()

if __name__ == '__main__':
    main()
