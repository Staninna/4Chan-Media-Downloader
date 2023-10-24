# 4Chan-Media-Downloader

<div align="center">
    <img width="80%" src="https://i.imgur.com/9fxunds.png">
</div>

<br>

<div align="center">
    <img alt="GitHub code size" src="https://img.shields.io/github/languages/code-size/staninna/4Chan-Media-Downloader">
    <img alt="GitHub Pipenv locked Python version" src="https://img.shields.io/github/pipenv/locked/python-version/Staninna/4Chan-Media-Downloader">
    <img alt="Lines of code" src="https://img.shields.io/tokei/lines/github/Staninna/4Chan-Media-Downloader">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Staninna/4Chan-Media-Downloader">
</div>

<br>

## What is it?

It's a great media scraper for [4chan.org](https://4chan.org/) using multiple threads

## How does it work?

You create a watchlist file with the urls for the 4chan threads you want to monitor, and the program downloads all the media files of those active threads

## Installing

You need to download the latest version from [this link](https://github.com/Staninna/4Chan-Media-Downloader/releases/latest), extract the file and run `Downloader.exe`, Windows will complain about viruses, but it is totally fine, if you really do not trust the program, use `Downloader.py` instead

## Configuring

`config.json` is the configuration file for this program

### `config.json`

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
        "Enabled": true,
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
| Enabled         | Checks if there are new files are uploaded                         | True    |
| IntervalSeconds | Interval between checks if there are new files uploaded on threads | 300     |

## License

This project is licensed under the [MIT License](LICENSE).
