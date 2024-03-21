from googlesearch import search
import requests
from bs4 import BeautifulSoup


def recommend_resources(query):
  results = search(query + " learning resources", num=3, stop=3)
  return list(results)


def get_page_title(url):
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for unsuccessful requests
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.title.string.strip() if soup.title else None
  except requests.exceptions.RequestException as e:
    print(f"Error retrieving title: {e}")
    return None



query = "types of blockchain"#"machine learning"#subject name + chapter name + topic name
recommendations = recommend_resources(query)

print("Recommended Resources:")
for recommendation in recommendations:
  print(get_page_title(recommendation),"-->",recommendation)





















