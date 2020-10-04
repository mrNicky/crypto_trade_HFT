# crypto_trade_hft
Just simulation of how to make money in crypto world with 1000 dollars


## INSTALL
pip3 install -r requirements.txt

## RUN
python3 main.py YOUR_CODE_COIN


You can find code crypto here: 
https://coinmarketcap.com/

9dollars in 3 hours, but we have to wait, and test. According to the average commission brokers (0.1%) like bittrex, we define 0.25% rate for selling, so we make 0.15% by each trade, if we increase this rate, we make less trades, in the other hand, if we descrease this rate, we make more trades but with less benefits.
To improvement this code we can define the optimal rate depend on crypto type, volume, volatily...More volatily is good because we can increase our rate !


## Some improvements: 

- I use free api with limits, but you can subscribe a Premium API...

- Every second, we check the price with this code, one improvement is to use kafka streaming and scala or python to perform transactions with milliseconds instead of seconds

- Use leverage with stop loss

- Make somes predictions

- Add news data source that can impact coin price (news, twitter...)
