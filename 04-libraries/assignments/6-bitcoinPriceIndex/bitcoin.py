import requests
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    pass
else:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    result = response.json()
    price = result["bpi"]["USD"]["rate_float"]
    total = price * n
    print(f"${total:,.4f}")
