from pulsar import Function
from skmultiflow.bayes import NaiveBayes

import json
import numpy as np

class Agrawal(Function):
    model = None

    def __init__(self):
        self.model = NaiveBayes()

    def process(self, input, context):
        logger = context.get_logger()

        context.record_metric('predict-count', 1)

        arr = json.loads(input)

        X = np.array(arr['X'])

        arr['P'] = self.model.predict(arr['X']).tolist()

        if 'Y' in arr:
            Y = np.array(arr['Y'])

            if Y == arr['P']:
                context.record_metric('predict-count-success', 1)
            else:
                context.record_metric('predict-count-failure', 1)

            self.model.partial_fit(X, Y)

        if context.get_metrics()['user_metric_predict-count-success_count'] > 0:
            logger.info('success rate: {0}'.format((context.get_metrics()['user_metric_predict-count-success_count'] / context.get_metrics()['user_metric_predict-count_count']) * 100))
        if context.get_metrics()['user_metric_predict-count-failure_count'] > 0:
            logger.info('failure rate: {0}'.format((context.get_metrics()['user_metric_predict-count-failure_count'] / context.get_metrics()['user_metric_predict-count_count']) * 100))

        return json.dumps(arr)
