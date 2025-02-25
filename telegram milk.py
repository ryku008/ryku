import requests
from bs4 import BeautifulSoup

# Define Telegram credentials directly (No .env)
TELEGRAM_BOT_TOKEN = "7637899570:AAExAQRkD2nRnGiO2ewqeGPVCflsdT4_icw"
TELEGRAM_CHAT_ID = "-4638545764"  # Ensure this is your correct Chat ID

# Function to send Telegram message
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("✅ Telegram notification sent!")
    else:
        print(f"❌ Failed to send Telegram message: {response.text}")

# Scrape milk price
url = "https://jgsj.jayagrocer.com/products/farm-fresh-pure-fresh-milk-2l-1?_pos=3&_sid=8651fd951&_ss=r"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

try:
    page = requests.get(url, headers=headers, timeout=10)  # Added timeout
    page.raise_for_status()  # Raise error if request fails
    soup = BeautifulSoup(page.content, "html.parser")

    # Find the price
    price_element = soup.find("span", class_="price price--highlight")
    
    if price_element:
        price = price_element.text.strip()
        nprice = float(price.replace("RM", "").replace(",", "").strip())  # Convert to float

        print(f"MILK MILK MILK, NOW ONLY RM{nprice}!")

        # If price drops below 16, send a Telegram alert
        if nprice < 16:
            send_telegram_message(f"🚨 *Price Drop Alert!* 🚨\nMilk price is now RM{nprice}! Buy now! 🥛")
    else:
        print("❌ Price element not found on the website.")

except requests.exceptions.RequestException as e:
    print(f"❌ Failed to fetch page: {e}")
