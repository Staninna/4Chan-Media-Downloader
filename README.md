# 4Chan-Media-Downloader

<div align="center">
    <img width="80%" src="https://i.imgur.com/ifMGs02.png">      
</div>

<br>

<div align="center">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Staninna/4Chan-Media-Downloader">
    <img alt="GitHub Pipenv locked Python version" src="https://img.shields.io/github/pipenv/locked/python-version/Staninna/4Chan-Media-Downloader">
    <img alt="Lines of code" src="https://img.shields.io/tokei/lines/github/Staninna/4Chan-Media-Downloader">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Staninna/4Chan-Media-Downloader">
</div>

<br>

## What is it?

It's a great image/video scraper for [4chan](https://4chan.org/) using multiple threads

## How does it work?

You make a watchlist file with the urls for the 4chan threads you want to monitor, and the program downloads all the media files of those active threads

## Setting it up

You need to download `config.json` and `Downloader.py` and run `Downloader.py` with python 3.x.x obviously. It will make a watchlist file, paste your 4chan thread urls into it and, leave it alone the program will download all the media files till the thread dies

## Configuring

`config.json` is the configuration file for this program

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

### WatchList

| Options         | Function                                           | Default       |
| :-------------- | :------------------------------------------------- | :------------ |
| File            | Name of the watchlist file                         | watchlist.txt |
| IntervalSeconds | Amount of seconds between updates of the watchlist | 150           |

### Download

| Option | Function                         | Default   |
| :----- | :------------------------------- | :-------- |
| Path   | Directory where files get stored | Downloads |

### KeepAlive

| Option          | Function                                                           | Default |
| :-------------- | :----------------------------------------------------------------- | :------ |
| Enabled         | Directory where files get stored                                   | True    |
| IntervalSeconds | Interval between checks if there are new files uploaded on threads | 300     |
