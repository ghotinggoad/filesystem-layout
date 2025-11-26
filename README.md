# filesystem-layout
An Ansible playbook that provisions and mount Logical Volumes in Linux VMs given an input filesystem layout.
This project was tested on Rocky9 and Ubuntu Noble Server.
Automatic detection of device path is not implemented as Ubuntu Server udev is not populating the only deterministic field (Device Serial) during testing.

## Feature(s)
- Provision and mount Logical Volumes given desired filesystem layout.
- Supports simultaneously configuring VMs of different Linux Distros and inputs.
- Compatible with Terraform output ansible_inventory from my Terraform projects.
___
## Limitation(s)
- Requires User to manually set the initial vdisk device path which is not ideal.
___
## Requirement(s)
- **CHECK LIMITATION(S)**
___
## Instructions
1. Create inventory.json referencing sample_inventory.json
2. Run "ansible-playbook -i inventory.json filesystem_layout.yml"
___
## License
filesystem-layout is licensed under the MIT license, see [LICENSE](LICENSE) for details.
