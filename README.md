# QRZ bulk lookup

## Requirements

- Python 3

### Setup

You will need to install the python requirements from the `requirements.txt` file
```
pip install -r requirements.txt
```

## How to use

**You must have a QRZ XML data subscription for this script to work**

Put your QRZ credentials into the `credentials.ini` file in the appropriate places.
In the `callsigns.txt` file put all of the callsigns (1 per line) you would like to get data for.

You should be able to run the main.py file and it will create an `output.csv` with all of the data from QRZ on the callsigns you listed in the text file

```
python main.py
```