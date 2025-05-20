import requests
from bs4 import BeautifulSoup

def summarize_web_content(query):
    try:
        url = query.split(" ")[-1]
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = " ".join([p.text for p in paragraphs])
        return " ".join(text.split()[:100]) + "..."
    except Exception as e:
        return f"Failed to summarize web content: {e}"