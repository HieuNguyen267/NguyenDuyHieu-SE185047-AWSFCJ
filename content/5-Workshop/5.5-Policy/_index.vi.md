
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
echo pre : " <b> 5.5 </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.5 </b> " ) 
) 
pre : " <b> 5.5 </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Khi bạn tạo một Interface Endpoint  hoặc cổng, bạn có thể đính kèm một chính sách điểm cuối để kiểm soát quyền truy cập vào dịch vụ mà bạn đang kết nối. Chính sách VPC Endpoint là chính sách tài nguyên IAM mà bạn đính kèm vào điểm cuối. Nếu bạn không đính kèm chính sách khi tạo điểm cuối, thì AWS sẽ đính kèm chính sách mặc định cho bạn để cho phép toàn quyền truy cập vào dịch vụ thông qua điểm cuối.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Khi bạn tạo một Interface Endpoint  hoặc cổng, bạn có thể đính kèm một chính sách điểm cuối để kiểm soát quyền truy cập vào dịch vụ mà bạn đang kết nối. Chính sách VPC Endpoint là chính sách tài nguyên IAM mà bạn đính kèm vào điểm cuối. Nếu bạn không đính kèm chính sách khi tạo điểm cuối, thì AWS sẽ đính kèm chính sách mặc định cho bạn để cho phép toàn quyền truy cập vào dịch vụ thông qua điểm cuối. ) 
) 
Khi bạn tạo một Interface Endpoint  hoặc cổng, bạn có thể đính kèm một chính sách điểm cuối để kiểm soát quyền truy cập vào dịch vụ mà bạn đang kết nối. Chính sách VPC Endpoint là chính sách tài nguyên IAM mà bạn đính kèm vào điểm cuối. Nếu bạn không đính kèm chính sách khi tạo điểm cuối, thì AWS sẽ đính kèm chính sách mặc định cho bạn để cho phép toàn quyền truy cập vào dịch vụ thông qua điểm cuối.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Bạn có thể tạo chính sách chỉ hạn chế quyền truy cập vào các S3 bucket cụ thể. Điều này hữu ích nếu bạn chỉ muốn một số Bộ chứa S3 nhất định có thể truy cập được thông qua điểm cuối.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Bạn có thể tạo chính sách chỉ hạn chế quyền truy cập vào các S3 bucket cụ thể. Điều này hữu ích nếu bạn chỉ muốn một số Bộ chứa S3 nhất định có thể truy cập được thông qua điểm cuối. ) 
) 
Bạn có thể tạo chính sách chỉ hạn chế quyền truy cập vào các S3 bucket cụ thể. Điều này hữu ích nếu bạn chỉ muốn một số Bộ chứa S3 nhất định có thể truy cập được thông qua điểm cuối.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Trong phần này, bạn sẽ tạo chính sách VPC Endpoint hạn chế quyền truy cập vào S3 bucket được chỉ định trong chính sách VPC Endpoint.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Trong phần này, bạn sẽ tạo chính sách VPC Endpoint hạn chế quyền truy cập vào S3 bucket được chỉ định trong chính sách VPC Endpoint. ) 
) 
Trong phần này, bạn sẽ tạo chính sách VPC Endpoint hạn chế quyền truy cập vào S3 bucket được chỉ định trong chính sách VPC Endpoint.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![endpoint diagram](/images/5-Workshop/5.5-Policy/s3-bucket-policy.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![endpoint diagram](/images/5-Workshop/5.5-Policy/s3-bucket-policy.png) ) 
) 
![endpoint diagram](/images/5-Workshop/5.5-Policy/s3-bucket-policy.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Kết nối tới EC2 và xác minh kết nối tới S3.    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Kết nối tới EC2 và xác minh kết nối tới S3.  ) 
) 
#### Kết nối tới EC2 và xác minh kết nối tới S3. 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Bắt đầu một phiên AWS Session Manager mới trên máy chủ có tên là Test-Gateway-Endpoint. Từ phiên này, xác minh rằng bạn có thể liệt kê nội dung của bucket mà bạn đã tạo trong Phần 1: Truy cập S3 từ VPC.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Bắt đầu một phiên AWS Session Manager mới trên máy chủ có tên là Test-Gateway-Endpoint. Từ phiên này, xác minh rằng bạn có thể liệt kê nội dung của bucket mà bạn đã tạo trong Phần 1: Truy cập S3 từ VPC. ) 
) 
1. Bắt đầu một phiên AWS Session Manager mới trên máy chủ có tên là Test-Gateway-Endpoint. Từ phiên này, xác minh rằng bạn có thể liệt kê nội dung của bucket mà bạn đã tạo trong Phần 1: Truy cập S3 từ VPC.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ``` ) 
) 
```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo aws s3 ls s3://<your-bucket-name>   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo aws s3 ls s3://<your-bucket-name> ) 
) 
aws s3 ls s3://<your-bucket-name>

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
echo Nội dung của bucket bao gồm hai tệp có dung lượng 1GB đã được tải lên trước đó.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Nội dung của bucket bao gồm hai tệp có dung lượng 1GB đã được tải lên trước đó. ) 
) 
Nội dung của bucket bao gồm hai tệp có dung lượng 1GB đã được tải lên trước đó.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Tạo một bucket S3 mới; tuân thủ mẫu đặt tên mà bạn đã sử dụng trong Phần 1, nhưng thêm '-2' vào tên. Để các trường khác là mặc định và nhấp vào **Create**.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Tạo một bucket S3 mới; tuân thủ mẫu đặt tên mà bạn đã sử dụng trong Phần 1, nhưng thêm '-2' vào tên. Để các trường khác là mặc định và nhấp vào **Create**. ) 
) 
2. Tạo một bucket S3 mới; tuân thủ mẫu đặt tên mà bạn đã sử dụng trong Phần 1, nhưng thêm '-2' vào tên. Để các trường khác là mặc định và nhấp vào **Create**.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create bucket](/images/5-Workshop/5.5-Policy/create-bucket.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create bucket](/images/5-Workshop/5.5-Policy/create-bucket.png) ) 
) 
![create bucket](/images/5-Workshop/5.5-Policy/create-bucket.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Tạo bucket thành công.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Tạo bucket thành công. ) 
) 
3. Tạo bucket thành công.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Success](/images/5-Workshop/5.5-Policy/create-bucket-success.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Success](/images/5-Workshop/5.5-Policy/create-bucket-success.png) ) 
) 
![Success](/images/5-Workshop/5.5-Policy/create-bucket-success.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Policy mặc định cho phép truy cập vào tất cả các S3 Buckets thông qua VPC endpoint.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Policy mặc định cho phép truy cập vào tất cả các S3 Buckets thông qua VPC endpoint. ) 
) 
Policy mặc định cho phép truy cập vào tất cả các S3 Buckets thông qua VPC endpoint.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 4. Trong giao diện **Edit Policy**, sao chép và dán theo policy sau, thay thế yourbucketname-2 với tên bucket thứ hai của bạn. Policy này sẽ cho phép truy cập đến bucket mới thông qua VPC endpoint, nhưng không cho phép truy cập đến các bucket còn lại. Chọn **Save** để kích hoạt policy.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 4. Trong giao diện **Edit Policy**, sao chép và dán theo policy sau, thay thế yourbucketname-2 với tên bucket thứ hai của bạn. Policy này sẽ cho phép truy cập đến bucket mới thông qua VPC endpoint, nhưng không cho phép truy cập đến các bucket còn lại. Chọn **Save** để kích hoạt policy. ) 
) 
4. Trong giao diện **Edit Policy**, sao chép và dán theo policy sau, thay thế yourbucketname-2 với tên bucket thứ hai của bạn. Policy này sẽ cho phép truy cập đến bucket mới thông qua VPC endpoint, nhưng không cho phép truy cập đến các bucket còn lại. Chọn **Save** để kích hoạt policy.

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
echo Cấu hình policy thành công.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Cấu hình policy thành công. ) 
) 
Cấu hình policy thành công.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![success](/images/5-Workshop/5.5-Policy/success.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![success](/images/5-Workshop/5.5-Policy/success.png) ) 
) 
![success](/images/5-Workshop/5.5-Policy/success.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 5. Từ session của bạn trên Test-Gateway-Endpoint instance, kiểm tra truy cập đến S3 bucket bạn tạo ở bước đầu   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 5. Từ session của bạn trên Test-Gateway-Endpoint instance, kiểm tra truy cập đến S3 bucket bạn tạo ở bước đầu ) 
) 
5. Từ session của bạn trên Test-Gateway-Endpoint instance, kiểm tra truy cập đến S3 bucket bạn tạo ở bước đầu

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
echo Câu lệnh trả về lỗi bởi vì truy cập vào S3 bucket không có quyền trong VPC endpoint policy.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Câu lệnh trả về lỗi bởi vì truy cập vào S3 bucket không có quyền trong VPC endpoint policy. ) 
) 
Câu lệnh trả về lỗi bởi vì truy cập vào S3 bucket không có quyền trong VPC endpoint policy.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![error](/images/5-Workshop/5.5-Policy/error.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![error](/images/5-Workshop/5.5-Policy/error.png) ) 
) 
![error](/images/5-Workshop/5.5-Policy/error.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 6. Trở lại home directory của bạn trên EC2 instance ```cd~```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 6. Trở lại home directory của bạn trên EC2 instance ```cd~``` ) 
) 
6. Trở lại home directory của bạn trên EC2 instance ```cd~```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Tạo file ```fallocate -l 1G test-bucket2.xyz ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Tạo file ```fallocate -l 1G test-bucket2.xyz ``` ) 
) 
+ Tạo file ```fallocate -l 1G test-bucket2.xyz ```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Sao chép file lên bucket thứ  2 ```aws s3 cp test-bucket2.xyz s3://<your-2nd-bucket-name>```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Sao chép file lên bucket thứ  2 ```aws s3 cp test-bucket2.xyz s3://<your-2nd-bucket-name>``` ) 
) 
+ Sao chép file lên bucket thứ  2 ```aws s3 cp test-bucket2.xyz s3://<your-2nd-bucket-name>```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![success](/images/5-Workshop/5.5-Policy/test2.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![success](/images/5-Workshop/5.5-Policy/test2.png) ) 
) 
![success](/images/5-Workshop/5.5-Policy/test2.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Thao tác này được cho phép bởi VPC endpoint policy.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Thao tác này được cho phép bởi VPC endpoint policy. ) 
) 
Thao tác này được cho phép bởi VPC endpoint policy.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![success](/images/5-Workshop/5.5-Policy/test2-success.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![success](/images/5-Workshop/5.5-Policy/test2-success.png) ) 
) 
![success](/images/5-Workshop/5.5-Policy/test2-success.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Sau đó chúng ta kiểm tra truy cập vào S3 bucket đầu tiên   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Sau đó chúng ta kiểm tra truy cập vào S3 bucket đầu tiên ) 
) 
Sau đó chúng ta kiểm tra truy cập vào S3 bucket đầu tiên

E:\thuctap\report mau\fcj-workshop-template-main>(
echo  ```aws s3 cp test-bucket2.xyz s3://<your-1st-bucket-name>```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo  ```aws s3 cp test-bucket2.xyz s3://<your-1st-bucket-name>``` ) 
) 
 ```aws s3 cp test-bucket2.xyz s3://<your-1st-bucket-name>```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo  ![fail](/images/5-Workshop/5.5-Policy/test2-fail.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo  ![fail](/images/5-Workshop/5.5-Policy/test2-fail.png) ) 
) 
 ![fail](/images/5-Workshop/5.5-Policy/test2-fail.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo  Câu lệnh xảy ra lỗi bởi vì bucket không có quyền truy cập bởi VPC endpoint policy.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo  Câu lệnh xảy ra lỗi bởi vì bucket không có quyền truy cập bởi VPC endpoint policy. ) 
) 
 Câu lệnh xảy ra lỗi bởi vì bucket không có quyền truy cập bởi VPC endpoint policy.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Trong phần này, bạn đã tạo chính sách VPC Endpoint cho Amazon S3 và sử dụng AWS CLI để kiểm tra chính sách. Các hoạt động AWS CLI liên quan đến bucket S3 ban đầu của bạn thất bại vì bạn áp dụng một chính sách chỉ cho phép truy cập đến bucket thứ hai mà bạn đã tạo. Các hoạt động AWS CLI nhắm vào bucket thứ hai của bạn thành công vì chính sách cho phép chúng. Những chính sách này có thể hữu ích trong các tình huống khi bạn cần kiểm soát quyền truy cập vào tài nguyên thông qua VPC Endpoint.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Trong phần này, bạn đã tạo chính sách VPC Endpoint cho Amazon S3 và sử dụng AWS CLI để kiểm tra chính sách. Các hoạt động AWS CLI liên quan đến bucket S3 ban đầu của bạn thất bại vì bạn áp dụng một chính sách chỉ cho phép truy cập đến bucket thứ hai mà bạn đã tạo. Các hoạt động AWS CLI nhắm vào bucket thứ hai của bạn thành công vì chính sách cho phép chúng. Những chính sách này có thể hữu ích trong các tình huống khi bạn cần kiểm soát quyền truy cập vào tài nguyên thông qua VPC Endpoint. ) 
) 
Trong phần này, bạn đã tạo chính sách VPC Endpoint cho Amazon S3 và sử dụng AWS CLI để kiểm tra chính sách. Các hoạt động AWS CLI liên quan đến bucket S3 ban đầu của bạn thất bại vì bạn áp dụng một chính sách chỉ cho phép truy cập đến bucket thứ hai mà bạn đã tạo. Các hoạt động AWS CLI nhắm vào bucket thứ hai của bạn thành công vì chính sách cho phép chúng. Những chính sách này có thể hữu ích trong các tình huống khi bạn cần kiểm soát quyền truy cập vào tài nguyên thông qua VPC Endpoint.
