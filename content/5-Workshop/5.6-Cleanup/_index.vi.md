
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Dọn dẹp tài nguyên"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Dọn dẹp tài nguyên" ) 
) 
title : "Dọn dẹp tài nguyên"

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
echo #### Dọn dẹp tài nguyên   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Dọn dẹp tài nguyên ) 
) 
#### Dọn dẹp tài nguyên

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Xin chúc mừng bạn đã hoàn thành xong lab này!   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Xin chúc mừng bạn đã hoàn thành xong lab này! ) 
) 
Xin chúc mừng bạn đã hoàn thành xong lab này!

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Trong lab này, bạn đã học về các mô hình kiến trúc để truy cập Amazon S3 mà không sử dụng Public Internet.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Trong lab này, bạn đã học về các mô hình kiến trúc để truy cập Amazon S3 mà không sử dụng Public Internet. ) 
) 
Trong lab này, bạn đã học về các mô hình kiến trúc để truy cập Amazon S3 mà không sử dụng Public Internet.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Bằng cách tạo Gateway endpoint, bạn đã cho phép giao tiếp trực tiếp giữa các tài nguyên EC2 và Amazon S3, mà không đi qua Internet Gateway.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Bằng cách tạo Gateway endpoint, bạn đã cho phép giao tiếp trực tiếp giữa các tài nguyên EC2 và Amazon S3, mà không đi qua Internet Gateway. ) 
) 
+ Bằng cách tạo Gateway endpoint, bạn đã cho phép giao tiếp trực tiếp giữa các tài nguyên EC2 và Amazon S3, mà không đi qua Internet Gateway.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Bằng cách tạo Interface endpoint, bạn đã mở rộng kết nối S3 đến các tài nguyên chạy trên trung tâm dữ liệu trên chỗ của bạn thông qua AWS Site-to-Site VPN hoặc Direct Connect.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Bằng cách tạo Interface endpoint, bạn đã mở rộng kết nối S3 đến các tài nguyên chạy trên trung tâm dữ liệu trên chỗ của bạn thông qua AWS Site-to-Site VPN hoặc Direct Connect. ) 
) 
Bằng cách tạo Interface endpoint, bạn đã mở rộng kết nối S3 đến các tài nguyên chạy trên trung tâm dữ liệu trên chỗ của bạn thông qua AWS Site-to-Site VPN hoặc Direct Connect.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Dọn dẹp   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Dọn dẹp ) 
) 
#### Dọn dẹp

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Điều hướng đến Hosted Zones trên phía trái của bảng điều khiển Route 53. Nhấp vào tên của  s3.us-east-1.amazonaws.com zone. Nhấp vào Delete và xác nhận việc xóa bằng cách nhập từ khóa "delete".   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Điều hướng đến Hosted Zones trên phía trái của bảng điều khiển Route 53. Nhấp vào tên của  s3.us-east-1.amazonaws.com zone. Nhấp vào Delete và xác nhận việc xóa bằng cách nhập từ khóa "delete". ) 
) 
1. Điều hướng đến Hosted Zones trên phía trái của bảng điều khiển Route 53. Nhấp vào tên của  s3.us-east-1.amazonaws.com zone. Nhấp vào Delete và xác nhận việc xóa bằng cách nhập từ khóa "delete".

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![hosted zone](/images/5-Workshop/5.6-Cleanup/delete-zone.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![hosted zone](/images/5-Workshop/5.6-Cleanup/delete-zone.png) ) 
) 
![hosted zone](/images/5-Workshop/5.6-Cleanup/delete-zone.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Disassociate Route 53 Resolver Rule - myS3Rule from "VPC Onprem" and Delete it.    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Disassociate Route 53 Resolver Rule - myS3Rule from "VPC Onprem" and Delete it.  ) 
) 
2. Disassociate Route 53 Resolver Rule - myS3Rule from "VPC Onprem" and Delete it. 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![hosted zone](/images/5-Workshop/5.6-Cleanup/vpc.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![hosted zone](/images/5-Workshop/5.6-Cleanup/vpc.png) ) 
) 
![hosted zone](/images/5-Workshop/5.6-Cleanup/vpc.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 4.Mở console của CloudFormation và xóa hai stack CloudFormation mà bạn đã tạo cho bài thực hành này:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 4.Mở console của CloudFormation và xóa hai stack CloudFormation mà bạn đã tạo cho bài thực hành này: ) 
) 
4.Mở console của CloudFormation và xóa hai stack CloudFormation mà bạn đã tạo cho bài thực hành này:

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
echo 5. Xóa các S3 bucket   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 5. Xóa các S3 bucket ) 
) 
5. Xóa các S3 bucket

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Mở bảng điều khiển S3   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Mở bảng điều khiển S3 ) 
) 
+ Mở bảng điều khiển S3

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Chọn bucket chúng ta đã tạo cho lab, nhấp chuột và xác nhận là empty. Nhấp Delete và xác nhận delete.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Chọn bucket chúng ta đã tạo cho lab, nhấp chuột và xác nhận là empty. Nhấp Delete và xác nhận delete. ) 
) 
+ Chọn bucket chúng ta đã tạo cho lab, nhấp chuột và xác nhận là empty. Nhấp Delete và xác nhận delete.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo +    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo +  ) 
) 
+ 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![delete s3](/images/5-Workshop/5.6-Cleanup/delete-s3.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![delete s3](/images/5-Workshop/5.6-Cleanup/delete-s3.png) ) 
) 
![delete s3](/images/5-Workshop/5.6-Cleanup/delete-s3.png)
