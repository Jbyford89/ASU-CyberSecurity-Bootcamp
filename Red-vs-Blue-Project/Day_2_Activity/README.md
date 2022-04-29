
## Day 2 Activity File: Incident Analysis with Kibana


Today, you will use Kibana to analyze logs taken during the Red Team attack. As you analyze, you will use the data to develop ideas for new alerts that can improve your monitoring.

**Important**: Any time you use data in a dashboard to justify an answer, take a screenshot. You'll need these screenshots when you develop your presentation on Day 3 of this project.

:warning: **Heads Up**: To complete today's part of the project, you must complete steps 1-6 from the last class. Finding the flag isn't critical, but you want to get past the point of uploading the reverse shell script.

### Instructions

Even though you already know what you did to exploit the target, analyzing the logs is still valuable. It will teach you:
- What your attack looks like from a defender's perspective.

- How stealthy or detectable your tactics are.

- Which kinds of alarms and alerts SOC and IR professionals can set to spot attacks like yours while they occur, rather than after.



#### Adding Kibana Log Data

To start viewing logs in Kibana, we will need to import our filebeat, metricbeat and packetbeat data.

Double-click the Google Chrome icon on the Windows host's desktop to launch Kibana. If it doesn't load as the default page, navigate to http://192.168.1.105:5601.

This will open 4 tabs automatically, but for now, we only want to use the first tab.

Click on the `Explore My Own` link to get started.

##### Adding Appache logs
Click on `Add Log Data`
![](Images/Elk-setup-2/Add_logs.png)

Click on `Apache logs` 

![](Images/Elk-setup-2/apache_logs.png)

Scroll to the bottom of the page. 
Click on `Check Data`
You should see a message highlighted in green: `Data successfully received from this module`

![](Images/Elk-setup-2/apache_data.png)

Return to the Home screen by moving back 2 pages.

##### Adding System Logs
Click on `Add Log Data`


![](Images/Elk-setup-2/Add_logs.png))


Click on `System logs` 

![](Images/Elk-setup-2/system_logs.png)

Scroll to the bottom of the page. 
Click on `Check Data`
You should see a message highlighted in green: `Data successfully received from this module`

![](Images/Elk-setup-2/system_data.png)

Return to the Home screen by moving back 2 pages.

#### Adding Apache Metrics
Click on `Add Metric Data`

![](Images/Elk-setup-2/add_metrics.png)

Click on `Apache Metrics` 

![](Images/Elk-setup-2/apache_metrics.png)

Scroll to the bottom of the page. 
Click on `Check Data`
You should see a message highlighted in green: `Data successfully received from this module`

![](Images/Elk-setup-2/apache_metrics_data.png)

Return to the Home screen by moving back 2 pages.

#### Adding System Metrics
Click on `Add Metric Data`

![](Images/Elk-setup-2/add_metrics.png)

Click on `System Metrics` 

![](Images/Elk-setup-2/system_metrics.png)

Scroll to the bottom of the page. 
Click on `Check Data`
You should see a message highlighted in green: `Data successfully received from this module`

![](Images/Elk-setup-2/system_metrics_data.png)

Close Google Chrome and all of it's tabs. Double click on Chrome to re-open it.

#### Dashboard Creation

Create a Kibana dashboard using the pre-built visualizations. On the left navigation panel, click on **Dashboards**.

Click on **Create dashboard** in the upper right hand side. 

![](Images/Elk-setup-2/create_dashboard.png)

On the new page click on **Add an existing** to add the following existing reports:

- `HTTP status codes for the top queries [Packetbeat] ECS`
- `Top 10 HTTP requests [Packetbeat] ECS`
- `Network Traffic Between Hosts [Packetbeat Flows] ECS`
- `Top Hosts Creating Traffic [Packetbeat Flows] ECS`
- `Connections over time [Packetbeat Flows] ECS`
- `HTTP error codes [Packetbeat] ECS`
- `Errors vs successful transactions [Packetbeat] ECS`
- `HTTP Transactions [Packetbeat] ECS`

**Example for adding the first report:**

![](Images/Elk-setup-2/add_existing.png)

![](Images/Elk-setup-2/search.png)

The remaining steps will be a process of self-discovery to be completed without screen shot examples.

Get familiar with running search queries in the `Discover` screen with Packetbeat. This will be located on your fourth tab in Chrome. 

- On the Discover page, locate the search field.
- Start typing `source` and notice the suggestions that come up.
- Search for the `source.ip` of your attacking machine.
- Use `AND` and `NOT` to further filter you search and look for communications between your attacking machine and the victim machine.
- Other things to look for: 
	- `url`
	- `status_code`
	- `error_code`

After creating your dashboard and becoming familiar with the search syntax, use these tools to answer the questions below:


1. Identify the offensive traffic.
   - Identify the traffic between your machine and the web machine:
     - When did the interaction occur?
     - What responses did the victim send back?
     - What data is concerning from the Blue Team perspective?

2. Find the request for the hidden directory.
   - In your attack, you found a secret folder. Let's look at that interaction between these two machines.
     - How many requests were made to this directory? At what time and from which IP address(es)?
     - Which files were requested? What information did they contain?
     - What kind of alarm would you set to detect this behavior in the future?
     - Identify at least one way to harden the vulnerable machine that would mitigate this attack.

3. Identify the brute force attack.
   - After identifying the hidden directory, you used Hydra to brute-force the target server. Answer the following questions:
     - Can you identify packets specifically from Hydra?
     - How many requests were made in the brute-force attack?
     - How many requests had the attacker made before discovering the correct password in this one?
     - What kind of alarm would you set to detect this behavior in the future and at what threshold(s)?
     - Identify at least one way to harden the vulnerable machine that would mitigate this attack.

4. Find the WebDav connection.
   - Use your dashboard to answer the following questions:
     - How many requests were made to this directory? 
     - Which file(s) were requested?
     - What kind of alarm would you set to detect such access in the future?
     - Identify at least one way to harden the vulnerable machine that would mitigate this attack.

5. Identify the reverse shell and meterpreter traffic.
   - To finish off the attack, you uploaded a PHP reverse shell and started a meterpreter shell session. Answer the following questions:
     - Can you identify traffic from the meterpreter session?
     - What kinds of alarms would you set to detect this behavior in the future?
     - Identify at least one way to harden the vulnerable machine that would mitigate this attack.


---
© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
