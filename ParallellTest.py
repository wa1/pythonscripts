import requests
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
import time

urls = [
  'http://www.python.org', 
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
  'http://planet.python.org/',
  'https://wiki.python.org/moin/LocalUserGroups',
  'http://www.python.org/psf/',
  'http://docs.python.org/devguide/',
  'http://www.python.org/community/awards/'
  # etc.. 
  ]

t0 = time.time()

#responses = []
#for url in urls:
#    responses.append(requests.get(url))


## Make the Pool of workers
#pool = ThreadPool(12) 
## Open the urls in their own threads
## and return the results
#results = pool.map(requests.get, urls)
##close the pool and wait for the work to finish 
#pool.close() 
#pool.join() 

# Make the Pool of workers
pool = Pool() 
# Open the urls in their own threads
# and return the results
results = pool.map(requests.get, urls)
#close the pool and wait for the work to finish 
pool.close() 
pool.join() 

t1 = time.time()

print(t1 - t0)