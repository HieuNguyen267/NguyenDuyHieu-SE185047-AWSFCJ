
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Test the Gateway Endpoint"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Test the Gateway Endpoint" ) 
) 
title : "Test the Gateway Endpoint"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo date :  "`r Sys.Date()`"    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo date :  "`r Sys.Date()`"  ) 
) 
date :  "`r Sys.Date()`" 

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
echo pre : " <b> 5.3.2 </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.3.2 </b> " ) 
) 
pre : " <b> 5.3.2 </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Create S3 bucket   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Create S3 bucket ) 
) 
#### Create S3 bucket

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Navigate to **S3 management console**   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Navigate to **S3 management console** ) 
) 
1. Navigate to **S3 management console**

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. In the Bucket console, choose **Create bucket**   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. In the Bucket console, choose **Create bucket** ) 
) 
2. In the Bucket console, choose **Create bucket**

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Create bucket](/images/5-Workshop/5.3-S3-vpc/create-bucket.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Create bucket](/images/5-Workshop/5.3-S3-vpc/create-bucket.png) ) 
) 
![Create bucket](/images/5-Workshop/5.3-S3-vpc/create-bucket.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. In **the Create bucket console**   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. In **the Create bucket console** ) 
) 
3. In **the Create bucket console**

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + **Name the bucket**: choose a name that hasn't been given to any bucket globally (hint: lab number and your name)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + **Name the bucket**: choose a name that hasn't been given to any bucket globally (hint: lab number and your name) ) 
) 
+ **Name the bucket**: choose a name that hasn't been given to any bucket globally (hint: lab number and your name)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Bucket name](/images/5-Workshop/5.3-S3-vpc/bucket-name.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Bucket name](/images/5-Workshop/5.3-S3-vpc/bucket-name.png) ) 
) 
![Bucket name](/images/5-Workshop/5.3-S3-vpc/bucket-name.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Leave other fields as they are (default)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Leave other fields as they are (default) ) 
) 
+ Leave other fields as they are (default)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Scroll down and choose **Create bucket**   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Scroll down and choose **Create bucket** ) 
) 
+ Scroll down and choose **Create bucket**

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Create](/images/5-Workshop/5.3-S3-vpc/create-button.png)    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Create](/images/5-Workshop/5.3-S3-vpc/create-button.png)  ) 
) 
![Create](/images/5-Workshop/5.3-S3-vpc/create-button.png) 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Successfully create S3 bucket.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Successfully create S3 bucket. ) 
) 
+ Successfully create S3 bucket.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Success](/images/5-Workshop/5.3-S3-vpc/bucket-success.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Success](/images/5-Workshop/5.3-S3-vpc/bucket-success.png) ) 
) 
![Success](/images/5-Workshop/5.3-S3-vpc/bucket-success.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Connect to EC2 with session manager   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Connect to EC2 with session manager ) 
) 
#### Connect to EC2 with session manager

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + For this workshop, you will use **AWS Session Manager** to access several **EC2 instances**. **Session Manager** is a fully managed **AWS Systems Manager** capability that allows you to manage your **Amazon EC2 instances**  and on-premises virtual machines (VMs) through an interactive one-click browser-based shell. Session Manager provides secure and auditable instance management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + For this workshop, you will use **AWS Session Manager** to access several **EC2 instances**. **Session Manager** is a fully managed **AWS Systems Manager** capability that allows you to manage your **Amazon EC2 instances**  and on-premises virtual machines (VMs) through an interactive one-click browser-based shell. Session Manager provides secure and auditable instance management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys. ) 
) 
+ For this workshop, you will use **AWS Session Manager** to access several **EC2 instances**. **Session Manager** is a fully managed **AWS Systems Manager** capability that allows you to manage your **Amazon EC2 instances**  and on-premises virtual machines (VMs) through an interactive one-click browser-based shell. Session Manager provides secure and auditable instance management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + First cloud journey [Lab](https://000058.awsstudygroup.com/1-introduce/) for indepth understanding of Session manager.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + First cloud journey [Lab](https://000058.awsstudygroup.com/1-introduce/) for indepth understanding of Session manager. ) 
) 
+ First cloud journey [Lab](https://000058.awsstudygroup.com/1-introduce/) for indepth understanding of Session manager.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. In the **AWS Management Console**, start typing ```Systems Manager``` in the quick search box and press **Enter**:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. In the **AWS Management Console**, start typing ```Systems Manager``` in the quick search box and press **Enter**: ) 
) 
1. In the **AWS Management Console**, start typing ```Systems Manager``` in the quick search box and press **Enter**:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![system manager](/images/5-Workshop/5.3-S3-vpc/sm.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![system manager](/images/5-Workshop/5.3-S3-vpc/sm.png) ) 
) 
![system manager](/images/5-Workshop/5.3-S3-vpc/sm.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. From the **Systems Manager** menu, find **Node Management** in the left menu and click **Session Manager**:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. From the **Systems Manager** menu, find **Node Management** in the left menu and click **Session Manager**: ) 
) 
2. From the **Systems Manager** menu, find **Node Management** in the left menu and click **Session Manager**:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![system manager](/images/5-Workshop/5.3-S3-vpc/sm1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![system manager](/images/5-Workshop/5.3-S3-vpc/sm1.png) ) 
) 
![system manager](/images/5-Workshop/5.3-S3-vpc/sm1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Click **Start Session**, and select **the EC2 instance** named **Test-Gateway-Endpoint**.    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Click **Start Session**, and select **the EC2 instance** named **Test-Gateway-Endpoint**.  ) 
) 
3. Click **Start Session**, and select **the EC2 instance** named **Test-Gateway-Endpoint**. 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo {{% notice info %}}   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo {{% notice info %}} ) 
) 
{{% notice info %}}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo This EC2 instance is already running in "VPC Cloud" and will be used to test connectivity to Amazon S3 through the Gateway endpoint you just created (s3-gwe). {{% /notice %}}   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo This EC2 instance is already running in "VPC Cloud" and will be used to test connectivity to Amazon S3 through the Gateway endpoint you just created (s3-gwe). {{% /notice %}} ) 
) 
This EC2 instance is already running in "VPC Cloud" and will be used to test connectivity to Amazon S3 through the Gateway endpoint you just created (s3-gwe). {{% /notice %}}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Start session](/images/5-Workshop/5.3-S3-vpc/start-session.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Start session](/images/5-Workshop/5.3-S3-vpc/start-session.png) ) 
) 
![Start session](/images/5-Workshop/5.3-S3-vpc/start-session.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo **Session Manager** will open a new browser tab with a shell prompt: sh-4.2 $   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo **Session Manager** will open a new browser tab with a shell prompt: sh-4.2 $ ) 
) 
**Session Manager** will open a new browser tab with a shell prompt: sh-4.2 $

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Success](/images/5-Workshop/5.3-S3-vpc/start-session-success.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Success](/images/5-Workshop/5.3-S3-vpc/start-session-success.png) ) 
) 
![Success](/images/5-Workshop/5.3-S3-vpc/start-session-success.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo You have successfully start a session - connect to the EC2 instance in VPC cloud. In the next step, we will create a S3 bucket and a file in it.    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo You have successfully start a session - connect to the EC2 instance in VPC cloud. In the next step, we will create a S3 bucket and a file in it.  ) 
) 
You have successfully start a session - connect to the EC2 instance in VPC cloud. In the next step, we will create a S3 bucket and a file in it. 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Create a file and upload to s3 bucket   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Create a file and upload to s3 bucket ) 
) 
#### Create a file and upload to s3 bucket

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Change to the ssm-user's home directory by typing ```cd ~``` in the CLI   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Change to the ssm-user's home directory by typing ```cd ~``` in the CLI ) 
) 
1. Change to the ssm-user's home directory by typing ```cd ~``` in the CLI

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Change user's dir](/images/5-Workshop/5.3-S3-vpc/cli1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Change user's dir](/images/5-Workshop/5.3-S3-vpc/cli1.png) ) 
) 
![Change user's dir](/images/5-Workshop/5.3-S3-vpc/cli1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Create a new file to use for testing with the command ```fallocate -l 1G testfile.xyz```, which will create a file of 1GB size named "testfile.xyz".   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Create a new file to use for testing with the command ```fallocate -l 1G testfile.xyz```, which will create a file of 1GB size named "testfile.xyz". ) 
) 
2. Create a new file to use for testing with the command ```fallocate -l 1G testfile.xyz```, which will create a file of 1GB size named "testfile.xyz".

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Create file](/images/5-Workshop/5.3-S3-vpc/cli-file.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Create file](/images/5-Workshop/5.3-S3-vpc/cli-file.png) ) 
) 
![Create file](/images/5-Workshop/5.3-S3-vpc/cli-file.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Upload file to S3 bucket with command ```aws s3 cp testfile.xyz s3://your-bucket-name```. Replace your-bucket-name with the name of S3 bucket that you created earlier.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Upload file to S3 bucket with command ```aws s3 cp testfile.xyz s3://your-bucket-name```. Replace your-bucket-name with the name of S3 bucket that you created earlier. ) 
) 
3. Upload file to S3 bucket with command ```aws s3 cp testfile.xyz s3://your-bucket-name```. Replace your-bucket-name with the name of S3 bucket that you created earlier.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Uploaded](/images/5-Workshop/5.3-S3-vpc/uploaded.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Uploaded](/images/5-Workshop/5.3-S3-vpc/uploaded.png) ) 
) 
![Uploaded](/images/5-Workshop/5.3-S3-vpc/uploaded.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo You have successfully uploaded the file to your S3 bucket. You can now terminate the session.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo You have successfully uploaded the file to your S3 bucket. You can now terminate the session. ) 
) 
You have successfully uploaded the file to your S3 bucket. You can now terminate the session.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Check object in S3 bucket   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Check object in S3 bucket ) 
) 
#### Check object in S3 bucket

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Navigate to S3 console.     | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Navigate to S3 console.   ) 
) 
1. Navigate to S3 console.  

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Click the name of your s3 bucket   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Click the name of your s3 bucket ) 
) 
2. Click the name of your s3 bucket

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. In the Bucket console, you will see the file you have uploaded to your S3 bucket   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. In the Bucket console, you will see the file you have uploaded to your S3 bucket ) 
) 
3. In the Bucket console, you will see the file you have uploaded to your S3 bucket

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Check S3](/images/5-Workshop/5.3-S3-vpc/check-s3-bucket.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Check S3](/images/5-Workshop/5.3-S3-vpc/check-s3-bucket.png) ) 
) 
![Check S3](/images/5-Workshop/5.3-S3-vpc/check-s3-bucket.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Section summary   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Section summary ) 
) 
#### Section summary

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Congratulation on completing access to S3 from VPC. In this section, you created a Gateway endpoint for Amazon S3, and used the AWS CLI to upload an object. The upload worked because the Gateway endpoint allowed communication to S3, without needing an Internet Gateway attached to "VPC Cloud". This demonstrates the functionality of the Gateway endpoint as a secure path to S3 without traversing the Public Internet.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Congratulation on completing access to S3 from VPC. In this section, you created a Gateway endpoint for Amazon S3, and used the AWS CLI to upload an object. The upload worked because the Gateway endpoint allowed communication to S3, without needing an Internet Gateway attached to "VPC Cloud". This demonstrates the functionality of the Gateway endpoint as a secure path to S3 without traversing the Public Internet. ) 
) 
Congratulation on completing access to S3 from VPC. In this section, you created a Gateway endpoint for Amazon S3, and used the AWS CLI to upload an object. The upload worked because the Gateway endpoint allowed communication to S3, without needing an Internet Gateway attached to "VPC Cloud". This demonstrates the functionality of the Gateway endpoint as a secure path to S3 without traversing the Public Internet.
