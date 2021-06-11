import json

from datetime import date, datetime
from django.http import HttpResponse


class ReturnResultUtil:
    is_success = True
    message = None
    data = None

    def success(self):
        return self.is_success

    def result(self, is_success: bool = True, message: str = None, data=None):
        self.is_success = is_success
        self.message = message
        self.data = data
        result = {
            "status": is_success,
            "message": message,
            "data": data
        }
        return result

    def http_result(self, status: int = 200, message: str = None, data=None):
        result = {
            "status": status,
            "message": message,
            "data": data
        }
        try:
            result = json.dumps(result)
        except TypeError as e:
            result = json.dumps(result, cls=DateEncoder)
        return HttpResponse(result)


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)
