
1. **What is the primary function of DNS?**  
   DNS acts as the internet's phonebook, converting human-readable domain names (like www.example.com) into numerical IP addresses (like 192.0.2.1) that computers use to locate each other.

2. **Describe the process that occurs when you type a website URL into your browser.**  
   The browser first checks its cache for the IP address. If not found, it queries a DNS resolver, which then asks root name servers, TLD servers, and authoritative name servers in sequence to retrieve the IP address, allowing the browser to connect to the website.

3. **What is the role of a DNS resolver?**  
   A DNS resolver helps translate a domain name into its corresponding IP address by querying various DNS servers.

4. **What is the difference between an A Record and an AAAA Record in DNS?**  
   An A Record maps a domain name to an IPv4 address, while an AAAA Record maps it to an IPv6 address.

5. **Explain the purpose of the CNAME DNS record.**  
   A CNAME Record allows one domain name to point to another domain name. For example, www.example.com can point to example.com.

6. **What is an FQDN, and why is it important?**  
   A Fully Qualified Domain Name (FQDN) is the complete domain name, including the hostname and domain name. It ensures a unique address for resources on the internet.

7. **Name the three parts of a Fully Qualified Domain Name (FQDN).**  
   The three parts are the hostname (e.g., "www"), the domain name (e.g., "example"), and the top-level domain (TLD) (e.g., ".com").

8. **What is the function of a PTR DNS record?**  
   A PTR Record is used for reverse DNS lookups, allowing the translation of an IP address back into a domain name.

9. **Define the term “port” in the context of computer networking.**  
   A port is a virtual door that allows data to flow in and out of a device. It is identified by a number and helps in directing data to the right application.

10. **What is the significance of port 443 in network communication?**  
   Port 443 is used for HTTPS, providing secure web traffic by encrypting communication between the browser and the web server.

11. **What are the differences between well-known ports, registered ports, and dynamic/private ports?**  
   - **Well-known ports** (0-1023) are reserved for common services (e.g., HTTP, SSH).
   - **Registered ports** (1024-49151) are assigned to less common services.
   - **Dynamic/private ports** (49152-65535) are used for temporary connections, typically assigned by the OS.

12. **What are the 4 R’s of Domains, and what is the role of each?**  
   - **Registrar:** Authorized by ICANN to sell domain names.
   - **Reseller/Retail Service Provider:** Sells domains without direct ICANN accreditation.
   - **Registrant:** The owner of the domain.
   - **Registry:** Maintains the central database of all domains.

13. **Describe the domain lifecycle and its stages.**  
   - **Expiration:** Domain expires.
   - **Expiration Status (30 days):** Domain can be recovered.
   - **Renewal + Reinstallation:** Costs $35 for renewal.
   - **Renewal + Redemption (35-42 days):** Costs $355 to recover.
   - **Auction:** If not redeemed, domain goes to auction.
   - **Pending Delete (5 days):** Before permanent deletion.
   - **Available Again:** Domain becomes available for new registration.

14. **What are the criteria required for transferring a domain?**  
   The domain must be unlocked, an Auth/EPP code is needed, privacy should be disabled, and the domain should be active, not close to expiration.

15. **What is the AdultBlock service, and what does it protect against?**  
   AdultBlock prevents the registration of domains with adult-related extensions like .xxx, .porn, .adult, and .sex.

16. **What steps must be taken to initiate a domain transfer out of Network Solutions?**  
   You must disable domain protection, turn off private registration, ensure WHOIS information is correct, and request the authorization code from Network Solutions.

17. **What is the purpose of an IPS tag, and when is it used?**  
   An IPS tag is required for transferring domains between registrars in the UK (.uk, .co.uk). It specifies the new registrar.

18. **Explain the difference between static and dynamic IP addresses.**  
   - **Static IP addresses** remain constant and are often used for services requiring a stable address.
   - **Dynamic IP addresses** change periodically and are typically assigned by ISPs for temporary connections.

19. **What is the purpose of a WHOIS check when managing domain issues?**  
   WHOIS allows users to check domain ownership details, status, and contact information, helping in managing transfers and renewals.

20. **How do firewalls utilize port numbers to enhance network security?**  
   Firewalls use port numbers to control traffic flow, allowing or blocking specific services (e.g., blocking port 25 to prevent spam).

---

### Answers to the additional 20 questions:

1. **How does a browser check if it already knows the IP address of a website?**  
   The browser first checks its DNS cache to see if it has stored the IP address from a previous visit.

2. **What role does the root name server play in DNS resolution?**  
   The root name server directs the DNS resolver to the appropriate top-level domain (TLD) server.

3. **What is the function of an MX Record in DNS?**  
   MX Records specify the mail servers responsible for receiving email for a domain.

4. **Why is the SOA DNS record important, and what information does it contain?**  
   The SOA Record contains administrative information about a domain, including the primary name server, contact email, and domain versioning details.

5. **What services typically use port 22 and port 25?**  
   - **Port 22:** Secure Shell (SSH) for remote login.
   - **Port 25:** Simple Mail Transfer Protocol (SMTP) for sending emails.

6. **What is the function of port 3306, and which service commonly uses it?**  
   Port 3306 is used by MySQL database services for database access.

7. **Why are dynamic/private ports important in network connections?**  
   Dynamic/private ports are used for temporary, non-permanent connections, ensuring flexibility and scalability in network communication.

8. **How do ports help in running multiple services on a single device?**  
   Ports allow different applications to listen for and send data on different channels, preventing conflicts between services running simultaneously.

9. **What is a DNS PTR record used for, and when would you use it?**  
   A PTR Record is used for reverse DNS lookups, converting an IP address back into a domain name, often used for verifying the sender in email systems.

10. **What is the role of ICANN in domain licensing?**  
   ICANN oversees the global management of domain names and IP addresses, granting licenses to domain registrars.

11. **What is the responsibility of a domain registrar?**  
   A registrar is responsible for registering domain names, maintaining domain records, and ensuring compliance with ICANN policies.

12. **Explain the difference between a reseller and a registrar in domain management.**  
   A reseller offers domain registration services through partnerships with registrars, while a registrar holds direct ICANN accreditation.

13. **What is the purpose of a Transfer Lock in domain management?**  
   A Transfer Lock prevents unauthorized domain transfers within a certain period, typically the first 60 days after registration.

14. **Describe the role of a Technical Contact in domain management.**  
   The Technical Contact manages the technical aspects of a domain, including DNS settings and server configurations.

15. **What are the steps involved in renewing a domain after it has expired?**  
   After expiration, the owner has 30 days to renew the domain. If not renewed, it enters the redemption phase (35-42 days) with higher fees. After this, the domain might be auctioned or deleted.

16. **What is an Auth code or EPP code, and why is it necessary for domain transfer?**  
   The Auth or EPP code is a unique identifier required to authorize the transfer of a domain between registrars.

17. **What types of IP addresses are there, and how do they differ?**  
   - **Public IP:** Used on the internet, assigned by an ISP.
   - **Private IP:** Used within private networks.
   - **Static IP:** Remains constant.
   - **Dynamic IP:** Changes periodically.

18. **How can a private IP address be found on a local network?**  
   On Windows, you can find a private IP by typing `ipconfig` in the command prompt.

19. **What does DNS propagation mean, and how long does it typically take?**  
   DNS propagation is the time it takes for DNS changes to be updated across all DNS servers. It typically takes 2-48 hours.

20. **Why is it important to disable domain privacy during a domain transfer?**  
   Domain privacy must be disabled to reveal the contact details necessary for transferring the domain to a new registrar.
