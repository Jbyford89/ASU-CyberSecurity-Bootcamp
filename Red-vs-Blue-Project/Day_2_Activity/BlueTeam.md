## Day 2 Blue Team

1. Identify the offensive traffic.
   - Identify the traffic between your machine and the web machine:
     - When did the interaction occur?
       - `April 21 @ about 6pm`
     - What responses did the victim send back?
       - `401, 301, 207, 404, 200`
     - What data is concerning from the Blue Team perspective?
       - `Spike in connections over time`

2. Find the request for the hidden directory.
   - In your attack, you found a secret folder. Let's look at that interaction between these two machines.
     - How many requests were made to this directory? At what time and from which IP address(es)?
       - `16,747`
     - Which files were requested? What information did they contain?
       - `The connect_to_corp_server was requested 3 times.`
     - What kind of alarm would you set to detect this behavior in the future?
       - `An alarm that would trigger for any machine that trys to access this folder.`
     - Identify at least one way to harden the vulnerable machine that would mitigate this attack.
       - `Remove this directory along with the file completely.`

3. Identify the brute force attack.
   - After identifying the hidden directory, you used Hydra to brute-force the target server. Answer the following questions:
     - Can you identify packets specifically from Hydra?
       - `Yes, you can use url.path: /company_folders/secret_folder/ to show more details. Hydra is shown in the user_agent.original section`
     - How many requests were made in the brute-force attack?
       - `16,747`
     - How many requests had the attacker made before discovering the correct password in this one?
       - `5 were successful out of 16,747`
     - What kind of alarm would you set to detect this behavior in the future and at what threshold(s)?
       - `An alert that would trigger if 401 Unauthorized is returned from any server over a certain threshold of forgotten passwords.`
     - Identify at least one way to harden the vulnerable machine that would mitigate this attack.
       - `After limliting the 401 responses from the server, the server can automatically drop traffic from the offending IPs for 1 hour.`

4. Find the WebDav connection.
   - Use your dashboard to answer the following questions:
     - How many requests were made to this directory?
       - `64` 
     - Which file(s) were requested?
       - `shell.php`
     - What kind of alarm would you set to detect such access in the future?
       - `Anytime this directory is accessed an alarm would trigger by any unauthroized machines or users.`
     - Identify at least one way to harden the vulnerable machine that would mitigate this attack.
       - `Make sure that connections are not accessible through the browser.`
       - `You can also restrict access to the shared folder.`

5. Identify the reverse shell and meterpreter traffic.
   - To finish off the attack, you uploaded a PHP reverse shell and started a meterpreter shell session. Answer the following questions:
     - Can you identify traffic from the meterpreter session?
       - Yes, by using `source.ip : 192.168.1.105 and destination.port : 4444`
     - What kinds of alarms would you set to detect this behavior in the future?
       - `Set an alarm to trigger anytime port 4444 is accessed. As well as an alarm that will trigger if any .php files are uploaded.`
     - Identify at least one way to harden the vulnerable machine that would mitigate this attack.
       - `Remove the ability to upload files to this directory using the web browser.`