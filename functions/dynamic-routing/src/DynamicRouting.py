from pulsar import Function

import json

class DynamicRouting(Function):
    def __init__(self):
        self.click_topic = "persistent://public/default/check-click"
        self.impression_topic = "persistent://public/default/check-impression"

    @staticmethod
    def is_click(item):
        return 'type' in item and item['type'] == 'click'

    @staticmethod
    def is_impression(item):
        return 'type' in item and item['type'] == 'impression'

    def process(self, input, context):
        logger = context.get_logger()
        logger.info("Message Content: {0}".format(input))

        arr = json.loads(input)

        if self.is_click(arr):
            context.publish(self.click_topic, input)
        elif self.is_impression(arr):
            context.publish(self.impression_topic, input)
        else:
            logger.warn("The item {0} is neither a click nor an impression".format(input))
