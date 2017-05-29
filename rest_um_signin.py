import boto3
import json

from imports.models.central_system import CentralSystem
from imports.models.installations import Installations
from imports.models.device_state import DeviceState
from boto3.dynamodb.conditions import Key
from imports.models.user import User
from imports.user_level import UserLevel
from imports.constants import Constants
from imports.defaults import Defaults
from imports.response import Response
from imports.table import Table
from lib.cutomjtw import CustomJWT
from util.util import Util

lambdaClient = boto3.client('lambda')


def lambda_handler(event, context):
    util1 = Util()
    print(util1.get_current_time_utc())
