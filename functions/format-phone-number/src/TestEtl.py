from pulsar import Function

import phonenumbers, json

class TestEtl(Function):
    def __init__(self):
        pass

    def process(self, input, context):
        arr = json.loads(input)
        z = phonenumbers.parse(arr['phone'], 'US')
        arr['phone'] = phonenumbers.format_number(z, phonenumbers.PhoneNumberFormat.NATIONAL)
        return json.dumps(arr)
