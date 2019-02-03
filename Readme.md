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
    vars:
      vm_provider: digitalocean
      state: present
      wait_minutes: 4
      do_api_token: xxxxx
      pubkeyid: 235505
      dc: fra1
      name: s1.example.com
      size:  s-1vcpu-1gb
      image: debian-8-x64
      needIPv6: yes
      private_net: no
    roles:
      - role: exactpro.um
    tasks:
      - debug: msg="Droplet {{ vm.data.droplet.name }} {{ vm.data.ip_address }}"
```

## Issues

* arubacloudsmart: state=present cannot create VM, state=absent unimplemented.

## License

MIT / BSD

## Author Information

This is a work in progress by Mark Zhitomiskiy mz@exactpro.com
