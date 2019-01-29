# Ansible Role: Uniform basic server

Launch / Re-launch Digital Ocean's droplet or ArubaCloud Smart server

## Requirements

T.b.d.

## Role Variables

T.b.d.

## Dependencies

T.b.d.

## Example Playbook

```
  - hosts: localhost
    vars:
      vm_provider: digitalocean
      wait_minutes: 4
      do_api_token: xxxxx
      pubkeyid: 235505
      dc: fra1
      vps_name: s1.example.com
      size:  s-1vcpu-1gb
      image: debian-8-x64
      needIPv6: yes
      private_net: no
    roles:
      - role: mz0.ubse
    tasks:
      - debug: msg="Droplet {{vm.data.droplet.name}} {{vm.data.ip_address}}"
```

## License

MIT / BSD

## Author Information

This is a work in progress by Mark Zhitomiskiy mz@exactpro.com
