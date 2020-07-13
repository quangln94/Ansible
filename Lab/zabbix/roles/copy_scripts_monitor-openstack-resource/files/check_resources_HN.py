#!/usr/bin/python
#
#    Copyright 2015 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
import urllib2
import sys
import simplejson as json
import ConfigParser
from zabbix_checks_logger import get_logger

CONF_FILE = '/etc/zabbix/scripts/monitor-openstack-resource/check_api_HN.conf'


class OSAPI(object):
    """Openstack API"""

    def __init__(self, logger, config):
        self.logger = logger
        self.config = config
        self.username = self.config.get('api', 'user')
        self.userid = self.config.get('api','userid')
        self.password = self.config.get('api', 'password')
        self.projectid = self.config.get('api', 'projectid')
        self.keystone_timeout = self.config.get('api', 'keystone_timeout')
        self.endpoint_keystone = self.config.get('api', 'keystone_endpoints').split(',')
        self.token = None
        self.tenant_id = None
        self.get_token()
        self.total = 0

    def get_timeout(self, service):
        try:
            return int(self.config.get('api', '%s_timeout' % service))
        except ConfigParser.NoOptionError:
            return 1

    def get_token(self):
        data = json.dumps(
            {"auth": {"identity": {"methods": ["password"], "password": {
                "user": {"id": self.userid, "password": self.password}}},
                      "scope": {"project": {"id": self.projectid}}}}) 
        for keystone in self.endpoint_keystone:
            self.logger.info("Trying to get token from '%s'" % keystone)
            try:
                request = urllib2.Request(
                    '%s/tokens' % keystone,
                    data=data,
                    headers={
                        'Content-type': 'application/json' , 'accept': 'application/json'
                    })
                openrequest = urllib2.urlopen(request, timeout=self.get_timeout('keystone'))
                data = json.loads(openrequest.read())
                self.token = openrequest.info().getheader('X-Subject-Token')
                self.tenant_id = data['token']['project']['id']
                self.logger.debug("Got token '%s'" % self.token)
                return
            except Exception as e:
                self.logger.debug("Got exception '%s'" % e)
        self.logger.critical(0)

    def count_total(self, url, service,check_key,status):
        count = 0
        b = True
        bo = True
        if status == 'true':
            bo = True
        if status == 'false':
            bo = False

        self.logger.info("Trying '%s' on '%s'" % (service, url))
        try:
            request = urllib2.Request(url,
                                      headers={
                                          'X-Auth-Token': self.token,
                                      })
            openrequest2 = urllib2.urlopen(request, timeout=self.get_timeout(service))
        except Exception as e:
            self.logger.debug("Got exception from '%s' '%s'" % (service, e))
            self.logger.critical(0)
            sys.exit(1)
        data2 = json.loads(openrequest2.read())

        if check_key is None:
            for key in data2:
                if b is True:
                    self.total = len(data2[key])
                    b = False
        elif status == "CHECK_ARRAY":
            for key in data2:
                if b is True:
                     for i in range(0, len(data2[key])):
                        if len(data2[key][i][check_key]) > 0:
                            count =count +1
                b = False
            self.total = count
        elif check_key == "fixed_ips":

            for key in data2:
                if b is True:
                     for i in range(0, len(data2[key])):
                        for j in range(0,len(data2[key][i][check_key])):
                            a = int(data2[key][i][check_key][j]['ip_address'].split('.')[0])
                            b = int(data2[key][i][check_key][j]['ip_address'].split('.')[1])
                            if a !=10 and ( a != 172 or (a == 172 and (b <16 or b > 31))) and ( a !=192 or ( a == 192 and b != 168)):
                                count = count + 1
                b = False
            self.total = count
        else:
            for key in data2:
                if b is True:
                     for i in range(0, len(data2[key])):
                        if status == 'ceph_hdd':
                            if data2[key][i][check_key] == status or data2[key][i][check_key] is bo or data2[key][i][check_key] is None:
                                count =count +1
                        else:
                            if data2[key][i][check_key] == status or data2[key][i][check_key] is bo:
                                count = count + 1
                b = False
            self.total = count



        return self.total
#       self.logger.critical(1)


def main():
    config = ConfigParser.RawConfigParser()
    config.read(CONF_FILE)
    logger = get_logger(config.get('api', 'log_level'))

    API = OSAPI(logger, config)
    if len(sys.argv) < 5:
        logger.critical('No argvs, dunno what to do')
        sys.exit(1)
    map = config.get('api', '%s_map' % sys.argv[1])

    url = '%s://%s:%s/%s' % (sys.argv[2], sys.argv[3], sys.argv[4], map)
    url = url % API.__dict__
    if len(sys.argv) == 5:
        print API.count_total(url, sys.argv[1],None, None)

    if len(sys.argv) == 7:
        print API.count_total(url, sys.argv[1], sys.argv[5], sys.argv[6])


if __name__ == "__main__":
    main()

