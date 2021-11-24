import pickle
from collections import Counter
from itertools import count
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from unidecode import unidecode


def _filter(word, prefix, length):
    return word.upper().startswith(prefix.upper()) and (length is None or len(word) == length)


def _filter_soup(soup, prefix, word_length):
    for word in soup.findAll("span", {"class": "word"}):
        word = unidecode(word.get_text())
        if _filter(word, prefix, word_length):
            yield word


def _end_of_content(soup):
    return not soup.findAll("span", {"class": "word"})


def _lookup(prefix, word_length=None):
    for page in count():
        r = requests.get(f'http://rjecnik.hr/?letter={prefix[0]}&page={page}')
        assert r.ok

        soup = BeautifulSoup(r.content, 'html.parser')
        if _end_of_content(soup):
            return
        yield from _filter_soup(soup, prefix, word_length)


def lookup(prefix, word_length=None):
    dict_cache_path = Path(f'dictionary/{prefix[0].lower()}.pkl')

    if not dict_cache_path.exists():
        dict_cache_path.parent.mkdir(exist_ok=True)
        dict_cache_path.write_bytes(pickle.dumps(list(_lookup(prefix[0]))))

    dict_cache = pickle.loads(dict_cache_path.read_bytes())

    return dict_cache if (len(prefix) == 1 and word_length is None) else \
        [x for x in dict_cache if _filter(x, prefix, word_length)]


def _list_candidates(*, candidates):
    for c in candidates:
        print(c.upper(), end=", ")
    print()


def most_common_next_letter(prefix, word_length=None, k=10):
    hits = lookup(prefix, word_length)
    counter = Counter([x[len(prefix)] for x in hits if len(x) > len(prefix)])
    _list_candidates(candidates=hits)
    return [x[0].upper() for x in counter.most_common(k)]
