## Automated ELK Stack Deployment

The files in this repository were used to configure the network depicted below.

![](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Images/Diagrams/Cloud_Security_with_ELK.drawio.png)

These files have been tested and used to generate a live ELK deployment on Azure. They can be used to either recreate the entire deployment pictured above. Alternatively, select portions of the *yaml* and *config* file may be used to install only certain pieces of it, such as Filebeat.

  - [ELK Setup & Install](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/tree/main/ELK-Stack-Deployment-Project/Ansible/Docker/pentest.yml)
  - [Hosts](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Ansible/ELK_Stack/hosts)
  - [Ansible Configuration](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/e49e0240df25067ee8da9848829000346e14a037/ELK-Stack-Deployment-Project/Ansible/ELK_Stack/ansible.cfg) 
  - [Filebeat Configuration](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Ansible/Filebeat/filebeat-config.yml)
  - [Filebeat Playbook](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Ansible/Filebeat/filebeat-playbook.yml)
  - [Metricbeat Configuration](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Ansible/Metricbeat/metricbeat-config.yml)
  - [Metricbeat Playbook](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Ansible/Metricbeat/metricbeat-playbook.yml)

This document contains the following details:
- Description of the Topology
- Access Policies
- ELK Configuration
  - Beats in Use
  - Machines Being Monitored
- How to Use the Ansible Build


### Description of the Topology

The main purpose of this network is to expose a load-balanced and monitored instance of DVWA, the D*mn Vulnerable Web Application.

Load balancing ensures that the application will be highly _functional_ and _available_, in addition to restricting _traffic_ to the network.
- What aspect of security do load balancers protect?
  - _Load balancers add resiliency by rerouting live traffic from one server to another, if a server falls prey to a DDoS atack or becomes unavailable._
- What is the advantage of a jump box? 
  - _A Jump Box prevents Azure VMs from being exposed by a public IP Address. You can monior and log all within the same system/box. You can restrict who can access and from which IP._

Integrating an ELK server allows users to easily monitor the vulnerable VMs for changes to the _network_ and system _logs_.
- What does Filebeat watch for?
  - _Filebeat monitors the log files or locations that you specify. Filebeat collects log events and forwards them to Elasticsearch or Logstash for indexing._
- What does Metricbeat record?
  - _Metricbeat takes the metrics and statistics that it collects and then ships them to the output that you specify._

The configuration details of each machine may be found below.
_Note: Use the [Markdown Table Generator](http://www.tablesgenerator.com/markdown_tables) to add/remove values from the table_.

| Name     | Function              | IP Address | Operating System |
|----------|-----------------------|------------|------------------|
| Jump Box | Gateway               | 10.0.0.4   | Linux            |
| Web-1    | DVWA                  | 10.0.0.5   | Linux            |
| Web-2    | DVWA                  | 10.0.0.6   | Linux            |
| ELK      | Server                | 10.1.0.4   | Linux            |

### Access Policies

The machines on the internal network are not exposed to the public Internet. 

Only the _internal_ machine can accept connections from the Internet. Access to this machine is only allowed from the following IP addresses:
- _[My Public IP] through TCP 5601_

Machines within the network can only be accessed by my _workstation_ and _Jump Box_ through _SSH_.
- Which machine did you allow to access your ELK VM?
  - _Jump-Box Provisioner 10.0.0.4 via SSH port 22_
- What was its IP address?
  - _[My Public IP] via TCP 5601_

A summary of the access policies in place can be found in the table below.

| Name     | Publicly Accessible | Allowed IP Addresses                         |
|----------|---------------------|----------------------------------------------|
| Jump Box | Yes                 | 52.149.137.26 (SSH port 22)                  |
| Web-1    | No                  | 10.1.0.4 SSH port 22                         |
| Web-2    | No                  | 10.1.0.4 SSH port 22                         |
| ELK      | No                  | [My Public IP] using TCP 5601                |
### Elk Configuration

Ansible was used to automate configuration of the ELK machine. No configuration was performed manually, which is advantageous because...
- _What is the main advantage of automating configuration with Ansible?_
  - _Ansible lets you quickly deploy multi-tier applications by using a **YAML** playbook._
  - _Ansible can figure out how to get your systems to the correct state you would like them to be._

The playbook implements the following tasks:
- _In 3-5 bullets, explain the steps of the ELK installation play. E.g., install Docker; download image; etc._
  - Specify group for elk
  ```yaml
   - name: Config elk VM with Docker
     hosts: elk
     become: true
     tasks:
   ```
  - Installed Docker.io
  ```yaml
  - name: Install docker.io
    apt:
      update_cache: yes
      force_apt_get: yes
      name: docker.io
      state: present
  ```
  - Installed pip3
  ```yaml
  - name: Install pip3
    apt:
      force_apt_get: yes
      name: python3-pip
      state: present
  ```
  - Installed Docker python module
  ```yaml
  - name: Install docker python module
    pip:
      name: docker
      state: present
  ```
  - Increased Virtual Memory
  ```yaml
  - name: Use more memory
    sysctl:
      name: vm.max_map_count
      value: "262144"
      state: present
      reload: yes
  ```
  - Used the following Published ports
  ```yaml
  published_ports:
    - 5601:5601
    - 9200:9200
    - 5044:5044
  ```

The following screenshot displays the result of running `docker ps` after successfully configuring the ELK instance.

### Elk
![](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Images/elk_docker_ps.png)

### Web 1
![](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Images/web_1_docker_ps.png)

### Web 2
![](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Images/web_2_docker_ps.png)

### Target Machines & Beats
This ELK server is configured to monitor the following machines:
  - Web-1: 10.0.0.5
  - Web-2: 10.0.0.6

We have installed the following Beats on these machines:
  - Filebeat
    - [Filebeat Status](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Images/filebeat_data_status.png)
  - Metricbeat
    - [Metricbeat Status](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Images/metricbeat_data_status.png)

These Beats allow us to collect the following information from each machine:
- _In 1-2 sentences, explain what kind of data each beat collects, and provide 1 example of what you expect to see. E.g., `Winlogbeat` collects Windows logs, which we use to track user logon events, etc._
  - Filebeat is used to collect log data oon the specified machines. These files include Apache, Microsoft Azure tools and web servers as well as MySQL databases.
    - [Filebeat Kibana Dashboard](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Images/filebeat_system_logs_dashboard.png)
  - Metricbeat monitors the virtual machine statistics, CPU core stats, filesystem stats, memory and network stats.
    - [Metricbeat Kibana Dashboard - Docker Overview](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Images/metricbeat_docker_overview.png)
    - [Docker Web-1 Metrics](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Images/web_1_metrics.png)
    - [Docker Web-2 Metrics](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Images/web_2_metrics.png)
### Using the Playbook
In order to use the playbook, you will need to have an Ansible control node already configured. Assuming you have such a control node provisioned: 

SSH into the control node and follow the steps below:
- Copy the _yml_ file to _ansible_.
- Update the _config_ file to include _remote users_ and _ports_
- Run the playbook, and navigate to _Kibana [ELK IP]/app/kibana:5601_ to check that the installation worked as expected.

### For Elk VM
- Copy the [Elk Installation and Configuration](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Ansible/ELK_Stack/elk-packages.yml)
- Run the playbook using the `ansible-playbook /etc/ansible/elk-packages.yml`
- If you are in the `/etc/ansible/` directory you can run `ansible-playbook elk-packages.yml`
### Filebeat
- Download Filebeat playbook using:
  - `curl -L -O https://gist.githubusercontent.com/slape/5cc350109583af6cbe577bbcc0710c93/raw/eca603b72586fbe148c11f9c87bf96a63cb25760/Filebeat > /etc/ansible/filebeat-config.yml`
  - Copy [Filebeat Configuration File](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Ansible/Filebeat/filebeat-config.yml)
  - Update filebeat-config.yml to include _ELK private IP 10.1.0.4_ information provided below.
  - _Hint: Use `ctrl+w` while using `nano` inside the file to search for by keywords `output.elasticsearch` and `setup.kibana`._
  ```
  output.elasticsearch:
  # Boolean flag to enable or disable the output module.
  #enabled: true

  # Array of hosts to connect to.
  # Scheme and port can be left out and will be set to the default (http and 9200)
  # In case you specify and additional path, the scheme is required: http://localhost:9200/path
  # IPv6 addresses should always be defined as: https://[2001:db8::1]:9200
  hosts: ["10.1.0.4:9200"]
  username: "elastic"
  password: "changeme" # TODO: Change this to the password you set

  # Starting with Beats version 6.0.0, the dashboards are loaded via the Kibana API.
  # This requires a Kibana endpoint configuration.
  setup.kibana:
    host: "10.1.0.4:5601" 
  # TODO: Change this to the IP address of your ELK server
  ```
- Run the playbook `ansible-playbook filebeat-playbook.yml` then go to [Kibana](http://104.42.35.235:5601/app/kibana:5601) > Logs > Add log data > System Logs(deb) > Module status > check and verify that the installation worked by verifying there are incoming logs.
  - [Filebeat Status](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Images/filebeat_data_status.png)
  - [Filebeat Logs Daashboard](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Images/filebeat_system_logs_dashboard.png)
### Metricbeat
- Download Metricbeat playbook using:
  - `curl -L -O https://gist.githubusercontent.com/slape/58541585cc1886d2e26cd8be557ce04c/raw/0ce2c7e744c54513616966affb5e9d96f5e12f73/metricbeat > /etc/ansible/files/metricbeat-config.yml`
  - Copy the [Metricbeat Configuration File](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/ELK-Stack-Deployment-Project/Ansible/Metricbeat/metricbeat-config.yml)
  - Update the metricbeat-config.yml file _ELK Private IP 10.1.0.4_ information provided below.
  ```
  #============================== Kibana =====================================

  # Starting with Beats version 6.0.0, the dashboards are loaded via the Kibana API.
  # This requires a Kibana endpoint configuration.
  setup.kibana:
    host: "10.1.0.4:5601"
  
  #-------------------------- Elasticsearch output ------------------------------
  output.elasticsearch:
    # TODO: Change the hosts IP address to the IP address of your ELK server
    # TODO: Change password from `changeme` to the password you created
    hosts: ["10.1.0.4:9200"]
    username: "elastic"
    password: "changeme"
  ```
- Run the playbook `ansible-playbook metricbeat-config.yml` then go to [Kibana](http://104.42.35.235:5601/app/kibana:5601) > Logs > Add metric data > Docker Metrics(deb) > Module status > check and verify that the installation worked by any incoming metrics.
  - [Metricbeat Kibana Dashboard - Docker Overview](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Images/metricbeat_docker_overview.png)
  - [Docker Web-1 Metrics](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Images/web_1_metrics.png)
  - [Docker Web-2 Metrics](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Images/web_2_metrics.png)

_Answer the following questions to fill in the blanks:_
- _Which file is the playbook? Where do you copy it?_
  - [Ansible](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Ansible/Docker/pentest.yml)
  - Copy this file to `/etc/ansible`
  - [Filebeat](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Ansible/Filebeat/filebeat-playbook.yml)
  - Copy this file to `/etc/ansible`
  - [Metricbeat](https://github.com/Jbyford89/ASU-CyberSecurity-Bootcamp/blob/main/ELK-Stack-Deployment-Project/Ansible/Metricbeat/metricbeat-playbook.yml)
  - Copy this file to `/etc/ansible`
- _Which file do you update to make Ansible run the playbook on a specific machine? How do I specify which machine to install the ELK server on versus which to install Filebeat on?_
  - /etc/ansible/`hosts` file
  - The IP addresses are specified under groups there is _[webservers]_ and _[elk]_ this is located in the `/etc/ansible/hosts` file. Webservers contains the IPs of the two web machines that will contain filebat and the the elk group contains the ELK stack.
- Which URL do you navigate to in order to check that the ELK server is running?
  - http://ELKIP:5601/app/kibana

_As a **Bonus**, provide the specific commands the user will need to run to download the playbook, update the files, etc._
 - The commands below are used in the installation and configuration of the ELK Stack.

| Command                                   | Definition and Purpose                  |
|-------------------------------------------|-----------------------------------------|
| `ssh-keygen`                              | create ssh key to access and setup VM   |
| `sudo -l`                                 | check for sudo privledges               |
| `cat ~/.ssh/id_rsa.pub`                   | view the public ssh key                 |
| `ssh sysadmin@[Jump-Box IP]`              | log in to the Jump-Box                  |
| `sudo docker container list -a`           | list docker containers available        |
| `sudo docker start [container name]`      | start docker container                  |
| `sudo docker ps -a`                       | list all active and inactive containers |
| `sudo docker attatch [container name]`    | attaching and starting up container     |
| `cd /etc/ansible`                         | change to /etc/ansible directory        |
| `ls -la`                                  | list all files includes hidden          |
| `nano /etc/ansible/hosts`                 | edit hosts file                         |
| `nano /etc/ansible/ansible.cfg`           | edit ansible.confg file                 |
| `nano /etc/ansible/pentest.yml`           | edit pentest.yml file (setup)           | 
| `ansible-playbook [location][filename]`   | execute the specified playbook          |
| `ssh sysadmin@10.0.0.5` from `ansible`    | log into Web-1 VM from ansible          |
| `ssh sysadmin@10.0.0.6` from `ansible`    | log into Web-2 VM from ansible          |
| `ssh sysadmin@ELK-IP` from `ansible`      | log into ELK VM from ansible            |
| `exit`                                    | terminate current shell                 |
| `sudo apt update`                         | check for any updates in terminal       |
| `sudo apt upgrade`                        | install any updates                     |
| `sudo apt install docker.io`              | install docker.io                       |
| `sudo service docker start`               | start docker                            |
| `sudo systemctl status docker`            | check status of docker                  |
| `sudo systemctl start docker`             | start docker                            |
| `sudo docker pull cyberxsecurity/ansible` | pull docker container                   |
| `sudo docker run -ti [contianer name]`    | run and create docker container         |
| `ansible -m ping all`                     | check connection of ansible containers  |
| `curl -L -O [path of file]`               | download file via curl                  |
| `dpkg -i [file name]`                     | install file and metricbeat             |
| `nano filebeat-config.yml`                | edit filebeat config                    |
| `nano filebat-playbook.yml`               | edit filebeat playbook                  |
| `nano metricbeat-config.yml`              | edit metricbeat config                  |
| `nano metricbeat-playbook.yml`            | edit metricbeat playbook                |
| `http://ELK-IP:5601/app/kibana`           | kibana dashboard SUCCESS                |    
| `nano [file name]` `ctrl+w`               | edit and search inside a file           |
