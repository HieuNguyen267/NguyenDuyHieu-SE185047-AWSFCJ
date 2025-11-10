
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Giới thiệu"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Giới thiệu" ) 
) 
title : "Giới thiệu"

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
echo pre : " <b> 5.1. </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.1. </b> " ) 
) 
pre : " <b> 5.1. </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Giới thiệu về VPC Endpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Giới thiệu về VPC Endpoint ) 
) 
#### Giới thiệu về VPC Endpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Điểm cuối VPC (endpoint) là thiết bị ảo. Chúng là các thành phần VPC có thể mở rộng theo chiều ngang, dự phòng và có tính sẵn sàng cao. Chúng cho phép giao tiếp giữa tài nguyên điện toán của bạn và dịch vụ AWS mà không gây ra rủi ro về tính sẵn sàng.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Điểm cuối VPC (endpoint) là thiết bị ảo. Chúng là các thành phần VPC có thể mở rộng theo chiều ngang, dự phòng và có tính sẵn sàng cao. Chúng cho phép giao tiếp giữa tài nguyên điện toán của bạn và dịch vụ AWS mà không gây ra rủi ro về tính sẵn sàng. ) 
) 
+ Điểm cuối VPC (endpoint) là thiết bị ảo. Chúng là các thành phần VPC có thể mở rộng theo chiều ngang, dự phòng và có tính sẵn sàng cao. Chúng cho phép giao tiếp giữa tài nguyên điện toán của bạn và dịch vụ AWS mà không gây ra rủi ro về tính sẵn sàng.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Tài nguyên điện toán đang chạy trong VPC có thể truy cập Amazon S3 bằng cách sử dụng điểm cuối Gateway. Interface Endpoint  PrivateLink có thể được sử dụng bởi tài nguyên chạy trong VPC hoặc tại TTDL.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Tài nguyên điện toán đang chạy trong VPC có thể truy cập Amazon S3 bằng cách sử dụng điểm cuối Gateway. Interface Endpoint  PrivateLink có thể được sử dụng bởi tài nguyên chạy trong VPC hoặc tại TTDL. ) 
) 
+ Tài nguyên điện toán đang chạy trong VPC có thể truy cập Amazon S3 bằng cách sử dụng điểm cuối Gateway. Interface Endpoint  PrivateLink có thể được sử dụng bởi tài nguyên chạy trong VPC hoặc tại TTDL.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Tổng quan về workshop   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Tổng quan về workshop ) 
) 
#### Tổng quan về workshop

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Trong workshop này, bạn sẽ sử dụng hai VPC.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Trong workshop này, bạn sẽ sử dụng hai VPC. ) 
) 
Trong workshop này, bạn sẽ sử dụng hai VPC.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + **"VPC Cloud"** dành cho các tài nguyên cloud như Gateway endpoint và EC2 instance để kiểm tra.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + **"VPC Cloud"** dành cho các tài nguyên cloud như Gateway endpoint và EC2 instance để kiểm tra. ) 
) 
+ **"VPC Cloud"** dành cho các tài nguyên cloud như Gateway endpoint và EC2 instance để kiểm tra.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + **"VPC On-Prem"** mô phỏng môi trường truyền thống như nhà máy hoặc trung tâm dữ liệu của công ty. Một EC2 Instance chạy phần mềm StrongSwan VPN đã được triển khai trong "VPC On-prem" và được cấu hình tự động để thiết lập đường hầm VPN Site-to-Site với AWS Transit Gateway. VPN này mô phỏng kết nối từ một vị trí tại TTDL (on-prem) với AWS cloud. Để giảm thiểu chi phí, chỉ một phiên bản VPN được cung cấp để hỗ trợ workshop này. Khi lập kế hoạch kết nối VPN cho production workloads của bạn, AWS khuyên bạn nên sử dụng nhiều thiết bị VPN để có tính sẵn sàng cao.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + **"VPC On-Prem"** mô phỏng môi trường truyền thống như nhà máy hoặc trung tâm dữ liệu của công ty. Một EC2 Instance chạy phần mềm StrongSwan VPN đã được triển khai trong "VPC On-prem" và được cấu hình tự động để thiết lập đường hầm VPN Site-to-Site với AWS Transit Gateway. VPN này mô phỏng kết nối từ một vị trí tại TTDL (on-prem) với AWS cloud. Để giảm thiểu chi phí, chỉ một phiên bản VPN được cung cấp để hỗ trợ workshop này. Khi lập kế hoạch kết nối VPN cho production workloads của bạn, AWS khuyên bạn nên sử dụng nhiều thiết bị VPN để có tính sẵn sàng cao. ) 
) 
+ **"VPC On-Prem"** mô phỏng môi trường truyền thống như nhà máy hoặc trung tâm dữ liệu của công ty. Một EC2 Instance chạy phần mềm StrongSwan VPN đã được triển khai trong "VPC On-prem" và được cấu hình tự động để thiết lập đường hầm VPN Site-to-Site với AWS Transit Gateway. VPN này mô phỏng kết nối từ một vị trí tại TTDL (on-prem) với AWS cloud. Để giảm thiểu chi phí, chỉ một phiên bản VPN được cung cấp để hỗ trợ workshop này. Khi lập kế hoạch kết nối VPN cho production workloads của bạn, AWS khuyên bạn nên sử dụng nhiều thiết bị VPN để có tính sẵn sàng cao.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![overview](/images/5-Workshop/5.1-Workshop-overview/diagram1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![overview](/images/5-Workshop/5.1-Workshop-overview/diagram1.png) ) 
) 
![overview](/images/5-Workshop/5.1-Workshop-overview/diagram1.png)
