
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Truy cập S3 từ môi trường truyền thống"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Truy cập S3 từ môi trường truyền thống" ) 
) 
title : "Truy cập S3 từ môi trường truyền thống"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo date :  "`r Sys.Date()`"    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo date :  "`r Sys.Date()`"  ) 
) 
date :  "`r Sys.Date()`" 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo weight : 4    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo weight : 4  ) 
) 
weight : 4 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo chapter : false   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo chapter : false ) 
) 
chapter : false

E:\thuctap\report mau\fcj-workshop-template-main>(
echo pre : " <b> 5.4. </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.4. </b> " ) 
) 
pre : " <b> 5.4. </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Tổng quan   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Tổng quan ) 
) 
#### Tổng quan

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Trong phần này, bạn sẽ tạo một Interface Endpoint để truy cập Amazon S3 từ môi trường truyền thống mô phỏng. Interface Endpoint sẽ cho phép bạn định tuyến đến Amazon S3 qua kết nối VPN từ môi trường truyền thống mô phỏng của bạn.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Trong phần này, bạn sẽ tạo một Interface Endpoint để truy cập Amazon S3 từ môi trường truyền thống mô phỏng. Interface Endpoint sẽ cho phép bạn định tuyến đến Amazon S3 qua kết nối VPN từ môi trường truyền thống mô phỏng của bạn. ) 
) 
+ Trong phần này, bạn sẽ tạo một Interface Endpoint để truy cập Amazon S3 từ môi trường truyền thống mô phỏng. Interface Endpoint sẽ cho phép bạn định tuyến đến Amazon S3 qua kết nối VPN từ môi trường truyền thống mô phỏng của bạn.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Tại sao nên sử dụng **Interface Endpoint**:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Tại sao nên sử dụng **Interface Endpoint**: ) 
) 
+ Tại sao nên sử dụng **Interface Endpoint**:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo     + Các Gateway endpoints chỉ hoạt động với các tài nguyên đang chạy trong VPC nơi chúng được tạo. Interface Endpoint  hoạt động với tài nguyên chạy trong VPC và cả tài nguyên chạy trong môi trường truyền thống. Khả năng kết nối từ môi trường truyền thống của bạn với aws cloud có thể được cung cấp bởi AWS Site-to-Site VPN hoặc AWS Direct Connect.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo     + Các Gateway endpoints chỉ hoạt động với các tài nguyên đang chạy trong VPC nơi chúng được tạo. Interface Endpoint  hoạt động với tài nguyên chạy trong VPC và cả tài nguyên chạy trong môi trường truyền thống. Khả năng kết nối từ môi trường truyền thống của bạn với aws cloud có thể được cung cấp bởi AWS Site-to-Site VPN hoặc AWS Direct Connect. ) 
) 
    + Các Gateway endpoints chỉ hoạt động với các tài nguyên đang chạy trong VPC nơi chúng được tạo. Interface Endpoint  hoạt động với tài nguyên chạy trong VPC và cả tài nguyên chạy trong môi trường truyền thống. Khả năng kết nối từ môi trường truyền thống của bạn với aws cloud có thể được cung cấp bởi AWS Site-to-Site VPN hoặc AWS Direct Connect.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo     + Interface Endpoint cho phép bạn kết nối với các dịch vụ do AWS PrivateLink cung cấp. Các dịch vụ này bao gồm một số dịch vụ AWS, dịch vụ do các đối tác và khách hàng AWS lưu trữ trong VPC của riêng họ (gọi tắt là Dịch vụ PrivateLink endpoints) và các dịch vụ Đối tác AWS Marketplace. Đối với workshop này, chúng ta sẽ tập trung vào việc kết nối với Amazon S3.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo     + Interface Endpoint cho phép bạn kết nối với các dịch vụ do AWS PrivateLink cung cấp. Các dịch vụ này bao gồm một số dịch vụ AWS, dịch vụ do các đối tác và khách hàng AWS lưu trữ trong VPC của riêng họ (gọi tắt là Dịch vụ PrivateLink endpoints) và các dịch vụ Đối tác AWS Marketplace. Đối với workshop này, chúng ta sẽ tập trung vào việc kết nối với Amazon S3. ) 
) 
    + Interface Endpoint cho phép bạn kết nối với các dịch vụ do AWS PrivateLink cung cấp. Các dịch vụ này bao gồm một số dịch vụ AWS, dịch vụ do các đối tác và khách hàng AWS lưu trữ trong VPC của riêng họ (gọi tắt là Dịch vụ PrivateLink endpoints) và các dịch vụ Đối tác AWS Marketplace. Đối với workshop này, chúng ta sẽ tập trung vào việc kết nối với Amazon S3.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo        | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo      ) 
) 
ECHO is on.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Interface endpoint architecture](/images/5-Workshop/5.4-S3-onprem/diagram3.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Interface endpoint architecture](/images/5-Workshop/5.4-S3-onprem/diagram3.png) ) 
) 
![Interface endpoint architecture](/images/5-Workshop/5.4-S3-onprem/diagram3.png)
