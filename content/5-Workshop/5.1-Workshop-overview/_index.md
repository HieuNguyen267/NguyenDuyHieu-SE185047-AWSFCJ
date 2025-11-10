
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Introduction"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Introduction" ) 
) 
title : "Introduction"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo date :  "`r Sys.Date()`"    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo date :  "`r Sys.Date()`"  ) 
) 
date :  "`r Sys.Date()`" 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo weight : 1    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo weight : 1  ) 
) 
weight : 1 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo chapter : false   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo chapter : false ) 
) 
chapter : false

E:\thuctap\report mau\fcj-workshop-template-main>(
echo pre : " <b> 5.1. </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.1. </b> " ) 
) 
pre : " <b> 5.1. </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### VPC endpoints   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### VPC endpoints ) 
) 
#### VPC endpoints

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + **VPC endpoints** are virtual devices. They are horizontally scaled, redundant, and highly available VPC components. They allow communication between your compute resources and AWS services without imposing availability risks.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + **VPC endpoints** are virtual devices. They are horizontally scaled, redundant, and highly available VPC components. They allow communication between your compute resources and AWS services without imposing availability risks. ) 
) 
+ **VPC endpoints** are virtual devices. They are horizontally scaled, redundant, and highly available VPC components. They allow communication between your compute resources and AWS services without imposing availability risks.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Compute resources running in VPC can access  **Amazon S3**  using a Gateway endpoint. PrivateLink interface endpoints can be used by compute resources running in VPC or on-premises.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Compute resources running in VPC can access  **Amazon S3**  using a Gateway endpoint. PrivateLink interface endpoints can be used by compute resources running in VPC or on-premises. ) 
) 
+ Compute resources running in VPC can access  **Amazon S3**  using a Gateway endpoint. PrivateLink interface endpoints can be used by compute resources running in VPC or on-premises.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Workshop overview   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Workshop overview ) 
) 
#### Workshop overview

E:\thuctap\report mau\fcj-workshop-template-main>(
echo In this workshop, you will use two VPCs.    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo In this workshop, you will use two VPCs.  ) 
) 
In this workshop, you will use two VPCs. 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + **"VPC Cloud"** is for cloud resources such as a  **Gateway endpoint** and an EC2 instance to test with.    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + **"VPC Cloud"** is for cloud resources such as a  **Gateway endpoint** and an EC2 instance to test with.  ) 
) 
+ **"VPC Cloud"** is for cloud resources such as a  **Gateway endpoint** and an EC2 instance to test with. 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + **"VPC On-Prem"** simulates an on-premises environment such as a factory or corporate datacenter. An EC2 instance running strongSwan VPN software has been deployed in "VPC On-prem" and automatically configured to establish a Site-to-Site VPN tunnel with AWS Transit Gateway. This VPN simulates connectivity from an on-premises location to the AWS cloud. To minimize costs, only one VPN instance is provisioned to support this workshop. When planning VPN connectivity for your production workloads, AWS recommends using multiple VPN devices for high availability.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + **"VPC On-Prem"** simulates an on-premises environment such as a factory or corporate datacenter. An EC2 instance running strongSwan VPN software has been deployed in "VPC On-prem" and automatically configured to establish a Site-to-Site VPN tunnel with AWS Transit Gateway. This VPN simulates connectivity from an on-premises location to the AWS cloud. To minimize costs, only one VPN instance is provisioned to support this workshop. When planning VPN connectivity for your production workloads, AWS recommends using multiple VPN devices for high availability. ) 
) 
+ **"VPC On-Prem"** simulates an on-premises environment such as a factory or corporate datacenter. An EC2 instance running strongSwan VPN software has been deployed in "VPC On-prem" and automatically configured to establish a Site-to-Site VPN tunnel with AWS Transit Gateway. This VPN simulates connectivity from an on-premises location to the AWS cloud. To minimize costs, only one VPN instance is provisioned to support this workshop. When planning VPN connectivity for your production workloads, AWS recommends using multiple VPN devices for high availability.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![overview](/images/5-Workshop/5.1-Workshop-overview/diagram1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![overview](/images/5-Workshop/5.1-Workshop-overview/diagram1.png) ) 
) 
![overview](/images/5-Workshop/5.1-Workshop-overview/diagram1.png)
