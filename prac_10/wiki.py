import wikipedia


def search_wikipedia():
    continue_search = True
    while continue_search:
        try:
            title = input("Enter the title to search on Wikipedia (or press Enter to exit): ")
            if not title:
                continue_search = False
                break

            page = wikipedia.page(title, auto_suggest=False)
            print("\nTitle:", page.title)
            print("Summary:", page.summary)
            print("URL:", page.url, "\n")

        except wikipedia.DisambiguationError as e:
            print("This page is a disambiguation page.")
            print("Options include:", e.options)
        except wikipedia.PageError:
            print("Page not found.")
        except Exception as e:
            print("An error occurred:", e)


search_wikipedia()
