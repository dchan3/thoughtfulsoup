from thoughtfulsoup.a_n_plus_b import AnPlusB

class Counter(object):
    def __init__(self, destination, from_last):
        self.from_last = from_last
        self.destination = destination if destination is not None else 1

    def nth_child_of_type(self, tag, tags, tags_f, fil):
        tha_list = list(node for node in list(tags_f if fil else tags) if node != u'\n')
        if not isinstance(self.destination, AnPlusB):
            if fil:
                return len(tha_list) >= self.destination and tag == tha_list[-1 * self.destination if self.from_last else self.destination - 1]
            else:
                return len(tha_list) >= self.destination and tag == tha_list[self.destination - 1]
        else:
            if fil:
                return (tha_list.index(tag) + 1 in self.destination.seq(len(tha_list))) or (tha_list[::-1].find(tag) in self.destination.seq(len(tha_list)))
                tha_list[::-1]
            else:
                return tha_list.index(tag) + 1 in self.destination.seq(len(tha_list))
