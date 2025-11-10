
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title: "Workshop"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title: "Workshop" ) 
) 
title: "Workshop"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo date: 2025-01-01   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo date: 2025-01-01 ) 
) 
date: 2025-01-01T00:00:00Z

E:\thuctap\report mau\fcj-workshop-template-main>(
echo weight: 5   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo weight: 5 ) 
) 
weight: 5

E:\thuctap\report mau\fcj-workshop-template-main>(
echo chapter: false   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo chapter: false ) 
) 
chapter: false

E:\thuctap\report mau\fcj-workshop-template-main>(
echo pre: " <b> 5. </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre: " <b> 5. </b> " ) 
) 
pre: " <b> 5. </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo {{% notice warning %}}   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo {{% notice warning %}} ) 
) 
{{% notice warning %}}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ⚠️ **Note:** The information below is for reference purposes only. Please **do not copy verbatim** for your report, including this warning.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ⚠️ **Note:** The information below is for reference purposes only. Please **do not copy verbatim** for your report, including this warning. ) 
) 
⚠️ **Note:** The information below is for reference purposes only. Please **do not copy verbatim** for your report, including this warning.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo {{% /notice %}}   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo {{% /notice %}} ) 
) 
{{% /notice %}}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo # Secure Hybrid Access to S3 using VPC Endpoints   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo # Secure Hybrid Access to S3 using VPC Endpoints ) 
) 
# Secure Hybrid Access to S3 using VPC Endpoints

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Overview   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Overview ) 
) 
#### Overview

E:\thuctap\report mau\fcj-workshop-template-main>(
echo **AWS PrivateLink** provides private connectivity to AWS services from VPCs and your on-premises networks, without exposing your traffic to the Public Internet.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo **AWS PrivateLink** provides private connectivity to AWS services from VPCs and your on-premises networks, without exposing your traffic to the Public Internet. ) 
) 
**AWS PrivateLink** provides private connectivity to AWS services from VPCs and your on-premises networks, without exposing your traffic to the Public Internet.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo In this lab, you will learn how to create, configure, and test VPC endpoints that enable your workloads to reach AWS services without traversing the Public Internet.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo In this lab, you will learn how to create, configure, and test VPC endpoints that enable your workloads to reach AWS services without traversing the Public Internet. ) 
) 
In this lab, you will learn how to create, configure, and test VPC endpoints that enable your workloads to reach AWS services without traversing the Public Internet.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo You will create two types of endpoints to access Amazon S3: a Gateway VPC endpoint, and an Interface VPC endpoint. These two types of VPC endpoints offer different benefits depending on if you are accessing Amazon S3 from the cloud or your on-premises location   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo You will create two types of endpoints to access Amazon S3: a Gateway VPC endpoint, and an Interface VPC endpoint. These two types of VPC endpoints offer different benefits depending on if you are accessing Amazon S3 from the cloud or your on-premises location ) 
) 
You will create two types of endpoints to access Amazon S3: a Gateway VPC endpoint, and an Interface VPC endpoint. These two types of VPC endpoints offer different benefits depending on if you are accessing Amazon S3 from the cloud or your on-premises location

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + **Gateway** - Create a gateway endpoint to send traffic to Amazon S3 or DynamoDB using private IP addresses.You route traffic from your VPC to the gateway endpoint using route tables.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + **Gateway** - Create a gateway endpoint to send traffic to Amazon S3 or DynamoDB using private IP addresses.You route traffic from your VPC to the gateway endpoint using route tables. ) 
) 
+ **Gateway** - Create a gateway endpoint to send traffic to Amazon S3 or DynamoDB using private IP addresses.You route traffic from your VPC to the gateway endpoint using route tables.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + **Interface** - Create an interface endpoint to send traffic to endpoint services that use a Network Load Balancer to distribute traffic. Traffic destined for the endpoint service is resolved using DNS.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + **Interface** - Create an interface endpoint to send traffic to endpoint services that use a Network Load Balancer to distribute traffic. Traffic destined for the endpoint service is resolved using DNS. ) 
) 
+ **Interface** - Create an interface endpoint to send traffic to endpoint services that use a Network Load Balancer to distribute traffic. Traffic destined for the endpoint service is resolved using DNS.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Content   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Content ) 
) 
#### Content

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. [Workshop overview](5.1-Workshop-overview)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. [Workshop overview](5.1-Workshop-overview) ) 
) 
1. [Workshop overview](5.1-Workshop-overview)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. [Prerequiste](5.2-Prerequiste/)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. [Prerequiste](5.2-Prerequiste/) ) 
) 
2. [Prerequiste](5.2-Prerequiste/)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. [Access S3 from VPC](5.3-S3-vpc/)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. [Access S3 from VPC](5.3-S3-vpc/) ) 
) 
3. [Access S3 from VPC](5.3-S3-vpc/)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 4. [Access S3 from On-premises](5.4-S3-onprem/)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 4. [Access S3 from On-premises](5.4-S3-onprem/) ) 
) 
4. [Access S3 from On-premises](5.4-S3-onprem/)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 5. [VPC Endpoint Policies (Bonus)](5.5-Policy/)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 5. [VPC Endpoint Policies (Bonus)](5.5-Policy/) ) 
) 
5. [VPC Endpoint Policies (Bonus)](5.5-Policy/)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 6. [Clean up](5.6-Cleanup/)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 6. [Clean up](5.6-Cleanup/) ) 
) 
6. [Clean up](5.6-Cleanup/)
