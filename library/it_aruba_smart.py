#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018 Mark Zhitomirski <marcuzero0gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
'''

EXAMPLES = '''
'''

RETURN = '''
srv:
    description: Aruba Cloud Smart servers
    returned: success and no resource constraint
    type: list
    sample: [
         {
              "dc": 5,
              "busy": false,
              "id": 19652,
              "isON": true,
              "name": "Lemp",
              "size": "S",
              "templateId": 448
         }
    ]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.it_aruba import ArubaCloudAPI


def main():
    module = AnsibleModule(
        argument_spec=ArubaCloudAPI.it_aruba_argument_spec(),
        supports_check_mode=False,
    )

    api = ArubaCloudAPI(module)
    servers=[]
    dc = module.params['dc']
    for s in api.get_servers(dc):
        servers.append(api.get_server(dc, s['id']))

    module.exit_json(changed=False, srv=servers)


if __name__ == '__main__':
    main()
