from datetime import timedelta
import re

ccna_str = """
Section: 1
0 / 6
Welcome
1. Introduction
1:07
2. How to Make the Most of This Course
6:00
3. The Study Plan
4:32
CCNA Study Plan.pdf
CCNA Study Plan.docx
4. The Udemy Interface
3:29
5. Why Passing the CCNA is Going to Turbo Charge Your Career
3:46
6. Cisco Certifications
7:12
Section: 2
0 / 5
How to Set Up the Lab
7. Important Note
8. Introduction
7:48
9. GNS3 Installation and Configuration
16:42
10. Cisco Packet Tracer Installation and Configuration
6:40
11. GNS3 and Packet Tracer Installation Notes and FAQ
Section: 3
0 / 6
Host to Host Communications
12. Introduction
0:57
13. A (Very) Basic Introduction to Networking
5:44
03-02 A (Very) Basic Introduction to Networking.pdf
14. The OSI Reference Model Overview
9:25
03-03 Open Systems Interconnection OSI Model Overview.pdf
15. The TCP/IP Stack
5:11
03-04 The TCPIP Stack (Transmission Control Protocol Internet Protocol).pdf
16. The Upper OSI Layers
3:23
03-05 The Upper OSI Layers.pdf
17. The Lower OSI Layers
5:06
03-06 The Lower OSI Layers.pdf
Section: 4
0 / 7
The Cisco IOS Operating System
18. Introduction
1:17
19. Cisco Operating Systems
5:08
04-02 Cisco Operating Systems.pdf
20. Making the Initial Connection to a Cisco Device
10:35
04-03 Initial Connection to a Cisco Device.pdf
21. Navigating the Cisco IOS Operating System Part 1
10:17
04-04 Navigating the Cisco IOS Operating System.pdf
22. Navigating the Cisco IOS Operating System Part 2
10:31
23. Cisco IOS Configuration Management
9:05
04-05 IOS Configuration Management.pdf
24. The IOS Operating System - Lab Exercises
04 The IOS Operating System Lab Exercises.zip
Section: 5
0 / 2
OSI Layer 4 - The Transport Layer
25. Introduction
0:41
26. The Transport Layer Header, TCP and UDP
12:30
05-02 The Transport Layer Header, Transmission Control Protocol TCP and User Datagram Protocol UDP.pdf
Section: 6
0 / 8
OSI Layer 3 - The Network Layer
27. Introduction
0:48
28. The IP Header
8:48
06-02 The IP Header.pdf
29. Unicast, Broadcast and Multicast Traffic
4:17
06-03 Unicast, Broadcast and Multicast Traffic.pdf
30. How to Count in Binary
5:04
06-04 Converting from Decimal to Binary.pdf
31. IPv4 Addresses
8:11
06-05 IPv4 Addresses.pdf
32. Calculating an IPv4 Address in Binary
8:22
06-06 Calculating an IPv4 Address in Binary.pdf
33. The Subnet Mask
10:38
06-07 The Subnet Mask.pdf
34. Slash Notation
4:01
06-08 Slash Notation.pdf
Section: 7
0 / 4
IP Address Classes
35. Introduction
0:33
36. Class A IP Addresses
11:31
07-02 Class A IP Addresses.pdf
37. IP Address Classes B and C
4:29
07-03 IP Address Classes B and C.pdf
38. IP Address Classes D and E
8:25
07-04 IP Address Classes D and E.pdf
Section: 8
0 / 15
Subnetting
39. Introduction
0:53
40. CIDR Classless Inter-Domain Routing
5:46
08-02 CIDR Classless Inter-Domain Routing.pdf
41. Subnetting Overview
9:52
08-03 Subnetting Overview.pdf
42. Subnetting Class C Networks and VLSM
11:25
08-04 Subnetting Class C Networks and VLSM.pdf
43. Subnetting Practice Questions
7:56
08-05 Subnetting Practice Question.pdf
44. Variable Length Subnet Masking Example Part 1
10:01
08-06 VLSM Example Part 1.pdf
45. Variable Length Subnet Masking Example Part 2
7:48
08-07 VLSM Example Part 2.pdf
46. Subnetting Large Networks Part 1
11:30
08-08 Subnetting Large Networks Part 1.pdf
47. Subnetting Large Networks Part 2
7:58
08-09 Subnetting Large Networks Part 2.pdf
48. Subnetting on the 4th Octet - Written Example
Subnetting on the 4th Octet - Written Example.pdf
49. Subnetting on the 3rd Octet - Written Example
Subnetting on the 3rd Octet - Written Example.pdf
50. Private IP Addresses Part 1
10:47
08-10 Private IP Addresses Part 1.pdf
51. Private IP Addresses Part 2
9:07
08-11 Private IP Addresses Part 2.pdf
52. Where to Get More Subnetting Practice
3:05
08-12 Where to Get More Subnetting Practice.pdf
53. Additional Subnetting Practice Sites
Section: 9
0 / 2
OSI Layer 2 - The Data-Link Layer
54. Introduction
0:47
55. Local Area Network Layer 2 - Ethernet
10:19
09-02 Local Area Network Layer 2 - Ethernet.pdf
Section: 10
0 / 2
OSI Layer 1 - The Physical Layer
56. Introduction
0:36
57. Ethernet Connection Media
9:53
10-02 Ethernet Connection Media.pdf
Section: 11
0 / 6
Cisco Device Functions
58. Introduction
1:01
59. Switches vs Hubs
4:57
11-02 Switches vs Hubs.pdf
60. Switch Operation
7:52
11-03 Switch Operation.pdf
61. Routers
5:58
11-04 Routers.pdf
62. Other Cisco Devices
4:44
11-05 Other Cisco Devices.pdf
63. Cisco Device Functions - Lab Exercises
11 Cisco Device Functions Lab Exercises.zip
Section: 12
0 / 8
The Life of a Packet
64. Introduction
1:22
65. DNS The Domain Name System
5:47
12-02 DNS The Domain Name System.pdf
66. DNS on Cisco Routers
7:01
12-03 DNS on Cisco Routers.pdf
67. ARP Address Resolution Protocol
7:42
12-04 ARP Address Resolution Protocol.pdf
68. ARP for Routed Traffic
8:57
12-05 ARP for Routed Traffic.pdf
69. Life of a Packet Example Part 1 - DNS
16:29
12-06 The Life of a Packet.pdf
70. Life of a Packet Example Part 2 - HTTP
9:44
71. The Life of a Packet - Lab Exercises
12 The Life of a Packet Lab Exercises.zip
Section: 13
0 / 4
The Cisco Troubleshooting Methodology
72. Introduction
0:44
73. The Cisco Troubleshooting Methodology
10:17
13-02 The Cisco Troubleshooting Methodology.pdf
74. Cisco Troubleshooting Methodology - Lab Example
7:21
75. The Cisco Troubleshooting Methodology - Lab Exercises
13 The Cisco Troubleshooting Methodology Lab Exercises.zip
Section: 14
0 / 8
Cisco Router and Switch Basics
76. Introduction
0:46
77. Basic Router and Switch Configuration
12:41
14-02 Basic Router and Switch Configuration.pdf
78. The Setup Wizard
8:00
79. Speed and Duplex Settings
7:48
14-04 Speed and Duplex Settings.pdf
80. CDP and LLDP
8:22
14-05 CDP and LLDP.pdf
81. Basic Layer 1 and 2 Troubleshooting
7:52
14-06 Basic Layer 1 and Layer 2 Troubleshooting.pdf
82. Basic Layer 1 and 2 Troubleshooting - Lab Demo
9:02
83. Cisco Router and Switch Basics - Lab Exercises
14 Cisco Router and Switch Basics Lab Exercises.zip
Section: 15
0 / 9
Cisco Device Management
84. Introduction
1:11
85. The Boot Up Process
6:57
15-02 The Boot-up Process.pdf
86. The Boot Up Process Lab Demo
7:57
87. Factory Reset and Password Recovery
9:17
15-04 Factory Reset and Password Recovery.pdf
88. Password Recovery Lab Demo
8:32
89. Backing up the System Image and Configuration
8:23
15-06 Backing up the System Image and Configuration.pdf
90. Upgrading IOS
5:06
15-07 Upgrading IOS.pdf
91. Licensing
3:21
15-08 Licensing.pdf
92. Cisco Device Management - Lab Exercises
15 Cisco Device Management Lab Exercises.zip
Section: 16
0 / 9
Routing Fundamentals
93. Introduction
0:58
94. Connected and Local Routes
6:29
16-02 Connected and Local Routes.pdf
95. Connected and Local Routes Lab Demo
6:24
96. Static Routes
6:12
16-04 Static Routes.pdf
97. Static Routes Lab Demo
10:04
98. Summarisation and Default Routes
9:50
16-06 Summarisation and Default Routes.pdf
99. Summary Routes and Longest Prefix Match Lab Demo
12:19
100. Default Routes and Load Balancing Lab Demo
11:39
101. Routing Fundamentals - Lab Exercises
16 Routing Fundamentals Lab Exercises.zip
Section: 17
0 / 15
Dynamic Routing Protocols
102. Introduction
1:38
103. Dynamic Routing Protocols vs Static Routes
10:06
17-02 Dynamic Routing Protocols vs Static Routes.pdf
104. Dynamic Routing Protocols Lab Demo
7:18
105. Routing Protocol Types
7:04
17-04 Routing Protocol Types.pdf
106. Routing Protocol Types Lab Demo
6:52
107. Routing Protocol Metrics
14:58
17-06 Routing Protocol Metrics.pdf
108. Routing Protocol Metrics Lab Demo
15:01
109. Equal Cost Multi Path
4:23
17-08 Equal Cost Multi Path.pdf
110. Equal Cost Multi Path Lab Demo
10:58
111. Administrative Distance
10:07
17-10 Administrative Distance.pdf
112. Administrative Distance Lab Demo
8:25
113. Loopback Interfaces
8:53
17-12 Loopback Interfaces.pdf
114. Adjacencies and Passive Interfaces
7:12
17-13 Adjacencies and Passive Interfaces.pdf
115. Adjacencies and Passive Interfaces Lab Demo
6:37
116. Dynamic Routing Protocols - Lab Exercises
17 Dynamic Routing Protocols Lab Exercises.zip
Section: 18
0 / 4
Connectivity Troubleshooting
117. Introduction
0:59
118. Basic Connectivity Troubleshooting
13:17
18-02 Basic Connectivity Troubleshooting.pdf
119. IP SLA
11:40
18-03 IP SLA.pdf
120. Connectivity Troubleshooting - Lab Exercises
18 Connectivity Troubleshooting Lab Exercises.zip
Section: 19
0 / 5
RIP - the Routing Information Protocol
121. Introduction
0:57
122. RIP the Routing Information Protocol
11:21
19-02 RIP.pdf
123. RIP Advanced Topics
10:31
19-03 RIP Advanced Topics.pdf
124. RIP Lab Demo
14:04
125. RIP Configuration - Lab Exercises
19-1 RIP Configuration Lab Exercises.zip
Section: 20
0 / 9
EIGRP - Enhanced Interior Gateway Routing Protocol
126. Introduction
1:21
127. EIGRP Characteristics and Configuration
11:26
20-02 EIGRP Characteristics and Configuration.pdf
128. EIGRP Verification and Lab Demo
6:34
20-03 EIGRP Verification and Lab Demo.pdf
129. EIGRP Advanced Topics
9:39
20-04 EIGRP Advanced Topics.pdf
130. EIGRP Advanced Topics Lab Demo
11:18
131. EIGRP Successors and Feasible Successors
11:42
20-06 EIGRP Successors and Feasible Successors.pdf
132. EIGRP Metric
8:09
20-07 EIGRP Metric.pdf
133. EIGRP Metric and Successors Lab Demo
8:30
134. EIGRP Configuration - Lab Exercises
20-1 EIGRP Configuration Lab Exercises.zip
Section: 21
0 / 11
OSPF - Open Shortest Path First
135. Introduction
1:09
136. OSPF Characteristics
6:09
21-02 OSPF Characteristics.pdf
137. OSPF Basic Configuration
11:10
21-03 OSPF Basic Configuration.pdf
138. OSPF Basic Configuration Lab Demo
4:39
139. OSPF Advanced Topics
7:15
21-05 OSPF Advanced Topics.pdf
140. OSPF Advanced Topics Lab Demo
7:18
141. OSPF Cost Metric
9:35
21-07 OSPF Cost Metric.pdf
142. OSPF Cost Metric Lab Demo
7:59
143. OSPF Areas
14:18
21-09 OSPF Areas.pdf
144. OSPF Areas Lab Demo
11:10
145. OSPF Configuration - Lab Exercises
21-1 OSPF Configuration Lab Exercises.zip
Section: 22
0 / 11
VLANs Virtual Local Area Networks
146. Introduction
1:01
147. Campus LAN Design - Core, Distribution and Access Layers
8:08
22-02 Campus Design - Access, Distribution and Core Layers.pdf
148. Why we have VLANs
9:51
22-03 Why we have VLANs.pdf
149. VLAN Access Ports
6:56
22-04 VLAN Access Ports.pdf
150. VLAN Access Ports Lab Demo
8:21
151. VLAN Trunk Ports
12:54
22-06 VLAN Trunk Ports.pdf
152. VLAN Trunk Ports Lab Demo
13:28
153. DTP Dynamic Trunking Protocol
5:36
22-08 DTP Dynamic Trunking Protocol.pdf
154. VTP VLAN Trunking Protocol
7:46
22-09 VTP VLAN Trunking Protocol.pdf
155. VTP Lab Demo
10:21
156. VLAN Configuration Lab Exercises
Section: 23
0 / 6
Inter-VLAN Routing
157. Introduction
1:11
158. Router with Separate Interfaces
11:40
23-02 Option 1 - Router with Separate Interfaces.pdf
159. Router on a Stick
11:33
23-03 Option 2 - Router on a Stick.pdf
160. Layer 3 Switch
8:10
23-04 Option 3 - Layer 3 Switch.pdf
161. Layer 3 Switch Lab Demo
9:23
162. VLAN and Inter-VLAN Routing Configuration - Lab Exercises
23-1 VLAN and Inter-VLAN Routing Configuration Lab Exercises.zip
Section: 24
0 / 6
DHCP - Dynamic Host Configuration Protocol
163. Introduction
0:59
164. DHCP Dynamic Host Configuration Protocol
6:31
24-02 DHCP.pdf
165. Cisco DHCP Server
6:49
24-03 Cisco DHCP Server.pdf
166. External DHCP Server
5:16
24-04 External DHCP Server.pdf
167. Cisco DHCP Client
5:02
24-05 Cisco DHCP Client.pdf
168. DHCP Configuration - Lab Exercises
24-1 DHCP Configuration Lab Exercises.zip
Section: 25
0 / 6
HSRP - Hot Standby Router Protocol
169. Introduction
2:00
170. Network Redundancy
8:50
25-02 Network Redundancy.pdf
171. FHRP First Hop Redundancy Protocols
7:09
25-03 FHRP First Hop Redundancy Protocols.pdf
172. HSRP Hot Standby Router Protocol
9:12
25-04 HSRP Hot Standby Router Protocol.pdf
173. HSRP Advanced Topics
7:37
25-05 HSRP Advanced Topics.pdf
174. HSRP Configuration - Lab Exercises
25-1 HSRP Configuration Lab Exercises.zip
Section: 26
0 / 13
STP - Spanning Tree Protocol
175. Introduction
1:38
176. Layer 3 Path Selection and Loop Prevention Review
11:30
26-02 Layer 3 Path Selection and Loop Prevention Review.pdf
177. Why we have the Spanning Tree Protocol
12:42
26-03 Why we have the Spanning Tree Protocol.pdf
178. Spanning Tree Terminology - The Bridge
3:20
26-04 Spanning Tree Terminology - The Bridge.pdf
179. How Spanning Tree Works
20:23
26-05 How Spanning Tree Works.pdf
180. Spanning Tree Versions
7:53
26-06 Spanning Tree Versions.pdf
181. Verification - show spanning-tree
11:11
26-07 Verification - show spanning-tree.pdf
182. Verification - show mac address-table
5:23
26-08 Verification - show mac address-table.pdf
183. Manipulating the Root Bridge Election
7:02
26-09 Manipulating the Root Bridge Election.pdf
184. Spanning Tree and HSRP Alignment
6:56
26-10 Spanning Tree and HSRP Alignment.pdf
185. Portfast and BPDU Guard
4:29
26-11 Portfast and BPDU Guard.pdf
186. STP Troubleshooting - Lab Exercises
26-1 STP Troubleshooting Lab Exercises.zip
187. STP Configuration - Lab Exercises
26-2 STP Configuration Lab Exercises.zip
Section: 27
0 / 7
EtherChannel
188. Introduction
1:21
189. Why we have EtherChannel
8:38
27-02 Why we have EtherChannel.pdf
190. EtherChannel Load Balancing
4:39
27-03 EtherChannel Load Balancing.pdf
191. EtherChannel Protocols and Configuration
10:21
27-04 EtherChannel Protocols and Configuration.pdf
192. EtherChannel Lab Demo
12:59
27-05 EtherChannel Lab Demo.pdf
193. StackWise, VSS and vPC
8:23
27-06 StackWise, VSS and vPC.pdf
194. EtherChannel Configuration - Lab Exercises
27-1 EtherChannel Configuration Lab Exercises.zip
Section: 28
0 / 9
Switch Security
195. Introduction
1:07
196. DHCP Snooping
5:35
28-02 DHCP Snooping.pdf
197. DAI Dynamic ARP Inspection
8:01
28-03 DAI Dynamic ARP Inspection.pdf
198. 802.1X Identity Based Networking
3:13
28-04 802.1X Identity Based Networking.pdf
199. Preventing Unauthorised Devices with Port Security
11:00
28-05 Preventing Unauthorised Devices with Port Security.pdf
200. Preventing Unauthorised Devices with Port Security Lab Demo
8:09
201. Locking Ports to Hosts with Port Security
6:08
28-07 Locking Ports to Hosts with Port Security.pdf
202. Locking Ports to Hosts with Port Security Lab Demo
10:40
203. Port Security Configuration - Lab Exercises
28-1 Port Security Configuration Lab Exercises.zip
Section: 29
0 / 9
ACLs - Access Control Lists
204. Introduction
4:35
205. Access Control Lists Overview
4:29
29-02 ACLs - Access Control Lists.pdf
206. Standard, Extended and Named ACLs
10:42
29-03 Standard, Extended and Named ACLs.pdf
207. ACL Syntax
10:11
29-04 ACL Syntax.pdf
208. ACL Operations
15:20
29-05 ACL Operations.pdf
209. Numbered ACLs Lab Demo
14:03
210. Named ACLs Lab Demo
10:29
211. Packet Filters vs Stateful Firewalls
10:12
29-08 Packet Filters vs Stateful Firewalls.pdf
212. Access Control Lists Configuration - Lab Exercise
29-1 ACL Configuration Lab Exercises.zip
Section: 30
0 / 10
NAT - Network Address Translation
213. Introduction
2:14
214. IPv4 Address Exhaustion and NAT
8:04
30-02 IPv4 Address Exhaustion and NAT.pdf
215. Static NAT
6:48
30-03 Static NAT.pdf
216. NAT Translations - Inside Local, Inside Global, Outside Local, Outside Global
9:37
30-04 NAT Translations - Inside Local, Inside Global, Outside Local, Outside Global.pdf
217. Static NAT Lab Demo
8:21
218. Dynamic NAT
9:18
30-06 Dynamic NAT.pdf
219. Dynamic NAT Lab Demo
7:49
220. PAT Port Address Translation
14:21
30-08 PAT Port Address Translation.pdf
221. PAT Port Address Translation Lab Demo
6:57
222. Network Address Translation Configuration - Lab Exercise
30-1 NAT Configuration Lab Exercises.zip
Section: 31
0 / 11
IPv6 Addressing
223. Introduction
1:29
224. Why We Need IPv6
10:28
31-02 Why we need IPv6.pdf
225. The IPv6 Address Format
7:56
31-03 The IPv6 Address Format.pdf
226. IPv6 Global Unicast Addresses
9:49
31-04 IPv6 Global Unicast Addresses.pdf
227. IPv6 Global Unicast Addresses Lab Demo
7:35
31-05 IPv6 Global Unicast Addresses Lab Demo.pdf
228. EUI-64 Addresses
8:49
31-06 EUI-64 Addresses.pdf
229. Unique Local and Link Local Addresses
10:57
31-07 Unique Local and Link Local Addresses.pdf
230. Link Local Addresses Lab Demo
6:46
231. SLAAC Stateless Address AutoConfiguration
10:02
31-09 SLAAC Stateless Address AutoConfiguration.pdf
232. IPv6 Access Control Lists
7:10
31-10 IPv6 Access Control Lists.pdf
233. IPv6 Addressing - Lab Exercise
31 IPv6 Addressing Lab Exercises.zip
Section: 32
0 / 10
IPv6 Routing
234. Introduction
2:02
235. IPv6 Static Routes
13:36
32-02 IPv6 Static Routes.pdf
236. IPv6 Static Routes Lab Demo
17:44
237. OSPFv3
8:50
32-04 OSPFv3.pdf
238. OSPFv3 Verification
8:23
32-05 OSPFv3 Verification.pdf
239. OSPFv3 Lab Demo
11:32
240. EIGRP for IPv6
5:08
32-07 EIGRP for IPv6.pdf
241. EIGRP for IPv6 Verification
6:17
32-08 EIGRP for IPv6 Verification.pdf
242. EIGRP for IPv6 Lab Demo
7:03
243. IPv6 Routing Configuration - Lab Exercise
32-1 IPv6 Routing Configuration Lab Exercises.zip
Section: 33
0 / 18
WAN - Wide Area Networks
244. Introduction
1:37
245. WAN Overview
4:51
33-02 WAN Overview.pdf
246. VPN - Virtual Private Networks
9:52
33-03 VPN Virtual Private Networks.pdf
247. WAN Connectivity Options
8:45
33-04 WAN Connectivity Options.pdf
248. Leased Lines
10:19
33-05 Leased Lines.pdf
249. HDLC and PPP
8:21
33-06 HDLC and PPP.pdf
250. HDLC and PPP Lab Demo
8:41
251. PAP Authentication
10:28
33-08 PAP Authentication.pdf
252. CHAP Authentication
12:24
33-09 CHAP Authentication.pdf
253. MLP MultiLink PPP
5:41
33-10 MLP MultiLink PPP.pdf
254. MLP Lab Demo
8:11
255. MPLS Multi Protocol Label Switching
12:19
33-12 MPLS Multi Protocol Label Switching.pdf
256. PPPoE Point to Point Protocol over Ethernet
7:38
33-13 PPPoE Point to Point Protocol over Ethernet.pdf
257. PPPoE Lab Demo
4:06
258. GRE Generic Routing Encapsulation
8:01
33-15 GRE Generic Routing Encapsulation.pdf
259. GRE Lab Demo
10:01
260. WAN Topology Options
4:40
33-17 WAN Topology Options.pdf
261. WAN Configuration - Lab Exercise
33-1 WAN Configuration Lab Exercises.zip
Section: 34
0 / 10
BGP - Border Gateway Protocol
262. Introduction
1:52
263. Why We Need BGP
12:48
34-02 The Need for BGP.pdf
264. BGP for Service Providers
13:17
34-03 BGP for Service Providers.pdf
265. Configuring BGP Neighbors
14:18
34-04 Configuring BGP Neighbors.pdf
266. Advertising Routes in BGP
10:34
34-05 Advertising Routes in BGP.pdf
267. BGP for Service Providers Lab Demo
16:16
34 BGP for Service Providers Lab.zip
268. BGP for Enterprises
16:12
34-07 BGP for Enterprises.pdf
269. BGP in MPLS Networks
9:06
34-08 BGP in MPLS Networks.pdf
270. BGP for Enterprises Lab Demo
7:39
34-09 BGP in MPLS Networks Lab Demo.pdf
271. BGP Configuration - Lab Exercise
34-1 BGP Configuration Lab Exercises.zip
Section: 35
0 / 12
Cisco Device Security
272. Introduction
1:25
273. Line Level Security
13:53
35-02 Line Level Security.pdf
274. Privileged Exec and Password Encryption
4:32
35-03 Privileged Exec and Password Encryption.pdf
275. Line Level Security Lab Demo
9:34
35-04 Line Level Security Lab Demo.pdf
276. Usernames and Privilege Levels
11:20
35-05 Usernames and Privilege Levels.pdf
277. SSH Secure Shell
4:47
35-06 SSH Secure Shell.pdf
278. SSH Secure Shell Lab Demo
5:32
35-07 SSH Secure Shell Lab Demo.pdf
279. AAA Authentication, Authorization and Accounting
12:10
35-08 AAA Authentication, Authorization and Accounting.pdf
280. AAA Configuration
8:38
35-09 AAA Configuration.pdf
281. Global Security Best Practices
9:48
35-10 Global Security Best Practices.pdf
282. Global Security Best Practices Lab Demo
5:01
35-11 Global Security Best Practices Lab Demo.pdf
283. Cisco Device Security Configuration - Lab Exercises
35-1 Cisco Device Security Configuration Lab Exercises.zip
Section: 36
0 / 9
Network Device Management
284. Introduction
1:29
285. Syslog
15:05
36-02 Syslog.pdf
286. Terminal Monitor and Logging Synchronous
6:10
36-03 Terminal Monitor and Logging Synchronous.pdf
287. Syslog Lab Demo
6:10
36-04 Syslog Lab Demo.pdf
288. SNMP Simple Network Management Protocol
9:19
36-05 SNMP Simple Network Management Protocol.pdf
289. SNMP Lab Demo
3:57
36-06 SNMP Lab Demo.pdf
290. Syslog vs SNMP
5:53
36-07 Syslog vs SNMP.pdf
291. SPAN Switched Port Analyser
11:02
36-08 SPAN Switched Port Analyser.pdf
292. Network Device Management - Lab Exercises
36 Network Device Management Lab Exercises.zip
Section: 37
0 / 5
QoS Quality of Service
293. Introduction
1:24
294. QoS Overview
19:08
37-02 QoS Overview.pdf
295. Classification and Marking
14:22
37-03 Classification and Marking.pdf
296. Congestion Management
10:51
37-04 Congestion Management.pdf
297. Policing and Shaping
12:45
37-05 Policing and Shaping.pdf
Section: 38
0 / 9
Cloud Computing
298. Introduction
1:28
299. Traditional IT Deployment Models
6:10
38-02 Traditional IT Deployment Models - On Prem and Colo.pdf
300. Defining Cloud Computing
6:55
38-03 Defining Cloud Computing.pdf
301. Cloud Computing Case Study
13:38
38-04 Cloud Computing Case Study.pdf
302. Server Virtualization
13:08
38-05 Server Virtualization.pdf
303. Virtualizing Network Devices
14:09
38-06 Virtualizing Network Devices.pdf
304. Cloud Service Models
10:32
38-07 Cloud Service Models.pdf
305. Cloud Deployment Models
11:05
38-08 Cloud Deployment Models.pdf
306. Cloud Computing Advantages
8:31
38-09 Cloud Computing Advantages.pdf
Section: 39
0 / 4
SDN Software-Defined Networking
307. Introduction
1:30
308. SDN Software Defined Networking
8:11
39-02 SDN Software Defined Networking.pdf
309. The Cisco APIC-EM
13:08
39-03 The Cisco APIC-EM.pdf
310. Thank You!
1:00
"""

aws_str = """
Section: 1
0 / 4
Introduction
1. Introduction To The Certified Developer - Associate Course
1:56
2. Information For Students Who Have Completed The Solutions Architect Course
1:39
3. Exam Blue Print
5:46
2018 Exam BluePrint
4. The Free Alexa Skill For Amazon Echo
3:31
Section: 2
0 / 5
Beginners Guide To IAM
5. IAM 101
5:18
6. IAM Lab
19:23
7. IAM Summary
3:38
AWS Security Best Practices - Whitepaper
8. AWS This Week
1:13
Quiz 1: Identity Access Management Quiz
Section: 3
0 / 13
Beginners Guide to EC2
9. EC2 101
20:45
10. EC2 Lab
13:47
index.html
11. Using Putty For SSH (Windows Users Only)
6:31
12. Elastic Load Balancer
8:01
13. Route53 Lab
11:23
14. CLI Demo
12:28
15. EC2 with S3 Role Lab
10:36
16. RDS 101
9:11
RDSBootStrap.sh
17. RDS Lab
14:11
rds.zip
18. RDS Multi-AZ & Read Replicas
16:39
19. Elasticache 101
6:45
20. Summary
10:15
Quiz 2: EC2 Quiz
Section: 4
0 / 12
S3
21. S3 101
21:28
22. S3 Security
3:53
23. S3 Policies
15:24
24. S3 Encryption
8:39
25. Setup Encryption On An S3 Bucket
7:23
26. CORS Configuration Lab
11:05
Website_files.zip
27. CloudFront
10:59
28. CloudFront Lab
24:22
29. S3 Performance Optimization
5:12
30. S3 Performance Update
1:49
31. S3 Summary
18:56
S3 FAQ
Quiz 3: S3 Quiz
Section: 5
0 / 15
Introduction to Serverless Computing
32. Serverless 101
8:18
33. Lambda
12:44
34. API Gateway
16:32
35. Build a Simple Serverless Website with Route 53, API Gateway, Lambda and S3
18:29
serverless_website.zip
36. Version Control With Lambda
9:04
37. Using Polly to Help Your Exam Lab - Part 1
17:55
polly.zip
PollyJson.zip
38. Using Polly to Help Your Exam Lab - Part 2
16:18
polly.zip
39. Make an Alexa Skill Lab
17:41
Github Repo for our Alexa Skill
40. Step Functions
6:56
41. X-Ray
13:24
X-Ray Link
eb-java-scorekeep-xray-gettingstarted-v1.3.zip
42. Advanced API Gateway
4:21
43. Guru Of The Week
1:12
44. Serverless Summary
5:01
Quiz 4: Introduction to Serverless Computing
45. Learn More About Serverless
0:40
Section: 6
0 / 9
DynamoDB
46. Introduction to DynamoDB
12:43
47. Creating a DynamoDB Table Lab
14:52
dynamodb_lab.sh
Install_Commands.zip
48. Indexes Deepdive
3:46
49. Scan vs Query API Call
9:03
50. DynamoDB Provisioned Throughput
6:40
51. DynamoDB Accelerator (DAX)
4:36
52. Elasticache
8:16
53. DynamoDB Summary
8:15
Quiz 5: DynamoDB
Section: 7
0 / 4
KMS & Encryption on AWS
54. KMS 101
8:27
55. KMS API Calls
9:43
56. KMS Envelope Encryption
2:23
57. KMS Exam Tips
3:57
Section: 8
0 / 14
Other AWS Services
58. SQS
12:48
59. Simple Notification Service
5:19
60. Mobile App
0:47
61. SES vs SNS
3:06
62. ElasticBeanstalk 101
3:46
63. Deploying Applications Using ElasticBeanstalk
4:14
Version1.zip
64. Updating ElasticBeanstalk
10:02
Version2.zip
65. Advanced ElasticBeanstalk
2:25
66. RDS & ElasticBeanstalk
3:05
67. Kinesis 101
9:25
68. Kinesis Lab
5:54
Kinesis Cloud Formation Template URL
69. Maker Labs
1:02
70. Other AWS Services Summary
7:46
Quiz 6: Other AWS Services Quiz
Section: 9
0 / 13
Developer Theory
71. What Is CI/CD
11:37
72. CodeCommit 101
3:03
73. CodeCommit Lab
19:31
74. CodeDeploy Lab 1
10:15
CodeDeployCommands.txt
CodeDeployDemo-EC2-Permissions.json
mywebapp.zip
75. CodeDeploy Lab 2
9:29
CodeDeployCommands.txt
CodeDeployDemo-EC2-Permissions.json
mywebapp.zip
CodeDeploy Agent Region Specific Bucket Names
76. CodeDeploy Lab 3
9:24
Templates in YAML & JSON
CodeDeployCommands.txt
CodeDeployDemo-EC2-Permissions.json
mywebapp.zip
77. CodePipeline 101
5:03
78. CodePipeline Lab
18:54
mywebapp2.0.zip
79. Advanced CodeDeploy the AppSpec File
13:20
80. Docker and CodeBuild Lab Part 1
23:43
docker.zip
Docker Install Instructions
81. Docker and CodeBuild Lab Part 2
13:54
docker.zip
Docker Install Instructions
82. Developer Theory Summary
9:27
Practicing CI / CD on AWS - Whitepaper
Blue / Green Deployments on AWS - Whitepaper
Quiz 7: Dev Theory Quiz
Section: 10
0 / 5
Advanced IAM
83. Web Identity Federation
3:49
84. Cognito User Pools
3:12
85. Inline Policies vs Managed Policies vs Custom Policies
4:52
86. Advanced IAM Summary
3:52
Quiz 8: Advanced IAM
Section: 11
0 / 2
The End!!
87. What to expect?
2:54
Quiz 9: Mega Quiz 1
"""

txt_str = """

"""

secs =  aws_str.split("Section")
# print len(secs)
# print secs[39]

table = []

l=0
for sec in secs:									#for every section
	if len(sec)==1:		#empty line [0]
		# print(len(sec))
		continue

	lines = sec.split("\n")

	sec_num = lines[0].split(" ")[-1]
	table.append(sec_num)

	for i in range(len(lines)):
		# print(lines[i])
		if (lines[i].find(".")!=-1 and 					#found lesson, ignore attachments
				lines[i].find("pdf")==-1 and 
				lines[i].find("docx")==-1 and
				lines[i].find("Lab Exercise")==-1):		

			# m = re.search()

			if(lines[i+1].find(":")!=-1):		#check if a time exists in following line
				# print("in condition")
				table.append(lines[i] + " " + lines[i+1])

	table.append("\n")
	
	# l = l+1
	# if l>2:
		# break;

# print(len(table))
# print(table)

for cont in table:
	print(cont)



def print_secs_times(print_fmt=1):
	"""
	print_fmt:
		1	-	Total Time
		2	-	Section Number, Section Time, Total Time
		3	-	Section Number, lesson Times, Section Time, Total Time
	"""
	section_time = timedelta()
	tot_time = timedelta()
	total_seconds = 0;


	for i in range(0,len(table)):

		if (len(table[i])<3 and table[i]!="\n"):		#print section num
			if print_fmt>=2:	
				print("\n")
				print("Section " + str(table[i]) )
		elif (table[i]=="\n" or table[i]==""):
			tot_time = tot_time + section_time
			(sec_h, sec_m, sec_s) = get_hms(section_time.total_seconds())
			section_time = timedelta()

			if print_fmt>=2:
				print("\t Section Time - " + str(sec_h).split(".")[0] + ":" +
								  			str(sec_m).split(".")[0] + ":" +
								  			str(sec_s).split(".")[0] )
			continue
		else:
			time = table[i].split(" ")[-1]
			if print_fmt>=3:
				print time 
			time = time.split(":")

			# print(time)

			# total_seconds = (int(time[0])*60) + int(time[1]) + total_seconds

			mins = int(time[0])
			secs = int(time[1])
			section_time = section_time + timedelta(minutes=mins, seconds=secs)


	(tot_h, tot_m, tot_s) = get_hms(tot_time.total_seconds())
	# (tot_h, tot_m, tot_s) = get_hms(total_seconds)

	# print(tot_time.total_seconds())
	if print_fmt>=1:
		print("\t\t\tTotal Time -  " + str(tot_h).split(".")[0] + ":" +
								  str(tot_m).split(".")[0] + ":" +
								  str(tot_s).split(".")[0] )

def get_hms(seconds_total):
	tot_h = seconds_total // 3600
	tot_m = seconds_total % 3600 // 60
	tot_s = seconds_total % 3600 % 60

	return(tot_h, tot_m, tot_s)




print_secs_times(3)