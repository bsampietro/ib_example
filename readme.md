# Interactive Brokers Python API example

This program prints live quotes from stock tickers passed as parameters.

To run it: first edit the correct path to the API library on ib_example.py, enable ActiveX and Socket Clients in your TWS software (check: http://interactivebrokers.github.io/tws-api/initial_setup.html#tws), and then execute the main file:

```
python main.py ticker1 ticker2 ... tickerN
```

for example:

```
python main.py SPY QQQ
```

To stop it, use Ctrl + c

Note that this example is only tested on Linux, but it should also work on Windows and macOS.