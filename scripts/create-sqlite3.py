import gzip
import json
import os
import sqlite3
import sys
import xml.etree.ElementTree as ET


FILE = 'latest.xml'
DB = 'latest.db'


def parse_xml(xmlfile):
    tree = ET.parse(xmlfile)

    root = tree.getroot()

    parsed_anime = []

    for anime_item in root.findall('./anime'):
        anime_id = anime_item.attrib['aid']
        anime = {
            'id': anime_id,
            'titles': [],
        }

        for title_item in anime_item.findall('./title'):
            title = {
                'type': title_item.attrib['type'].strip(),
                'language': title_item.attrib['{http://www.w3.org/XML/1998/namespace}lang'].strip(),
                'content': title_item.text.strip(),
            }

            anime['titles'].append(title)

        parsed_anime.append(anime)

    return parsed_anime


def main():
    MAX_XML_SIZE = 16 * 1024 * 1024
    fi = os.stat(FILE)
    if fi.st_size > MAX_XML_SIZE:
        return 1

    with open(FILE, 'r', encoding='utf-8') as f:
        parsed = parse_xml(f)

    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('create table anime_titles (anime_id int, type text, language text, title text)')
    for anime in parsed:
        for anime_title in anime['titles']:
            cur.execute('insert into anime_titles (anime_id, type, language, title) values (?, ?, ?, ?)', (
                anime['id'],
                anime_title['type'],
                anime_title['language'],
                anime_title['content'],
            ))

    conn.commit()
    conn.close()

    return 0


if __name__ == '__main__':
    sys.exit(main())
