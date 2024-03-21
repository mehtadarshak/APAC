import re
from PyPDF2 import PdfReader

def extract_chapters_topics(pdf_path):
  """
  Extracts chapter names and topics from a syllabus PDF.

  Args:
    pdf_path: The path to the syllabus PDF file.

  Returns:
    A dictionary where keys are chapter names and values are lists of topics
    under that chapter.
  """
  chapters = {}

  # Read the PDF file
  with open(pdf_path, 'rb') as pdf_file:
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
      text += page.extract_text()

  chapter_pattern = r"(Chapter|Unit) ?\s*([-\d]+):?\s*(.*)"
  topic_pattern = r"\s*-\s*(.*)"

  chapter_match = re.search(chapter_pattern, text, re.MULTILINE)
  while chapter_match:
    chapter_type, chapter_num, chapter_name = chapter_match.groups()
    # Combine chapter type and number into a consistent format
    chapter_name = f"{chapter_type} {chapter_num}".strip()
    chapters[chapter_name] = []
    text = text[chapter_match.end():]

    topic_match = re.findall(topic_pattern, text, re.MULTILINE)
    chapters[chapter_name].extend(topic_match)

    chapter_match = re.search(chapter_pattern, text, re.MULTILINE)

  return chapters

# Example usage (assuming the syllabus.pdf file is in the same directory)
pdf_path = "EDM.pdf"
chapters = extract_chapters_topics(pdf_path)

# Print the extracted chapters and topics
for chapter_name, topics in chapters.items():
  print(f"Chapter: {chapter_name}")
  for topic in topics:
    print(f"\t- {topic}")
