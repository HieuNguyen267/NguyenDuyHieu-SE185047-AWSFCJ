
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Test the Interface Endpoint"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Test the Interface Endpoint" ) 
) 
title : "Test the Interface Endpoint"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo date : "`r Sys.Date()`"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo date : "`r Sys.Date()`" ) 
) 
date : "`r Sys.Date()`"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo weight : 3   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo weight : 3 ) 
) 
weight : 3

E:\thuctap\report mau\fcj-workshop-template-main>(
echo chapter : false   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo chapter : false ) 
) 
chapter : false

E:\thuctap\report mau\fcj-workshop-template-main>(
echo pre : " <b> 5.4.3 </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.4.3 </b> " ) 
) 
pre : " <b> 5.4.3 </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Get the regional DNS name of S3 interface endpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Get the regional DNS name of S3 interface endpoint ) 
) 
#### Get the regional DNS name of S3 interface endpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. From the Amazon VPC menu, choose Endpoints.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. From the Amazon VPC menu, choose Endpoints. ) 
) 
1. From the Amazon VPC menu, choose Endpoints.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Click the name of newly created endpoint: s3-interface-endpoint. Click details and save the regional DNS name of the endpoint (the first one) to your text-editor for later use.    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Click the name of newly created endpoint: s3-interface-endpoint. Click details and save the regional DNS name of the endpoint (the first one) to your text-editor for later use.  ) 
) 
2. Click the name of newly created endpoint: s3-interface-endpoint. Click details and save the regional DNS name of the endpoint (the first one) to your text-editor for later use. 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![dns name](/images/5-Workshop/5.4-S3-onprem/dns.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![dns name](/images/5-Workshop/5.4-S3-onprem/dns.png) ) 
) 
![dns name](/images/5-Workshop/5.4-S3-onprem/dns.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Connect to EC2 instance in "VPC On-prem"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Connect to EC2 instance in "VPC On-prem" ) 
) 
#### Connect to EC2 instance in "VPC On-prem"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Navigate to **Session manager** by typing "session manager" in the search box    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Navigate to **Session manager** by typing "session manager" in the search box  ) 
) 
1. Navigate to **Session manager** by typing "session manager" in the search box 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Click **Start Session**, and select the EC2 instance named **Test-Interface-Endpoint**. This EC2 instance is running in "VPC On-prem" and will be used to test connectivty to Amazon S3 through the Interface endpoint we just created. Session Manager will open a new browser tab with a shell prompt: **sh-4.2 $**   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Click **Start Session**, and select the EC2 instance named **Test-Interface-Endpoint**. This EC2 instance is running in "VPC On-prem" and will be used to test connectivty to Amazon S3 through the Interface endpoint we just created. Session Manager will open a new browser tab with a shell prompt: **sh-4.2 $** ) 
) 
2. Click **Start Session**, and select the EC2 instance named **Test-Interface-Endpoint**. This EC2 instance is running in "VPC On-prem" and will be used to test connectivty to Amazon S3 through the Interface endpoint we just created. Session Manager will open a new browser tab with a shell prompt: **sh-4.2 $**

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Start session](/images/5-Workshop/5.4-S3-onprem/start-session.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Start session](/images/5-Workshop/5.4-S3-onprem/start-session.png) ) 
) 
![Start session](/images/5-Workshop/5.4-S3-onprem/start-session.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Change to the ssm-user's home directory with command "cd ~"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Change to the ssm-user's home directory with command "cd ~" ) 
) 
3. Change to the ssm-user's home directory with command "cd ~"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 4. Create a file named testfile2.xyz   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 4. Create a file named testfile2.xyz ) 
) 
4. Create a file named testfile2.xyz

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ``` ) 
) 
```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo fallocate -l 1G testfile2.xyz   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo fallocate -l 1G testfile2.xyz ) 
) 
fallocate -l 1G testfile2.xyz

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ``` ) 
) 
```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![user](/images/5-Workshop/5.4-S3-onprem/cli1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![user](/images/5-Workshop/5.4-S3-onprem/cli1.png) ) 
) 
![user](/images/5-Workshop/5.4-S3-onprem/cli1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 5. Copy file to the same S3 bucket we created in section 3.2   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 5. Copy file to the same S3 bucket we created in section 3.2 ) 
) 
5. Copy file to the same S3 bucket we created in section 3.2

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ``` ) 
) 
```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo aws s3 cp --endpoint-url https://bucket.<Regional-DNS-Name> testfile2.xyz s3://<your-bucket-name>   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo aws s3 cp --endpoint-url https://bucket.<Regional-DNS-Name> testfile2.xyz s3://<your-bucket-name> ) 
) 
aws s3 cp --endpoint-url https://bucket.<Regional-DNS-Name> testfile2.xyz s3://<your-bucket-name>

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ```  ) 
) 
``` 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + This command requires the --endpoint-url parameter, because you need to use the endpoint-specific DNS name to access S3 using an Interface endpoint.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + This command requires the --endpoint-url parameter, because you need to use the endpoint-specific DNS name to access S3 using an Interface endpoint. ) 
) 
+ This command requires the --endpoint-url parameter, because you need to use the endpoint-specific DNS name to access S3 using an Interface endpoint.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Do not include the leading ' * ' when copying/pasting the regional DNS name.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Do not include the leading ' * ' when copying/pasting the regional DNS name. ) 
) 
+ Do not include the leading ' * ' when copying/pasting the regional DNS name.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Provide your S3 bucket name created earlier   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Provide your S3 bucket name created earlier ) 
) 
+ Provide your S3 bucket name created earlier

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![copy file](/images/5-Workshop/5.4-S3-onprem/cli2.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![copy file](/images/5-Workshop/5.4-S3-onprem/cli2.png) ) 
) 
![copy file](/images/5-Workshop/5.4-S3-onprem/cli2.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Now the file has been added to your S3 bucket. Let check your S3 bucket in the next step.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Now the file has been added to your S3 bucket. Let check your S3 bucket in the next step. ) 
) 
Now the file has been added to your S3 bucket. Let check your S3 bucket in the next step.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Check Object in S3 bucket   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Check Object in S3 bucket ) 
) 
#### Check Object in S3 bucket

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Navigate to S3 console   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Navigate to S3 console ) 
) 
1. Navigate to S3 console

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Click Buckets   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Click Buckets ) 
) 
2. Click Buckets

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Click the name of your bucket and you will see testfile2.xyz has been added to your bucket   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Click the name of your bucket and you will see testfile2.xyz has been added to your bucket ) 
) 
3. Click the name of your bucket and you will see testfile2.xyz has been added to your bucket

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![check bucket](/images/5-Workshop/5.4-S3-onprem/check-bucket.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![check bucket](/images/5-Workshop/5.4-S3-onprem/check-bucket.png) ) 
) 
![check bucket](/images/5-Workshop/5.4-S3-onprem/check-bucket.png)
