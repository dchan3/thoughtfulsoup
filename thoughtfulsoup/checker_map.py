from thoughtfulsoup.counter import Counter

ID_CLASS_CHECKER = {
    '#': lambda tag, tok: tag.get('id', None) == tok.split('#', 1)[1],
    '.': lambda tag, tok: set(tok.split('.', 1)[1].split('.')).issubset(tag.get('class', []))
}

PSEUDO_TYPE_CHECKER = lambda pseudo_value: {
    'nth-child': {
        "f": lambda tag, tags, tags_f: Counter(pseudo_value, False).nth_child_of_type(tag, tags, tags_f, False)
    },
    'nth-of-type': {
        "f": lambda tag, tags, tags_f: Counter(pseudo_value, False).nth_child_of_type(tag, tags, tags_f, True)
    },
    'first-child': {
        "f": lambda tag, tags, tags_f: Counter(1, False).nth_child_of_type(tag, tags, tags_f, False)
    },
    'first-of-type': {
        "f": lambda tag, tags, tags_f: Counter(1, False).nth_child_of_type(tag, tags, tags_f, True)
    },
    'nth-last-of-type': {
        "f": lambda tag, tags, tags_f: Counter(pseudo_value, True).nth_child_of_type(tag, tags, tags_f, True)
    },
    'last-child': {
        "f": lambda tag, tags, tags_f: Counter(1, True).nth_child_of_type(tag, tags, tags_f, False)
    },
    'last-of-type': {
        "f": lambda tag, tags, tags_f: Counter(1, True).nth_child_of_type(tag, tags, tags_f, True)
    }
}
