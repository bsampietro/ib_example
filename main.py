import sys
import logging
import time

from ib_example import IBExample

if __name__ == "__main__":

    """ Creating basic logging file """
    logging.basicConfig(filename='./example.log', level=logging.INFO)
    
    try:
        """ Create an instance of the class connecting to the API and call the request_market_data method for 
            different tickers sent by command line parameters """
        ib_example = IBExample()
        for ticker in sys.argv[1:]:
            ib_example.request_market_data(ticker)

        """ Waiting indefinitely to keep the main thread running and catch the program termination exception """
        time.sleep(1000000000)
    except (KeyboardInterrupt, SystemExit) as e:
        ib_example.clear_all()
        print("Program stopped")
    except:
        ib_example.clear_all()
        raise
