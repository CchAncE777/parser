import time
from element_pasrser import elementParser



def main():
    parser = elementParser('https://5element.by/catalog/571-buterbrodnicy')
    parser.accept_cookie()
    try:
        while True:
            time.sleep(1)
            parser.get_links_on_page()
            time.sleep(1)
            parser.go_to_the_next_page()
    except Exception as e:
        print(e)
    print(parser.get_info())

if __name__ == "__main__":
    main()