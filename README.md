# DevOpsTechnicalChallenge
## Purpose:

This challenge is designed to test the SRE/DevOps candidate’s understanding and abilities in
the following areas of infrastructure as code:
• Cloud access management
• Cloud networking
• Security concerns awareness
• Automation and clean coding practices
• Containerization concepts

## Tasks:
• Use Terraform or Ansible or CloudFormation to automate the following tasks against
any cloud provider platform, e.g. AWS, GCP, Aliyun.
• Provision a new VPC and any networking related configurations.
• In this environment provision a virtual machine instance, with an OS of your choice.
• Apply any security hardening (OS, firewall, etc..) you see fit for the VM instance.
• Install Docker CE on that VM instance.
• Deploy/Start an Nginx container on that VM instance.
• Demonstrate how you would test the healthiness of the Nginx container.
• Expose the Nginx container to the public web on port 80.
• Fetch the output of the Nginx container’s default welcome page.
• Excluding any HTML/JS/CSS tags and symbols, output the words and their frequency
count for the words that occurred the most times on the default welcome page.
• Demonstrate how you would log the resource usage of the containers every 10
seconds.

## Bonus Points:
• Replace VM instance(s) with K8S cluster
• Use AWS as cloud provider platform
• Use Terraform instead of Ansible or CloudFormation
• Visualize monitoring with metrics query language
• Submit your solution with git and README


python3 -m venv env
source venv/bin/activate 

https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
pip install ansible
pip install ansible-lint
pip install awscli 
pip install boto
pip install boto3
pip install bs4

some problem issues:
https://github.com/microsoft/vscode-python/issues/14327

https://docs.ansible.com/ansible/latest/collections/amazon/aws/ec2_group_module.html

https://docs.ansible.com/ansible/latest/collections/amazon/aws/ec2_vpc_nat_gateway_module.html#ansible-collections-amazon-aws-ec2-vpc-nat-gateway-module

https://docs.ansible.com/ansible/latest/collections/community/aws/route53_module.html

ansible-playbook -i ansibled.inventory vpc.yml --vault-password-file ansibled.vault

ansible-playbook -i hosts.inventory vpc.yml --vault-password-file ansibled.vault  

ansible-playbook -i hosts.inventory ec2.key.yml --vault-password-file ansibled.vault  
ansible-playbook -i hosts.inventory ec2-key-delete.yml --vault-password-file ansibled.vault  