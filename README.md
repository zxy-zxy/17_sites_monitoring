# Sites Monitoring Utility
A python script what provides you following information about website:
1. Server correctly responds over HTTP.
2. Domain expires less than in a month.

## Requirements
Python 3 should be already installed.

Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:
```bash
pip install -r requirements.txt
```
For better interaction is recommended to use [virtualenv](https://github.com/pypa/virtualenv).

### Example input
```bash
python check_sites_health.py -filepath sites.txt
```

### Example output
```bash
URL: http://google.com
With domain name : google.com
Respond with status 200 - True
Is domain paid? - True
```

### Project goals
The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)