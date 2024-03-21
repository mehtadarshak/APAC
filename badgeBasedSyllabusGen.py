import requests
from bs4 import BeautifulSoup


def get_topics_from_web(profession):
  url = "https://en.wikipedia.org/wiki/" + profession.replace(" ", "_")
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  potential_topics = []
  # Look directly for li tags with divs having class "vector-toc-text"
  toc_items = soup.find_all("div", class_=lambda class_: class_ and "vector-toc-text" in class_)
  result_set = []
  for toc_item in toc_items:
    #topic_text = toc_item.find("div", class_="vector-toc-text").text.strip().split(" ", 1)[1]  # Remove numbering
    potential_topics.append(toc_item)
    if toc_item:
        result_set.append((str(toc_item).replace("</span>"," ").replace("</div>","").replace("<span class=\"vector-toc-numb\">","").replace("<div class=\"vector-toc-text\">","")))
  return result_set#[t for t in result_set if len(t) > 3]  # Filter out short strings


def extract_topics_from_html(html_content):
  soup = BeautifulSoup(html_content, 'html.parser')
  toc_items = soup.find_all("li", class_="vector-toc-list-item-expanded")
  extracted_topics = []

  if toc_items:
    for toc_item in toc_items:
      text_elements = toc_item.find_all("div", class_="vector-toc-text")
      for text_element in text_elements:
        topic_text = text_element.text.strip().split(" ", 1)[1]  # Remove numbering
        extracted_topics.append(topic_text)
  return extracted_topics


def design_syllabus(profession):
  syllabus = {
      "Profession": profession,
      "Learning Objectives": [],
      "Modules": [],
      "Resources": []
  }

  # Gather user input for Learning Objectives
  # ... (similar to previous code)

  # Gather user input for Modules
  # ... (similar to previous code)

  # Attempt to generate topics using web scraping (modify URL as needed)
  scraped_topics = get_topics_from_web(profession)

  # Allow user to provide HTML content (optional)
  has_html_content = input("Do you have HTML content with a TOC? (y/n): ")
  if has_html_content.lower() == "y":
    html_content = input("Enter the HTML content: ")
    extracted_topics = extract_topics_from_html(html_content)
    scraped_topics.extend(extracted_topics)  # Combine scraped and extracted topics


  # Limit topics and avoid duplicates
  unique_topics = list(set(scraped_topics))#[:10]  # Limit to top 10 unique topics
  unique_topics = [topic for topic in unique_topics if len(topic)>5]
  #print(unique_topics)
  # Assign topics to modules (simple assignment for now)
  for i, module in enumerate(syllabus["Modules"]):
    module_topics = unique_topics[i * 2:(i * 2) + 2]  # Assign 2 topics per module (adjust as needed)
    module["Topics"] = module_topics[: len(module_topics)]  # Handle potential shortage

  # User can add resources later...
  # ... (similar to previous code)

  return unique_topics


# Get user input for profession
profession = input("Enter the profession or skill: ")

# Design syllabus and print
syllabus = design_syllabus(profession)
print("\n** Syllabus for", profession, "**")

print("\nLearning Objectives:")
for objective in syllabus:
  if len(objective)>2:
      print("-", objective[2:], "in",profession)























