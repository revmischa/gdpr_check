from setuptools import setup

setup(
    name='gdpr-check',
    version='0.1',
    description='Check if a user is covered by GDPR. Compare IP address to list of EEA/EU countries.',
    url='http://github.com/revmischa/gdpr-check',
    author='Mischa Spiegelmock',
    author_email='revmischa@cpan.org',
    license='ABRMS',
    packages=['gdpr_check'],
    zip_safe=False
)
