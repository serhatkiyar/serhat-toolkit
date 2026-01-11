import requests
import sys

def get_price(symbol):
    pair = f"{symbol.upper()}USDT"
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={pair}"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            print(f"Hata: {symbol} bulunamadı veya sembol yanlış.")
            return

        data = response.json()
        price = float(data['price'])

        print(f"{symbol.upper()}: ${price:,.2f}")

    except Exception as e:
        print(f"Bir hata oluştu {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
        get_price(user_input)
    else:
        print("Lütfem bir coin sembolü girin. Örnek: crypto.py ETH")