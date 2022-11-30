# PoC of chrome extension archive downloader

Download and print download numbers for extensions in the chrome store.

## Usage


```
$ python download_numbers 
```

HTML files will be downloaded to a folder for the specific chrome extension, then every file is read and the number of users reported for each timestamp is printed.


## Using existing files

Alternatively, you may use the `wayback_machine_downloader` gem to download the files and then run `print_wayback_gem.py`:

```
$ wayback_machine_downloader -s -e 'https://chrome.google.com/webstore/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb'
$ python print_wayback_gem.py
```
