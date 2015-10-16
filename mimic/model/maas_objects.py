"""
MaaS API data model
"""

from __future__ import unicode_literals

import random
import string
from uuid import uuid4

from characteristic import attributes, Attribute
from six import text_type

from mimic.util.helper import random_hex_generator, random_string

METRIC_TYPE_INTEGER = 'i'
METRIC_TYPE_NUMBER = 'n'
METRIC_TYPE_STRING = 's'


@attributes([Attribute('agent_id', default_value=None),
             Attribute('created_at', instance_of=int),
             Attribute('id',
                       default_factory=(lambda: u'en' + random_hex_generator(4)),
                       instance_of=text_type),
             Attribute('ip_addresses', default_factory=dict, instance_of=dict),
             Attribute('label', default_value=u'', instance_of=text_type),
             Attribute('managed', default_value=False, instance_of=bool),
             Attribute('metadata', default_factory=dict, instance_of=dict),
             Attribute('updated_at', instance_of=int),
             Attribute('uri', default_value=None)])
class Entity(object):
    """
    Models a MaaS Entity.
    """
    USER_SPECIFIABLE_KEYS = ['agent_id',
                             'ip_addresses',
                             'label',
                             'managed',
                             'metadata',
                             'uri']

    def to_json(self):
        """
        Serializes the Entity to a JSON-encodable dict.
        """
        return {'label': self.label,
                'id': self.id,
                'agent_id': self.agent_id,
                'created_at': self.created_at,
                'updated_at': self.updated_at,
                'managed': self.managed,
                'metadata': self.metadata,
                'ip_addresses': self.ip_addresses,
                'uri': self.uri}

    def update(self, **kwargs):
        """
        Updates this Entity.
        """
        for key in Entity.USER_SPECIFIABLE_KEYS:
            if key in kwargs:
                setattr(self, key, kwargs[key])
        self.updated_at = int(1000 * kwargs['clock'].seconds())


@attributes([Attribute('created_at', instance_of=int),
             Attribute('details', default_factory=dict, instance_of=dict),
             Attribute('disabled', default_value=False, instance_of=bool),
             Attribute('entity_id', instance_of=text_type),
             Attribute('id',
                       default_factory=(lambda: u'ch' + random_hex_generator(4)),
                       instance_of=text_type),
             Attribute('label', default_value=u'', instance_of=text_type),
             Attribute('metadata', default_factory=dict, instance_of=dict),
             Attribute('monitoring_zones_poll', default_factory=list, instance_of=list),
             Attribute('period', default_value=60, instance_of=int),
             Attribute('target_alias', default_value=None),
             Attribute('target_hostname', default_value=None),
             Attribute('target_resolver', default_value=None),
             Attribute('timeout', default_value=10, instance_of=int),
             Attribute('type', instance_of=text_type),
             Attribute('updated_at', instance_of=int)])
class Check(object):
    """
    Models a MaaS Check.
    """
    USER_SPECIFIABLE_KEYS = ['details',
                             'disabled',
                             'label',
                             'metadata',
                             'monitoring_zones_poll',
                             'period',
                             'target_alias',
                             'target_hostname',
                             'target_resolver',
                             'timeout',
                             'type']

    def to_json(self):
        """
        Serializes the Check to a JSON-encodable dict.
        """
        return {'label': self.label,
                'id': self.id,
                'type': self.type,
                'monitoring_zones_poll': self.monitoring_zones_poll,
                'created_at': self.created_at,
                'updated_at': self.updated_at,
                'timeout': self.timeout,
                'period': self.period,
                'disabled': self.disabled,
                'metadata': self.metadata,
                'target_alias': self.target_alias,
                'target_resolver': self.target_resolver,
                'target_hostname': self.target_hostname,
                'details': self.details}

    def update(self, **kwargs):
        """
        Updates this Check.
        """
        for key in Check.USER_SPECIFIABLE_KEYS:
            if key in kwargs:
                setattr(self, key, kwargs[key])
        self.updated_at = int(1000 * kwargs['clock'].seconds())


@attributes([Attribute('check_id', instance_of=text_type),
             Attribute('created_at', instance_of=int),
             Attribute('criteria', default_value=u'', instance_of=text_type),
             Attribute('disabled', default_value=False, instance_of=bool),
             Attribute('entity_id', instance_of=text_type),
             Attribute('id',
                       default_factory=(lambda: u'al' + random_hex_generator(4)),
                       instance_of=text_type),
             Attribute('label', default_value=u'', instance_of=text_type),
             Attribute('metadata', default_factory=dict, instance_of=dict),
             Attribute('notification_plan_id', instance_of=text_type),
             Attribute('updated_at', instance_of=int)])
class Alarm(object):
    """
    Models a MaaS Alarm.
    """
    USER_SPECIFIABLE_KEYS = ['check_id',
                             'criteria',
                             'disabled',
                             'label',
                             'metadata',
                             'notification_plan_id']

    def to_json(self):
        """
        Serializes the Alarm to a JSON-encodable dict.
        """
        return {'id': self.id,
                'label': self.label,
                'criteria': self.criteria,
                'check_id': self.check_id,
                'entity_id': self.entity_id,
                'notification_plan_id': self.notification_plan_id,
                'created_at': self.created_at,
                'updated_at': self.updated_at,
                'disabled': self.disabled,
                'metadata': self.metadata}

    def update(self, **kwargs):
        """
        Updates this Alarm.
        """
        for key in Alarm.USER_SPECIFIABLE_KEYS:
            if key in kwargs:
                setattr(self, key, kwargs[key])
        self.updated_at = int(1000 * kwargs['clock'].seconds())


@attributes([Attribute('created_at', instance_of=int),
             Attribute('details', default_factory=dict, instance_of=dict),
             Attribute('id',
                       default_factory=(lambda: u'nt' + random_hex_generator(4)),
                       instance_of=text_type),
             Attribute('label', default_value=u'', instance_of=text_type),
             Attribute('metadata', default_factory=dict, instance_of=dict),
             Attribute('type', default_value='email', instance_of=text_type),
             Attribute('updated_at', instance_of=int)])
class Notification(object):
    """
    Models a MaaS Notification.
    """
    USER_SPECIFIABLE_KEYS = ['details', 'label', 'metadata', 'type']

    def to_json(self):
        """
        Serializes the Notification to a JSON-encodable dict.
        """
        return {'id': self.id,
                'label': self.label,
                'type': self.type,
                'details': self.details,
                'created_at': self.created_at,
                'updated_at': self.updated_at,
                'metadata': self.metadata}

    def update(self, **kwargs):
        """
        Updates this Notification.
        """
        for key in Notification.USER_SPECIFIABLE_KEYS:
            if key in kwargs:
                setattr(self, key, kwargs[key])
        self.updated_at = int(1000 * kwargs['clock'].seconds())


@attributes([Attribute('created_at', instance_of=int),
             Attribute('critical_state', default_factory=list, instance_of=list),
             Attribute('id',
                       default_factory=(lambda: u'np' + random_hex_generator(4)),
                       instance_of=text_type),
             Attribute('label', default_value=u'', instance_of=text_type),
             Attribute('metadata', default_factory=dict, instance_of=dict),
             Attribute('ok_state', default_factory=list, instance_of=list),
             Attribute('updated_at', instance_of=int),
             Attribute('warning_state', default_factory=list, instance_of=list)])
class NotificationPlan(object):
    """
    Models a MaaS notification plan.
    """
    USER_SPECIFIABLE_KEYS = ['critical_state',
                             'label',
                             'metadata',
                             'ok_state',
                             'warning_state']

    def to_json(self):
        """
        Serializes the Notification Plan to a JSON-encodable dict.
        """
        return {'id': self.id,
                'label': self.label,
                'critical_state': self.critical_state,
                'warning_state': self.warning_state,
                'ok_state': self.ok_state,
                'created_at': self.created_at,
                'updated_at': self.updated_at,
                'metadata': self.metadata}

    def update(self, **kwargs):
        """
        Updates this Notification Plan.
        """
        for key in NotificationPlan.USER_SPECIFIABLE_KEYS:
            if key in kwargs:
                setattr(self, key, kwargs[key])
        self.updated_at = int(1000 * kwargs['clock'].seconds())


@attributes([Attribute('alarms', default_factory=list, instance_of=list),
             Attribute('checks', default_factory=list, instance_of=list),
             Attribute('created_at', instance_of=int),
             Attribute('end_time', default_value=0, instance_of=int),
             Attribute('entities', default_factory=list, instance_of=list),
             Attribute('id',
                       default_factory=(lambda: u'sp' + random_hex_generator(4)),
                       instance_of=text_type),
             Attribute('label', default_value=u'', instance_of=text_type),
             Attribute('notification_plans', default_factory=list, instance_of=list),
             Attribute('start_time', default_value=0, instance_of=int),
             Attribute('updated_at', instance_of=int)])
class Suppression(object):
    """
    Models a MaaS suppression.
    """
    USER_SPECIFIABLE_KEYS = ['alarms',
                             'checks',
                             'end_time',
                             'entities',
                             'label',
                             'notification_plans',
                             'start_time']

    def to_json(self):
        """
        Serializes the Suppression to a JSON-encodable dict.
        """
        return {'id': self.id,
                'label': self.label,
                'start_time': self.start_time,
                'end_time': self.end_time,
                'notification_plans': self.notification_plans,
                'entities': self.entities,
                'checks': self.checks,
                'alarms': self.alarms}

    def update(self, **kwargs):
        """
        Updates this Suppression.
        """
        for key in Suppression.USER_SPECIFIABLE_KEYS:
            if key in kwargs:
                setattr(self, key, kwargs[key])
        self.updated_at = int(1000 * kwargs['clock'].seconds())


@attributes([Attribute('alarm_changelog_id',
                       default_factory=(lambda: unicode(uuid4())),
                       instance_of=text_type),
             Attribute('alarm_id', instance_of=text_type),
             Attribute('alarm_label', instance_of=text_type),
             Attribute('analyzed_by_monitoring_zone_id', default_value=u'mzord', instance_of=text_type),
             Attribute('check_id', instance_of=text_type),
             Attribute('entity_id', instance_of=text_type),
             Attribute('id',
                       default_factory=(lambda: u'as' + random_hex_generator(4)),
                       instance_of=text_type),
             Attribute('previous_state', instance_of=text_type),
             Attribute('state', instance_of=text_type),
             Attribute('status', instance_of=text_type),
             Attribute('timestamp', instance_of=int)])
class AlarmState(object):
    """
    Models a MaaS alarm state.
    """
    def brief_json(self):
        """
        Serializes this alarm state to a JSON-encodable dict.
        """
        return {'timestamp': self.timestamp,
                'entity_id': self.entity_id,
                'alarm_id': self.alarm_id,
                'check_id': self.check_id,
                'status': self.status,
                'state': self.state,
                'previous_state': self.previous_state,
                'alarm_changelog_id': self.alarm_changelog_id,
                'analyzed_by_monitoring_zone_id': self.analyzed_by_monitoring_zone_id}

    def detail_json(self):
        """
        Serializes this alarm state with additional details.
        """
        details = self.brief_json()
        details.update(alarm_label=self.alarm_label)
        return details


@attributes(["name",
             "type",
             Attribute("unit", default_value="other"),
             Attribute("_overrides", default_factory=dict),
             Attribute("_override_key")])
class Metric(object):
    """
    Models a MaaS metric type.
    """
    def set_override(self, **kwargs):
        """
        Sets the override metric for a given tenant, entity and check.

        Override metrics are defined as a function which takes a timestamp
        and returns the metric value.
        """
        self._overrides[self._override_key(**kwargs)] = kwargs['override_fn']

    def clear_overrides(self):
        """
        Clears the override metric values.
        """
        self._overrides = {}

    def _get_default_data(self):
        """
        Gets the default data point. This data point may be overridden by
        setting the override value.
        """
        if self.type == METRIC_TYPE_INTEGER:
            return random.randint(0, 100000)
        elif self.type == METRIC_TYPE_NUMBER:
            if self.unit == 'percent':
                return random.uniform(0, 100)
            else:
                return random.uniform(0, 100000)
        elif self.type == METRIC_TYPE_STRING:
            return random_string(random.randint(12, 30), selectable=(string.letters + string.digits))
        raise ValueError('No default data getter for type {0}!'.format(self.type))

    def get_value(self, **kwargs):
        """
        Gets the value of the metric at the specified timestamp.

        Overrides will be applied as necessary.
        """
        override_key = self._override_key(**kwargs)
        timestamp = kwargs['timestamp']
        if override_key in self._overrides:
            return self._overrides[override_key](timestamp)
        return self._get_default_data()

    def get_value_for_test_check(self, **kwargs):
        """
        Gets the metric data object as returned from the test-check API.
        """
        return {'type': self.type,
                'unit': self.unit,
                'data': self.get_value(**kwargs)}


@attributes(["metrics",
             Attribute("_clock"),
             Attribute("test_check_available", default_factory=dict),
             Attribute("test_check_status", default_factory=dict),
             Attribute("test_check_response_code", default_factory=dict)])
class CheckType(object):
    """
    Data model for a MaaS check type (e.g., remote.ping).
    """
    def clear_overrides(self):
        """
        Clears the overrides for test-checks and metrics.
        """
        self.test_check_available = {}
        self.test_check_status = {}
        self.test_check_response_code = {}

        for metric in self.metrics:
            metric.clear_overrides()

    def get_metric_by_name(self, metric_name):
        """
        Gets the metric on this check type.

        This method is useful for setting and clearing overrides on the
        test metrics.
        """
        for metric in self.metrics:
            if metric.name == metric_name:
                return metric
        raise NameError('No metric named "{0}"!'.format(metric_name))

    def get_test_check_response(self, **kwargs):
        """
        Gets the response as would have been returned by the test-check API.
        """
        entity_id = kwargs['entity_id']
        check_id = kwargs.get('check_id', '__test_check')
        monitoring_zones = kwargs.get('monitoring_zones') or ['__AGENT__']

        ench_key = (entity_id, check_id)
        timestamp = int(1000 * self._clock.seconds())

        return (self.test_check_response_code.get(ench_key, 200),
                [{'timestamp': timestamp,
                  'monitoring_zone_id': monitoring_zone,
                  'available': self.test_check_available.get(ench_key, True),
                  'status': self.test_check_status.get(
                      ench_key, 'code=200,rt=0.4s,bytes=99'),
                  'metrics': dict([(m.name,
                                    m.get_value_for_test_check(
                                        entity_id=entity_id,
                                        check_id=check_id,
                                        monitoring_zone=monitoring_zone,
                                        timestamp=timestamp))
                                   for m in self.metrics])}
                 for monitoring_zone in monitoring_zones])


@attributes([Attribute('metrics', instance_of=list)])
class SingleHostInfoType(object):
    """
    Models a MaaS host info type returning a single block of metrics,
    i.e., a hash for the info field as opposed to an array.
    """
    def get_info(self, entity_id, agent_id, timestamp):
        """
        Gets the host info.
        """
        return {'timestamp': timestamp,
                'error': None,
                'info': dict([(metric.name,
                               metric.get_value(
                                   entity_id=entity_id,
                                   agent_id=agent_id,
                                   timestamp=timestamp))
                              for metric in self.metrics])}


@attributes([Attribute('metrics', instance_of=list)])
class MultiHostInfoType(object):
    """
    Models a MaaS host info type returning multiple blocks of metrics,
    such as the CPU agent host info (one for each CPU).
    """
    def get_info(self, entity_id, agent_id, timestamp, num_blocks):
        """
        Gets the host info.
        """
        return {'timestamp': timestamp,
                'error': None,
                'info': [dict([(metric.name,
                                metric.get_value(
                                    entity_id=entity_id,
                                    agent_id=agent_id,
                                    block_index=i,
                                    timestamp=timestamp))
                               for metric in self.metrics])
                         for i in range(num_blocks)]}


@attributes([Attribute('id', instance_of=text_type, default_factory=lambda: unicode(uuid4())),
             Attribute('counts',
                       instance_of=dict,
                       default_factory=lambda: {
                           'cpus': 1,
                           'processes': 20,
                           'who': 1,
                           'filesystems': 4,
                           'disks': 1,
                           'network_interfaces': 2})])
class Agent(object):
    """
    Models a MaaS agent.
    """
    def get_host_info(self, available_types, requested_types, entity_id, clock):
        """
        Gets this agent's host information.
        """
        current_timestamp = int(1000 * clock.seconds())

        return dict([(rtype,
                      (available_types[rtype].get_info(
                          entity_id,
                          self.id,
                          current_timestamp,
                          self.counts[rtype])
                       if rtype in self.counts
                       else available_types[rtype].get_info(
                           entity_id,
                           self.id,
                           current_timestamp)))
                     for rtype in requested_types])


@attributes([Attribute('_factory_fn'),
             Attribute('_type', default_value=METRIC_TYPE_INTEGER),
             Attribute('_unit', default_value=None),
             Attribute('values', default_factory=list)])
class MetricListBuilder(object):
    """
    Stateful builder for concisely creating a lot of metrics.
    """
    @classmethod
    def agent_type(cls):
        """
        Creates a builder that builds agent metrics.
        """
        return cls(factory_fn=lambda **kwargs: Metric(
            override_key=lambda **ikwargs: (ikwargs['entity_id'], ikwargs['check_id']),
            **kwargs))

    @classmethod
    def remote_type(cls):
        """
        Creates a builder that builds remote metrics.
        """
        return cls(factory_fn=lambda **kwargs: Metric(
            override_key=lambda **ikwargs: (
                ikwargs['entity_id'],
                ikwargs['check_id'],
                ikwargs['monitoring_zone']),
            **kwargs))

    @classmethod
    def single_host_info_type(cls):
        """
        Creates a builder for metrics that model an agent host info type.
        """
        return cls(factory_fn=lambda **kwargs: Metric(
            override_key=lambda **ikwargs: (ikwargs['entity_id'], ikwargs['agent_id']),
            **kwargs))

    @classmethod
    def multi_host_info_type(cls):
        """
        Creates a builder for metrics that model an agent host info with
        multiple return blocks.

        For instance, the CPU host info generates a block of metrics for each CPU
        on the host. Users may pin or override the values individually for each
        block (each CPU in the CPU example). This requires that a block index be
        incorporated into the metric override key.
        """
        return cls(factory_fn=lambda **kwargs: Metric(
            override_key=lambda **ikwargs: (ikwargs['entity_id'],
                                            ikwargs['agent_id'],
                                            ikwargs['block_index']),
            **kwargs))

    def percents(self):
        """
        Configures the builder to produce percent metrics.
        """
        self._type = METRIC_TYPE_NUMBER
        self._unit = 'percent'
        return self

    def strings(self):
        """
        Configures the builder to produce string metrics.
        """
        self._type = METRIC_TYPE_STRING
        self._unit = 'string'
        return self

    def bytes(self):
        """
        Configures the builder to produce byte metrics.
        """
        self._type = METRIC_TYPE_INTEGER
        self._unit = 'bytes'
        return self

    def kilobytes(self):
        """
        Configures the builder to produce kilobyte metrics.
        """
        self._type = METRIC_TYPE_INTEGER
        self._unit = 'kilobytes'
        return self

    def counts(self):
        """
        Configures the builder to produce count metrics.
        """
        self._type = METRIC_TYPE_INTEGER
        self._unit = 'count'
        return self

    def types(self, typ):
        """
        Configures the type that will be used for built metrics.
        """
        self._type = typ
        return self

    def units(self, unit):
        """
        Configures the unit that will be used for built metrics.
        """
        self._unit = unit
        return self

    def metrics(self, *args):
        """
        Builds metrics and appends to self.values.
        """
        base_config = {'type': self._type}
        if self._unit is not None:
            base_config['unit'] = self._unit

        self.values.extend([self._factory_fn(**dict(base_config, name=name)) for name in args])
        return self


class MaasStore(object):
    """
    A collection of MaaS configuration objects.
    """
    def __init__(self, clock):
        """
        Initializes the MaaS configuration using the provided clock.

        This initializer reflects the variety of available check types and
        metrics supported by MaaS. Some MaaS check types have been omitted
        for simplicity and clarity. The full list of check types and metrics
        can be found in `the Rackspace Cloud Monitoring Developer Guide, appendix B
            <http://docs.rackspace.com/cm/api/v1.0/cm-devguide/content/appendix-check-types.html>`_
        """
        self.agents = []
        self.alarm_states = []

        self.check_types = {
            'agent.cpu': CheckType(
                clock=clock, metrics=MetricListBuilder.agent_type()
                .percents().metrics(
                    'user_percent_average', 'wait_percent_average', 'sys_percent_average',
                    'idle_percent_average', 'irq_percent_average', 'usage_average', 'min_cpu_usage',
                    'max_cpu_usage', 'stolen_percent_average'
                ).values),

            'agent.disk': CheckType(
                clock=clock, metrics=MetricListBuilder.agent_type()
                .types(METRIC_TYPE_INTEGER).metrics('queue', 'rtime', 'wtime')
                .bytes().metrics('read_bytes', 'write_bytes')
                .counts().metrics('reads', 'writes').values),

            'agent.filesystem': CheckType(
                clock=clock, metrics=MetricListBuilder.agent_type()
                .kilobytes().metrics('avail', 'free', 'total', 'used')
                .counts().metrics('files', 'free_files')
                .strings().metrics('options').values),

            'agent.load_average': CheckType(
                clock=clock, metrics=MetricListBuilder.agent_type()
                .types(METRIC_TYPE_NUMBER).metrics('1m', '5m', '10m').values),

            'agent.memory': CheckType(
                clock=clock, metrics=MetricListBuilder.agent_type()
                .bytes().metrics('actual_free', 'actual_used', 'free', 'swap_free', 'swap_page_in',
                                 'swap_page_out', 'swap_total', 'swap_used', 'total', 'used')
                .units('megabytes').metrics('ram').values),

            'agent.network': CheckType(
                clock=clock, metrics=MetricListBuilder.agent_type()
                .bytes().metrics('rx_bytes', 'rx_dropped', 'rx_errors', 'rx_packets',
                                 'tx_bytes', 'tx_dropped', 'tx_errors', 'tx_packets')
                .values),

            'remote.http': CheckType(
                clock=clock, metrics=MetricListBuilder.remote_type()
                .strings().metrics('cert_error', 'cert_issuer', 'cert_subject',
                                   'cert_subject_alternative_names', 'code')
                .bytes().metrics('bytes', 'truncated')
                .types(METRIC_TYPE_INTEGER).units(None).metrics(
                    'cert_end', 'cert_end_in', 'cert_start', 'duration', 'tt_connect', 'tt_firstbyte'
                ).values),

            'remote.ping': CheckType(
                clock=clock, metrics=MetricListBuilder.remote_type()
                .types(METRIC_TYPE_NUMBER).metrics('average', 'maximum', 'minimum')
                .percents().metrics('available')
                .counts().metrics('count').values)}

        self.host_info_types = {
            'cpus': MultiHostInfoType(
                metrics=MetricListBuilder.multi_host_info_type().types(METRIC_TYPE_INTEGER).metrics(
                    'idle', 'irq', 'mhz', 'soft_irq', 'stolen', 'sys', 'total', 'total_cores',
                    'user', 'wait')
                .strings().metrics('model', 'name', 'vendor').values),

            'disks': MultiHostInfoType(
                metrics=MetricListBuilder.multi_host_info_type().types(METRIC_TYPE_INTEGER).metrics(
                    'read_bytes', 'reads', 'rtime', 'time', 'write_bytes', 'writes', 'wtime')
                .strings().metrics('name').values),

            'filesystems': MultiHostInfoType(
                metrics=MetricListBuilder.multi_host_info_type().types(METRIC_TYPE_INTEGER).metrics(
                    'avail', 'files', 'free', 'free_files', 'total', 'used')
                .strings().metrics('dev_name', 'dir_name', 'options', 'sys_type_name').values),

            'memory': SingleHostInfoType(
                metrics=MetricListBuilder.single_host_info_type().types(METRIC_TYPE_INTEGER).metrics(
                    'actual_free', 'actual_used', 'free', 'ram', 'total', 'used')
                .percents().metrics('free_percent', 'used_percent').values),

            'network_interfaces': MultiHostInfoType(
                metrics=MetricListBuilder.multi_host_info_type().strings().metrics(
                    'address', 'address6', 'broadcast', 'hwaddr', 'name', 'netmask', 'type')
                .types(METRIC_TYPE_INTEGER).units(None).metrics(
                    'flags', 'mtu', 'rx_bytes', 'rx_packets', 'tx_bytes', 'tx_packets').values),

            'processes': MultiHostInfoType(
                metrics=MetricListBuilder.multi_host_info_type().types(METRIC_TYPE_INTEGER).metrics(
                    'memory_major_faults', 'memory_minor_faults', 'memory_page_faults',
                    'memory_resident', 'memory_share', 'memory_size', 'pid', 'state_priority',
                    'state_threads', 'time_start_time', 'time_sys', 'time_total', 'time_user')
                .strings().metrics('cred_group', 'cred_user', 'exe_cwd', 'exe_name',
                                   'exe_root', 'state_name').values),

            'system': SingleHostInfoType(
                metrics=MetricListBuilder.single_host_info_type().strings().metrics(
                    'arch', 'name', 'vendor', 'vendor_name', 'vendor_version', 'version').values),

            'who': MultiHostInfoType(
                metrics=MetricListBuilder.multi_host_info_type()
                .strings().metrics('device', 'host', 'user')
                .types(METRIC_TYPE_INTEGER).units(None).metrics('time').values)}

    def latest_alarm_states_for_entity(self, entity_id):
        """
        Computes the latest alarm states for the specified entity.

        Newer alarm states are assumed to be always appended to the list of
        alarm states.
        """
        alarm_states_for_entity = [state for state in self.alarm_states
                                   if state.entity_id == entity_id]
        latest_alarm_states_by_alarm = {}
        for state in alarm_states_for_entity:
            latest_alarm_states_by_alarm[state.alarm_id] = state
        return latest_alarm_states_by_alarm.values()
