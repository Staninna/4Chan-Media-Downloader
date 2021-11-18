# Imports
import os
import re
import json
import time
import logging
import datetime
import urllib.request
from threading import Thread


# Functions
def log(level, 
        message):
    print(message)
    logging.log(level, message)

def read_config(config_file):
    file = open(config_file)
    data, config = json.load(file), []
    file.close()
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
    return config

def downloader(url, download_path, keep_alive_enabled, keep_alive_interval, watch_list_file):
    _, _, _, board, _, thread = url.split('/')
    path = f'{os.getcwd()}/{download_path}/{board}/{thread}'
    if not os.path.isdir(path):
        os.makedirs(path)
    
    _404 = False
    known_urls = []
    while True:
        try:
            html = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
        except urllib.error.HTTPError:
            log(logging.INFO, 'page 404\'d')
            _404 = True
        html_text = html.read().decode(html.info().get_param('charset'))

        pattern = re.compile(r'[\/]{2}.+?(?=\/' + re.escape(board) + r'\/)[^"|s]*')
        matches = re.findall(pattern, html_text)

        urls, file_extentions = [], ['jpg', 'png', 'webm', 'gif']
        for match in matches:
            try:
                if match not in urls:
                    if str(match).split('.')[3] in file_extentions:
                        urls.append(match[:0] + 'https:' + match[0:])
            except IndexError:
                pass

        for file_url in urls:
            if file_url not in known_urls:
                known_urls.append(file_url)
                if not os.path.isfile(f'{path}/{file_url.split("/")[-1]}'):
                    urllib.request.urlretrieve(file_url, f'{path}/{file_url.split("/")[-1]}')
                    log(logging.INFO, f'{path}/{file_url.split("/")[-1]}')
                else:
                    log(logging.INFO, 'file exists')
                

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
        else:
            log(logging.INFO, 'waiting for new files in thread')
            time.sleep(keep_alive_interval)

# Making Log File
date = datetime.datetime.now()
logging.basicConfig(filename=f"logs/{date.day}-{date.month}-{date.year}_{date.hour}-{date.minute}-{date.second}.log", # Filename https://stackoverflow.com/questions/9135936/how-do-you-add-datetime-to-a-logfile-name
                    level=logging.INFO, #On what level do you wanna log
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
if not os.path.isfile(watch_list_file):
    open(watch_list_file, 'w').close()


# Main loop
while True:
    opened = True
    tries = 0
    while opened:
        try:
            urls = []
            with open(watch_list_file, 'r') as watch_list:
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
        except FileNotFoundError as e:
            tries += 1
            if tries == 666:
                log(logging.INFO, e)
                input('Press a key to close...')
                exit(0)
    for url in urls:
        if url not in known_urls:
            known_urls.append(url)
            thread = Thread(target=downloader, args=(url, download_path, keep_alive_enabled, keep_alive_interval, watch_list_file), daemon=True)
            thread.start()

    log(logging.INFO, 'waiting for to watchlist update')
    time.sleep(watch_list_interval_seconds)