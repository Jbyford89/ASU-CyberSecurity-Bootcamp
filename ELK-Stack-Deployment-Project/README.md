## Automated ELK Stack Deployment

The files in this repository were used to configure the network depicted below.

![](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Images/Diagrams/Cloud_Security_with_ELK.drawio.png)

These files have been tested and used to generate a live ELK deployment on Azure. They can be used to either recreate the entire deployment pictured above. Alternatively, select portions of the *yaml* and *config* file may be used to install only certain pieces of it, such as Filebeat.

  - [My First Playbook](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/tree/main/ELK-Stack-Deployment-Project/Ansible/Docker/pentest.yml)
  - [Hosts](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Ansible/ELK_Stack/hosts)
  - [Ansible Configuration](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/e49e0240df25067ee8da9848829000346e14a037/ELK-Stack-Deployment-Project/Ansible/ELK_Stack/ansible.cfg) 
  - [ELK Setup & Install](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Ansible/ELK_Stack/elk-packages.yml)
  - [Filebeat Configuration]()
  - [Filebeat Playbook]()
  - [Metricbeat Configuration]()
  - [Metricbeat Playbook]()

This document contains the following details:
- Description of the Topologu
- Access Policies
- ELK Configuration
  - Beats in Use
  - Machines Being Monitored
- How to Use the Ansible Build


### Description of the Topology

The main purpose of this network is to expose a load-balanced and monitored instance of DVWA, the D*mn Vulnerable Web Application.

Load balancing ensures that the application will be highly _functional_ and _available_, in addition to restricting _traffic_ to the network.
- What aspect of security do load balancers protect?
  -_Load balancers add resiliency by rerouting live traffic from one server to another, if a server falls prey to a DDoS atack or becomes unailable._
- What is the advantage of a jump box? 
  -_A Jump Box prevents Azure VMs from being exposed by a public IP Address. You can monior and log all within the same system/box. You can restrict who can access and from which IP._

Integrating an ELK server allows users to easily monitor the vulnerable VMs for changes to the _network_ and system _logs_.
- _What does Filebeat watch for?
  -_Filebeat monitors the log files or locations that you specify. Filebeat collecs log events and forwards them to Elasticsearch or Logstash for indexing._
- What does Metricbeat record?
  -_Metricbeat takes the metrics and statistics that it collects and then ships them to the output that you specify._

The configuration details of each machine may be found below.
_Note: Use the [Markdown Table Generator](http://www.tablesgenerator.com/markdown_tables) to add/remove values from the table_.

| Name     | Function              | IP Address | Operating System |
|----------|-----------------------|------------|------------------|
| Jump Box | Gateway               | 10.0.0.4   | Linux            |
| Web-1    | UbuntuServer          | 10.0.0.5   | Linux            |
| Web-2    | UbuntuServer          | 10.0.0.6   | Linux            |
| ELK      | UbuntuServer          | 10.1.0.4   | Linux            |

### Access Policies

The machines on the internal network are not exposed to the public Internet. 

Only the _internal_ machine can accept connections from the Internet. Access to this machine is only allowed from the following IP addresses:
- _[My Public IP] through TCP 5601_

Machines within the network can only be accessed by my _workstation_ and _Jump Box_ through _SSH_.
- Which machine did you allow to access your ELK VM?
  -_Jump-Box Provisioner 10.0.0.4 via SSH port 22_
- What was its IP address?
  -[My public IP] via TCP 5601

A summary of the access policies in place can be found in the table below.

| Name     | Publicly Accessible | Allowed IP Addresses                         |
|----------|---------------------|----------------------------------------------|
| Jump Box | Yes                 | 52.149.137.26 (Workstation IP SSH port 22    |
| Web-1    | No                  | 10.1.0.4 SSH port 22                         |
| Web-2    | No                  | 10.1.0.4 SSH port 22                         |
| ELK      | No                  | Workstation [My Public IP] using TCP 5601    |
### Elk Configuration

Ansible was used to automate configuration of the ELK machine. No configuration was performed manually, which is advantageous because...
- _What is the main advantage of automating configuration with Ansible?_
  -_Ansible lets you quickly deploy multi-tier applications by using a **YAML** playbook._ 
  -_No custom code needed to automate systems._
  -_Ansible can figure out how to get your systems to the correct state you would like them to be._

The playbook implements the following tasks:
- _In 3-5 bullets, explain the steps of the ELK installation play. E.g., install Docker; download image; etc._
  - Specify a different group of machines
  ```yaml
   - name: Config elk VM with Docker
     hosts: elk
     become: true
     tasks:
   ```
  - Install Docker.io
  ```yaml
  - name: Install docker.io
    apt:
      update_cache: yes
      force_apt_get: yes
      name: docker.io
      state: present
  ```
  - Install pip3
  ```yaml
  - name: Install pip3
    apt:
      force_apt_get: yes
      name: python3-pip
      state: present
  ```
  - Install Docker python module
  ```yaml
  - name: Install docker python module
    pip:
      name: docker
      state: present
  ```
  - Increase Virtual Memory
  ```yaml
  - name: Use more memory
    sysctl:
      name: vm.max_map_count
      value: "262144"
      state: present
      reload: yes
  ```
  - Published ports 5044, 5601, and 9200 available
  ```yaml
  published_ports:
    - 5601:5601
    - 9200:9200
    - 5044:5044
  ```

The following screenshot displays the result of running `docker ps` after successfully configuring the ELK instance.

![](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Images/docker_ps_elk)

### Target Machines & Beats
This ELK server is configured to monitor the following machines:
- _TODO: List the IP addresses of the machines you are monitoring_

We have installed the following Beats on these machines:
- _TODO: Specify which Beats you successfully installed_

These Beats allow us to collect the following information from each machine:
- _TODO: In 1-2 sentences, explain what kind of data each beat collects, and provide 1 example of what you expect to see. E.g., `Winlogbeat` collects Windows logs, which we use to track user logon events, etc._

### Using the Playbook
In order to use the playbook, you will need to have an Ansible control node already configured. Assuming you have such a control node provisioned: 

SSH into the control node and follow the steps below:
- Copy the _____ file to _____.
- Update the _____ file to include...
- Run the playbook, and navigate to ____ to check that the installation worked as expected.

_TODO: Answer the following questions to fill in the blanks:_
- _Which file is the playbook? Where do you copy it?_
- _Which file do you update to make Ansible run the playbook on a specific machine? How do I specify which machine to install the ELK server on versus which to install Filebeat on?_
- _Which URL do you navigate to in order to check that the ELK server is running?

_As a **Bonus**, provide the specific commands the user will need to run to download the playbook, update the files, etc.
