
import wikipedia


def main():

    page_title = input("Enter in Wikipedia page title or search term\n>>> ")
    while page_title != "":
        try:
            page = wikipedia.page(page_title)
            print()
            print_page_info(page)
            print()
        except wikipedia.exceptions.DisambiguationError as e:
            for index, option_title in enumerate(e.options):
                print("{}) {}".format(index, option_title))
            page = wikipedia.page(e.options[int(input("Select option: "))])  # no error checking on input
            print()
            print_page_info(page)
            print()
        page_title = input("Enter in Wikipedia page title or search term\n>>> ")


def print_page_info(page):
    print(page.title)
    print(page.summary)
    print(page.url)



main()
