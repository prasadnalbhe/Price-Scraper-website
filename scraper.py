# scraper.py
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Accept-Language': 'da, en-gb, en',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}




def get_flipkart_price(name):
    try:
        name1 = name.replace(" ", "%20")
        flipkart_url = f"https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        
        res = requests.get(flipkart_url)
        soup = BeautifulSoup(res.content, 'html.parser')

        if soup.select('.KzDlHZ'):
            flipkart_name = soup.select('.KzDlHZ')[0].getText().strip().upper()
            if name.upper() in flipkart_name:
                flipkart_price = soup.select('.Nx9bqj')[0].getText().strip()
        elif soup.select('.wjcEIp'):
            flipkart_name = soup.select('.wjcEIp')[0].getText().strip().upper()
            if name.upper() in flipkart_name:
                flipkart_price = soup.select('.Nx9bqj')[0].getText().strip()
        elif soup.select('.s1Q9rs'):
            flipkart_name = soup.select('.s1Q9rs')[0].getText().strip().upper()
            if name.upper() in flipkart_name:
                flipkart_price = soup.select('._30jeq3')[0].getText().strip()
        else:
            return '0'
        
        return flipkart_price


    except Exception as e:
        print("Error occurred while fetching data from Flipkart:", e)
        return '0'


def get_flipkart_image(name):
    try:
        name1 = name.replace(" ", "%20")
        flipkart_url = f"https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        
        res = requests.get(flipkart_url, headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')

        for img in soup.select('.DByuf4.IZexXJ.jLEJ7H'):
            if name.upper() in img.get('alt', '').upper():
                flipkart_image = "https://rukminim2.flixcart.com/image/312/312/kmmcrrk0/mobile/d/e/m/8-pro-rmx3081-realme-original-imagfgpgfexvzngd.jpeg?q=70"
                return flipkart_image

        return 'No image available'

    except Exception as e:
        print("Error occurred while fetching Flipkart image:", e)
        return 'No image available'
        

def get_amazon_image(name):
    try:
        name1 = name.replace(" ", "-")
        name2 = name.replace(" ", "+")
        amazon_url = f'https://www.amazon.in/{name1}/s?k={name2}'
        res = requests.get(amazon_url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        for img in soup.select('.s-image'):
            if name.upper() in img.get('alt', '').upper():
                return img['src']

        return 'No image available'

    except Exception as e:
        print("Error occurred while fetching Amazon image:", e)
        return 'No image available'
    
def get_flipkart_link(name):
    try:
        name1 = name.replace(" ", "%20")
        flipkart_url = f"https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        return flipkart_url
    except Exception as e:
        print("Error occurred while fetching Flipkart link:", e)
        return ''


def get_flipkart_rating(name):
    try:
        name1 = name.replace(" ", "%20")
        flipkart_url = f"https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        
        res = requests.get(flipkart_url, headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')

        if soup.select('.XQDdHH'):
            flipkart_rating = soup.select('.XQDdHH')[0].getText().strip()
        elif soup.select('.ipqd2A'):
            flipkart_rating = soup.select('.ipqd2A')[0].getText().strip()
        else:
            flipkart_rating = 'Not available'

        return flipkart_rating
    except Exception as e:
        print("Error occurred while fetching Flipkart ratings:", e)
        return '0'


def get_flipkart_highlights(name):
    try:
        normalized_name = name.replace(" ", "%20")
        flipkart_url = f"https://www.flipkart.com/search?q={normalized_name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        
        res = requests.get(flipkart_url, headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')

        highlights = []
        # Check for unordered list highlights
        if soup.select('.G4BRas'):
            highlights = [highlight.text.strip() for highlight in soup.select('.G4BRas > li')]
         
                
        # If no highlights found in <ul>, check for ordered list highlights
        elif not highlights and soup.select('.J+igdf'):
            highlights = [highlight.text.strip() for highlight in soup.select('.J+igdf > li')]
 

        # Fallback if no highlights are found
        elif not highlights:
            highlights = ['No highlights available']

        return highlights
    except Exception as e:
        print("Error occurred while fetching Flipkart highlights:", e)
        return ['No highlights available']


        
def get_amazon_price(name):
    try:
        name1 = name.replace(" ", "-")
        name2 = name.replace(" ", "+")
        amazon_url = f'https://www.amazon.in/{name1}/s?k={name2}'
        
        res = requests.get(amazon_url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        if soup.select('.a-color-base.a-text-normal'):
            amazon_price = soup.select('.a-price-whole')[0].getText().strip()
            return amazon_price
        else:
            amazon_price = '0'

    except Exception as e:
        print("Error occurred while fetching data from Amazon:", e)
        return '0'


def get_amazon_link(name):
    try:
        name1 = name.replace(" ", "-")
        name2 = name.replace(" ", "+")
        amazon_url = f'https://www.amazon.in/{name1}/s?k={name2}'
        return amazon_url
    except Exception as e:
        print("Error occurred while fetching Amazon link:", e)
        return ''


def get_amazon_rating(name):
    try:
        name1 = name.replace(" ", "-")
        name2 = name.replace(" ", "+")
        amazon_url = f'https://www.amazon.in/{name1}/s?k={name2}'
        
        res = requests.get(amazon_url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        # Logic to scrape Amazon ratings
        if soup.select('.a-icon-alt'):
            amazon_rating = soup.select('.a-icon-alt')[0].getText().strip()
            amazon_rating= amazon_rating.replace("out of 5 stars."," ")
        else:
            amazon_rating = 'Not available'

        return amazon_rating
    except Exception as e:
        print("Error occurred while fetching Amazon ratings:", e)
        return '0'
