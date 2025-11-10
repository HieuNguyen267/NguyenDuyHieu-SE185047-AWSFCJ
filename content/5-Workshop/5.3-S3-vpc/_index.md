
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Access S3 from VPC"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Access S3 from VPC" ) 
) 
title : "Access S3 from VPC"

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
echo pre : " <b> 5.3. </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.3. </b> " ) 
) 
pre : " <b> 5.3. </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Using Gateway endpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Using Gateway endpoint ) 
) 
#### Using Gateway endpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo In this section, you will create **a Gateway eendpoint** to access **Amazon S3** from **an EC2 instance**. **The Gateway endpoint** will allow upload an object to S3 buckets without using **the Public Internet**. To create an endpoint, you must specify the VPC in which you want to create the endpoint, and the service (in this case, S3) to which you want to establish the connection.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo In this section, you will create **a Gateway eendpoint** to access **Amazon S3** from **an EC2 instance**. **The Gateway endpoint** will allow upload an object to S3 buckets without using **the Public Internet**. To create an endpoint, you must specify the VPC in which you want to create the endpoint, and the service (in this case, S3) to which you want to establish the connection. ) 
) 
In this section, you will create **a Gateway eendpoint** to access **Amazon S3** from **an EC2 instance**. **The Gateway endpoint** will allow upload an object to S3 buckets without using **the Public Internet**. To create an endpoint, you must specify the VPC in which you want to create the endpoint, and the service (in this case, S3) to which you want to establish the connection.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![overview](/images/5-Workshop/5.3-S3-vpc/diagram2.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![overview](/images/5-Workshop/5.3-S3-vpc/diagram2.png) ) 
) 
![overview](/images/5-Workshop/5.3-S3-vpc/diagram2.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Content   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Content ) 
) 
#### Content

E:\thuctap\report mau\fcj-workshop-template-main>(
echo - [Create gateway endpoint](3.1-create-gwe/)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo - [Create gateway endpoint](3.1-create-gwe/) ) 
) 
- [Create gateway endpoint](3.1-create-gwe/)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo - [Test gateway endpoint](3.2-test-gwe/)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo - [Test gateway endpoint](3.2-test-gwe/) ) 
) 
- [Test gateway endpoint](3.2-test-gwe/)
