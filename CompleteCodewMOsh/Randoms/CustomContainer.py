class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):

        self.tags[tag.upper()] = self.tags.get(tag.upper(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.upper(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.upper()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud["guava"] = 10
cloud.add('Pigga')
cloud.add('pigga')
cloud.add('piggA')
print(len(cloud))

print(cloud.tags)
