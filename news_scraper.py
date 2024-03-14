import requests
from bs4 import BeautifulSoup

def scrape_news(company_name):
    # Define the URL pattern for a news search related to the company
    url = f"https://www.google.com/search?q={company_name}+news"
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the news article titles and URLs
    news_articles = []
    for headline in soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd'):
        title = headline.text
        link = headline.find_parent('a')['href']
        news_articles.append({'title': title, 'link': link})
    
    return news_articles

def generate_email_template(company_name, news_articles):
    email_body = f"Latest news about {company_name}:\n\n"
    for article in news_articles:
        email_body += f"{article['title']}: {article['link']}\n"
    return email_body

if __name__ == "__main__":
    company_name = input("Enter the company name: ")
    news_articles = scrape_news(company_name)
    email_body = generate_email_template(company_name, news_articles)
    print(email_body)  # You can modify this to send an email through Outlook