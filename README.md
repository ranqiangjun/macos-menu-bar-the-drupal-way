# macOS menu bar -- The drupal way

Two examples of utilizing Bitbar to watching changes on Drupal.org

### Two tools

- [Dozer](https://github.com/Mortennn/Dozer) -- Hide status bar icons on macOS
  ![](https://github.com/Mortennn/Dozer/raw/master/Stuff/demo.gif)

- [Bitbar](https://github.com/matryer/bitbar) -- Put anything in your Mac OS X menu bar

---

The two examples are Bitbar plugins actually.

- Python3 is required to get them running

And you should change the Drupal.org credentials in do.5m.py to your own.

```python
# Change your drupal.org credentials here
username = 'YOUR_DRUAP.ORG_ACCOUNT'
password = "YOUR_PASSWORD"
```

- Two python packages are used: beautifulsoup4 and requests

```bash
$ pip3 install beautifulsoup4 requests 
```

Or 

```bash
$ pip3 -r requirements.txt

```

### Extras


- macos-menu-bar-the-drupal-way.mp4 is the demo in mp4 format
- macos-menu-bar-the-drupal-way.gif is converted from macos-menu-bar-the-drupal-way.mp4
- macos-menu-bar-the-drupal-way.md is the soure of the blog post https://jungleran.com/node/75 
