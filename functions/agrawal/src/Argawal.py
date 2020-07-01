from pulsar import Function
from skmultiflow.bayes import NaiveBayes

import json, numpy

class Argawal(Function):
    model = None
    def __init__(self):
        self.model = NaiveBayes()

    def process(self, input, context):
        logger = context.get_logger()
        logger.info("Message Content: {0}".format(input))

        context.record_metric('predict-count', 1)

        arr = json.loads(input)

        X = np.array(arr['X'])

        arr['P'] = self.model.predict(arr['X'])

        if 'Y' in arr:
            Y = np.array(arr['Y'])

            if Y == arr['P']:
                context.record_metric('predict-count-success', 1)
            else:
                context.record_metric('predict-count-failure', 1)

            self.model.partial_fit(X, Y)

        return json.dumps(arr)
