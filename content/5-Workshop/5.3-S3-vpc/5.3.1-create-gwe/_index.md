
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Create a gateway endpoint"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Create a gateway endpoint" ) 
) 
title : "Create a gateway endpoint"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo date :  "`r Sys.Date()`"    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo date :  "`r Sys.Date()`"  ) 
) 
date :  "`r Sys.Date()`" 

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
echo pre : " <b> 5.3.1 </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.3.1 </b> " ) 
) 
pre : " <b> 5.3.1 </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Open the [Amazon VPC console](https://us-east-1.console.aws.amazon.com/vpc/home?region=us-east-1#Home:)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Open the [Amazon VPC console](https://us-east-1.console.aws.amazon.com/vpc/home?region=us-east-1#Home:) ) 
) 
1. Open the [Amazon VPC console](https://us-east-1.console.aws.amazon.com/vpc/home?region=us-east-1#Home:)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. In the navigation pane, choose **Endpoints**, then click **Create Endpoint**:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. In the navigation pane, choose **Endpoints**, then click **Create Endpoint**: ) 
) 
2. In the navigation pane, choose **Endpoints**, then click **Create Endpoint**:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo {{% notice note %}}   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo {{% notice note %}} ) 
) 
{{% notice note %}}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo You will see **6 existing VPC endpoints** that support **AWS Systems Manager (SSM)**. These endpoints were deployed automatically by the **CloudFormation Templates** for this workshop.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo You will see **6 existing VPC endpoints** that support **AWS Systems Manager (SSM)**. These endpoints were deployed automatically by the **CloudFormation Templates** for this workshop. ) 
) 
You will see **6 existing VPC endpoints** that support **AWS Systems Manager (SSM)**. These endpoints were deployed automatically by the **CloudFormation Templates** for this workshop.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo {{% /notice %}}   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo {{% /notice %}} ) 
) 
{{% /notice %}}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/endpoints.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/endpoints.png) ) 
) 
![endpoint](/images/5-Workshop/5.3-S3-vpc/endpoints.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. In the Create endpoint console:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. In the Create endpoint console: ) 
) 
3. In the Create endpoint console:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Specify name of the endpoint: ```s3-gwe```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Specify name of the endpoint: ```s3-gwe``` ) 
) 
+ Specify name of the endpoint: ```s3-gwe```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + In service category, choose **AWS services**   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + In service category, choose **AWS services** ) 
) 
+ In service category, choose **AWS services**

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/create-s3-gwe1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/create-s3-gwe1.png) ) 
) 
![endpoint](/images/5-Workshop/5.3-S3-vpc/create-s3-gwe1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + In **Services**, type ```s3``` in the search box and choose the service with type **gateway**   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + In **Services**, type ```s3``` in the search box and choose the service with type **gateway** ) 
) 
+ In **Services**, type ```s3``` in the search box and choose the service with type **gateway**

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/services.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/services.png) ) 
) 
![endpoint](/images/5-Workshop/5.3-S3-vpc/services.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + For VPC, select **VPC Cloud** from the drop-down.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + For VPC, select **VPC Cloud** from the drop-down. ) 
) 
+ For VPC, select **VPC Cloud** from the drop-down.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + For **Configure route tables**, select the route table that is already associated with **two subnets** (note: this is not the main route table for the VPC, but a second route table created by CloudFormation).   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + For **Configure route tables**, select the route table that is already associated with **two subnets** (note: this is not the main route table for the VPC, but a second route table created by CloudFormation). ) 
) 
+ For **Configure route tables**, select the route table that is already associated with **two subnets** (note: this is not the main route table for the VPC, but a second route table created by CloudFormation).

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/vpc.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/vpc.png) ) 
) 
![endpoint](/images/5-Workshop/5.3-S3-vpc/vpc.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + **For Policy**, leave the default option, **Full Access**, to allow full access to the service. You will deploy **a VPC endpoint policy** in a later lab module to demonstrate restricting access to **S3 buckets** based on policies.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + **For Policy**, leave the default option, **Full Access**, to allow full access to the service. You will deploy **a VPC endpoint policy** in a later lab module to demonstrate restricting access to **S3 buckets** based on policies. ) 
) 
+ **For Policy**, leave the default option, **Full Access**, to allow full access to the service. You will deploy **a VPC endpoint policy** in a later lab module to demonstrate restricting access to **S3 buckets** based on policies.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/policy.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/policy.png) ) 
) 
![endpoint](/images/5-Workshop/5.3-S3-vpc/policy.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Do not add a tag to the VPC endpoint at this time.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Do not add a tag to the VPC endpoint at this time. ) 
) 
+ Do not add a tag to the VPC endpoint at this time.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Click **Create endpoint**, then click x after receiving a successful creation message.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Click **Create endpoint**, then click x after receiving a successful creation message. ) 
) 
+ Click **Create endpoint**, then click x after receiving a successful creation message.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/complete.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/complete.png) ) 
) 
![endpoint](/images/5-Workshop/5.3-S3-vpc/complete.png)
