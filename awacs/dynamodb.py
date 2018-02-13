# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon DynamoDB'
prefix = 'dynamodb'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchGetItem = Action('BatchGetItem')
BatchWriteItem = Action('BatchWriteItem')
CreateTable = Action('CreateTable')
DeleteItem = Action('DeleteItem')
DeleteTable = Action('DeleteTable')
DescribeLimits = Action('DescribeLimits')
DescribeReservedCapacity = Action('DescribeReservedCapacity')
DescribeReservedCapacityOfferings = \
    Action('DescribeReservedCapacityOfferings')
DescribeStream = Action('DescribeStream')
DescribeTable = Action('DescribeTable')
DescribeTimeToLive = Action('DescribeTimeToLive')
GetItem = Action('GetItem')
GetRecords = Action('GetRecords')
GetShardIterator = Action('GetShardIterator')
ListStreams = Action('ListStreams')
ListTables = Action('ListTables')
ListTagsOfResource = Action('ListTagsOfResource')
PurchaseReservedCapacityOfferings = \
    Action('PurchaseReservedCapacityOfferings')
PutItem = Action('PutItem')
Query = Action('Query')
Scan = Action('Scan')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateItem = Action('UpdateItem')
UpdateTable = Action('UpdateTable')
UpdateTimeToLive = Action('UpdateTimeToLive')
