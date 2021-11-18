# 4Chan-Media-Downloader

```
  ,---. ,-----.,--.
 /    |'  .--./|  ,---.  ,--,--.,--,--,
/  '  ||  |    |  .-.  |' ,-.  ||      \
'--|  |'  '--'\|  | |  |\ '-'  ||  ||  |
   `--' `-----'`--' `--' `--`--'`--''--'
,--.   ,--.          ,--.,--.
|   `.'   | ,---.  ,-|  |`--' ,--,--.
|  |'.'|  || .-. :' .-. |,--.' ,-.  |
|  |   |  |\   --.\ `-' ||  |\ '-'  |
`--'   `--' `----' `---' `--' `--`--'
,------.                            ,--.                  ,--.
|  .-.  \  ,---. ,--.   ,--.,--,--, |  | ,---.  ,--,--. ,-|  | ,---. ,--.--.
|  |  \  :| .-. ||  |.'.|  ||      \|  || .-. |' ,-.  |' .-. || .-. :|  .--'
|  '--'  /' '-' '|   .'.   ||  ||  ||  |' '-' '\ '-'  |\ `-' |\   --.|  |
`-------'  `---' '--'   '--'`--''--'`--' `---'  `--`--' `---'  `----'`--'
```

---

## What is it?

It's a great image/video scraper for [4chan](https://4chan.org/) using multiple threads

---

## How does it work?

You make a watchlist file with the urls for the 4chan threads you want to monitor, and the program downloads all the media files of those active threads

---

## Setting it up

You need to download `config.json` and `Downloader.py` and run `Downloader.py` with python 3.x.x obviously. It will make a watchlist file, paste your 4chan thread urls into it and, leave it alone the program will download all the media files till the thread dies

---

## Configuring

`config.json` is the configuration file for this program

---

```json
{
    "WatchList": {
        "File": "watchlist.txt",
        "IntervalSeconds": 150
    },
    "Download": {
        "Path": "Downloads"
    },
    "KeepAlive": {
        "Enabled": false,
        "IntervalSeconds": 300
    }
}
```

---

### WatchList

| Options         | Function                                           | Default       |
| :-------------- | :------------------------------------------------- | :------------ |
| File            | Name of the watchlist file                         | watchlist.txt |
| IntervalSeconds | Amount of seconds between updates of the watchlist | 150           |

<br>

### Download

| Option | Function                         | Default   |
| :----- | :------------------------------- | :-------- |
| Path   | Directory where files get stored | Downloads |

<br>

### KeepAlive

| Option          | Function                                                           | Default |
| :-------------- | :----------------------------------------------------------------- | :------ |
| Enabled         | Directory where files get stored                                   | True    |
| IntervalSeconds | Interval between checks if there are new files uploaded on threads | 300     |

---
