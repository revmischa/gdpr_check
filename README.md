## GDPR Checker

This module is designed to make it easier to look up if a user appears to be a resident covered by the GDPR based on IP address.

This is only a best-effort guess, no guarantee or claim is made that this information will always be accurate or reliable.

## Installation:
`pip install gdpr_check`

## Usage:
```
from gdpr_check import Checker

# default uses bundled GeoLite2 DB:
c = Checker()

# optional: pass path to local maxmind GeoIP2 database
c = Checker('/path/to/GeoLite2-Country_20180501/GeoLite2-Country.mmdb')

# check IPs
c.is_gdpr_resident_ip('162.255.119.253')  # returns True - Czech Republic IP
c.is_gdpr_resident_ip('98.158.84.74')  # returns False - Canadian IP
```
