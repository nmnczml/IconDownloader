import urllib.request
from datetime import datetime

class ApiKeyPair:
    ApiKey=""
    Secret=""
    
class AvailableCoins:
    Market=""
    Pair=""    
  


def logMeError(msg):
    
    print(msg)
     
      

def getAvailablePairs():
    try:
          
        with open('coins.txt', 'r') as coinList:
            coins = coinList.readlines()
        
        
        marketPairs = []
        for row in coins:
            inPair= AvailableCoins()  
 
            inPair.Pair = row.strip()
            marketPairs.append(inPair)
        return marketPairs
           
    except BaseException as error:
        logMeError('An exception occurred:'+format(error))   
 
      
        
      

 

import time

import ssl
def jobDef():
    try:
       

        marketPairs = getAvailablePairs()
        ssl._create_default_https_context = ssl._create_unverified_context

        for coin in marketPairs:
            try:
                print(coin.Pair)

            
                # imgURL = "https://static.okex.com/cdn/oksupport/asset/currency/icon/"+symbol.lower()+".png"
                # imgURL = "https://borsa.bitci.com/img/coin/"+coin.Pair.lower()+".png"
               
                imgURL = "https://s3-symbol-logo.tradingview.com/crypto/XTVC"+coin.Pair+".svg"
                urllib.request.urlretrieve(imgURL, './Icons/'+coin.Pair.lower()+'.svg')
                time.sleep(2)
                
                print('completed')

                
            except BaseException as error:
                logMeError('An exception occurred: {}'+format(error))  
        
        
                
    except BaseException as error:
        logMeError('An exception occurred: {}'+format(error))  
        
        
 
if __name__ == '__main__':
    
    jobDef()
  


