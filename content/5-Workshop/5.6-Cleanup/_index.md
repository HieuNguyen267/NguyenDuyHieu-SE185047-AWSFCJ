
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Clean up"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Clean up" ) 
) 
title : "Clean up"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo date : "`r Sys.Date()`"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo date : "`r Sys.Date()`" ) 
) 
date : "`r Sys.Date()`"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo weight : 6   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo weight : 6 ) 
) 
weight : 6

E:\thuctap\report mau\fcj-workshop-template-main>(
echo chapter : false   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo chapter : false ) 
) 
chapter : false

E:\thuctap\report mau\fcj-workshop-template-main>(
echo pre : " <b> 5.6. </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.6. </b> " ) 
) 
pre : " <b> 5.6. </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Congratulations on completing this workshop!    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Congratulations on completing this workshop!  ) 
) 
Congratulations on completing this workshop! 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo In this workshop, you learned architecture patterns for accessing Amazon S3 without using the Public Internet.    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo In this workshop, you learned architecture patterns for accessing Amazon S3 without using the Public Internet.  ) 
) 
In this workshop, you learned architecture patterns for accessing Amazon S3 without using the Public Internet. 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + By creating a gateway endpoint, you enabled direct communication between EC2 resources and Amazon S3, without traversing an Internet Gateway.    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + By creating a gateway endpoint, you enabled direct communication between EC2 resources and Amazon S3, without traversing an Internet Gateway.  ) 
) 
+ By creating a gateway endpoint, you enabled direct communication between EC2 resources and Amazon S3, without traversing an Internet Gateway. 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + By creating an interface endpoint you extended S3 connectivity to resources running in your on-premises data center via AWS Site-to-Site VPN or Direct Connect.    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + By creating an interface endpoint you extended S3 connectivity to resources running in your on-premises data center via AWS Site-to-Site VPN or Direct Connect.  ) 
) 
+ By creating an interface endpoint you extended S3 connectivity to resources running in your on-premises data center via AWS Site-to-Site VPN or Direct Connect. 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### clean up   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### clean up ) 
) 
#### clean up

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Navigate to Hosted Zones on the left side of Route 53 console. Click the name of *s3.us-east-1.amazonaws.com* zone. Click Delete and confirm deletion by typing delete.    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Navigate to Hosted Zones on the left side of Route 53 console. Click the name of *s3.us-east-1.amazonaws.com* zone. Click Delete and confirm deletion by typing delete.  ) 
) 
1. Navigate to Hosted Zones on the left side of Route 53 console. Click the name of *s3.us-east-1.amazonaws.com* zone. Click Delete and confirm deletion by typing delete. 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![hosted zone](/images/5-Workshop/5.6-Cleanup/delete-zone.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![hosted zone](/images/5-Workshop/5.6-Cleanup/delete-zone.png) ) 
) 
![hosted zone](/images/5-Workshop/5.6-Cleanup/delete-zone.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Disassociate the Route 53 Resolver Rule - myS3Rule from "VPC Onprem" and Delete it.    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Disassociate the Route 53 Resolver Rule - myS3Rule from "VPC Onprem" and Delete it.  ) 
) 
2. Disassociate the Route 53 Resolver Rule - myS3Rule from "VPC Onprem" and Delete it. 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![hosted zone](/images/5-Workshop/5.6-Cleanup/vpc.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![hosted zone](/images/5-Workshop/5.6-Cleanup/vpc.png) ) 
) 
![hosted zone](/images/5-Workshop/5.6-Cleanup/vpc.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 4. Open the CloudFormation console  and delete the two CloudFormation Stacks that you created for this lab:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 4. Open the CloudFormation console  and delete the two CloudFormation Stacks that you created for this lab: ) 
) 
4. Open the CloudFormation console  and delete the two CloudFormation Stacks that you created for this lab:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + PLOnpremSetup   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + PLOnpremSetup ) 
) 
+ PLOnpremSetup

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + PLCloudSetup   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + PLCloudSetup ) 
) 
+ PLCloudSetup

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![delete stack](/images/5-Workshop/5.6-Cleanup/delete-stack.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![delete stack](/images/5-Workshop/5.6-Cleanup/delete-stack.png) ) 
) 
![delete stack](/images/5-Workshop/5.6-Cleanup/delete-stack.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 5. Delete S3 buckets   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 5. Delete S3 buckets ) 
) 
5. Delete S3 buckets

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Open S3 console   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Open S3 console ) 
) 
+ Open S3 console

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Choose the bucket we created for the lab, click and confirm empty. Click delete and confirm delete.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Choose the bucket we created for the lab, click and confirm empty. Click delete and confirm delete. ) 
) 
+ Choose the bucket we created for the lab, click and confirm empty. Click delete and confirm delete.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![delete s3](/images/5-Workshop/5.6-Cleanup/delete-s3.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![delete s3](/images/5-Workshop/5.6-Cleanup/delete-s3.png) ) 
) 
![delete s3](/images/5-Workshop/5.6-Cleanup/delete-s3.png)
