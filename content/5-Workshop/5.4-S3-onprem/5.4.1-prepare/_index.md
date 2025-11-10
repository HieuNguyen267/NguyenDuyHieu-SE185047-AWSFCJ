
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Prepare the environment"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Prepare the environment" ) 
) 
title : "Prepare the environment"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo date : "`r Sys.Date()`"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo date : "`r Sys.Date()`" ) 
) 
date : "`r Sys.Date()`"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo weight : 1   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo weight : 1 ) 
) 
weight : 1

E:\thuctap\report mau\fcj-workshop-template-main>(
echo chapter : false   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo chapter : false ) 
) 
chapter : false

E:\thuctap\report mau\fcj-workshop-template-main>(
echo pre : " <b> 5.4.1 </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.4.1 </b> " ) 
) 
pre : " <b> 5.4.1 </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo To prepare for this part of the workshop you will need to:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo To prepare for this part of the workshop you will need to: ) 
) 
To prepare for this part of the workshop you will need to:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Deploying a CloudFormation stack    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Deploying a CloudFormation stack  ) 
) 
+ Deploying a CloudFormation stack 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Modifying a VPC route table.    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Modifying a VPC route table.  ) 
) 
+ Modifying a VPC route table. 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo These components work together to simulate on-premises DNS forwarding and name resolution.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo These components work together to simulate on-premises DNS forwarding and name resolution. ) 
) 
These components work together to simulate on-premises DNS forwarding and name resolution.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Deploy the CloudFormation stack   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Deploy the CloudFormation stack ) 
) 
#### Deploy the CloudFormation stack

E:\thuctap\report mau\fcj-workshop-template-main>(
echo The CloudFormation template will create additional services to support an on-premises simulation:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo The CloudFormation template will create additional services to support an on-premises simulation: ) 
) 
The CloudFormation template will create additional services to support an on-premises simulation:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + One Route 53 Private Hosted Zone that hosts Alias records for the PrivateLink S3 endpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + One Route 53 Private Hosted Zone that hosts Alias records for the PrivateLink S3 endpoint ) 
) 
+ One Route 53 Private Hosted Zone that hosts Alias records for the PrivateLink S3 endpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + One Route 53 Inbound Resolver endpoint that enables "VPC Cloud" to resolve inbound DNS resolution requests to the Private Hosted Zone   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + One Route 53 Inbound Resolver endpoint that enables "VPC Cloud" to resolve inbound DNS resolution requests to the Private Hosted Zone ) 
) 
+ One Route 53 Inbound Resolver endpoint that enables "VPC Cloud" to resolve inbound DNS resolution requests to the Private Hosted Zone

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + One Route 53 Outbound Resolver endpoint that enables "VPC On-prem" to forward DNS requests for S3 to "VPC Cloud"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + One Route 53 Outbound Resolver endpoint that enables "VPC On-prem" to forward DNS requests for S3 to "VPC Cloud" ) 
) 
+ One Route 53 Outbound Resolver endpoint that enables "VPC On-prem" to forward DNS requests for S3 to "VPC Cloud"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![route 53 diagram](/images/5-Workshop/5.4-S3-onprem/route53.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![route 53 diagram](/images/5-Workshop/5.4-S3-onprem/route53.png) ) 
) 
![route 53 diagram](/images/5-Workshop/5.4-S3-onprem/route53.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Click the following link to open the [AWS CloudFormation console](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://s3.amazonaws.com/reinvent-endpoints-builders-session/R53CF.yaml&stackName=PLOnpremSetup). The required template will be pre-loaded into the menu. Accept all default and click Create stack.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Click the following link to open the [AWS CloudFormation console](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://s3.amazonaws.com/reinvent-endpoints-builders-session/R53CF.yaml&stackName=PLOnpremSetup). The required template will be pre-loaded into the menu. Accept all default and click Create stack. ) 
) 
1. Click the following link to open the [AWS CloudFormation console](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://s3.amazonaws.com/reinvent-endpoints-builders-session/R53CF.yaml&stackName=PLOnpremSetup). The required template will be pre-loaded into the menu. Accept all default and click Create stack.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Create stack](/images/5-Workshop/5.4-S3-onprem/create-stack.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Create stack](/images/5-Workshop/5.4-S3-onprem/create-stack.png) ) 
) 
![Create stack](/images/5-Workshop/5.4-S3-onprem/create-stack.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Button](/images/5-Workshop/5.4-S3-onprem/create-stack-button.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Button](/images/5-Workshop/5.4-S3-onprem/create-stack-button.png) ) 
) 
![Button](/images/5-Workshop/5.4-S3-onprem/create-stack-button.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo It may take a few minutes for stack deployment to complete. You can continue with the next step without waiting for the deployemnt to finish.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo It may take a few minutes for stack deployment to complete. You can continue with the next step without waiting for the deployemnt to finish. ) 
) 
It may take a few minutes for stack deployment to complete. You can continue with the next step without waiting for the deployemnt to finish.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Update on-premise private route table   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Update on-premise private route table ) 
) 
#### Update on-premise private route table

E:\thuctap\report mau\fcj-workshop-template-main>(
echo This workshop uses a strongSwan VPN running on an EC2 instance to simulate connectivty between an on-premises datacenter and the AWS cloud. Most of the required components are provisioned before your start. To finalize the VPN configuration, you will modify the "VPC On-prem" routing table to direct traffic destined for the cloud to the strongSwan VPN instance.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo This workshop uses a strongSwan VPN running on an EC2 instance to simulate connectivty between an on-premises datacenter and the AWS cloud. Most of the required components are provisioned before your start. To finalize the VPN configuration, you will modify the "VPC On-prem" routing table to direct traffic destined for the cloud to the strongSwan VPN instance. ) 
) 
This workshop uses a strongSwan VPN running on an EC2 instance to simulate connectivty between an on-premises datacenter and the AWS cloud. Most of the required components are provisioned before your start. To finalize the VPN configuration, you will modify the "VPC On-prem" routing table to direct traffic destined for the cloud to the strongSwan VPN instance.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Open the Amazon EC2 console    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Open the Amazon EC2 console  ) 
) 
1. Open the Amazon EC2 console 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Select the instance named infra-vpngw-test. From the Details tab, copy the Instance ID and paste this into your text editor   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Select the instance named infra-vpngw-test. From the Details tab, copy the Instance ID and paste this into your text editor ) 
) 
2. Select the instance named infra-vpngw-test. From the Details tab, copy the Instance ID and paste this into your text editor

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![ec2 id](/images/5-Workshop/5.4-S3-onprem/ec2-onprem-id.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![ec2 id](/images/5-Workshop/5.4-S3-onprem/ec2-onprem-id.png) ) 
) 
![ec2 id](/images/5-Workshop/5.4-S3-onprem/ec2-onprem-id.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Navigate to the VPC menu by using the Search box at the top of the browser window.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Navigate to the VPC menu by using the Search box at the top of the browser window. ) 
) 
3. Navigate to the VPC menu by using the Search box at the top of the browser window.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 4. Click on Route Tables, select the RT Private On-prem route table, select the Routes tab, and click Edit Routes.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 4. Click on Route Tables, select the RT Private On-prem route table, select the Routes tab, and click Edit Routes. ) 
) 
4. Click on Route Tables, select the RT Private On-prem route table, select the Routes tab, and click Edit Routes.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![rt](/images/5-Workshop/5.4-S3-onprem/rt.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![rt](/images/5-Workshop/5.4-S3-onprem/rt.png) ) 
) 
![rt](/images/5-Workshop/5.4-S3-onprem/rt.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 5. Click Add route.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 5. Click Add route. ) 
) 
5. Click Add route.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Destination: your Cloud VPC cidr range   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Destination: your Cloud VPC cidr range ) 
) 
+ Destination: your Cloud VPC cidr range

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Target: ID of your infra-vpngw-test instance (you saved in your editor at step 1)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Target: ID of your infra-vpngw-test instance (you saved in your editor at step 1) ) 
) 
+ Target: ID of your infra-vpngw-test instance (you saved in your editor at step 1)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![add route](/images/5-Workshop/5.4-S3-onprem/add-route.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![add route](/images/5-Workshop/5.4-S3-onprem/add-route.png) ) 
) 
![add route](/images/5-Workshop/5.4-S3-onprem/add-route.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 6. Click Save changes   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 6. Click Save changes ) 
) 
6. Click Save changes
