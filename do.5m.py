#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3

import requests
from bs4 import BeautifulSoup

# base64 format Drupalicon
drupalicon = 'iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAACKElEQVQ4T2NkwAEce3fE7b98+zzDgtzLuNQw4pLo3n3jWena80IMzP/UGaZGP8SmDkOzYd364GIfw2Vf/7Gwpa++xsDw+9d/hm/vTzL8+ZCG7goUzf17brxLt1MVvPvuO4PnrHMMTz7+QFgIMuTr61UMcxMjYIJwzUfuvfupJ8XHtuHqa4aCDTcY3n37jd1HH5/NYpiTkA6SBGsWK1p1qTbYUnfJ2ecMJx9+wBUMEPGPzxkYvrxTZFhR+ABic96WfwysbDgDD8W0d48YGL6+W8uwqiyEkSFhdhODsHwtfuugsr++MjC8uc/A8O/vJ4aVpfyMDGkrChh4hfphmgU4WRjiTaQYPnz/w3Dw3nuGB+++Q6RAGt89YjCQFWK4cP8FA8PKUkZGhriZOQyiipNB8iCN96tswTQMNOy8wzBxx3kGA2EGhvogSwYHLRmGksX7f/bGOXFA/Jm/6TcDCwdLgqkUw/xwbRQffPz2i2HDmTtgTfIifGC5ni1nzpX6mhpDNCfN7WfgkyhQEOVjuFBkwcDPAbF54aFrDDsuPWBQlxRkWH/6DsOiTA8GkBqH2iVhF/pSViNCOLh1BwMbp7sAFzuDgYIow4FrT8AGgGwEsUGaHrz+xKAsxl1yd2J6Lzye4e4M74lmYGRsZ2BklAUpTrDTZrjw8BWDgig/w9k7z94cvvYkkWFN2RaYeuxxG9Llw8D8z4WBmfUDw6+fEgx//x9gWF+9Aj06Ac9KxxAHZTm1AAAAAElFTkSuQmCC';

# Change your drupal.org credentials here
username = 'YOUR_DRUAP.ORG_ACCOUNT'
password = "YOUR_PASSWORD"


def form_values(session):
    """
    Combines form values from the login page with user credentials.

    :param session: The Requests session.
    :return: Form values ready for submission or exists if fails.
    """
    response = session.get('https://www.drupal.org/user')
    if response.status_code != 200:
        exit()
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    form_build_id = soup.select('input[name="form_build_id"]')[0]['value']
    form_token = soup.select('input[name="form_token"]')[0]['value']
    form_id = soup.select('input[name="form_id"]')[0]['value']
    return {
        'name': username,
        'pass': password,
        'form_build_id': form_build_id,
        'form_token': form_token,
        'form_id': form_id,
        'op': 'Log in'
    }


def login(session, values):
    """
    Performs login.

    :param session: The Requests session.
    :param values: Form values.
    :return: Nothing or exits if fails.
    """
    response = session.post('https://www.drupal.org/user', data=values)
    if response.status_code != 200:
        exit()


def dashboard_soup(session):
    """
    The BeautifulSoup instance of Dashboard.

    :param session: The Requests session.
    :return: The soup or exits if fails.
    """
    response = session.get('https://www.drupal.org/dashboard')
    if response.status_code != 200:
        exit()
    return BeautifulSoup(response.text, 'html.parser')


def new_count(soup):
    """
    The count of posts/issues which has update(s) or new comments.

    :param soup: The BeautifulSoup instance of Dashboard.
    :return: the count of updated items
    """
    markers = soup.select('#homebox-block-drupalorg_tracker_user .item-list li span.marker')
    return len(markers)


def output_icon(count):
    """
    Display the icon with the count badge or not.

    :param count: The count of new items.
    """
    if count > 0:
        print("{0} | image={1}\n".format(count, drupalicon))
    else:
        print("| image={0}\n".format(drupalicon))


def output_posts(soup):
    """
    Outputs my posts items.

    :param soup: The BeautifulSoup instance of Dashboard.
    """
    items = soup.select('#homebox-block-drupalorg_tracker_user .item-list li')
    for item in items:
        li_soup = BeautifulSoup(item.prettify(), 'html.parser')
        links = li_soup.select('a')
        marker = li_soup.select('.marker')
        link = links[0]
        if len(marker) == 0:
            print("{0} | href=https://www.drupal.org{1} color=blue \n".format(link.text.strip(), link['href']))
        else:
            link_new = links[1]
            print("{0} ({1}) | href=https://www.drupal.org{2} color=blue \n".format(link.text.strip(), link_new.text.strip(), link['href']))


def output_planet(soup):
    """
    Outputs Planet Drupal items.

    :param soup: The BeautifulSoup instance of Dashboard.
    """
    items = soup.select('#homebox-block-aggregator_category-2 .item-list li a')
    for item in items:
        print("{0} | href={1} color=blue \n".format(item.text, item['href']))


def new_section(section_title):
    """
    A new section with a line separator.

    :param section_name: The section title.
    """
    print("---\n{0}".format(section_title))


def main():
    """
    The "main" function
    """
    # Initial the request session.
    session = requests.Session()
    # Login.
    login(session, form_values(session))
    # Let BeautifulSoup start extracting information from the dashboard.
    soup = dashboard_soup(session)

    # Outputs the icon.
    count = new_count(soup)
    output_icon(count)

    # Output my posts section.
    new_section('My posts')
    output_posts(soup)

    # Output Planet Drupal section.
    new_section("Planet Drupal")
    output_planet(soup)


if __name__ == '__main__':
    main()
