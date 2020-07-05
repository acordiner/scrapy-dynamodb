===============
scrapy-dynamodb
===============

scrapy-dynamodb allows you to export your items to a DynamoDB database.

Installation
=============

You can install ``scrapy-dynamodb`` either via the Python Package Index (PyPI)
or from source.

To install using ``pip``,::

    $ pip install scrapy-dynamodb

To install using ``easy_install``,::

    $ easy_install scrapy-dynamodb

Downloading and installing from source
--------------------------------------

Download the latest version of ``scrapy-dynamodb`` from
http://pypi.python.org/pypi/scrapy-dynamodb/

You can install it by doing the following,::

    $ tar xvfz scrapy-dynamodb-0.0.0.tar.gz
    $ cd scrapy-dynamodb-0.0.0
    # python setup.py install # as root

Using the development version
------------------------------

You can clone the git repository by doing the following::

    $ git clone git://github.com/acordiner/scrapy-dynamodb.git
    
Setup
=====================
In ``pipelines.py`` add import statement::   

    from scrapy_dynamodb import DynamoDbPipeline

Using scrapy-dynamodb
=====================

To use ``scrapy-dynamodb`` in your Scrapy project, add
the following line to your ``settings.py``::

    ITEM_PIPELINES = {
        'scraper.pipelines.DynamoDbPipeline': 1,
        # replace scraper with your scrapy project name
    }

    AWS_ACCESS_KEY_ID = '<aws access key id>'
    AWS_SECRET_ACCESS_KEY = '<aws secret access key>'
    DYNAMODB_PIPELINE_REGION_NAME = 'us-east-1'
    DYNAMODB_PIPELINE_TABLE_NAME = 'my_table'
    DYNAMODB_ENDPOINT_URL = '<dynamodb endpoint url>'

That's it!
