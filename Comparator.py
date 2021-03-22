class Person():

    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    def __eq__(self, other):
        return ((self.last, self.first) == (other.last, other.first))

    def __ne__(self, other):
        return ((self.last, self.first) != (other.last, other.first))

    def __lt__(self, other):
        return ((self.last, self.first) < (other.last, other.first))

    def __le__(self, other):
        return ((self.last, self.first) <= (other.last, other.first))

    def __gt__(self, other):
        return ((self.last, self.first) > (other.last, other.first))

    def __ge__(self, other):
        return ((self.last, self.first) >= (other.last, other.first))

    def __repr__(self):
        return "%s %s" % (self.first, self.last)

def main():
    pass

if __name__ == '__main__':
    main()