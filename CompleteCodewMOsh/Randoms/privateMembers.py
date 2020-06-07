class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):

        self.__tags[tag.upper()] = self.__tags.get(tag.upper(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.upper(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.upper()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()

cloud.add('Pigga')
cloud.add('pigga')
cloud.add('piggA')

print(cloud.__dict__)
print(cloud._TagCloud__tags)

