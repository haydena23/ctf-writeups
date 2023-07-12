# Wireshark Phishing
[suspicious.pcap](/Wireshark%20Phishing/suspicious.pcap)
## Question 1
```
There are objects in the PCAP file that can exported by Wireshark and/or Tshark. What type of objects can be exported from this PCAP?
```

For this, simply open up the PCAP file in Wireshark. Go to File > Export Objects > HTTP. We can see there are two files to be exported, so we know they are HTML objects.

<b><u>Answer:</b></u>  HTTP

---
## Question 2
```
What is the file name of the largest file we can export?
```

We can see in the Export Objects window that app.php has the largest size of 808 kB.

<b><u>Answer:</b></u>  app.php

---

## Question 3
```
What packet number starts that app.php file?
```

We can see that from the Export Objects window that it is either packet 8 or packet 687. Packet 687 is the second OK after downloading the file.

<b><u>Answer:</b></u>  687

---

## Question 4
```
What is the IP of the Apache server?
```
We can see that the GET requests were being sent to 192.185.57.242, therefore we can assume that this is the server.

<b><u>Answer:</b></u> 192.185.57.242

---

## Question 5
```
What file is saved to the infected host?
```

For this problem, you can rightclick on one of the packets and click Follow > HTTP Stream. Here, we can see the HTML that has been executed. At the bottom, it appears to have saved a file by the name of "Ref_Sept24-2020.zip."

<b><u>Answer:</b></u> Ref_Sept24-2020.zip

---
## Question 6
```
Attackers used bad TLS certificates in this traffic. Which countries were they reistered to? Submit the names of the countries in alphabetical order seperated by a commas (Ex: Norway, South Korea).
```

This problem was a little trickier. Here, we want to search Wireshark for all of the packets that contained a certificate using the display filter:
```
tls.handshake.certificate
```
From here, we can look at the details of each of the packets. Click on:
1. Transport Layer Security 
2. TLSv1.2 Record Layer 
3. Handshake Protocol: Certificate
4. Certificates
5. Certificate
6. signedCertificate 
7. issuer 
8. rdnSequence

This shows us the country code that the certificate was issued by. If we look at all of the certificates, we find that four countries were involved. Ireland, Israel, South Sudan, United States.

<b><u>Answer</b></u>: Ireland, Israel, South Sudan, United States

---
## Question 7
```
Is the host infected (Yes/No)?
```

<b><u>Answer:</b></u> Yes