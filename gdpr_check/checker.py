from geolite2 import geolite2
import geoip2.database

# source: https://gist.github.com/henrik/1688572
# info: https://planit.legal/blog/en/the-applicability-of-the-gdpr-within-the-eea/
GDPR_COUNTRIES = (
    # EU countries
    "at","be","bg","hr","cy","cz","dk","ee","fi","fr",
    "de","gr","hu","ie","it","lv","lt","lu","mt","nl",
    "pl","pt","ro","sk","si","es","se",

    # EFTA countries
    "is", "li", "no", "ch",

    # maybe not much longer lol
    "gb",
)

class Checker:
    def __init__(self, database_path=None):
        """Return a new checker instance.

        By default it uses the bundled GeoLite2 database.
        :param database_path: path to MaxMind GeoIP database on disk.
        """
        if database_path:
            self.db = geoip2.database.Reader(database_path)
        else:
            # use geolite2
            self.db = geolite2.reader()

    def is_gdpr_resident_ip(self, ip):
        """Check to see if `ip` is in the list of GDPR-covered countries.

        :returns: False if not in EU/EFTA countries. Returns True if detected as being in EU/EFTA. Returns None if unable to determine country of origin.
        """
        if not ip:
            return None  # your problem, not mine

        # annoying logic depending on if what sort of GeoIP reader we have.
        # if anyone knows a better way to handle different sorts of DBs, please let me know!
        if hasattr(self.db, 'get'):
            lookup = self.db.get(ip)
            if not lookup:
                return None
            if not 'country' in lookup:
                return None
            country = lookup['country']
            if 'is_in_european_union' in country and country['is_in_european_union']:
                return True
            if not 'iso_code' in country:
                return None
            cc_iso = country['iso_code']
            return self.is_gdpr_cc(cc_iso)

        country = None
        try:
            country = self.db.city(ip).country
        except TypeError:
            # okay.. try country
            country = self.db.country(ip).country

        if not country:
            # oh well... what to do?
            return None

        if hasattr(country, 'is_in_european_union') and country.is_in_european_union:
            return True

        cc_iso = country.iso_code
        if not cc_iso:
            return None

        return self.is_gdpr_cc(cc_iso)

    def is_gdpr_cc(self, cc_iso):
        return cc_iso.lower() in GDPR_COUNTRIES
