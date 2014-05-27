##this implements a custom CSV serializer method
##Resources in API_resources.py can override the default serializer class
##using serializer=CSVSerializer() in the Meta class


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
        writer = csv.writer(raw_data, quotechar="'", quoting=csv.QUOTE_NONNUMERIC)

        if "meta" in data.keys():#if multiple objects are returned
            objects = data.get("objects")
            writer.writerow(objects[0].keys())

            for object in objects:
                test = object.values()
                writer.writerow(test)
        else:
            writer.writerow(data.values())

        CSVContent=raw_data.getvalue()
        return CSVContent

    def from_csv(self, content):
        raw_data = StringIO.StringIO(content)
        data = []
        # Untested, so this might not work exactly right.
        for item in csv.DictReader(raw_data):
            data.append(item)
        return data