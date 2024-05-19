# app.py
from flask import Flask, render_template, request
from scraper import get_flipkart_price, get_flipkart_link, get_flipkart_rating, get_flipkart_highlights, get_flipkart_image ,get_amazon_image,get_amazon_price, get_amazon_link, get_amazon_rating

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product_name = request.form['product_name']
        
        flipkart_price = get_flipkart_price(product_name)
        flipkart_link = get_flipkart_link(product_name)
        flipkart_rating = get_flipkart_rating(product_name)
        flipkart_highlights = get_flipkart_highlights(product_name)

        amazon_price = get_amazon_price(product_name)
        amazon_link = get_amazon_link(product_name)
        amazon_rating = get_amazon_rating(product_name)
        amazon_rating=amazon_rating.replace("out of 5 stars"," ")
        flipkart_image_link = get_flipkart_image(product_name)
        amazon_image_link= get_amazon_image(product_name)

        return render_template('index.html', product_name=product_name,
                                flipkart_price=flipkart_price, flipkart_link=flipkart_link,
                                flipkart_rating=flipkart_rating, flipkart_highlights=flipkart_highlights,
                                amazon_price=amazon_price, amazon_link=amazon_link, amazon_rating=amazon_rating,
                                 amazon_image_link=amazon_image_link,flipkart_image_link=flipkart_image_link)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
