import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'crawler'                    #capital coz we want to keep it constant
HOMEPAGE = 'http://www.youtube.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)           #work is the job is the job of the threads
        t.daemon = True
        t.start()

# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()

# each link in queue is a new job
def create_jobs():
    for link in (file_to_set(QUEUE_FILE)):
        queue.put(link)
    queue.join()
    crawl()

# check if there are items in the queue if yes crawl
def crawl():
    queue_links = file_to_set(QUEUE_FILE)
    if len(queue_links) > 0:
        print(str(len(queue_links)) + ' items remaining')
        create_jobs()

create_workers()
crawl()
