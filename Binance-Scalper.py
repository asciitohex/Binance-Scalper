from binance.client import Client
import os
import time
import configparser

def main():
    config = configparser.ConfigParser()
    config.read('c:\creds\creds.conf')
    client = Client(config['binance']['api_key'], config['binance']['api_secret'])
    clear()
    selected_order = select_open_order(client)

def clear():
    try:
        os.system('cls')
    except:
        os.system('clear')

def get_asset_details(client, symbol):
    asset_details = []
    info = client.get_symbol_info(symbol)
    asset_details.append(info["baseAsset"])
    asset_details.append(info["baseAssetPrecision"])
    asset_details.append(info["quoteAsset"])
    asset_details.append(info["quotePrecision"])
    asset_details.append(info["filters"][2]["stepSize"])
    return asset_details

def show_open_orders(client):
    order_details = []
    orders = client.get_open_orders()
    print("Showing open orders.")
    print("")
    for order in orders:
        print("Order ID: " + str(order["orderId"]))
        print("Asset Pair: " + order["symbol"])
        print("Order Type: " + order["side"])
        print("Quantity: " + (str(order["origQty"])))
        print("Executed Quantity: " + (str(order["executedQty"])))
        print("Price: " + str(order["price"]))
        print("")

def select_open_order(client):
    show_open_orders(client)
    open_order_id = input("Which order ID should this action be set to? ")
    open_order_symbol = input("Which symbol is the transaction? ")  
    open_order_symbol_upper = open_order_symbol.upper()
    while len(open_order_id) <= 7:
        print("Invalid Order ID")
        open_order_id = input("Which order ID should this action be set to? ")
    orders = client.get_open_orders()
    for order in orders:
        if int(order["orderId"]) == int(open_order_id):
            symbol_details = get_asset_details(client, open_order_symbol_upper)
            status = order_status(client, open_order_symbol_upper, open_order_id)
            next_order = configure_next_order(status[2])
            print("")
            while status != "FILLED":
                print("")
                print("Waiting for the current order to fill.")
                print("")
                time.sleep(60)
                status = order_status(open_order_symbol_upper, open_order_id)
            if next_order[0] == "BUY":
                buy_order(client, open_order_symbol_upper, next_order[1])
            elif next_order[0] == "SELL":
                sell_order(client, open_order_symbol_upper, next_order[1])
        else:
            print("not matched")

def order_status(client, symbol, orderId):
    clear()
    order_status = client.get_order(symbol=symbol, orderId=orderId)
    status = []
    print("Checking order status")
    print("")
    print("Order ID: " + str(order_status["orderId"]))
    print("Asset Pair: " + order_status["symbol"])
    print("Order Type: " + order_status["side"])
    print("Quantity: " + (str(order_status["origQty"])))
    print("Executed Quantity: " + (str(order_status["executedQty"])))
    print("Price: " + str(order_status["price"]))
    print("Status: " + order_status["status"])
    status.append(order_status["status"])
    status.append(order_status["symbol"])
    status.append(order_status["side"])
    return status

def configure_next_order(side):
    next_order = []
    print("")
    if side == "BUY":
        next_order_type = "SELL"
        print("Current order type is " + side + ", next order type will be " + next_order_type + ".")
    elif side == "SELL":
        next_order_type = "BUY"
        print("Current order type is " + side + ", next order type will be " + next_order_type + ".")
    print("Enter the price for the next " + next_order_type + " order.")
    next_price = input("Price: ")
    next_order.append(next_order_type)
    next_order.append(next_price)
    return next_order

def buy_order(client, symbol, price):
    asset_details = get_asset_details(client, symbol)
    base_balance = client.get_asset_balance(asset=asset_details[0])
    quote_balance = client.get_asset_balance(asset=asset_details[2])
    step_size = asset_details[4]

    if float(step_size) == 1.00000000:
        str_to_float = float(quote_balance["free"])
        quantity = float(str_to_float) / float(price)
        quantity_to_int = int(quantity)
    elif float(step_size) < 1.00000000:
        step_size_split = step_size.split('.')
        step_size_split[1]
        step_size_cleaned = step_size_split[1].rstrip('0')
        step_size_length = len(step_size_cleaned) + 2
        #
        str_to_float = float(quote_balance["free"])
        quantity = float(str_to_float) / float(price)
        back_to_str = str(quantity)
        quantity_cleaned = str(back_to_str[:step_size_length])

    order = client.order_limit_buy(symbol=symbol, quantity=quantity_cleaned, price=price)
    print(order)

def sell_order(client, symbol, price):
    asset_details = get_asset_details(client, symbol)
    base_balance = client.get_asset_balance(asset=asset_details[0])
    quote_balance = client.get_asset_balance(asset=asset_details[2])
    step_size = asset_details[4]

    if float(step_size) == 1.00000000:
        str_to_float = float(base_balance["free"])
        quantity = int(str_to_float)
    elif float(step_size) < 1.00000000:
        step_size_split = step_size.split('.')
        step_size_split[1]
        step_size_cleaned = step_size_split[1].rstrip('0')
        step_size_length = len(step_size_cleaned) + 2
        #
        str_to_float = base_balance["free"]
        str_to_float_cleaned = str(str_to_float[:step_size_length])
        quantity =  str(str_to_float[:step_size_length])
    order = client.order_limit_sell(symbol=symbol, quantity=quantity, price=price)
    print(order)

if __name__ == "__main__":
    main()