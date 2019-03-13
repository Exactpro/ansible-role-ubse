# Ansible Role: Uniform (Virtual) machine

Launch / Re-launch Digital Ocean's droplet or ArubaCloud Smart server

## Requirements

* DigitalOcean - set `vm_provider: digitalocean` and API key in `do_api_token`.
* ArubaCloud - set `vm_provider: arubacloudsmart`, `aruba_account`, `aruba_password`.

## Role Variables

* digitalocean only: pubkeyid, private_net
* arubacloudsmart: `dc` is one of [1..8] (1,2,7 - IT[123]; 3 - CZ; 4 - FR; 5 - DE; 6 - UK; 8 - PL)

## Dependencies

None.

## Example Playbook

```
- hosts: localhost
  gather_facts: no
  tasks:
    - add_host:
        name: s1
        ansible_port: 2222
        vm:
          cloud: digitalocean
          dc: fra1
          name: s1.example.com
          size:  s-1vcpu-1gb
          image: debian-8-x64
          private_net: yes
          doIPv6: yes
- hosts: s1
  gather_facts: no
  tasks:
    - include_role: name=exactpro.um
      vars:
        do_api_token: "{{ lookup('file', '~/.ssh/do/my.apikey') }}"
        pubkeyid: 235505
        wait_minutes:  4     # max time to create VM, usually it's under 2 minutes
        wait_ssh:     25     # max wait for SSH to come up
        state: pristine
      register: m1
    - debug: msg="Host {{ inventory_hostname }} {{ ansible_host }}:{{ ansible_port }}"
```

## Issues

* arubacloudsmart: state=present cannot create VM, state=absent unimplemented.

## License

MIT / BSD

## Author Information

This is a work in progress by Mark Zhitomirskiy mz@exactpro.com
```
