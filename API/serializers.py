##this implements a custom CSV serializer method
##Resources in API_resources.py can import this to override the default serializer class
##by including serializer=CSVSerializer() in the Meta class


import csv
import StringIO
from tastypie.serializers import Serializer


class CSVSerializer(Serializer):
    formats = ['json', 'jsonp', 'xml', 'yaml', 'html', 'plist', 'csv']
    content_types = {
        'json': 'application/json',
        'jsonp': 'text/javascript',
        'xml': 'application/xml',
        'yaml': 'text/yaml',
        'html': 'text/html',
        'plist': 'application/x-plist',
        'csv': 'text/csv',
    }

    def to_csv(self, data, options=None):
        options = options or {}
        data = self.to_simple(data, options)

        raw_data = StringIO.StringIO()
        first = True

        if "meta" in data.keys():#if multiple objects are returned
            objects = data.get("objects")

            for value in objects:
                test = {}
                self.flatten(value, test)
                if first:
                    writer = csv.DictWriter(raw_data, test.keys(), quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
                    writer.writeheader()
                    writer.writerow(test)
                    first=False
                else:
                    writer.writerow(test)
        else:
            test = {}
            self.flatten(data, test)
            if first:
                writer = csv.DictWriter(raw_data, test.keys(), quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
                writer.writeheader()
                writer.writerow(test)
                first=False
            else:
                writer.writerow(test)

        CSVContent=raw_data.getvalue()
        return CSVContent

    #method to be applied recursively to flatten any dictionaries that get returned from related objects
    def flatten(self, data, odict = {}):
        if isinstance(data, list):
            for value in data:
                self.flatten(value, odict)
        elif isinstance(data, dict):
            for (key, value) in data.items():
                if not isinstance(value, (dict, list)):
                    odict[key] = value
                else:
                    self.flatten(value, odict)

    #we don't use this because this is a GET only api
    def from_csv(self, content):
        raw_data = StringIO.StringIO(content)
        data = []
        # Untested, so this might not work exactly right.
        for item in csv.DictReader(raw_data):
            data.append(item)
        return data