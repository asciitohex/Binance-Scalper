# Binance-Scalper
The script was written as a scalping helper which immedietely places an additional order once the current order executes.  When running the scalping tool it will have you select an open order, then configure parameters for the next order.  Once set it will wait for the selected open order to close and then place an additional order with the configured parameters.  After it creates the "next" order it will send an email notification then exit.
<br>
![Scalp1](images/scalp1.jpg?raw=true "Scalp1") <br>
![Scalp2](images/scalp2.jpg?raw=true "Scalp2")


## Getting Started
Clone project or download the zip file.  Once the Binance-Scalper.py file is on your disk, run it as follows:<br>
```
python .\Binance-Scalper.py
```

### Prerequisites
Python API wrappers for Binance

```
pip install python-binance
```
<br>

To use this tool you will need a set of API keys from Binance and they have to be passed into the Binance client.<br>
https://support.binance.com/hc/en-us/articles/360002502072-How-to-create-API
<br><br>
The way this script passes in API creds is with a *.conf file sitting on the disk as shown below.  
```
if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('c:\creds\creds.conf')
    main_menu(config)
```
<br>
You would need to also create a file on disk with the API creds if you took this pattern of passing in API keys.
<br>
Example of the conf file<br>
```
[binance]
api_key: 123456789123456789123456789123456789123456789
api_secret: 123456789123456789123456789123456789123456789123456789
```

## Disclaimer
** Use this tool at your own risk! I am not resposible for any financial losses as a result of using this script.
<br><br>
Scalping works best in ranged based market conditions.  It is important to be able to recognize market conditions prior to using tools such as this.

## Donations
If you find this tool or function patterns useful then donations are always welcome!<br><br>
You can find me on Twitter @Crypto_Watcher_<br><br>

BTC: bc1qvga6sudluhcdru4rg5xyvl7s2ywxtnyffwcwdt<br>
LTC: LKNbQmEqE5k9e9RqfkDsoPzKcFDjPSHyFy

## Acknowledgments
Thanks to sammchardy for writting the Binance API wrappers in Python!<br>
https://github.com/sammchardy/python-binance