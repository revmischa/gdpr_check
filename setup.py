from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='gdpr_check',
    version='0.6',
    description='Check if a user is covered by GDPR. Compare IP address to list of EEA/EU countries.',
    url='http://github.com/revmischa/gdpr_check',
    author='Mischa Spiegelmock',
    author_email='revmischa@cpan.org',
    license='ABRMS',
    packages=['gdpr_check'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='gdpr eea eu ip check geoip country',
    setup_requires=['setuptools>=38.6.0'],
    install_requires=[
        'maxminddb-geolite2>=2018.308',
        'requests>=2.18.4',
        'geoip2>=2.8.0',
    ]
)
