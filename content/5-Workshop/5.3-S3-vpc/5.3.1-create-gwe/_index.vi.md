
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Tạo một Gateway Endpoint"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Tạo một Gateway Endpoint" ) 
) 
title : "Tạo một Gateway Endpoint"

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
echo 1. Mở [Amazon VPC console](https://us-east-1.console.aws.amazon.com/vpc/home?region=us-east-1#Home:)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Mở [Amazon VPC console](https://us-east-1.console.aws.amazon.com/vpc/home?region=us-east-1#Home:) ) 
) 
1. Mở [Amazon VPC console](https://us-east-1.console.aws.amazon.com/vpc/home?region=us-east-1#Home:)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Trong thanh điều hướng, chọn **Endpoints**, click **Create Endpoint**:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Trong thanh điều hướng, chọn **Endpoints**, click **Create Endpoint**: ) 
) 
2. Trong thanh điều hướng, chọn **Endpoints**, click **Create Endpoint**:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo {{% notice note %}}   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo {{% notice note %}} ) 
) 
{{% notice note %}}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Bạn sẽ thấy 6 điểm cuối VPC hiện có hỗ trợ AWS Systems Manager (SSM). Các điểm cuối này được Mẫu CloudFormation triển khai tự động cho workshop này.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Bạn sẽ thấy 6 điểm cuối VPC hiện có hỗ trợ AWS Systems Manager (SSM). Các điểm cuối này được Mẫu CloudFormation triển khai tự động cho workshop này. ) 
) 
Bạn sẽ thấy 6 điểm cuối VPC hiện có hỗ trợ AWS Systems Manager (SSM). Các điểm cuối này được Mẫu CloudFormation triển khai tự động cho workshop này.

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
echo 3. Trong Create endpoint console:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Trong Create endpoint console: ) 
) 
3. Trong Create endpoint console:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Đặt tên cho endpoint: s3-gwe   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Đặt tên cho endpoint: s3-gwe ) 
) 
+ Đặt tên cho endpoint: s3-gwe

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Trong service category, chọn **aws services**   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Trong service category, chọn **aws services** ) 
) 
+ Trong service category, chọn **aws services**

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/create-s3-gwe1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/create-s3-gwe1.png) ) 
) 
![endpoint](/images/5-Workshop/5.3-S3-vpc/create-s3-gwe1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Trong **Services**, gõ "s3" trong hộp tìm kiếm và chọn dịch vụ với loại **gateway**   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Trong **Services**, gõ "s3" trong hộp tìm kiếm và chọn dịch vụ với loại **gateway** ) 
) 
+ Trong **Services**, gõ "s3" trong hộp tìm kiếm và chọn dịch vụ với loại **gateway**

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/services.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/services.png) ) 
) 
![endpoint](/images/5-Workshop/5.3-S3-vpc/services.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Đối với VPC, chọn **VPC Cloud** từ drop-down menu.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Đối với VPC, chọn **VPC Cloud** từ drop-down menu. ) 
) 
+ Đối với VPC, chọn **VPC Cloud** từ drop-down menu.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Đối với Route tables, chọn bảng định tuyến mà đã liên kết với 2 subnets (lưu ý: đây không phải là bảng định tuyến chính cho VPC mà là bảng định tuyến thứ hai do CloudFormation tạo).   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Đối với Route tables, chọn bảng định tuyến mà đã liên kết với 2 subnets (lưu ý: đây không phải là bảng định tuyến chính cho VPC mà là bảng định tuyến thứ hai do CloudFormation tạo). ) 
) 
+ Đối với Route tables, chọn bảng định tuyến mà đã liên kết với 2 subnets (lưu ý: đây không phải là bảng định tuyến chính cho VPC mà là bảng định tuyến thứ hai do CloudFormation tạo).

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/vpc.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/vpc.png) ) 
) 
![endpoint](/images/5-Workshop/5.3-S3-vpc/vpc.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Đối với Policy, để tùy chọn mặc định là Full access để cho phép toàn quyền truy cập vào dịch vụ. Bạn sẽ triển khai VPC endpoint policy trong phần sau để chứng minh việc hạn chế quyền truy cập vào S3 bucket dựa trên các policies.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Đối với Policy, để tùy chọn mặc định là Full access để cho phép toàn quyền truy cập vào dịch vụ. Bạn sẽ triển khai VPC endpoint policy trong phần sau để chứng minh việc hạn chế quyền truy cập vào S3 bucket dựa trên các policies. ) 
) 
+ Đối với Policy, để tùy chọn mặc định là Full access để cho phép toàn quyền truy cập vào dịch vụ. Bạn sẽ triển khai VPC endpoint policy trong phần sau để chứng minh việc hạn chế quyền truy cập vào S3 bucket dựa trên các policies.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/policy.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/policy.png) ) 
) 
![endpoint](/images/5-Workshop/5.3-S3-vpc/policy.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Không thêm tag vào VPC endpoint.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Không thêm tag vào VPC endpoint. ) 
) 
+ Không thêm tag vào VPC endpoint.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Click Create endpoint, click x sau khi nhận được thông báo tạo thành công.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Click Create endpoint, click x sau khi nhận được thông báo tạo thành công. ) 
) 
+ Click Create endpoint, click x sau khi nhận được thông báo tạo thành công.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/complete.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![endpoint](/images/5-Workshop/5.3-S3-vpc/complete.png) ) 
) 
![endpoint](/images/5-Workshop/5.3-S3-vpc/complete.png)
