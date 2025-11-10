
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "VPC Endpoint Policies"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "VPC Endpoint Policies" ) 
) 
title : "VPC Endpoint Policies"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo date : "`r Sys.Date()`"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo date : "`r Sys.Date()`" ) 
) 
date : "`r Sys.Date()`"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo weight : 5   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo weight : 5 ) 
) 
weight : 5

E:\thuctap\report mau\fcj-workshop-template-main>(
echo chapter : false   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo chapter : false ) 
) 
chapter : false

E:\thuctap\report mau\fcj-workshop-template-main>(
echo pre : " <b> 5.5. </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.5. </b> " ) 
) 
pre : " <b> 5.5. </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo When you create an interface or gateway endpoint, you can attach an endpoint policy to it that controls access to the service to which you are connecting. A VPC endpoint policy is an IAM resource policy that you attach to an endpoint. If you do not attach a policy when you create an endpoint, AWS attaches a default policy for you that allows full access to the service through the endpoint.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo When you create an interface or gateway endpoint, you can attach an endpoint policy to it that controls access to the service to which you are connecting. A VPC endpoint policy is an IAM resource policy that you attach to an endpoint. If you do not attach a policy when you create an endpoint, AWS attaches a default policy for you that allows full access to the service through the endpoint. ) 
) 
When you create an interface or gateway endpoint, you can attach an endpoint policy to it that controls access to the service to which you are connecting. A VPC endpoint policy is an IAM resource policy that you attach to an endpoint. If you do not attach a policy when you create an endpoint, AWS attaches a default policy for you that allows full access to the service through the endpoint.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo You can create a policy that restricts access to specific S3 buckets only. This is useful if you only want certain S3 Buckets to be accessible through the endpoint.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo You can create a policy that restricts access to specific S3 buckets only. This is useful if you only want certain S3 Buckets to be accessible through the endpoint. ) 
) 
You can create a policy that restricts access to specific S3 buckets only. This is useful if you only want certain S3 Buckets to be accessible through the endpoint.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo In this section you will create a VPC endpoint policy that restricts access to the S3 bucket specified in the VPC endpoint policy.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo In this section you will create a VPC endpoint policy that restricts access to the S3 bucket specified in the VPC endpoint policy. ) 
) 
In this section you will create a VPC endpoint policy that restricts access to the S3 bucket specified in the VPC endpoint policy.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![endpoint diagram](/images/5-Workshop/5.5-Policy/s3-bucket-policy.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![endpoint diagram](/images/5-Workshop/5.5-Policy/s3-bucket-policy.png) ) 
) 
![endpoint diagram](/images/5-Workshop/5.5-Policy/s3-bucket-policy.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Connect to an EC2 instance and verify connectivity to S3   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Connect to an EC2 instance and verify connectivity to S3 ) 
) 
#### Connect to an EC2 instance and verify connectivity to S3

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Start a new AWS Session Manager session on the instance named Test-Gateway-Endpoint. From the session, verify that you can list the contents of the bucket you created in Part 1: Access S3 from VPC:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Start a new AWS Session Manager session on the instance named Test-Gateway-Endpoint. From the session, verify that you can list the contents of the bucket you created in Part 1: Access S3 from VPC: ) 
) 
1. Start a new AWS Session Manager session on the instance named Test-Gateway-Endpoint. From the session, verify that you can list the contents of the bucket you created in Part 1: Access S3 from VPC:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ``` ) 
) 
```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo aws s3 ls s3://\<your-bucket-name\>   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo aws s3 ls s3://\<your-bucket-name\> ) 
) 
aws s3 ls s3://\<your-bucket-name\>

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ``` ) 
) 
```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![test](/images/5-Workshop/5.5-Policy/test1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![test](/images/5-Workshop/5.5-Policy/test1.png) ) 
) 
![test](/images/5-Workshop/5.5-Policy/test1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo The bucket contents include the two 1 GB files uploaded in earlier.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo The bucket contents include the two 1 GB files uploaded in earlier. ) 
) 
The bucket contents include the two 1 GB files uploaded in earlier.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Create a new S3 bucket; follow the naming pattern you used in Part 1, but add a '-2' to the name. Leave other fields as default and click create   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Create a new S3 bucket; follow the naming pattern you used in Part 1, but add a '-2' to the name. Leave other fields as default and click create ) 
) 
2. Create a new S3 bucket; follow the naming pattern you used in Part 1, but add a '-2' to the name. Leave other fields as default and click create

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create bucket](/images/5-Workshop/5.5-Policy/create-bucket.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create bucket](/images/5-Workshop/5.5-Policy/create-bucket.png) ) 
) 
![create bucket](/images/5-Workshop/5.5-Policy/create-bucket.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Successfully create bucket   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Successfully create bucket ) 
) 
Successfully create bucket

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Success](/images/5-Workshop/5.5-Policy/create-bucket-success.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Success](/images/5-Workshop/5.5-Policy/create-bucket-success.png) ) 
) 
![Success](/images/5-Workshop/5.5-Policy/create-bucket-success.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Navigate to: Services > VPC > Endpoints, then select the Gateway VPC endpoint you created earlier. Click the Policy tab. Click Edit policy.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Navigate to: Services > VPC > Endpoints, then select the Gateway VPC endpoint you created earlier. Click the Policy tab. Click Edit policy. ) 
) 
3. Navigate to: Services > VPC > Endpoints, then select the Gateway VPC endpoint you created earlier. Click the Policy tab. Click Edit policy.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![policy](/images/5-Workshop/5.5-Policy/policy1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![policy](/images/5-Workshop/5.5-Policy/policy1.png) ) 
) 
![policy](/images/5-Workshop/5.5-Policy/policy1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo The default policy allows access to all S3 Buckets through the VPC endpoint.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo The default policy allows access to all S3 Buckets through the VPC endpoint. ) 
) 
The default policy allows access to all S3 Buckets through the VPC endpoint.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 4. In Edit Policy console, copy & Paste the following policy, then replace yourbucketname-2 with your 2nd bucket name. This policy will allow access through the VPC endpoint to your new bucket, but not any other bucket in Amazon S3. Click Save to apply the policy.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 4. In Edit Policy console, copy & Paste the following policy, then replace yourbucketname-2 with your 2nd bucket name. This policy will allow access through the VPC endpoint to your new bucket, but not any other bucket in Amazon S3. Click Save to apply the policy. ) 
) 
4. In Edit Policy console, copy & Paste the following policy, then replace yourbucketname-2 with your 2nd bucket name. This policy will allow access through the VPC endpoint to your new bucket, but not any other bucket in Amazon S3. Click Save to apply the policy.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ``` ) 
) 
```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo {   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo { ) 
) 
{

E:\thuctap\report mau\fcj-workshop-template-main>(
echo   "Id": "Policy1631305502445",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo   "Id": "Policy1631305502445", ) 
) 
  "Id": "Policy1631305502445",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo   "Version": "2012-10-17",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo   "Version": "2012-10-17", ) 
) 
  "Version": "2012-10-17",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo   "Statement": [   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo   "Statement": [ ) 
) 
  "Statement": [

E:\thuctap\report mau\fcj-workshop-template-main>(
echo     {   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo     { ) 
) 
    {

E:\thuctap\report mau\fcj-workshop-template-main>(
echo       "Sid": "Stmt1631305501021",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo       "Sid": "Stmt1631305501021", ) 
) 
      "Sid": "Stmt1631305501021",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo       "Action": "s3:*",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo       "Action": "s3:*", ) 
) 
      "Action": "s3:*",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo       "Effect": "Allow",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo       "Effect": "Allow", ) 
) 
      "Effect": "Allow",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo       "Resource": [   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo       "Resource": [ ) 
) 
      "Resource": [

E:\thuctap\report mau\fcj-workshop-template-main>(
echo       				"arn:aws:s3:::yourbucketname-2",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo       				"arn:aws:s3:::yourbucketname-2", ) 
) 
      				"arn:aws:s3:::yourbucketname-2",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo        				"arn:aws:s3:::yourbucketname-2/*"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo        				"arn:aws:s3:::yourbucketname-2/*" ) 
) 
       				"arn:aws:s3:::yourbucketname-2/*"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo        ],   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo        ], ) 
) 
       ],

E:\thuctap\report mau\fcj-workshop-template-main>(
echo       "Principal": "*"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo       "Principal": "*" ) 
) 
      "Principal": "*"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo     }   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo     } ) 
) 
    }

E:\thuctap\report mau\fcj-workshop-template-main>(
echo   ]   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo   ] ) 
) 
  ]

E:\thuctap\report mau\fcj-workshop-template-main>(
echo }   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo } ) 
) 
}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ``` ) 
) 
```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![custom policy](/images/5-Workshop/5.5-Policy/policy2.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![custom policy](/images/5-Workshop/5.5-Policy/policy2.png) ) 
) 
![custom policy](/images/5-Workshop/5.5-Policy/policy2.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Successfully customize policy   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Successfully customize policy ) 
) 
Successfully customize policy

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![success](/static/images/5-Workshop/5.5-Policy/success.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![success](/static/images/5-Workshop/5.5-Policy/success.png) ) 
) 
![success](/static/images/5-Workshop/5.5-Policy/success.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 5. From your session on the Test-Gateway-Endpoint instance, test access to the S3 bucket you created in Part 1: Access S3 from VPC   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 5. From your session on the Test-Gateway-Endpoint instance, test access to the S3 bucket you created in Part 1: Access S3 from VPC ) 
) 
5. From your session on the Test-Gateway-Endpoint instance, test access to the S3 bucket you created in Part 1: Access S3 from VPC

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ``` ) 
) 
```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo aws s3 ls s3://<yourbucketname>   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo aws s3 ls s3://<yourbucketname> ) 
) 
aws s3 ls s3://<yourbucketname>

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ``` ) 
) 
```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo This command will return an error because access to this bucket is not permitted by your new VPC endpoint policy:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo This command will return an error because access to this bucket is not permitted by your new VPC endpoint policy: ) 
) 
This command will return an error because access to this bucket is not permitted by your new VPC endpoint policy:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![error](/static/images/5-Workshop/5.5-Policy/error.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![error](/static/images/5-Workshop/5.5-Policy/error.png) ) 
) 
![error](/static/images/5-Workshop/5.5-Policy/error.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 6. Return to your home directory on your EC2 instance ` cd~ `   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 6. Return to your home directory on your EC2 instance ` cd~ ` ) 
) 
6. Return to your home directory on your EC2 instance ` cd~ `

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Create a file ```fallocate -l 1G test-bucket2.xyz ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Create a file ```fallocate -l 1G test-bucket2.xyz ``` ) 
) 
+ Create a file ```fallocate -l 1G test-bucket2.xyz ```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Copy file to 2nd bucket ```aws s3 cp test-bucket2.xyz s3://<your-2nd-bucket-name>```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Copy file to 2nd bucket ```aws s3 cp test-bucket2.xyz s3://<your-2nd-bucket-name>``` ) 
) 
+ Copy file to 2nd bucket ```aws s3 cp test-bucket2.xyz s3://<your-2nd-bucket-name>```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![success](/static/images/5-Workshop/5.5-Policy/test2.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![success](/static/images/5-Workshop/5.5-Policy/test2.png) ) 
) 
![success](/static/images/5-Workshop/5.5-Policy/test2.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo This operation succeeds because it is permitted by the VPC endpoint policy.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo This operation succeeds because it is permitted by the VPC endpoint policy. ) 
) 
This operation succeeds because it is permitted by the VPC endpoint policy.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![success](/static/images/5-Workshop/5.5-Policy/test2-success.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![success](/static/images/5-Workshop/5.5-Policy/test2-success.png) ) 
) 
![success](/static/images/5-Workshop/5.5-Policy/test2-success.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Then we test access to the first bucket by copy the file to 1st bucket `aws s3 cp test-bucket2.xyz s3://<your-1st-bucket-name>`   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Then we test access to the first bucket by copy the file to 1st bucket `aws s3 cp test-bucket2.xyz s3://<your-1st-bucket-name>` ) 
) 
+ Then we test access to the first bucket by copy the file to 1st bucket `aws s3 cp test-bucket2.xyz s3://<your-1st-bucket-name>`

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![fail](/static/images/5-Workshop/5.5-Policy/test2-fail.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![fail](/static/images/5-Workshop/5.5-Policy/test2-fail.png) ) 
) 
![fail](/static/images/5-Workshop/5.5-Policy/test2-fail.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo This command will return an error because access to this bucket is not permitted by your new VPC endpoint policy.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo This command will return an error because access to this bucket is not permitted by your new VPC endpoint policy. ) 
) 
This command will return an error because access to this bucket is not permitted by your new VPC endpoint policy.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Part 3 Summary:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Part 3 Summary: ) 
) 
#### Part 3 Summary:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo In this section, you created a VPC endpoint policy for Amazon S3, and used the AWS CLI to test the policy. AWS CLI actions targeted to your original S3 bucket failed because you applied a policy that only allowed access to the second bucket you created. AWS CLI actions targeted for your second bucket succeeded because the policy allowed them. These policies can be useful in situations where you need to control access to resources through VPC endpoints.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo In this section, you created a VPC endpoint policy for Amazon S3, and used the AWS CLI to test the policy. AWS CLI actions targeted to your original S3 bucket failed because you applied a policy that only allowed access to the second bucket you created. AWS CLI actions targeted for your second bucket succeeded because the policy allowed them. These policies can be useful in situations where you need to control access to resources through VPC endpoints. ) 
) 
In this section, you created a VPC endpoint policy for Amazon S3, and used the AWS CLI to test the policy. AWS CLI actions targeted to your original S3 bucket failed because you applied a policy that only allowed access to the second bucket you created. AWS CLI actions targeted for your second bucket succeeded because the policy allowed them. These policies can be useful in situations where you need to control access to resources through VPC endpoints.
