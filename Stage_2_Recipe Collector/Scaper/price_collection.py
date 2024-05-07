from bs4 import BeautifulSoup
import requests

def find_price_on_instacart(product_name):
    search_url = f"https://www.instacart.com/search?q={product_name}"
    
    try:
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Assuming you're looking for the first result
        first_result = soup.find("div", class_="product-card")
        product_title = first_result.find("div", class_="product-title").text.strip()
        product_price = first_result.find("div", class_="product-price").text.strip()
        
        return f"Product: {product_title}, Price: {product_price}"
    except Exception as e:
        print(f"Error: {e}")
        return None

print(find_price_on_instacart("eggs"))
