from pulsar import Function

from pulsar.schema import *


class Person(Record):
    name = String()
    phone = String()


class Schema:
    schema = None

    def __init__(self, *args):
        self.schema = args[0]

    def __call__(self, f):
        def wrapped(*args):
            args = list(args)
            args[1] = self.schema.decode(args[1].encode())
            return self.schema.encode(f(*tuple(args))).decode("utf-8")

        return wrapped


class PythonSchema(Function):
    def __init__(self):
        pass

    @Schema(AvroSchema(Person))
    def process(self, input, context):
        logger = context.get_logger()
        logger.info("Message: {0}".format(input))
        logger.info("Name: {0}".format(input.name))

        return input
