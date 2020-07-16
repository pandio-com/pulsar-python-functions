<a href="https://pandio.com"><img src="assets/pandio_225_blue-05.svg" alt="Pandio Logo"></a>

Learn more about Pandio at https://pandio.com

<a href="https://pulsar.apache.org/"><img src="assets/pulsar.svg" alt="Apache Pulsar Logo"></a>

Learn more about Pulsar at https://pulsar.apache.org

# Apache Pulsar Python Functions

The purpose of this repository is to help facilitate creating Pulsar Functions in Python.

## Existing Functions

### Dynamic Routing

Based on the contents of a JSON formatted message, route the message to one or more topics.

Helpful when ingesting on a single topic and needing to process messages differently based on content.

### Format Phone Number

Use Google's excellent [libphonenumber](https://github.com/google/libphonenumber) to format, validate, or manipulate a phone number
in an event.

### Naive Bayes Agrawal

Implementation of the excellent [scikit-multiflow](https://scikit-multiflow.github.io/) to train & predict a Naive Bayes model on a stream
of data. Data generated using an AGRAWAL generator. Watch the log consumer as the accuracy of the model increases with each event produced.

### Python Schema

As of 2.6.0, [Functions written in Python do not support schemas](https://apache-pulsar.slack.com/archives/C5Z4T36F7/p1593488633393600), even though the Python client does. A workaround was developed in this example.

## Requirements

- Python 3.7 (2.x will require some modification for existing functions that are written in 3.7, new functions can be written in either version of Python)
- zip
- tar
- wget
- Java 8
- docker (optional)

## Getting started

Run Apache Pulsar locally by following these steps:

1. `wget https://archive.apache.org/dist/pulsar/pulsar-2.6.0/apache-pulsar-2.6.0-bin.tar.gz`

2. `tar xvfz apache-pulsar-2.6.0-bin.tar.gz`

3. `cd apache-pulsar-2.6.0`

4. `bin/pulsar-admin standalone`

If you'd prefer to use Docker, a `docker-compose.yaml` file is included. Simply run `docker-compose up` in the same folder as the yaml file.

If you use Docker, you still need to perform the steps above to run the Pulsar Functions locally.

### Function Example

To make this as simple as possible, the existing function `./functions/format-phone-number` is used as a template function.

Once you create a new function, make sure you update all references in the commands below for the new function name and details.

For more information on packaging Python functions, see this [Quickstart Guide](https://pulsar.apache.org/docs/fr/functions-quickstart/#package-python-dependencies).

#### Existing function in `./functions/` folder

1. `cd ~/pulsar-python-functions/functions`

2. This downloads and installs the requirements for the function so that everything needed is included in the ZIP file created in the next step.

```
pip download \
--only-binary :all: \
--platform manylinux1_x86_64 \
--python-version 37 \
--implementation cp \
--abi cp27m -r requirements.txt -d deps
```

Alternative depending on the requirements, you may have to research the options needed.

```
pip download \
--only-binary :all: \
--platform manylinux1_x86_64 \
--python-version 37 -r requirements.txt -d deps
```

```
pip download --only-binary :all: -r requirements.txt -d deps
```

3. `zip -r name-of-file.zip format-phone-number -x */test/*`

Zip the function folder, ignoring all contents in the test folder.

4. `mv name-of-file.zip /tmp/`

Move the file to a temporary location, since the next command pollutes the directory of the zip file.

5. Runs the function in localmode on the host computer allowing quick iterations and debugging.

```
bin/pulsar-admin functions localrun \
  --tenant public \
  --namespace default \
  --py /tmp/name-of-file.zip \
  --classname TestEtl.TestEtl \
  --inputs persistent://public/default/in \
  --output persistent://public/default/out \
  --log-topic persistent://public/default/log
```

Pay special attention to the path of the python file in `--py` to make sure it is valid, and the value of `--classname` follows the format of `filename.classname`

This command will also show error information from the uploaded function in the command output. This will be helpful in debugging.

6. Install testing requirements: `pip install -r format-phone-number/test/requirements.txt`

This makes sure the test scripts for your function can operate properly.

7. Start consumer: `python format-phone-number/test/test-consumer.py`

Individual python script as a consumer created to allow flexibility editing the consumer.

8. Start log consumer: `python format-phone-number/test/test-log-consumer.py`

9. Start producer: `python format-phone-number/test/test-producer.py`

Individual python script as a producer created to allow flexibility editing the producer.

#### New functions

1. `cd ~/pulsar-python-functions/functions`

2. `cp -rf format-phone-number new-function-folder`

Make modifications to the python class in `new-function-folder/src/` and rename as needed, then follow the instructions for an existing function above.

## That is it!

You should now be able to easily build and test Apache Pulsar Python Functions!

## Notes

- If the Pulsar function throws an exception, it will be available in the terminal output for the command with `localrun`. Additionally, `raise Exception('Hello world')` can be used inside of the `process` method for quick debugging. Don't forget about having access to the logger as well.

## Future Plans

The next contribution will be around [scikit-multiflow](https://github.com/scikit-multiflow/scikit-multiflow) to demonstrate building a machine learning model iteratively on an event stream.

Ideally all examples found here will make their way into the [Apache Pulsar](https://github.com/apache/pulsar) repository.

## Contributing

All pull requests welcome. Especially interested in example functions to help show what can be done with Pulsar Functions.

## License

Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0