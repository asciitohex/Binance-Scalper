You can find me on Twitter @Crypto_Watcher_

# Binance-Scalper
This script was written with Python v3 and utilizes the python-binance module.  The script was written as a scalping helper which immedietely places an additional order once the current order executes.  When running the scalping tool it will have you select an open order, then configure parameters for the next order.  Once set it will wait for the selected open order to close and then place an order with the configured parameters.  After it creates the "next" order it will send an email notification then close.

![Scalp1](images/scalp1.jpg?raw=true "Scalp1")
![Scalp2](images/scalp2.jpg?raw=true "Scalp2")

Thanks to sammchardy for writtign the Binance API wrappers in Python!
https://github.com/sammchardy/python-binance

pip install python-binance

To use this tool you will need a set of API keys from Binance and they have to be passed into the Binance client.

The way this script does that is with a *.conf file sitting on the disk as shown below.  

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('c:\creds\creds.conf')
    main_menu(config)


You would need to also create a file on disk with the API creds if you took this pattern of passing in API keys.

Example of the conf file

[binance]
api_key: 123456789123456789123456789123456789123456789
api_secret: 123456789123456789123456789123456789123456789123456789


** Use this tool at your own risk! I am not resposible for any financial losses as a result of using this script.

If you find this tool or function patterns useful then donations are always welcome!

BTC: bc1qvga6sudluhcdru4rg5xyvl7s2ywxtnyffwcwdt
LTC: LKNbQmEqE5k9e9RqfkDsoPzKcFDjPSHyFy