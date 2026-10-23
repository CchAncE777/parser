from parser_class import Parser
import time

def main():
    parser = Parser('https://5element.by/catalog/571-buterbrodnicy')
    parser.accept_cookie()
    try:
        while True:
            time.sleep(1)
            parser.get_links_on_page()
            print(len(parser.links_list))
            time.sleep(1)
            parser.go_to_the_next_page()

    except Exception as e:
        print(e)
    parser.get_info()
    print(parser.info_list)

if __name__ == "__main__":
    main()