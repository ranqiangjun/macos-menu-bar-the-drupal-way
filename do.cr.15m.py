#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3

import requests
from bs4 import BeautifulSoup


def change_record_soup(session, url):
    """
    The BeautifulSoup instance for a change records list page.

    :param session: The Requests session.
    :param url: The URL of change records list page.
    :return: An instance of BeautifulSoup.
    """
    response = session.get(url)
    if response.status_code != 200:
        exit()
    return BeautifulSoup(response.text, 'html.parser')


def output_icon():
    """
    Output the icon, here just a simple string.

    """
    print("CR\n")


def new_section(section_title):
    """
    Outputs a new section with a line separator.

    :param section_name: The title of the section.
    :return:
    """
    print("---\n{0}".format(section_title))


def output_change_records(soup):
    """
    Outputs change record items.

    :soup: BeautifulSoup instance of change records list page.
    """
    items = soup.select('.view-change-records tbody tr')
    for item in items:
        "Cut it down to 5 items per category, or it will be too long"
        if items.index(item) > 5:
            break
        tr_soup = BeautifulSoup(item.prettify(), 'html.parser')
        branch = tr_soup.select('.views-field-field-change-to-branch')[0].text
        date = tr_soup.select('.views-field-created')[0].text
        link = tr_soup.select('.views-field-title a')[0]
        link_text = link.text
        link_href = link['href']
        print("[{0}] {1} ({2}) | href={3} color=blue \n".format(date.strip(), link_text.strip(), branch.strip(), link_href))


def main():
    """
    The "Main" function.
    """
    session = requests.Session()
    try:
        output_icon()

        published_soup = change_record_soup(session, 'https://www.drupal.org/list-changes/drupal')
        drafts_soup = change_record_soup(session, 'https://www.drupal.org/list-changes/drupal/drafts')
        review_soup = change_record_soup(session, 'https://www.drupal.org/list-changes/drupal/review')

        new_section('Published')
        output_change_records(published_soup)

        new_section('Drafts')
        output_change_records(drafts_soup)

        new_section('Review')
        output_change_records(review_soup)

    except:
        print(":bug:")


if __name__ == '__main__':
    main()
