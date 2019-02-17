from lxml import etree
from urllib.request import urlopen
from io import StringIO, BytesIO

host = "https://www.nativeskatestore.co.uk"

def main():
    # specify the url
    sk_link = host+"/skateboards-c7"
    sh_link = host+"/skate-shoes-c1"
    cl_link = host+"/skate-clothing-c9"
    ac_link = host+"/accessories-c3"

    print("-----------------------------------------------------------")
    print("Skateboards")
    print_products(sk_link)
    for i in range(2,47,1):
        print("Page number ", i)
        print_products(sk_link + "?page=" + str(i))
    print("-----------------------------------------------------------")
    print("Shoes")
    print_products(sh_link)
    for i in range(2, 13, 1):
        print("Page number ", i)
        print_products(sh_link + "?page=" + str(i))
    print("-----------------------------------------------------------")
    print("Clothing")
    print_products(cl_link)
    for i in range(61, 83, 1):
        print("Page number ", i)
        print_products(cl_link + "?page=" + str(i))

    print("-----------------------------------------------------------")
    print("Accessories")
    print_products(ac_link)
    for i in range(2, 14, 1):
        print("Page number ", i)
        print_products(ac_link + "?page=" + str(i))

    # data = urlopen(quote_page).read()  # bytes
    # body = data.decode('utf-8')
    #
    # parser = etree.HTMLParser()
    # tree = etree.parse(StringIO(body), parser)
    #
    # links = tree.xpath('//div[contains(@class,"product__details__title")]'
    #                       '/a')
    # prices = tree.findall('//span[@class="product-content__price--inc"]'
    #                       '/span[@class="GBP"]')
    # images = tree.xpath('//div[@class="product__image"]'
    #                     '/a'
    #                     '/img'
    #                     )
    #
    #
    # print(len(prices))
    # print(len(links))
    # print(len(images))
    #
    # for i in range((int)(len(links)/4)):
    #     # for j in range(4):
    #     print("titles: ",
    #           links[i].attrib.get('title'),   '|',
    #           links[i+1].attrib.get('title'), '|',
    #           links[i+2].attrib.get('title'), '|',
    #           links[i+3].attrib.get('title'))
    #     print("prices: ",
    #           prices[i].text, '|',
    #           prices[i + 1].text, '|',
    #           prices[i + 2].text, '|',
    #           prices[i + 3].text)
    #     print("links: ",
    #           host+links[i].attrib.get('href'), '|',
    #           host+links[i + 1].attrib.get('href'), '|',
    #           host+links[i + 2].attrib.get('href'), '|',
    #           host+links[i + 3].attrib.get('href'))
    #     print("images: ",
    #           host+images[i].attrib.get('data-src'), '|',
    #           host+images[i + 1].attrib.get('data-src'), '|',
    #           host+images[i + 2].attrib.get('data-src'), '|',
    #           host+images[i + 3].attrib.get('data-src'))


def print_products(link):
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


    print(len(prices))
    print(len(links))
    print(len(images))

    # for i in range((int)(len(links) / 4)):
    #     # for j in range(4):
    #     print("titles: ",
    #           links[i].attrib.get('title'), '|',
    #           links[i + 1].attrib.get('title'), '|',
    #           links[i + 2].attrib.get('title'), '|',
    #           links[i + 3].attrib.get('title'))
    #     print("prices: ",
    #           prices[i].text, '|',
    #           prices[i + 1].text, '|',
    #           prices[i + 2].text, '|',
    #           prices[i + 3].text)
    #     print("links: ",
    #           host + links[i].attrib.get('href'), '|',
    #           host + links[i + 1].attrib.get('href'), '|',
    #           host + links[i + 2].attrib.get('href'), '|',
    #           host + links[i + 3].attrib.get('href'))
    #     print("images: ",
    #           host + images[i].attrib.get('data-src'), '|',
    #           host + images[i + 1].attrib.get('data-src'), '|',
    #           host + images[i + 2].attrib.get('data-src'), '|',
    #           host + images[i + 3].attrib.get('data-src'))

if __name__ == '__main__':
    main()
