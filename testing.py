from googlesearch import search
# def google_search(query, num_results=10):
#     try:
#         # Performing a Google search and iterating through the results
#         for j in search(query, num_results=num_results):
#             print(j)
#     except Exception as e:
#         print(f"An error occurred in searching google: {e}")

# google_search('How to cook pizza')

import webbrowser

def google_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

# Example usage
search_query = input("what do you want to search?\n ")
google_search(search_query)
