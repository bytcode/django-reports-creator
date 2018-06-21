# -*- coding: utf-8 -*-
from os.path import join, dirname
from setuptools import setup, find_packages

version = __import__('reports_creator').__version__

LONG_DESCRIPTION = """
django-reports-creator
===================

django reports integrated with highcharts

    # $ git clone git://github.com/juanpex/django-model-report.git
"""


def long_description():
    try:
        return open(join(dirname(__file__), 'README.md')).read()
    except IOError:
        return LONG_DESCRIPTION


setup(name='django-reports-creator',
      version=version,
      author='Joseph M. Daudi',
      author_email='joseph@bytcode.com',
      description='Django reports Creator integrated with highcharts.',
      license='BSD',
      keywords='django, reports, creator, highcharts, chart, charts',
      url='https://github.com/juanpex/django-reports-creator',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      long_description=long_description(),
      install_requires=[
          'django==1.11',
          'reportlab',
          'html5lib',
          'BeautifulSoup',
          'xhtml2pdf',
          'xlwt==0.7.4',
      ],
      classifiers=[
          'Framework :: Django',
          'Development Status :: 1 - Beta',
          'Topic :: Internet',
          'License :: OSI Approved :: BSD License',
          'Intended Audience :: Developers',
          'Environment :: Web Environment',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.5',
      ]
      )
