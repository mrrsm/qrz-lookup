import configparser
import csv
from qrzlib import QRZ

def getInfo(callsign) -> QRZ:
    try:
        qrz.get_call(callsign)
        return qrz
    except QRZ.NotFound as err:
        print(err)

config = configparser.ConfigParser()
config.read('credentials.ini')

qrz = QRZ()
qrz.authenticate(config['qrz']['username'], config['qrz']['password'])

with open("callsigns.txt", "r") as f:
    callsigns = f.readlines()

with open('output.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = qrz._xml_keys)
    writer.writeheader()
    for callsign in callsigns:
        try:
            info = getInfo(callsign.strip()).to_dict()
            if "_DBMCache_expire_" in info:
                del(info["_DBMCache_expire_"])
            writer.writerow(info)
        except:
            print(f'Error with callsign {callsign}')
            print(info)
            break