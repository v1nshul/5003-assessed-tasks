
from time import time
from time import sleep
import newspaper
import queue

def retrive_title(urls):  #function to retrive the headlines                                
    result = newspaper.build(urls, memoize_articles=False) #to avoid memory error
    store_headlines = []                                   #store the headlines                                       
    for i in range(1, 6):                                  #get the first 5 headlines      
        art = result.articles[i]                           #get the article     
        art.download()                                     #download the article              
        art.parse()                                        #parse the article        
        if art.title:                                      #if title is not None   
            store_headlines.append(art.title)              #append the title to store_headlines
    return store_headlines                                 #return the store_headlines

def get_headlines(): #function to get the headlines
    URLs = ['http://www.foxnews.com/',                     #list of URLs
            'http://www.cnn.com/',
            'http://www.derspiegel.de/',
            'http://www.bbc.co.uk/',
            'https://theguardian.com',]
    ord_q = queue.Queue()                                 #managing race condition            
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:  #setting up the thread pool
        for url in URLs:                                      #iterating through the URLs                            
            future_obj = executor.submit((retrive_title, url))#retireve_title to thread pool
            ord_q.put(url,future_obj)                         #push url,future_obj to queue
        while not ord_q.empty():                              #while queue not empty
            url, future_obj = ord_q.get()                     #get url,future_obj from queue
            headLines = future_obj.result()                   #get the title from future_obj
            print("\nthe headlines from" + url +"are:\n")     #print the headlines
            for headLine in headLines:                        #iterate through the headlines
                print(headLine)                               #print the headlines
                      
if __name__ == '__main__':
    import timeit
    elapsed_time = timeit.timeit("get_headlines()", setup="from __main__ import get_headlines", number=2)/2             
    print(elapsed_time) 

