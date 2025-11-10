
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Kiểm tra Interface Endpoint"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Kiểm tra Interface Endpoint" ) 
) 
title : "Kiểm tra Interface Endpoint"

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
echo #### Lấy regional DNS name (tên DNS khu vực) của S3 interface endpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Lấy regional DNS name (tên DNS khu vực) của S3 interface endpoint ) 
) 
#### Lấy regional DNS name (tên DNS khu vực) của S3 interface endpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Trong Amazon VPC menu, chọn Endpoints.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Trong Amazon VPC menu, chọn Endpoints. ) 
) 
1. Trong Amazon VPC menu, chọn Endpoints.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Click tên của endpoint chúng ta mới tạo ở mục 4.2: s3-interface-endpoint. Click details và lưu lại regional DNS name của endpoint (cái đầu tiên) vào text-editor của bạn để dùng ở các bước sau.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Click tên của endpoint chúng ta mới tạo ở mục 4.2: s3-interface-endpoint. Click details và lưu lại regional DNS name của endpoint (cái đầu tiên) vào text-editor của bạn để dùng ở các bước sau. ) 
) 
2. Click tên của endpoint chúng ta mới tạo ở mục 4.2: s3-interface-endpoint. Click details và lưu lại regional DNS name của endpoint (cái đầu tiên) vào text-editor của bạn để dùng ở các bước sau.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![dns name](/images/5-Workshop/5.4-S3-onprem/dns.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![dns name](/images/5-Workshop/5.4-S3-onprem/dns.png) ) 
) 
![dns name](/images/5-Workshop/5.4-S3-onprem/dns.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Kết nối đến EC2 instance ở trong "VPC On-prem" (giả lập môi trường truyền thống)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Kết nối đến EC2 instance ở trong "VPC On-prem" (giả lập môi trường truyền thống) ) 
) 
#### Kết nối đến EC2 instance ở trong "VPC On-prem" (giả lập môi trường truyền thống)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Đi đến **Session manager** bằng cách gõ "session manager" vào ô tìm kiếm   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Đi đến **Session manager** bằng cách gõ "session manager" vào ô tìm kiếm ) 
) 
1. Đi đến **Session manager** bằng cách gõ "session manager" vào ô tìm kiếm

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Click **Start Session**, chọn EC2 instance có tên **Test-Interface-Endpoint**. EC2 instance này đang chạy trên "VPC On-prem" và sẽ được sử dụng để kiểm tra kết nối đến Amazon S3 thông qua Interface endpoint. Session Manager sẽ mở 1 browser tab mới với shell prompt: **sh-4.2 $**   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Click **Start Session**, chọn EC2 instance có tên **Test-Interface-Endpoint**. EC2 instance này đang chạy trên "VPC On-prem" và sẽ được sử dụng để kiểm tra kết nối đến Amazon S3 thông qua Interface endpoint. Session Manager sẽ mở 1 browser tab mới với shell prompt: **sh-4.2 $** ) 
) 
2. Click **Start Session**, chọn EC2 instance có tên **Test-Interface-Endpoint**. EC2 instance này đang chạy trên "VPC On-prem" và sẽ được sử dụng để kiểm tra kết nối đến Amazon S3 thông qua Interface endpoint. Session Manager sẽ mở 1 browser tab mới với shell prompt: **sh-4.2 $**

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Start session](/images/5-Workshop/5.4-S3-onprem/start-session.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Start session](/images/5-Workshop/5.4-S3-onprem/start-session.png) ) 
) 
![Start session](/images/5-Workshop/5.4-S3-onprem/start-session.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Đi đến ssm-user's home directory với lệnh "cd ~"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Đi đến ssm-user's home directory với lệnh "cd ~" ) 
) 
3. Đi đến ssm-user's home directory với lệnh "cd ~"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 4. Tạo 1 file tên testfile2.xyz   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 4. Tạo 1 file tên testfile2.xyz ) 
) 
4. Tạo 1 file tên testfile2.xyz

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
echo 5. Copy file vào S3 bucket mình tạo ở section 4.2   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 5. Copy file vào S3 bucket mình tạo ở section 4.2 ) 
) 
5. Copy file vào S3 bucket mình tạo ở section 4.2

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
echo + Câu lệnh này yêu cầu thông số --endpoint-url, bởi vì bạn cần sử dụng DNS name chỉ định cho endpoint để truy cập vào S3 thông qua Interface endpoint.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Câu lệnh này yêu cầu thông số --endpoint-url, bởi vì bạn cần sử dụng DNS name chỉ định cho endpoint để truy cập vào S3 thông qua Interface endpoint. ) 
) 
+ Câu lệnh này yêu cầu thông số --endpoint-url, bởi vì bạn cần sử dụng DNS name chỉ định cho endpoint để truy cập vào S3 thông qua Interface endpoint.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Không lấy ' * ' khi copy/paste tên DNS khu vực.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Không lấy ' * ' khi copy/paste tên DNS khu vực. ) 
) 
+ Không lấy ' * ' khi copy/paste tên DNS khu vực.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Cung cấp tên S3 bucket của bạn   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Cung cấp tên S3 bucket của bạn ) 
) 
+ Cung cấp tên S3 bucket của bạn

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![copy file](/images/5-Workshop/5.4-S3-onprem/cli2.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![copy file](/images/5-Workshop/5.4-S3-onprem/cli2.png) ) 
) 
![copy file](/images/5-Workshop/5.4-S3-onprem/cli2.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Bây giờ tệp đã được thêm vào bộ chứa S3 của bạn. Hãy kiểm tra bộ chứa S3 của bạn trong bước tiếp theo.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Bây giờ tệp đã được thêm vào bộ chứa S3 của bạn. Hãy kiểm tra bộ chứa S3 của bạn trong bước tiếp theo. ) 
) 
Bây giờ tệp đã được thêm vào bộ chứa S3 của bạn. Hãy kiểm tra bộ chứa S3 của bạn trong bước tiếp theo.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Kiểm tra Object trong S3 bucket   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Kiểm tra Object trong S3 bucket ) 
) 
#### Kiểm tra Object trong S3 bucket

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Đi đến S3 console   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Đi đến S3 console ) 
) 
1. Đi đến S3 console

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Click Buckets   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Click Buckets ) 
) 
2. Click Buckets

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Click tên bucket của bạn và bạn sẽ thấy testfile2.xyz đã được thêm vào s3 bucket của bạn   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Click tên bucket của bạn và bạn sẽ thấy testfile2.xyz đã được thêm vào s3 bucket của bạn ) 
) 
3. Click tên bucket của bạn và bạn sẽ thấy testfile2.xyz đã được thêm vào s3 bucket của bạn

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![check bucket](/images/5-Workshop/5.4-S3-onprem/check-bucket.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![check bucket](/images/5-Workshop/5.4-S3-onprem/check-bucket.png) ) 
) 
![check bucket](/images/5-Workshop/5.4-S3-onprem/check-bucket.png)
