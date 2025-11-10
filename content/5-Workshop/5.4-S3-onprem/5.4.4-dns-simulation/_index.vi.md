
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Mô phỏng On-premises DNS "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Mô phỏng On-premises DNS " ) 
) 
title : "Mô phỏng On-premises DNS "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo date : "`r Sys.Date()`"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo date : "`r Sys.Date()`" ) 
) 
date : "`r Sys.Date()`"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo weight : 4   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo weight : 4 ) 
) 
weight : 4

E:\thuctap\report mau\fcj-workshop-template-main>(
echo chapter : false   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo chapter : false ) 
) 
chapter : false

E:\thuctap\report mau\fcj-workshop-template-main>(
echo pre : " <b> 5.4.4 </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.4.4 </b> " ) 
) 
pre : " <b> 5.4.4 </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo  AWS PrivateLink endpoint có một địa chỉ IP cố định trong từng AZ nơi chúng được triển khai, trong suốt thời gian tồn tại của endpoint (cho đến khi endpoint bị xóa). Các địa chỉ IP này được gắn vào Elastic network interface (ENI). AWS khuyến nghị sử dụng DNS để resolve địa chỉ IP cho endpoint để các ứng dụng downstream sử dụng địa chỉ IP mới nhất khi ENIs được thêm vào AZ mới hoặc bị xóa theo thời gian.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo  AWS PrivateLink endpoint có một địa chỉ IP cố định trong từng AZ nơi chúng được triển khai, trong suốt thời gian tồn tại của endpoint (cho đến khi endpoint bị xóa). Các địa chỉ IP này được gắn vào Elastic network interface (ENI). AWS khuyến nghị sử dụng DNS để resolve địa chỉ IP cho endpoint để các ứng dụng downstream sử dụng địa chỉ IP mới nhất khi ENIs được thêm vào AZ mới hoặc bị xóa theo thời gian. ) 
) 
 AWS PrivateLink endpoint có một địa chỉ IP cố định trong từng AZ nơi chúng được triển khai, trong suốt thời gian tồn tại của endpoint (cho đến khi endpoint bị xóa). Các địa chỉ IP này được gắn vào Elastic network interface (ENI). AWS khuyến nghị sử dụng DNS để resolve địa chỉ IP cho endpoint để các ứng dụng downstream sử dụng địa chỉ IP mới nhất khi ENIs được thêm vào AZ mới hoặc bị xóa theo thời gian.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Trong phần này, bạn sẽ tạo một quy tắc chuyển tiếp (forwarding rule) để gửi các yêu cầu resolve DNS từ môi trường truyền thống (mô phỏng) đến Private Hosted Zone trên Route 53. Phần này tận dụng cơ sở hạ tầng do CloudFormation triển khai trong phần Chuẩn bị môi trường.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Trong phần này, bạn sẽ tạo một quy tắc chuyển tiếp (forwarding rule) để gửi các yêu cầu resolve DNS từ môi trường truyền thống (mô phỏng) đến Private Hosted Zone trên Route 53. Phần này tận dụng cơ sở hạ tầng do CloudFormation triển khai trong phần Chuẩn bị môi trường. ) 
) 
Trong phần này, bạn sẽ tạo một quy tắc chuyển tiếp (forwarding rule) để gửi các yêu cầu resolve DNS từ môi trường truyền thống (mô phỏng) đến Private Hosted Zone trên Route 53. Phần này tận dụng cơ sở hạ tầng do CloudFormation triển khai trong phần Chuẩn bị môi trường.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Tạo DNS Alias Records cho Interface endpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Tạo DNS Alias Records cho Interface endpoint ) 
) 
#### Tạo DNS Alias Records cho Interface endpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Click link để đi đến [Route 53 management console](https://us-east-1.console.aws.amazon.com/route53/v2/hostedzones?region=us-east-1#) (Hosted Zones section).  Mẫu CloudFormation mà bạn triển khai trong phần Chuẩn bị môi trường đã tạo Private Hosted Zone này. Nhấp vào tên của Private Hosted Zone, s3.us-east-1.amazonaws.com:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Click link để đi đến [Route 53 management console](https://us-east-1.console.aws.amazon.com/route53/v2/hostedzones?region=us-east-1#) (Hosted Zones section).  Mẫu CloudFormation mà bạn triển khai trong phần Chuẩn bị môi trường đã tạo Private Hosted Zone này. Nhấp vào tên của Private Hosted Zone, s3.us-east-1.amazonaws.com: ) 
) 
1. Click link để đi đến [Route 53 management console](https://us-east-1.console.aws.amazon.com/route53/v2/hostedzones?region=us-east-1#) (Hosted Zones section).  Mẫu CloudFormation mà bạn triển khai trong phần Chuẩn bị môi trường đã tạo Private Hosted Zone này. Nhấp vào tên của Private Hosted Zone, s3.us-east-1.amazonaws.com:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![hosted zone](/images/5-Workshop/5.4-S3-onprem/hosted-zone.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![hosted zone](/images/5-Workshop/5.4-S3-onprem/hosted-zone.png) ) 
) 
![hosted zone](/images/5-Workshop/5.4-S3-onprem/hosted-zone.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Tạo 1 record mới trong Private Hosted Zone:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Tạo 1 record mới trong Private Hosted Zone: ) 
) 
2. Tạo 1 record mới trong Private Hosted Zone:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Create record](/images/5-Workshop/5.4-S3-onprem/create-record1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Create record](/images/5-Workshop/5.4-S3-onprem/create-record1.png) ) 
) 
![Create record](/images/5-Workshop/5.4-S3-onprem/create-record1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Giữ nguyên Record name và record type   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Giữ nguyên Record name và record type ) 
) 
+ Giữ nguyên Record name và record type

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Alias Button: click để enable   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Alias Button: click để enable ) 
) 
+ Alias Button: click để enable

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Route traffic to: Alias to VPC Endpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Route traffic to: Alias to VPC Endpoint ) 
) 
+ Route traffic to: Alias to VPC Endpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Region: US East (N. Virginia) [us-east-1]   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Region: US East (N. Virginia) [us-east-1] ) 
) 
+ Region: US East (N. Virginia) [us-east-1]

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Chọn endpoint: Paste tên (Regional VPC Endpoint DNS) bạn đã lưu lại ở phần 4.3   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Chọn endpoint: Paste tên (Regional VPC Endpoint DNS) bạn đã lưu lại ở phần 4.3 ) 
) 
+ Chọn endpoint: Paste tên (Regional VPC Endpoint DNS) bạn đã lưu lại ở phần 4.3

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![record1](/images/5-Workshop/5.4-S3-onprem/record1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![record1](/images/5-Workshop/5.4-S3-onprem/record1.png) ) 
) 
![record1](/images/5-Workshop/5.4-S3-onprem/record1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Click Add another record, và add 1 cái record thứ 2 sử dụng những thông số sau:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Click Add another record, và add 1 cái record thứ 2 sử dụng những thông số sau: ) 
) 
3. Click Add another record, và add 1 cái record thứ 2 sử dụng những thông số sau:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Record name: *.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Record name: *. ) 
) 
+ Record name: *.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Record type: giữ giá trị default (type A)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Record type: giữ giá trị default (type A) ) 
) 
+ Record type: giữ giá trị default (type A)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Alias Button: Click để enable   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Alias Button: Click để enable ) 
) 
+ Alias Button: Click để enable

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Route traffic to: Alias to VPC Endpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Route traffic to: Alias to VPC Endpoint ) 
) 
+ Route traffic to: Alias to VPC Endpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Region: US East (N. Virginia) [us-east-1]   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Region: US East (N. Virginia) [us-east-1] ) 
) 
+ Region: US East (N. Virginia) [us-east-1]

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Chọn endpoint: Paste tên (Regional VPC Endpoint DNS) bạn đã lưu lại ở phần 4.3   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Chọn endpoint: Paste tên (Regional VPC Endpoint DNS) bạn đã lưu lại ở phần 4.3 ) 
) 
+ Chọn endpoint: Paste tên (Regional VPC Endpoint DNS) bạn đã lưu lại ở phần 4.3

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Click **Create records**    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Click **Create records**  ) 
) 
+ Click **Create records** 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![record 2](/images/5-Workshop/5.4-S3-onprem/record2.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![record 2](/images/5-Workshop/5.4-S3-onprem/record2.png) ) 
) 
![record 2](/images/5-Workshop/5.4-S3-onprem/record2.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Record mới xuất hiện trên giao diện Route 53.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Record mới xuất hiện trên giao diện Route 53. ) 
) 
Record mới xuất hiện trên giao diện Route 53.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![result](/images/5-Workshop/5.4-S3-onprem/result.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![result](/images/5-Workshop/5.4-S3-onprem/result.png) ) 
) 
![result](/images/5-Workshop/5.4-S3-onprem/result.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Tạo một Resolver Forwarding Rule   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Tạo một Resolver Forwarding Rule ) 
) 
#### Tạo một Resolver Forwarding Rule

E:\thuctap\report mau\fcj-workshop-template-main>(
echo **Route 53 Resolver Forwarding Rules** cho phép bạn chuyển tiếp các DNS queries từ VPC của bạn đến các nguồn khác để resolve name. Bên ngoài môi trường workshop, bạn có thể sử dụng tính năng này để chuyển tiếp các DNS queries từ VPC của bạn đến các máy chủ DNS chạy trên on-premises. Trong phần này, bạn sẽ mô phỏng một on-premises conditional forwarder bằng cách tạo một forwarding rule để chuyển tiếp các DNS queries for Amazon S3 đến một Private Hosted Zone chạy trong "VPC Cloud" để resolve PrivateLink interface endpoint regional DNS name.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo **Route 53 Resolver Forwarding Rules** cho phép bạn chuyển tiếp các DNS queries từ VPC của bạn đến các nguồn khác để resolve name. Bên ngoài môi trường workshop, bạn có thể sử dụng tính năng này để chuyển tiếp các DNS queries từ VPC của bạn đến các máy chủ DNS chạy trên on-premises. Trong phần này, bạn sẽ mô phỏng một on-premises conditional forwarder bằng cách tạo một forwarding rule để chuyển tiếp các DNS queries for Amazon S3 đến một Private Hosted Zone chạy trong "VPC Cloud" để resolve PrivateLink interface endpoint regional DNS name. ) 
) 
**Route 53 Resolver Forwarding Rules** cho phép bạn chuyển tiếp các DNS queries từ VPC của bạn đến các nguồn khác để resolve name. Bên ngoài môi trường workshop, bạn có thể sử dụng tính năng này để chuyển tiếp các DNS queries từ VPC của bạn đến các máy chủ DNS chạy trên on-premises. Trong phần này, bạn sẽ mô phỏng một on-premises conditional forwarder bằng cách tạo một forwarding rule để chuyển tiếp các DNS queries for Amazon S3 đến một Private Hosted Zone chạy trong "VPC Cloud" để resolve PrivateLink interface endpoint regional DNS name.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Từ giao diện  **Route 53**, chọn **Inbound endpoints** trên thanh bên trái   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Từ giao diện  **Route 53**, chọn **Inbound endpoints** trên thanh bên trái ) 
) 
1. Từ giao diện  **Route 53**, chọn **Inbound endpoints** trên thanh bên trái

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Trong giao diện **Inbound endpoint**, Chọn ID của Inbound endpoint.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Trong giao diện **Inbound endpoint**, Chọn ID của Inbound endpoint. ) 
) 
2. Trong giao diện **Inbound endpoint**, Chọn ID của Inbound endpoint.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Inbound endpoint](/images/5-Workshop/5.4-S3-onprem/route53-1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Inbound endpoint](/images/5-Workshop/5.4-S3-onprem/route53-1.png) ) 
) 
![Inbound endpoint](/images/5-Workshop/5.4-S3-onprem/route53-1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Sao chép 2 địa chỉ IP trong danh sách vào trình chỉnh sửa.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Sao chép 2 địa chỉ IP trong danh sách vào trình chỉnh sửa. ) 
) 
3. Sao chép 2 địa chỉ IP trong danh sách vào trình chỉnh sửa.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Ip addresses](/images/5-Workshop/5.4-S3-onprem/route53-2.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Ip addresses](/images/5-Workshop/5.4-S3-onprem/route53-2.png) ) 
) 
![Ip addresses](/images/5-Workshop/5.4-S3-onprem/route53-2.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 4. Từ giao diện Route 53, chọn  **Resolver** > **Rules** và chọn **Create rule**   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 4. Từ giao diện Route 53, chọn  **Resolver** > **Rules** và chọn **Create rule** ) 
) 
4. Từ giao diện Route 53, chọn  **Resolver** > **Rules** và chọn **Create rule**

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Ip addresses](/images/5-Workshop/5.4-S3-onprem/route53-3.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Ip addresses](/images/5-Workshop/5.4-S3-onprem/route53-3.png) ) 
) 
![Ip addresses](/images/5-Workshop/5.4-S3-onprem/route53-3.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 5. Trong giao diện **Create rule**   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 5. Trong giao diện **Create rule** ) 
) 
5. Trong giao diện **Create rule**

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Name: myS3Rule   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Name: myS3Rule ) 
) 
+ Name: myS3Rule

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Rule type: Forward   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Rule type: Forward ) 
) 
+ Rule type: Forward

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Domain name: s3.us-east-1.amazonaws.com   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Domain name: s3.us-east-1.amazonaws.com ) 
) 
+ Domain name: s3.us-east-1.amazonaws.com

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create rule](/images/5-Workshop/5.4-S3-onprem/route53-4.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create rule](/images/5-Workshop/5.4-S3-onprem/route53-4.png) ) 
) 
![create rule](/images/5-Workshop/5.4-S3-onprem/route53-4.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + VPC: VPC On-prem   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + VPC: VPC On-prem ) 
) 
+ VPC: VPC On-prem

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Outbound endpoint: VPCOnpremOutboundEndpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Outbound endpoint: VPCOnpremOutboundEndpoint ) 
) 
+ Outbound endpoint: VPCOnpremOutboundEndpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create rule](/images/5-Workshop/5.4-S3-onprem/route53-5.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create rule](/images/5-Workshop/5.4-S3-onprem/route53-5.png) ) 
) 
![create rule](/images/5-Workshop/5.4-S3-onprem/route53-5.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Target IP Addresses: điền cả hai IP bạn đã lưu trữ trên trình soạn thảo (inbound endpoint addresses) và sau đó chọn **Submit**   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Target IP Addresses: điền cả hai IP bạn đã lưu trữ trên trình soạn thảo (inbound endpoint addresses) và sau đó chọn **Submit** ) 
) 
+ Target IP Addresses: điền cả hai IP bạn đã lưu trữ trên trình soạn thảo (inbound endpoint addresses) và sau đó chọn **Submit**

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create rule](/images/5-Workshop/5.4-S3-onprem/route53-6.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create rule](/images/5-Workshop/5.4-S3-onprem/route53-6.png) ) 
) 
![create rule](/images/5-Workshop/5.4-S3-onprem/route53-6.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Bạn đã tạo thành công resolver forwarding rule.    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Bạn đã tạo thành công resolver forwarding rule.  ) 
) 
Bạn đã tạo thành công resolver forwarding rule. 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create rule](/images/5-Workshop/5.4-S3-onprem/route53-7.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create rule](/images/5-Workshop/5.4-S3-onprem/route53-7.png) ) 
) 
![create rule](/images/5-Workshop/5.4-S3-onprem/route53-7.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Kiểm tra on-premises DNS mô phỏng.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Kiểm tra on-premises DNS mô phỏng. ) 
) 
#### Kiểm tra on-premises DNS mô phỏng.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Kết nối đến **Test-Interface-Endpoint EC2 instance** với **Session Manager**   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Kết nối đến **Test-Interface-Endpoint EC2 instance** với **Session Manager** ) 
) 
1. Kết nối đến **Test-Interface-Endpoint EC2 instance** với **Session Manager**

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create rule](/images/5-Workshop/5.4-S3-onprem/test1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create rule](/images/5-Workshop/5.4-S3-onprem/test1.png) ) 
) 
![create rule](/images/5-Workshop/5.4-S3-onprem/test1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Kiểm tra DNS resolution. Lệnh dig sẽ trả về địa chỉ IP được gán cho VPC endpoint interface đang chạy trên VPC (địa chỉ IP của bạn sẽ khác):   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Kiểm tra DNS resolution. Lệnh dig sẽ trả về địa chỉ IP được gán cho VPC endpoint interface đang chạy trên VPC (địa chỉ IP của bạn sẽ khác): ) 
) 
2. Kiểm tra DNS resolution. Lệnh dig sẽ trả về địa chỉ IP được gán cho VPC endpoint interface đang chạy trên VPC (địa chỉ IP của bạn sẽ khác):

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ``` ) 
) 
```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo dig +short s3.us-east-1.amazonaws.com    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo dig +short s3.us-east-1.amazonaws.com  ) 
) 
dig +short s3.us-east-1.amazonaws.com 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ``` ) 
) 
```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo {{% notice note %}}   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo {{% notice note %}} ) 
) 
{{% notice note %}}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Các địa chỉ IP được trả về là các địa chỉ IP VPC enpoint, KHÔNG phải là các địa chỉ IP Resolver mà bạn đã dán từ trình chỉnh sửa văn bản của mình. Các địa chỉ IP của  Resolver endpoint  và  VPC endpoin trông giống nhau vì chúng đều từ khối CIDR VPC Cloud.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Các địa chỉ IP được trả về là các địa chỉ IP VPC enpoint, KHÔNG phải là các địa chỉ IP Resolver mà bạn đã dán từ trình chỉnh sửa văn bản của mình. Các địa chỉ IP của  Resolver endpoint  và  VPC endpoin trông giống nhau vì chúng đều từ khối CIDR VPC Cloud. ) 
) 
Các địa chỉ IP được trả về là các địa chỉ IP VPC enpoint, KHÔNG phải là các địa chỉ IP Resolver mà bạn đã dán từ trình chỉnh sửa văn bản của mình. Các địa chỉ IP của  Resolver endpoint  và  VPC endpoin trông giống nhau vì chúng đều từ khối CIDR VPC Cloud.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo {{% /notice %}}   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo {{% /notice %}} ) 
) 
{{% /notice %}}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create rule](/images/5-Workshop/5.4-S3-onprem/dig.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create rule](/images/5-Workshop/5.4-S3-onprem/dig.png) ) 
) 
![create rule](/images/5-Workshop/5.4-S3-onprem/dig.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Truy cập vào menu VPC (phần Endpoints), chọn S3 interface endpoint. Nhấp vào tab Subnets và xác nhận rằng các địa chỉ IP được trả về bởi lệnh Dig khớp với VPC endpoint:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Truy cập vào menu VPC (phần Endpoints), chọn S3 interface endpoint. Nhấp vào tab Subnets và xác nhận rằng các địa chỉ IP được trả về bởi lệnh Dig khớp với VPC endpoint: ) 
) 
3. Truy cập vào menu VPC (phần Endpoints), chọn S3 interface endpoint. Nhấp vào tab Subnets và xác nhận rằng các địa chỉ IP được trả về bởi lệnh Dig khớp với VPC endpoint:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create rule](/images/5-Workshop/5.4-S3-onprem/subnet.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create rule](/images/5-Workshop/5.4-S3-onprem/subnet.png) ) 
) 
![create rule](/images/5-Workshop/5.4-S3-onprem/subnet.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 4. Hãy quay lại shell của bạn và sử dụng AWS CLI để kiểm tra danh sách các bucket S3 của bạn:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 4. Hãy quay lại shell của bạn và sử dụng AWS CLI để kiểm tra danh sách các bucket S3 của bạn: ) 
) 
4. Hãy quay lại shell của bạn và sử dụng AWS CLI để kiểm tra danh sách các bucket S3 của bạn:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ``` ) 
) 
```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo aws s3 ls --endpoint-url https://s3.us-east-1.amazonaws.com   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo aws s3 ls --endpoint-url https://s3.us-east-1.amazonaws.com ) 
) 
aws s3 ls --endpoint-url https://s3.us-east-1.amazonaws.com

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ``` ) 
) 
```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create rule](/images/5-Workshop/5.4-S3-onprem/endpoint.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create rule](/images/5-Workshop/5.4-S3-onprem/endpoint.png) ) 
) 
![create rule](/images/5-Workshop/5.4-S3-onprem/endpoint.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 5. Kết thúc phiên làm việc của Session Manager của bạn:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 5. Kết thúc phiên làm việc của Session Manager của bạn: ) 
) 
5. Kết thúc phiên làm việc của Session Manager của bạn:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create rule](/images/5-Workshop/5.4-S3-onprem/terminal.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create rule](/images/5-Workshop/5.4-S3-onprem/terminal.png) ) 
) 
![create rule](/images/5-Workshop/5.4-S3-onprem/terminal.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Trong phần này, bạn đã tạo một  **Interface Endpoint**  cho Amazon S3. Điểm cuối này có thể được truy cập từ on-premises thông qua Site-to-Site VPN hoặc AWS Direct Connect. Các điểm cuối Route 53 Resolver outbound giả lập chuyển tiếp các yêu cầu DNS từ on-premises đến một Private Hosted Zone đang chạy trên đám mây. Các điểm cuối Route 53 inbound nhận yêu cầu giải quyết và trả về một phản hồi chứa địa chỉ IP của  **Interface Endpoint**  VPC. Sử dụng DNS để giải quyết các địa chỉ IP của điểm cuối cung cấp tính sẵn sàng cao trong trường hợp một Availability Zone gặp sự cố.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Trong phần này, bạn đã tạo một  **Interface Endpoint**  cho Amazon S3. Điểm cuối này có thể được truy cập từ on-premises thông qua Site-to-Site VPN hoặc AWS Direct Connect. Các điểm cuối Route 53 Resolver outbound giả lập chuyển tiếp các yêu cầu DNS từ on-premises đến một Private Hosted Zone đang chạy trên đám mây. Các điểm cuối Route 53 inbound nhận yêu cầu giải quyết và trả về một phản hồi chứa địa chỉ IP của  **Interface Endpoint**  VPC. Sử dụng DNS để giải quyết các địa chỉ IP của điểm cuối cung cấp tính sẵn sàng cao trong trường hợp một Availability Zone gặp sự cố. ) 
) 
Trong phần này, bạn đã tạo một  **Interface Endpoint**  cho Amazon S3. Điểm cuối này có thể được truy cập từ on-premises thông qua Site-to-Site VPN hoặc AWS Direct Connect. Các điểm cuối Route 53 Resolver outbound giả lập chuyển tiếp các yêu cầu DNS từ on-premises đến một Private Hosted Zone đang chạy trên đám mây. Các điểm cuối Route 53 inbound nhận yêu cầu giải quyết và trả về một phản hồi chứa địa chỉ IP của  **Interface Endpoint**  VPC. Sử dụng DNS để giải quyết các địa chỉ IP của điểm cuối cung cấp tính sẵn sàng cao trong trường hợp một Availability Zone gặp sự cố.
