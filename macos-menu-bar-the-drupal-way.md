![](https://raw.githubusercontent.com/jungleran/macos-menu-bar-the-drupal-way/master/macos-menu-bar-the-drupal-way.gif)

### Pre-requisites

- [Dozer](https://github.com/Mortennn/Dozer) -- Hide status bar icons on macOS
  
![](https://github.com/Mortennn/Dozer/raw/master/Stuff/demo.gif)

- [Bitbar](https://github.com/matryer/bitbar) -- Put anything in your Mac OS X menu bar

### Problem/Motivation

Can't get (real-time) notifications without checking mailbox or logging into drupal.org when

1. An issue having a new comment,
2. A documentation page gets updated
3. A new post is published to Planet Drupal  
4. A new Change Record is published

The 4 cases can be classified into two types:

- **Login required**: 1.2, 3 is available on user's dashboard page, logging in drupal.org is required
- **Login optional**: 4 do not have to login drupal.org, anonymous ussers is able to access Change Record list pages.

### Proposed resolution

Using **Bitbar**, which can put anything in the menu bar by using any programing langage. and put Drupalicon in your macOS's menu bar!

See the demo:  https://github.com/jungleran/macos-menu-bar-the-drupal-way/blob/master/macos-menu-bar-the-drupal-way.gif or https://github.com/jungleran/macos-menu-bar-the-drupal-way/blob/master/macos-menu-bar-the-drupal-way.mp4

**Login required**

Using a HTTP client to visit the target page which contains information we care, further more, the HTTP client handles over the page content to a DOM parser to extract information we want, The last stop is  to output them to a proper format following Bitbar's documentation. and display icon(s) in the menu bar.

An eample: [https://github.com/jungleran/macos-menu-bar-the-drupal-way/blob/master/do.5m.py](https://github.com/jungleran/macos-menu-bar-the-drupal-way/blob/master/do.5m.py)

By changing  your drupal.org credentials in the code, you should be able to see issue/documentation links of  "My posts" and posts of "Planet Drupal" from you drupal.org dashboard page as menu items on your macOs menu bar.

```py
# Change your drupal.org credentials here
username = 'YOUR_DRUAP.ORG_ACCOUNT'
password = "YOUR_PASSWORD"
```

Read the documentation [https://github.com/matryer/bitbar](https://github.com/matryer/bitbar) to get the example working for you.

**Login optional**

The process is similar to the above, just do not have to handle logging in.

See example: [https://github.com/jungleran/macos-menu-bar-the-drupal-way/blob/master/do.cr.15m.py](https://github.com/jungleran/macos-menu-bar-the-drupal-way/blob/master/do.cr.15m.py)

This example pulls Change Records(CR) from https://www.drupal.org/list-changes/drupal, all three types of CR are pulled and display each item as menu item. The three types of CR are:

- Published
- Reviews
- Draft

Also see the README.md in the repo of the examples. [https://github.com/jungleran/macos-menu-bar-the-drupal-way](https://github.com/jungleran/macos-menu-bar-the-drupal-way)

#### Enhancement

As more menus are putting into the menu bar, it's going to get crowded soon. So Here comes **Dozer** to hide some of them when necessary.

**Dozer** is a free and open-source project,  an alternative of Bartender which is a payware.

PS: **Python3** is used to write the examples. 


### Remaining tasks

Get ready your own Drupal menu bar.

### User interface changes

Drupalicon conquers your menu bar.

### Release notes snippet

* Target OS: macOS
* Target readers : Drupal contributors/Core contributors.
* Target goal: Happy Drupaling!

