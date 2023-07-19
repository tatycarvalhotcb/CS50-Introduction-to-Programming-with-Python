import json
import requests
import sys

def check_argv():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif sys.argv[1]:
        argv = sys.argv[1]
        try:
            float_argv = float(argv)
            return float_argv
        except ValueError:
            sys.exit("Command-line argument is not a number")


def bitcoin_price_usd():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        bitcoin_usd_price = o["bpi"]["USD"]["rate_float"]
        amound = check_argv()
        if amound:
            converted_price = amound * bitcoin_usd_price
            print(f"${converted_price:,.4f}")
    except requests.RequestException:
        pass

bitcoin_price_usd()