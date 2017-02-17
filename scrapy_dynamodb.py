import datetime
import boto3


def default_encoder(value):
    if isinstance(value, datetime.datetime):
        return value.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(value, datetime.date):
        return value.strftime('%Y-%m-%d')
    elif isinstance(value, datetime.time):
        return value.strftime('%H:%M:%S')
    else:
        return value


class DynamoDbPipeline(object):

    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name,
                 table_name, encoder=default_encoder):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region_name = region_name
        self.table_name = table_name
        self.encoder = encoder
        self.table = None

    @classmethod
    def from_crawler(cls, crawler):
        aws_access_key_id = crawler.settings['AWS_ACCESS_KEY_ID']
        aws_secret_access_key = crawler.settings['AWS_SECRET_ACCESS_KEY']
        region_name = crawler.settings['DYNAMODB_PIPELINE_REGION_NAME']
        table_name = crawler.settings['DYNAMODB_PIPELINE_TABLE_NAME']
        return cls(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name,
            table_name=table_name
        )

    def open_spider(self, spider):
        db = boto3.resource(
            'dynamodb',
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.region_name,
        )
        self.table = db.Table(self.table_name)

    def close_spider(self, spider):
        self.table = None

    def process_item(self, item, spider):
        self.table.put_item(
            TableName=self.table_name,
            Item={k: self.encoder(v) for k, v in item.items()},
        )
        return item
