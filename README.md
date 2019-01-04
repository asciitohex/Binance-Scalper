You can find me on Twitter @Crypto_Watcher_

# Binance-Scalper
This script was written with Python v3 and utilizes the python-binance module.  The script was written as a scalping helper which immedietely places an additional order once the current order executes.  When running the scalping tool it will have you select an open order, then configure parameters for the next order.  Once set it will wait for the selected open order to close and then place an order with the configured parameters.  After it creates the "next" order it will send an email notification then close.
<br>
![Scalp1](images/scalp1.jpg?raw=true "Scalp1") <br>
![Scalp2](images/scalp2.jpg?raw=true "Scalp2")

Thanks to sammchardy for writtign the Binance API wrappers in Python!<br>
https://github.com/sammchardy/python-binance
<br>
pip install python-binance
<br>
To use this tool you will need a set of API keys from Binance and they have to be passed into the Binance client.
<br>
The way this script does that is with a *.conf file sitting on the disk as shown below.  
<br>
if __name__ == "__main__":<br>
    config = configparser.ConfigParser()<br>
    config.read('c:\creds\creds.conf')<br>
    main_menu(config)<br>
<br>

You would need to also create a file on disk with the API creds if you took this pattern of passing in API keys.
<br>
Example of the conf file<br>

[binance]
api_key: 123456789123456789123456789123456789123456789<br>
api_secret: 123456789123456789123456789123456789123456789123456789<br>
<br>

** Use this tool at your own risk! I am not resposible for any financial losses as a result of using this script.
<br>
If you find this tool or function patterns useful then donations are always welcome!

BTC: bc1qvga6sudluhcdru4rg5xyvl7s2ywxtnyffwcwdt<br>
LTC: LKNbQmEqE5k9e9RqfkDsoPzKcFDjPSHyFy