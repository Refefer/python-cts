import os.path
from collections import namedtuple

import ctags

ENTRY_FIELDS = ("name", "file", "pattern", "lineNumber", "kind", "fileScope")
Entry = namedtuple("Entry", ENTRY_FIELDS)
class TagScanner(object):

    def __init__(self, tag_file, base_dir, **opts):
        self.tag_file = tag_file
        self.base_dir = base_dir

    def query(self, query):
        raise NotImplementedError()

    def entry_to_Entry(self, entry):
        ed = dict((f, entry[f]) for f in ENTRY_FIELDS)
        ed['file'] = os.path.abspath(os.path.join(self.base_dir, ed['file']))
        return Entry(**ed)

class FullTagScanner(TagScanner):
    def query(self, query):
        entry = ctags.TagEntry()
        if self.tag_file.first(entry):
            yield self.entry_to_Entry(entry)
            while self.tag_file.next(entry):
                yield self.entry_to_Entry(entry)

class PartialTagScanner(FullTagScanner):
    def __init__(self, tag_file, base_dir, insensitive=False, **opts):
        super(FullTagScanner, self).__init__(tag_file, base_dir)
        self.insensitive=insensitive
        
    def query(self, query):
        if self.insensitive:
            query = query.lower()

        for entry in super(PartialTagScanner, self).query(query):
            tag = entry.name.lower() if self.insensitive else entry.name
            if query in tag: 
                yield entry

class IndexedTagScanner(TagScanner):

    def __init__(self, tag_file, base_dir, prefix=False, insensitive=False, **opts):
        super(IndexedTagScanner, self).__init__(tag_file, base_dir)
        self.prefix = prefix
        self.insensitive = insensitive

    def build_flags(self):
        search_type = ctags.TAG_PARTIALMATCH if self.prefix else ctags.TAG_FULLMATCH
        case = ctags.TAG_IGNORECASE if self.insensitive else ctags.TAG_OBSERVECASE
        return search_type | case

    def query(self, query):
        entry = ctags.TagEntry()
        flags = self.build_flags()

        if self.tag_file.find(entry, query, flags):
            yield self.entry_to_Entry(entry)
            while self.tag_file.findNext(entry):
                yield self.entry_to_Entry(entry)

