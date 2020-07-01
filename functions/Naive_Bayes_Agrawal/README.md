# NaiveBayes

```
bin/pulsar-admin functions localrun \
  --name NaiveBayesExample \
  --tenant public \
  --namespace default \
  --py /tmp/Naive_Bayes_Agrawal.zip \
  --classname NaiveBayesExample.NaiveBayesExample \
  --inputs persistent://public/default/in \
  --output persistent://public/default/out \
  --log-topic persistent://public/default/log
```

`python test/test-consumer.py`

`python test/test-log-consumer.py`

`python test/test-producer.py`