
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Truy cập S3 từ VPC"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Truy cập S3 từ VPC" ) 
) 
title : "Truy cập S3 từ VPC"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo date :  "`r Sys.Date()`"    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo date :  "`r Sys.Date()`"  ) 
) 
date :  "`r Sys.Date()`" 

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
echo #### Sử dụng Gateway endpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Sử dụng Gateway endpoint ) 
) 
#### Sử dụng Gateway endpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Trong phần này, bạn sẽ tạo một Gateway endpoint để truy cập Amazon S3 từ một EC2 instance. Gateway endpoint sẽ cho phép tải một object lên S3 bucket mà không cần sử dụng Internet Công cộng. Để tạo endpoint, bạn phải chỉ định VPC mà bạn muốn tạo endpoint và dịch vụ (trong trường hợp này là S3) mà bạn muốn thiết lập kết nối.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Trong phần này, bạn sẽ tạo một Gateway endpoint để truy cập Amazon S3 từ một EC2 instance. Gateway endpoint sẽ cho phép tải một object lên S3 bucket mà không cần sử dụng Internet Công cộng. Để tạo endpoint, bạn phải chỉ định VPC mà bạn muốn tạo endpoint và dịch vụ (trong trường hợp này là S3) mà bạn muốn thiết lập kết nối. ) 
) 
Trong phần này, bạn sẽ tạo một Gateway endpoint để truy cập Amazon S3 từ một EC2 instance. Gateway endpoint sẽ cho phép tải một object lên S3 bucket mà không cần sử dụng Internet Công cộng. Để tạo endpoint, bạn phải chỉ định VPC mà bạn muốn tạo endpoint và dịch vụ (trong trường hợp này là S3) mà bạn muốn thiết lập kết nối.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![overview](/images/5-Workshop/5.3-S3-vpc/diagram2.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![overview](/images/5-Workshop/5.3-S3-vpc/diagram2.png) ) 
) 
![overview](/images/5-Workshop/5.3-S3-vpc/diagram2.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Nội dung   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Nội dung ) 
) 
#### Nội dung

E:\thuctap\report mau\fcj-workshop-template-main>(
echo - [Tạo gateway endpoint](3.1-create-gwe/)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo - [Tạo gateway endpoint](3.1-create-gwe/) ) 
) 
- [Tạo gateway endpoint](3.1-create-gwe/)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo - [Test gateway endpoint](3.2-test-gwe/)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo - [Test gateway endpoint](3.2-test-gwe/) ) 
) 
- [Test gateway endpoint](3.2-test-gwe/)
