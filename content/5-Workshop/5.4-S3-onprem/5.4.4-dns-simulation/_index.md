
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "On-premises DNS Simulation"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "On-premises DNS Simulation" ) 
) 
title : "On-premises DNS Simulation"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo date : "`r Sys.Date()`"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo date : "`r Sys.Date()`" ) 
) 
date : "`r Sys.Date()`"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo weight : 4   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo weight : 4 ) 
) 
weight : 4

E:\thuctap\report mau\fcj-workshop-template-main>(
echo chapter : false   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo chapter : false ) 
) 
chapter : false

E:\thuctap\report mau\fcj-workshop-template-main>(
echo pre : " <b> 5.4.4 </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.4.4 </b> " ) 
) 
pre : " <b> 5.4.4 </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo AWS PrivateLink endpoints have a fixed IP address in each Availability Zone where they are deployed, for the life of the endpoint (until it is deleted). These IP addresses are attached to Elastic Network Interfaces (ENIs). AWS recommends using DNS to resolve the IP addresses for endpoints so that downstream applications use the latest IP addresses when ENIs are added to new AZs, or deleted over time.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo AWS PrivateLink endpoints have a fixed IP address in each Availability Zone where they are deployed, for the life of the endpoint (until it is deleted). These IP addresses are attached to Elastic Network Interfaces (ENIs). AWS recommends using DNS to resolve the IP addresses for endpoints so that downstream applications use the latest IP addresses when ENIs are added to new AZs, or deleted over time. ) 
) 
AWS PrivateLink endpoints have a fixed IP address in each Availability Zone where they are deployed, for the life of the endpoint (until it is deleted). These IP addresses are attached to Elastic Network Interfaces (ENIs). AWS recommends using DNS to resolve the IP addresses for endpoints so that downstream applications use the latest IP addresses when ENIs are added to new AZs, or deleted over time.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo In this section, you will create a forwarding rule to send DNS resolution requests from a simulated on-premises environment to a Route 53 Private Hosted Zone. This section leverages the infrastructure deployed by CloudFormation in the Prepare the environment section.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo In this section, you will create a forwarding rule to send DNS resolution requests from a simulated on-premises environment to a Route 53 Private Hosted Zone. This section leverages the infrastructure deployed by CloudFormation in the Prepare the environment section. ) 
) 
In this section, you will create a forwarding rule to send DNS resolution requests from a simulated on-premises environment to a Route 53 Private Hosted Zone. This section leverages the infrastructure deployed by CloudFormation in the Prepare the environment section.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Create DNS Alias Records for the Interface endpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Create DNS Alias Records for the Interface endpoint ) 
) 
#### Create DNS Alias Records for the Interface endpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Navigate to the [Route 53 management console](https://us-east-1.console.aws.amazon.com/route53/v2/hostedzones?region=us-east-1#) (Hosted Zones section).  The CloudFormation template you deployed in the Prepare the environment section created this Private Hosted Zone. Click on the name of the Private Hosted Zone, s3.us-east-1.amazonaws.com:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Navigate to the [Route 53 management console](https://us-east-1.console.aws.amazon.com/route53/v2/hostedzones?region=us-east-1#) (Hosted Zones section).  The CloudFormation template you deployed in the Prepare the environment section created this Private Hosted Zone. Click on the name of the Private Hosted Zone, s3.us-east-1.amazonaws.com: ) 
) 
1. Navigate to the [Route 53 management console](https://us-east-1.console.aws.amazon.com/route53/v2/hostedzones?region=us-east-1#) (Hosted Zones section).  The CloudFormation template you deployed in the Prepare the environment section created this Private Hosted Zone. Click on the name of the Private Hosted Zone, s3.us-east-1.amazonaws.com:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![hosted zone](/images/5-Workshop/5.4-S3-onprem/hosted-zone.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![hosted zone](/images/5-Workshop/5.4-S3-onprem/hosted-zone.png) ) 
) 
![hosted zone](/images/5-Workshop/5.4-S3-onprem/hosted-zone.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Create a new record in the Private Hosted Zone:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Create a new record in the Private Hosted Zone: ) 
) 
2. Create a new record in the Private Hosted Zone:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Create record](/images/5-Workshop/5.4-S3-onprem/create-record1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Create record](/images/5-Workshop/5.4-S3-onprem/create-record1.png) ) 
) 
![Create record](/images/5-Workshop/5.4-S3-onprem/create-record1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Record name and record type keep default options   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Record name and record type keep default options ) 
) 
+ Record name and record type keep default options

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Alias Button: Click to enable   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Alias Button: Click to enable ) 
) 
+ Alias Button: Click to enable

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Route traffic to: Alias to VPC Endpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Route traffic to: Alias to VPC Endpoint ) 
) 
+ Route traffic to: Alias to VPC Endpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Region: US East (N. Virginia) [us-east-1]   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Region: US East (N. Virginia) [us-east-1] ) 
) 
+ Region: US East (N. Virginia) [us-east-1]

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Choose endpoint: Paste the Regional VPC Endpoint DNS name from your text editor (you saved when doing section 4.3)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Choose endpoint: Paste the Regional VPC Endpoint DNS name from your text editor (you saved when doing section 4.3) ) 
) 
+ Choose endpoint: Paste the Regional VPC Endpoint DNS name from your text editor (you saved when doing section 4.3)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![record1](/images/5-Workshop/5.4-S3-onprem/record1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![record1](/images/5-Workshop/5.4-S3-onprem/record1.png) ) 
) 
![record1](/images/5-Workshop/5.4-S3-onprem/record1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Click Add another record, and add a second record using the following values. Click Create records when finished to create both records.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Click Add another record, and add a second record using the following values. Click Create records when finished to create both records. ) 
) 
3. Click Add another record, and add a second record using the following values. Click Create records when finished to create both records.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Record name: *.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Record name: *. ) 
) 
+ Record name: *.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Record type: keep default value (type A)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Record type: keep default value (type A) ) 
) 
+ Record type: keep default value (type A)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Alias Button: Click to enable   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Alias Button: Click to enable ) 
) 
+ Alias Button: Click to enable

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Route traffic to: Alias to VPC Endpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Route traffic to: Alias to VPC Endpoint ) 
) 
+ Route traffic to: Alias to VPC Endpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Region: US East (N. Virginia) [us-east-1]   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Region: US East (N. Virginia) [us-east-1] ) 
) 
+ Region: US East (N. Virginia) [us-east-1]

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Choose endpoint: Paste the Regional VPC Endpoint DNS name from your text editor   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Choose endpoint: Paste the Regional VPC Endpoint DNS name from your text editor ) 
) 
+ Choose endpoint: Paste the Regional VPC Endpoint DNS name from your text editor

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![record 2](/images/5-Workshop/5.4-S3-onprem/record2.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![record 2](/images/5-Workshop/5.4-S3-onprem/record2.png) ) 
) 
![record 2](/images/5-Workshop/5.4-S3-onprem/record2.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo The new records appear in the Route 53 console:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo The new records appear in the Route 53 console: ) 
) 
The new records appear in the Route 53 console:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![result](/images/5-Workshop/5.4-S3-onprem/result.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![result](/images/5-Workshop/5.4-S3-onprem/result.png) ) 
) 
![result](/images/5-Workshop/5.4-S3-onprem/result.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Create a Resolver Forwarding Rule   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Create a Resolver Forwarding Rule ) 
) 
#### Create a Resolver Forwarding Rule

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Route 53 Resolver Forwarding Rules allow you to forward DNS queries from your VPC to other sources for name resolution. Outside of a workshop environment, you might use this feature to forward DNS queries from your VPC to DNS servers running on-premises. In this section, you will simulate an on-premises conditional forwarder by creating a forwarding rule that forwards DNS queries for Amazon S3 to a Private Hosted Zone running in "VPC Cloud" in-order to resolve the PrivateLink interface endpoint regional DNS name.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Route 53 Resolver Forwarding Rules allow you to forward DNS queries from your VPC to other sources for name resolution. Outside of a workshop environment, you might use this feature to forward DNS queries from your VPC to DNS servers running on-premises. In this section, you will simulate an on-premises conditional forwarder by creating a forwarding rule that forwards DNS queries for Amazon S3 to a Private Hosted Zone running in "VPC Cloud" in-order to resolve the PrivateLink interface endpoint regional DNS name. ) 
) 
Route 53 Resolver Forwarding Rules allow you to forward DNS queries from your VPC to other sources for name resolution. Outside of a workshop environment, you might use this feature to forward DNS queries from your VPC to DNS servers running on-premises. In this section, you will simulate an on-premises conditional forwarder by creating a forwarding rule that forwards DNS queries for Amazon S3 to a Private Hosted Zone running in "VPC Cloud" in-order to resolve the PrivateLink interface endpoint regional DNS name.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. From the Route 53 management console, click **Inbound endpoints** on the left side bar   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. From the Route 53 management console, click **Inbound endpoints** on the left side bar ) 
) 
1. From the Route 53 management console, click **Inbound endpoints** on the left side bar

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. In the Inbound endpoints console, click the ID of the inbound endpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. In the Inbound endpoints console, click the ID of the inbound endpoint ) 
) 
2. In the Inbound endpoints console, click the ID of the inbound endpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Inbound endpoint](/images/5-Workshop/5.4-S3-onprem/route53-1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Inbound endpoint](/images/5-Workshop/5.4-S3-onprem/route53-1.png) ) 
) 
![Inbound endpoint](/images/5-Workshop/5.4-S3-onprem/route53-1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Copy the two IP addresses listed to your text editor   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Copy the two IP addresses listed to your text editor ) 
) 
3. Copy the two IP addresses listed to your text editor

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Ip addresses](/images/5-Workshop/5.4-S3-onprem/route53-2.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Ip addresses](/images/5-Workshop/5.4-S3-onprem/route53-2.png) ) 
) 
![Ip addresses](/images/5-Workshop/5.4-S3-onprem/route53-2.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 4. From the Route 53 menu, choose **Resolver** > **Rules**, and click **Create rule**:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 4. From the Route 53 menu, choose **Resolver** > **Rules**, and click **Create rule**: ) 
) 
4. From the Route 53 menu, choose **Resolver** > **Rules**, and click **Create rule**:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Ip addresses](/images/5-Workshop/5.4-S3-onprem/route53-3.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Ip addresses](/images/5-Workshop/5.4-S3-onprem/route53-3.png) ) 
) 
![Ip addresses](/images/5-Workshop/5.4-S3-onprem/route53-3.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 5. In the Create rule console:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 5. In the Create rule console: ) 
) 
5. In the Create rule console:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Name: myS3Rule   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Name: myS3Rule ) 
) 
+ Name: myS3Rule

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Rule type: Forward   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Rule type: Forward ) 
) 
+ Rule type: Forward

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Domain name: s3.us-east-1.amazonaws.com   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Domain name: s3.us-east-1.amazonaws.com ) 
) 
+ Domain name: s3.us-east-1.amazonaws.com

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create rule](/images/5-Workshop/5.4-S3-onprem/route53-4.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create rule](/images/5-Workshop/5.4-S3-onprem/route53-4.png) ) 
) 
![create rule](/images/5-Workshop/5.4-S3-onprem/route53-4.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + VPC: VPC On-prem   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + VPC: VPC On-prem ) 
) 
+ VPC: VPC On-prem

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Outbound endpoint: VPCOnpremOutboundEndpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Outbound endpoint: VPCOnpremOutboundEndpoint ) 
) 
+ Outbound endpoint: VPCOnpremOutboundEndpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create rule](/images/5-Workshop/5.4-S3-onprem/route53-5.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create rule](/images/5-Workshop/5.4-S3-onprem/route53-5.png) ) 
) 
![create rule](/images/5-Workshop/5.4-S3-onprem/route53-5.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Target IP Addresses: Enter both IP addresses from your text editor (inbound endpoint addresses) and then click Submit   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Target IP Addresses: Enter both IP addresses from your text editor (inbound endpoint addresses) and then click Submit ) 
) 
+ Target IP Addresses: Enter both IP addresses from your text editor (inbound endpoint addresses) and then click Submit

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create rule](/images/5-Workshop/5.4-S3-onprem/route53-6.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create rule](/images/5-Workshop/5.4-S3-onprem/route53-6.png) ) 
) 
![create rule](/images/5-Workshop/5.4-S3-onprem/route53-6.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo You have successfully created resolver forwarding rule.    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo You have successfully created resolver forwarding rule.  ) 
) 
You have successfully created resolver forwarding rule. 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create rule](/images/5-Workshop/5.4-S3-onprem/route53-7.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create rule](/images/5-Workshop/5.4-S3-onprem/route53-7.png) ) 
) 
![create rule](/images/5-Workshop/5.4-S3-onprem/route53-7.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Test the on-premises DNS Simulation   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Test the on-premises DNS Simulation ) 
) 
#### Test the on-premises DNS Simulation

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Connect to **Test-Interface-Endpoint EC2 instance** with **Session manager**   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Connect to **Test-Interface-Endpoint EC2 instance** with **Session manager** ) 
) 
1. Connect to **Test-Interface-Endpoint EC2 instance** with **Session manager**

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create rule](/images/5-Workshop/5.4-S3-onprem/test1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create rule](/images/5-Workshop/5.4-S3-onprem/test1.png) ) 
) 
![create rule](/images/5-Workshop/5.4-S3-onprem/test1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Test DNS resolution. The dig command will return the IP addresses assigned to the VPC Interface endpoint running in VPC Cloud (your IP's will be different): dig +short s3.us-east-1.amazonaws.com    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Test DNS resolution. The dig command will return the IP addresses assigned to the VPC Interface endpoint running in VPC Cloud (your IP's will be different): dig +short s3.us-east-1.amazonaws.com  ) 
) 
2. Test DNS resolution. The dig command will return the IP addresses assigned to the VPC Interface endpoint running in VPC Cloud (your IP's will be different): dig +short s3.us-east-1.amazonaws.com 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo {{% notice note %}}   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo {{% notice note %}} ) 
) 
{{% notice note %}}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo The IP addresses returned are the VPC endpoint IP addresses, NOT the Resolver IP addresses you pasted from your text editor. The IP addresses of the Resolver endpoint and the VPC endpoint look similar because they are all from the VPC Cloud CIDR block.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo The IP addresses returned are the VPC endpoint IP addresses, NOT the Resolver IP addresses you pasted from your text editor. The IP addresses of the Resolver endpoint and the VPC endpoint look similar because they are all from the VPC Cloud CIDR block. ) 
) 
The IP addresses returned are the VPC endpoint IP addresses, NOT the Resolver IP addresses you pasted from your text editor. The IP addresses of the Resolver endpoint and the VPC endpoint look similar because they are all from the VPC Cloud CIDR block.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo {{% /notice %}}   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo {{% /notice %}} ) 
) 
{{% /notice %}}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create rule](/images/5-Workshop/5.4-S3-onprem/dig.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create rule](/images/5-Workshop/5.4-S3-onprem/dig.png) ) 
) 
![create rule](/images/5-Workshop/5.4-S3-onprem/dig.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Navigate to the VPC menu (Endpoints section), select the S3 Interface endpoint. Click the Subnets tab and verify that the IP addresses returned by Dig match the VPC endpoint:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Navigate to the VPC menu (Endpoints section), select the S3 Interface endpoint. Click the Subnets tab and verify that the IP addresses returned by Dig match the VPC endpoint: ) 
) 
3. Navigate to the VPC menu (Endpoints section), select the S3 Interface endpoint. Click the Subnets tab and verify that the IP addresses returned by Dig match the VPC endpoint:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create rule](/images/5-Workshop/5.4-S3-onprem/subnet.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create rule](/images/5-Workshop/5.4-S3-onprem/subnet.png) ) 
) 
![create rule](/images/5-Workshop/5.4-S3-onprem/subnet.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 4. Return to your shell and use the AWS CLI to test listing your S3 buckets:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 4. Return to your shell and use the AWS CLI to test listing your S3 buckets: ) 
) 
4. Return to your shell and use the AWS CLI to test listing your S3 buckets:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ``` ) 
) 
```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo aws s3 ls --endpoint-url https://s3.us-east-1.amazonaws.com   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo aws s3 ls --endpoint-url https://s3.us-east-1.amazonaws.com ) 
) 
aws s3 ls --endpoint-url https://s3.us-east-1.amazonaws.com

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ``` ) 
) 
```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create rule](/images/5-Workshop/5.4-S3-onprem/endpoint.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create rule](/images/5-Workshop/5.4-S3-onprem/endpoint.png) ) 
) 
![create rule](/images/5-Workshop/5.4-S3-onprem/endpoint.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 5. Terminate your Session Manager session:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 5. Terminate your Session Manager session: ) 
) 
5. Terminate your Session Manager session:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create rule](/images/5-Workshop/5.4-S3-onprem/terminal.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create rule](/images/5-Workshop/5.4-S3-onprem/terminal.png) ) 
) 
![create rule](/images/5-Workshop/5.4-S3-onprem/terminal.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo In this section you created an Interface endpoint for Amazon S3. This endpoint can be reached from on-premises through Site-to-Site VPN or AWS Direct Connect. Route 53 Resolver outbound endpoints simulated forwarding DNS requests from on-premises to a Private Hosted Zone running the cloud. Route 53 inbound Endpoints recieved the resolution request and returned a response containing the IP addresses of the VPC interface endpoint. Using DNS to resolve the endpoint IP addresses provides high availability in-case of an Availability Zone outage.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo In this section you created an Interface endpoint for Amazon S3. This endpoint can be reached from on-premises through Site-to-Site VPN or AWS Direct Connect. Route 53 Resolver outbound endpoints simulated forwarding DNS requests from on-premises to a Private Hosted Zone running the cloud. Route 53 inbound Endpoints recieved the resolution request and returned a response containing the IP addresses of the VPC interface endpoint. Using DNS to resolve the endpoint IP addresses provides high availability in-case of an Availability Zone outage. ) 
) 
In this section you created an Interface endpoint for Amazon S3. This endpoint can be reached from on-premises through Site-to-Site VPN or AWS Direct Connect. Route 53 Resolver outbound endpoints simulated forwarding DNS requests from on-premises to a Private Hosted Zone running the cloud. Route 53 inbound Endpoints recieved the resolution request and returned a response containing the IP addresses of the VPC interface endpoint. Using DNS to resolve the endpoint IP addresses provides high availability in-case of an Availability Zone outage.
