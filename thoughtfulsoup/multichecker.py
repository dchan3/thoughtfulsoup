from thoughtfulsoup.counter import Counter

class MultiChecker(object):
    def __init__(self, lambdas, is_not):
        self.lambdas = lambdas
        self.is_not = is_not

    def do_some_checking(self, tag, tags, tags_f):
        return False not in [self.lambdas[n](tag, tags, tags_f) if self.is_not else (not self.lambdas[n](tag, tags, tags_f)) for n in range(1, (len(self.lambdas)))]
