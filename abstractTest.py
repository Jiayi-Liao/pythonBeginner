import json
import re
from abc import ABCMeta, abstractmethod


class IDataParser(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def parse(selfcls, content): pass


class IDataLoader(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_content(self): pass


class ConfigData(object):
    def __init__(self, loader, parser):
        assert isinstance(loader, IDataLoader) and isinstance(parser, IDataParser)
        self.data = parser.parse(loader.get_content())

    def __getitem__(self, item):
        return self.data.get(item, None)


class JsonParser(IDataParser):
    def parse(cls, content):
        return json.loads(content)


class KvParser(IDataParser):
    def parse(cls, content):
        return dict(re.findall(r'(\w+)\s*=\s*"?([\w\s]+)"?', content))


class S3Storage(IDataLoader):
    def get_content(self):
        return '{ "d1": "s3 d1", "d2": "s3 d2" }'
class FileStorage(IDataLoader):
    def get_content(self):
        return 'd1="file d1", d2="file d2"'


s3_config=ConfigData(S3Storage(), JsonParser())
print s3_config['d1']