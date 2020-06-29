#!/usr/bin/env python3

"""
Grep for "courtesy" in repository content and roughly extract all mentioned names.
If they are not yet included in .all-contributorsrc, names are added with a unicorn
identicon based on a numeric hash of their full name.

USAGE:
Run from the root of the repository:
./tools/nonghcontrib.py
"""

import json
import hashlib
from pathlib import Path
from subprocess import run, PIPE


flatten = lambda l: [item for sublist in l for item in sublist]


def get_ack():
    """
    grep for "courtesy" to find translation contributors in the root of a git
    repository.

    :param path: Str, Path to the root of a git repo
    :return: result: set of str with contributor
    """
    cmd = ["git", "grep", "-i", "courtesy", "--", './*', ':!tools/*']
    # get translators
    log = run(cmd, stdout=PIPE).stdout.decode().split('\n')
    # this a long list, we have to get creative to split it correctly.
    # First: get rid of 'of' and stray ')' before or after names
    names_rough = [l.split('of ')[-1].strip(')').split(', ') for l in log]
    # there sometimes are 'and' or '&'
    better = [[n.split('&') for n in nr] for nr in names_rough]
    even_better = [b.split('and ') for b in flatten(flatten(better))]
    # take care of 'reviewed by', strip the command summary, and return list of
    # unique contributors
    result = set(flatten([eb.split('; reviewed by ') for eb in flatten(even_better) if eb]))

    return result


def unicornify(contributors):
    """
    turn contributor names into hashes for unicornify
    :param contributors: str
    :return: str
    """
    return int(hashlib.md5(contributors.encode('utf-8')).hexdigest(), 16)


def compose_json(contributor):
    return {"name" : contributor,
            "avatar_url" : 'https://unicornify.pictures/avatar/' + str(unicornify(contributor)) + '?s=128',
            "contributions": ["translation"]}


def write_json(contributors, path='./'):
    p = Path(path + '.all-contributorsrc')
    # map of known contributors logins
    mapping = Path(path + '.allcontrib_map.json')
    data = json.load(open(p))
    maps = json.load(open(mapping))
    names = [i['name'] for i in data['contributors']]
    known = [i['name'] for i in maps['known_contributors']]
    for contributor in contributors:
        if contributor not in names and contributor not in known:
            newone = compose_json(contributor)
            data['contributors'].append(newone)

    with open(p, 'w') as outfile:
        json.dump(data, outfile, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    translators = get_ack()
    write_json(translators)