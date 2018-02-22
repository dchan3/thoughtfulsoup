class Counter(object):
    def __init__(self, destination, from_last):
        self.from_last = from_last
        self.destination = destination if destination is not None else 1

    def nth_child_of_type(self, tag, tags, fil):
        if fil:
            return len(tags) >= self.destination and tag == tags[-1 * self.destination if self.from_last else self.destination - 1]
        else:
            tha_list = list(node for node in list(tags) if node != u'\n')
            return len(tha_list) >= self.destination and tag == tha_list[self.destination - 1]


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
