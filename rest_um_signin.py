import boto3
import json

from util.util import Util

lambdaClient = boto3.client('lambda')


def lambda_handler(event, context):
    util1 = Util()
    print(util1.get_current_time_utc())
