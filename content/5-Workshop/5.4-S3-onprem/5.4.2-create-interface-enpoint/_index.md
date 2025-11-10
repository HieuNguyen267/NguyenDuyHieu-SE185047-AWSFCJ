
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Create an S3 Interface endpoint"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Create an S3 Interface endpoint" ) 
) 
title : "Create an S3 Interface endpoint"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo date : "`r Sys.Date()`"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo date : "`r Sys.Date()`" ) 
) 
date : "`r Sys.Date()`"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo weight : 2   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo weight : 2 ) 
) 
weight : 2

E:\thuctap\report mau\fcj-workshop-template-main>(
echo chapter : false   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo chapter : false ) 
) 
chapter : false

E:\thuctap\report mau\fcj-workshop-template-main>(
echo pre : " <b> 5.4.2 </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.4.2 </b> " ) 
) 
pre : " <b> 5.4.2 </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo In this section you will create and test an S3 interface endpoint using the simulated on-premises environment deployed as part of this workshop.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo In this section you will create and test an S3 interface endpoint using the simulated on-premises environment deployed as part of this workshop. ) 
) 
In this section you will create and test an S3 interface endpoint using the simulated on-premises environment deployed as part of this workshop.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Return to the Amazon VPC menu. In the navigation pane, choose Endpoints, then click Create Endpoint.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Return to the Amazon VPC menu. In the navigation pane, choose Endpoints, then click Create Endpoint. ) 
) 
1. Return to the Amazon VPC menu. In the navigation pane, choose Endpoints, then click Create Endpoint.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. In Create endpoint console:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. In Create endpoint console: ) 
) 
2. In Create endpoint console:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Name the interface endpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Name the interface endpoint ) 
) 
+ Name the interface endpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + In Service category, choose **aws services**    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + In Service category, choose **aws services**  ) 
) 
+ In Service category, choose **aws services** 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![name](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![name](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint1.png) ) 
) 
![name](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3.  In the Search box, type S3 and press Enter. Select the endpoint named com.amazonaws.us-east-1.s3. Ensure that the Type column indicates Interface.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3.  In the Search box, type S3 and press Enter. Select the endpoint named com.amazonaws.us-east-1.s3. Ensure that the Type column indicates Interface. ) 
) 
3.  In the Search box, type S3 and press Enter. Select the endpoint named com.amazonaws.us-east-1.s3. Ensure that the Type column indicates Interface.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![service](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint2.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![service](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint2.png) ) 
) 
![service](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint2.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 4. For VPC, select VPC Cloud from the drop-down.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 4. For VPC, select VPC Cloud from the drop-down. ) 
) 
4. For VPC, select VPC Cloud from the drop-down.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo {{% notice warning %}}   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo {{% notice warning %}} ) 
) 
{{% notice warning %}}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Make sure to choose "VPC Cloud" and not "VPC On-prem"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Make sure to choose "VPC Cloud" and not "VPC On-prem" ) 
) 
Make sure to choose "VPC Cloud" and not "VPC On-prem"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo {{% /notice %}}   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo {{% /notice %}} ) 
) 
{{% /notice %}}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Expand **Additional settings** and ensure that Enable DNS name is *not* selected (we will use this in the next part of the workshop)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Expand **Additional settings** and ensure that Enable DNS name is *not* selected (we will use this in the next part of the workshop) ) 
) 
+ Expand **Additional settings** and ensure that Enable DNS name is *not* selected (we will use this in the next part of the workshop)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![vpc](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint3.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![vpc](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint3.png) ) 
) 
![vpc](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint3.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 5. Select 2 subnets in the following AZs: us-east-1a and us-east-1b   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 5. Select 2 subnets in the following AZs: us-east-1a and us-east-1b ) 
) 
5. Select 2 subnets in the following AZs: us-east-1a and us-east-1b

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![subnets](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint4.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![subnets](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint4.png) ) 
) 
![subnets](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint4.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 6. For Security group, choose SGforS3Endpoint:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 6. For Security group, choose SGforS3Endpoint: ) 
) 
6. For Security group, choose SGforS3Endpoint:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![sg](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint5.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![sg](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint5.png) ) 
) 
![sg](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint5.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 7. Keep the default policy - full access and click Create endpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 7. Keep the default policy - full access and click Create endpoint ) 
) 
7. Keep the default policy - full access and click Create endpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![success](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint-success.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![success](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint-success.png) ) 
) 
![success](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint-success.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Congratulation on successfully creating S3 interface endpoint. In the next step, we will test the interface endpoint.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Congratulation on successfully creating S3 interface endpoint. In the next step, we will test the interface endpoint. ) 
) 
Congratulation on successfully creating S3 interface endpoint. In the next step, we will test the interface endpoint.
