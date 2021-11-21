# Imports
from json import load
from time import sleep
from threading import Thread
from datetime import datetime
from os import getcwd, makedirs
from os.path import isdir, isfile
from urllib.error import HTTPError
from logging import log, basicConfig, INFO
from re import compile as recompile, escape, findall
from urllib.request import urlopen, Request, urlretrieve


# Functions
def log(level, 
        message):
    print(message)
    log(level, message)

def read_config(config_file):
    # Open the config file
    file = open(config_file)
    data, config = load(file), []
    file.close()


    # Loops over values in the config file
    x_index = -1
    for x in data.values():
        x_index += 1
        y_index = -1
        item = [list(data.keys())[x_index]]
        for y in x.values():
            y_index += 1
            name, value = [list(x.keys())[y_index]], [y]
            name.append(value)
            item.append(name)
        config.append(item)
    

    # Returns all the found configuration 
    return config

def downloader(url, download_path, keep_alive_enabled, keep_alive_interval, watch_list_file):
    # Setting up some variables
    _, _, _, board, _, thread = url.split('/')
    _404 = False
    known_urls = []
    

    # Makes path for thread
    path = f'{getcwd()}/{download_path}/{board}/{thread}'
    if not isdir(path):
        makedirs(path)
    

    # Main download loop
    while True:
        
        
        # Tries to download the html file stops after 10 retries
        for i in range(10 + 1):
            try:
                html = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
                break
            except HTTPError:
                log(INFO, 'page 404\'d')
                if i == 10:
                    _404 = True
                    break
        html_text = html.read().decode(html.info().get_param('charset'))

        
        # Setting some other variables
        pattern = recompile(r'[\/]{2}.+?(?=\/' + escape(board) + r'\/)[^"|s]*')
        matches = findall(pattern, html_text)
        urls, file_extentions = [], ['jpg', 'png', 'webm', 'gif']
        
        
        # Finding file urls and storing them in a list
        for match in matches:
            try:
                if match not in urls:
                    if str(match).split('.')[3] in file_extentions:
                        urls.append(match[:0] + 'https:' + match[0:])
            except IndexError:
                pass
        

        # Download file if url not in known urls
        for file_url in urls:
            if file_url not in known_urls:
                known_urls.append(file_url)
                if not isfile(f'{path}/{file_url.split("/")[-1]}'):
                    urlretrieve(file_url, f'{path}/{file_url.split("/")[-1]}')
                    log(INFO, f'{path}/{file_url.split("/")[-1]}')
                else:
                    log(INFO, 'file exists')
                

        # Stops downloading if thread is dead or keep alive is turned off
        if not keep_alive_enabled or _404:
            temp_file = open(watch_list_file, 'r')
            lines = temp_file.readlines()
            temp_file.close()

            new_file = open(watch_list_file, 'w')
            for line in lines:
                if line.strip('\n') != url:
                    new_file.write(line)
            new_file.close()
            break


        # Waiting for new files in thread
        else:
            log(INFO, 'waiting for new files in thread')
            sleep(keep_alive_interval)


# Making Log File
if not isdir("logs/"):
    makedirs("logs")
date = datetime.now()
basicConfig(filename=f"logs/{date.day}-{date.month}-{date.year}_{date.hour}-{date.minute}-{date.second}.log", # Filename https://stackoverflow.com/questions/9135936/how-do-you-add-datetime-to-a-logfile-name
                    level=INFO, #On what level do you wanna log
                    format="%(asctime)s %(levelname)s: %(message)s", # logging format https://docs.python.org/3/howto/logging.html#changing-the-format-of-displayed-messages
                    datefmt='%d/%m/%Y %H:%M:%S' # Time/Date format https://docs.python.org/3/howto/logging.html#displaying-the-date-time-in-messages
                    )


# Reading configuration file
config = read_config('config.json')


# Setting variables
watch_list_file = config[0][1][1][0]
watch_list_interval_seconds = config[0][2][1][0]
download_path = config[1][1][1][0]
keep_alive_enabled = config[2][1][1][0]
keep_alive_interval = config[2][2][1][0]
known_urls = []


# Making watchlist if not present
if not isfile(watch_list_file):
    open(watch_list_file, 'w').close()


# Main loop
while True:
    opened = True
    tries = 0


    # Reads watchlist
    while opened:
        try:
            urls = []
            with open(watch_list_file, 'r') as watch_list:
                
                
                # Formating urls
                raw_urls = watch_list.readlines()
                for url in raw_urls:
                    url_parts = url.split('/')
                    url, index = '', 0
                    for part in url_parts:
                        index += 1
                        if index <= 6:
                            url += part + '/'
                    urls.append(url[:-1].strip('\n'))
            opened = False
        
        
        # Logs error after trying to open watchlist
        except FileNotFoundError as e:
            tries += 1
            if tries == 666:
                log(INFO, e)
                input('Press a key to close...')
                exit(0)
    

    # Loops over urls if url not known starts a download thread for it
    for url in urls:
        if url not in known_urls:
            known_urls.append(url)
            thread = Thread(target=downloader, args=(url, download_path, keep_alive_enabled, keep_alive_interval, watch_list_file), daemon=True)
            thread.start()


    # Waiting for watchlist update interval to update watchlist
    log(INFO, 'waiting for to watchlist update')
    sleep(watch_list_interval_seconds)
