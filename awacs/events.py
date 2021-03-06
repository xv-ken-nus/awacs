# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon CloudWatch Events'
prefix = 'events'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


ActivateEventSource = Action('ActivateEventSource')
CreateEventBus = Action('CreateEventBus')
CreatePartnerEventSource = Action('CreatePartnerEventSource')
DeactivateEventSource = Action('DeactivateEventSource')
DeleteEventBus = Action('DeleteEventBus')
DeletePartnerEventSource = Action('DeletePartnerEventSource')
DeleteRule = Action('DeleteRule')
DescribeEventBus = Action('DescribeEventBus')
DescribeEventSource = Action('DescribeEventSource')
DescribePartnerEventSource = Action('DescribePartnerEventSource')
DescribeRule = Action('DescribeRule')
DisableRule = Action('DisableRule')
EnableRule = Action('EnableRule')
ListEventBuses = Action('ListEventBuses')
ListEventSources = Action('ListEventSources')
ListPartnerEventSourceAccounts = Action('ListPartnerEventSourceAccounts')
ListPartnerEventSources = Action('ListPartnerEventSources')
ListRuleNamesByTarget = Action('ListRuleNamesByTarget')
ListRules = Action('ListRules')
ListTagsForResource = Action('ListTagsForResource')
ListTargetsByRule = Action('ListTargetsByRule')
PutEvents = Action('PutEvents')
PutPartnerEvents = Action('PutPartnerEvents')
PutPermission = Action('PutPermission')
PutRule = Action('PutRule')
PutTargets = Action('PutTargets')
RemovePermission = Action('RemovePermission')
RemoveTargets = Action('RemoveTargets')
TagResource = Action('TagResource')
TestEventPattern = Action('TestEventPattern')
UntagResource = Action('UntagResource')
