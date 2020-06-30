# Apache Pulsar Python Functions

The purpose of this repository is to help facilitate creating Pulsar Functions in Python.

## Requirements

- Python 3.7 (2.x will require some modification for existing functions that are written in 3.7)
- Docker
- zip
- Java 8

## Getting started

Run Apache Pulsar locally by following these steps:

1. `wget https://archive.apache.org/dist/pulsar/pulsar-2.6.0/apache-pulsar-2.6.0-bin.tar.gz`

2. `tar xvfz apache-pulsar-2.6.0-bin.tar.gz`

3. `cd apache-pulsar-2.6.0`

4. `bin/pulsar-admin standalone`

### Function Example

To make this as simple as possible, the existing function `./functions/format-phone-number` is used as a template function.

Once you create a new function, make sure you update all references in the commands below for the new function name and details.

#### Existing function in `./functions/` folder

1. `cd ~/pulsar-python-functions/functions`

2. ```pip download \
--only-binary :all: \
--platform manylinux1_x86_64 \
--python-version 37 \
--implementation cp \
--abi cp27m -r requirements.txt -d ./format-phone-number/deps```

This downloads and installs the requirements for the function so that everything needed is included.

3. `zip -r name-of-file.zip format-phone-number -x */test/*`

Zip the function folder, ignoring all contents in the test folder.

4. ```bin/pulsar-admin functions localrun \
  --tenant public \
  --namespace default \
  --py /path/to/pulsar-python-functions/functions/test-python-library.zip \
  --classname TestEtl.TestEtl \
  --inputs persistent://public/default/in \
  --output persistent://public/default/out \
  --log-topic persistent://public/default/log```

Runs the function in localmode on the host computer allowing quick iterations and debugging.

Pay special attention to the path of the python file in `--py` to make sure it is valid, and the value of `--classname` follows the format of `filename.classname`

5. Install testing requirements: `pip install -r format-phone-number/test/requirements.txt`

6. Start consumer: `python format-phone-number/test/test-consumer.py`

Individual python script as a consumer created to allow flexibility editing the consumer.

7. Start log consumer: `python format-phone-number/test/test-log-consumer.py`

8. Start producer: `python format-phone-number/test/test-producer.py`

Individual python script as a producer created to allow flexibility editing the producer.

#### New functions

1. `cd ~/pulsar-python-functions/functions`

2. `cp -rf format-phone-number new-function-folder`

Make modifications to the python class in `new-function-folder/src/` and rename as needed, then follow the instructions for an existing function above.

## Notes

- As of 2.6.0, Functions written in Python do not support Schemas, even though the Python client does. Due to this, sending JSON in the messages is recommended.