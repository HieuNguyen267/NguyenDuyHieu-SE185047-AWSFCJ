
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Chuẩn bị tài nguyên"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Chuẩn bị tài nguyên" ) 
) 
title : "Chuẩn bị tài nguyên"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo date : "`r Sys.Date()`"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo date : "`r Sys.Date()`" ) 
) 
date : "`r Sys.Date()`"

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
echo pre : " <b> 5.4.1 </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.4.1 </b> " ) 
) 
pre : " <b> 5.4.1 </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Để chuẩn bị cho phần này của workshop, bạn sẽ cần phải:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Để chuẩn bị cho phần này của workshop, bạn sẽ cần phải: ) 
) 
Để chuẩn bị cho phần này của workshop, bạn sẽ cần phải:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Triển khai CloudFormation stack   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Triển khai CloudFormation stack ) 
) 
+ Triển khai CloudFormation stack

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Sửa đổi bảng định tuyến VPC.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Sửa đổi bảng định tuyến VPC. ) 
) 
+ Sửa đổi bảng định tuyến VPC.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Các thành phần này hoạt động cùng nhau để mô phỏng DNS forwarding và name resolution.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Các thành phần này hoạt động cùng nhau để mô phỏng DNS forwarding và name resolution. ) 
) 
Các thành phần này hoạt động cùng nhau để mô phỏng DNS forwarding và name resolution.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Triển khai CloudFormation stack   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Triển khai CloudFormation stack ) 
) 
#### Triển khai CloudFormation stack

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Mẫu CloudFormation sẽ tạo các dịch vụ bổ sung để hỗ trợ mô phỏng môi trường truyền thống:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Mẫu CloudFormation sẽ tạo các dịch vụ bổ sung để hỗ trợ mô phỏng môi trường truyền thống: ) 
) 
Mẫu CloudFormation sẽ tạo các dịch vụ bổ sung để hỗ trợ mô phỏng môi trường truyền thống:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Một Route 53 Private Hosted Zone lưu trữ các bản ghi Bí danh (Alias records) cho điểm cuối PrivateLink S3   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Một Route 53 Private Hosted Zone lưu trữ các bản ghi Bí danh (Alias records) cho điểm cuối PrivateLink S3 ) 
) 
+ Một Route 53 Private Hosted Zone lưu trữ các bản ghi Bí danh (Alias records) cho điểm cuối PrivateLink S3

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Một Route 53 Inbound Resolver endpoint cho phép "VPC Cloud" giải quyết các yêu cầu resolve DNS gửi đến Private Hosted Zone   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Một Route 53 Inbound Resolver endpoint cho phép "VPC Cloud" giải quyết các yêu cầu resolve DNS gửi đến Private Hosted Zone ) 
) 
+ Một Route 53 Inbound Resolver endpoint cho phép "VPC Cloud" giải quyết các yêu cầu resolve DNS gửi đến Private Hosted Zone

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Một Route 53 Outbound Resolver endpoint cho phép "VPC On-prem" chuyển tiếp các yêu cầu DNS cho S3 sang "VPC Cloud"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Một Route 53 Outbound Resolver endpoint cho phép "VPC On-prem" chuyển tiếp các yêu cầu DNS cho S3 sang "VPC Cloud" ) 
) 
+ Một Route 53 Outbound Resolver endpoint cho phép "VPC On-prem" chuyển tiếp các yêu cầu DNS cho S3 sang "VPC Cloud"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![route 53 diagram](/images/5-Workshop/5.4-S3-onprem/route53.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![route 53 diagram](/images/5-Workshop/5.4-S3-onprem/route53.png) ) 
) 
![route 53 diagram](/images/5-Workshop/5.4-S3-onprem/route53.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Click link sau để mở [AWS CloudFormation console](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://s3.amazonaws.com/reinvent-endpoints-builders-session/R53CF.yaml&stackName=PLOnpremSetup). Mẫu yêu cầu sẽ được tải sẵn vào menu. Chấp nhận tất cả mặc định và nhấp vào Tạo stack.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Click link sau để mở [AWS CloudFormation console](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://s3.amazonaws.com/reinvent-endpoints-builders-session/R53CF.yaml&stackName=PLOnpremSetup). Mẫu yêu cầu sẽ được tải sẵn vào menu. Chấp nhận tất cả mặc định và nhấp vào Tạo stack. ) 
) 
1. Click link sau để mở [AWS CloudFormation console](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://s3.amazonaws.com/reinvent-endpoints-builders-session/R53CF.yaml&stackName=PLOnpremSetup). Mẫu yêu cầu sẽ được tải sẵn vào menu. Chấp nhận tất cả mặc định và nhấp vào Tạo stack.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Create stack](/images/5-Workshop/5.4-S3-onprem/create-stack.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Create stack](/images/5-Workshop/5.4-S3-onprem/create-stack.png) ) 
) 
![Create stack](/images/5-Workshop/5.4-S3-onprem/create-stack.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Button](/images/5-Workshop/5.4-S3-onprem/create-stack-button.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Button](/images/5-Workshop/5.4-S3-onprem/create-stack-button.png) ) 
) 
![Button](/images/5-Workshop/5.4-S3-onprem/create-stack-button.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Có thể mất vài phút để triển khai stack hoàn tất. Bạn có thể tiếp tục với bước tiếp theo mà không cần đợi quá trình triển khai kết thúc.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Có thể mất vài phút để triển khai stack hoàn tất. Bạn có thể tiếp tục với bước tiếp theo mà không cần đợi quá trình triển khai kết thúc. ) 
) 
Có thể mất vài phút để triển khai stack hoàn tất. Bạn có thể tiếp tục với bước tiếp theo mà không cần đợi quá trình triển khai kết thúc.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ####  Cập nhật bảng định tuyến private on-premise    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ####  Cập nhật bảng định tuyến private on-premise  ) 
) 
####  Cập nhật bảng định tuyến private on-premise 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Workshop này sử dụng StrongSwan VPN chạy trên EC2 instance để mô phỏng khả năng kết nối giữa trung tâm dữ liệu truyền thống và môi trường cloud AWS. Hầu hết các thành phần bắt buộc đều được cung cấp trước khi bạn bắt đầu. Để hoàn tất cấu hình VPN, bạn sẽ sửa đổi bảng định tuyến "VPC on-prem" để hướng lưu lượng đến cloud đi qua StrongSwan VPN instance.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Workshop này sử dụng StrongSwan VPN chạy trên EC2 instance để mô phỏng khả năng kết nối giữa trung tâm dữ liệu truyền thống và môi trường cloud AWS. Hầu hết các thành phần bắt buộc đều được cung cấp trước khi bạn bắt đầu. Để hoàn tất cấu hình VPN, bạn sẽ sửa đổi bảng định tuyến "VPC on-prem" để hướng lưu lượng đến cloud đi qua StrongSwan VPN instance. ) 
) 
Workshop này sử dụng StrongSwan VPN chạy trên EC2 instance để mô phỏng khả năng kết nối giữa trung tâm dữ liệu truyền thống và môi trường cloud AWS. Hầu hết các thành phần bắt buộc đều được cung cấp trước khi bạn bắt đầu. Để hoàn tất cấu hình VPN, bạn sẽ sửa đổi bảng định tuyến "VPC on-prem" để hướng lưu lượng đến cloud đi qua StrongSwan VPN instance.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Mở Amazon EC2 console    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Mở Amazon EC2 console  ) 
) 
1. Mở Amazon EC2 console 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Chọn instance tên infra-vpngw-test. Từ Details tab, copy Instance ID và paste vào text editor của bạn để sử dụng ở những bước tiếp theo   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Chọn instance tên infra-vpngw-test. Từ Details tab, copy Instance ID và paste vào text editor của bạn để sử dụng ở những bước tiếp theo ) 
) 
2. Chọn instance tên infra-vpngw-test. Từ Details tab, copy Instance ID và paste vào text editor của bạn để sử dụng ở những bước tiếp theo

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![ec2 id](/images/5-Workshop/5.4-S3-onprem/ec2-onprem-id.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![ec2 id](/images/5-Workshop/5.4-S3-onprem/ec2-onprem-id.png) ) 
) 
![ec2 id](/images/5-Workshop/5.4-S3-onprem/ec2-onprem-id.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Đi đến VPC menu bằng cách gõ "VPC" vào Search box   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Đi đến VPC menu bằng cách gõ "VPC" vào Search box ) 
) 
3. Đi đến VPC menu bằng cách gõ "VPC" vào Search box

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 4. Click vào Route Tables, chọn RT Private On-prem route table, chọn Routes tab, và click Edit Routes.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 4. Click vào Route Tables, chọn RT Private On-prem route table, chọn Routes tab, và click Edit Routes. ) 
) 
4. Click vào Route Tables, chọn RT Private On-prem route table, chọn Routes tab, và click Edit Routes.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![rt](/images/5-Workshop/5.4-S3-onprem/rt.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![rt](/images/5-Workshop/5.4-S3-onprem/rt.png) ) 
) 
![rt](/images/5-Workshop/5.4-S3-onprem/rt.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 5. Click Add route.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 5. Click Add route. ) 
) 
5. Click Add route.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Destination: CIDR block của Cloud VPC   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Destination: CIDR block của Cloud VPC ) 
) 
+ Destination: CIDR block của Cloud VPC

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Target: ID của infra-vpngw-test instance (bạn đã lưu lại ở bước trên)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Target: ID của infra-vpngw-test instance (bạn đã lưu lại ở bước trên) ) 
) 
+ Target: ID của infra-vpngw-test instance (bạn đã lưu lại ở bước trên)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![add route](/images/5-Workshop/5.4-S3-onprem/add-route.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![add route](/images/5-Workshop/5.4-S3-onprem/add-route.png) ) 
) 
![add route](/images/5-Workshop/5.4-S3-onprem/add-route.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 6. Click Save changes   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 6. Click Save changes ) 
) 
6. Click Save changes
