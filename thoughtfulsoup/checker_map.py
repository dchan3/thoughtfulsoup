from thoughtfulsoup.counter import Counter

ID_CLASS_CHECKER = {
    '#': lambda tag, tok: tag.get('id', None) == tok.split('#', 1)[1],
    '.': lambda tag, tok: set(tok.split('.', 1)[1].split('.')).issubset(tag.get('class', []))
}

PSEUDO_TYPE_CHECKER = lambda pseudo_value: {
    'nth-child': {
        "f": lambda tag, tags: Counter(pseudo_value, False).nth_child_of_type(tag, tags, False),
        "l": False
    },
    'nth-of-type': {
        "f": lambda tag, tags: Counter(pseudo_value, False).nth_child_of_type(tag, tags, True),
        "l": True
    },
    'first-child': {
        "f": lambda tag, tags: Counter(1, False).nth_child_of_type(tag, tags, False),
        "l": False
    },
    'first-of-type': {
        "f": lambda tag, tags: Counter(1, False).nth_child_of_type(tag, tags, True),
        "l": True
    },
    'nth-last-of-type': {
        "f": lambda tag, tags: Counter(pseudo_value, True).nth_child_of_type(tag, tags, True),
        "l": True
    },
    'last-child': {
        "f": lambda tag, tags: Counter(1, True).nth_child_of_type(tag, tags, False),
        "l": False
    },
    'last-of-type': {
        "f": lambda tag, tags: Counter(1, True).nth_child_of_type(tag, tags, True),
        "l": True
    }
}
