import sys
import json
import csv
from flask import Flask

app = Flask(__name__)


@app.route('/less')
def less():
    result = {}
    with open(file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=':', quotechar='"')
        next(reader)
        for row in reader:
            transport, speed = row[4], int(float(row[3]) / float(row[5]))
            if transport not in result:
                result[transport] = [speed, speed]
            else:
                result[transport][0] = min(result[transport][0], speed)
                result[transport][1] = max(result[transport][1], speed)
    return json.dumps(result, indent=4)


if __name__ == '__main__':
    host, port, file = sys.argv[2], sys.argv[4], sys.argv[6]
    app.run(port=port, host=host)
