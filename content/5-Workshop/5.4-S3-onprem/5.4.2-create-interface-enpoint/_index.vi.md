
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Tạo một S3 Interface endpoint"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Tạo một S3 Interface endpoint" ) 
) 
title : "Tạo một S3 Interface endpoint"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo date : "`r Sys.Date()`"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo date : "`r Sys.Date()`" ) 
) 
date : "`r Sys.Date()`"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo weight : 2   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo weight : 2 ) 
) 
weight : 2

E:\thuctap\report mau\fcj-workshop-template-main>(
echo chapter : false   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo chapter : false ) 
) 
chapter : false

E:\thuctap\report mau\fcj-workshop-template-main>(
echo pre : " <b> 5.4.2 </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.4.2 </b> " ) 
) 
pre : " <b> 5.4.2 </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Trong phần này, bạn sẽ tạo và kiểm tra Interface Endpoint  S3 bằng cách sử dụng môi trường truyền thống mô phỏng.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Trong phần này, bạn sẽ tạo và kiểm tra Interface Endpoint  S3 bằng cách sử dụng môi trường truyền thống mô phỏng. ) 
) 
Trong phần này, bạn sẽ tạo và kiểm tra Interface Endpoint  S3 bằng cách sử dụng môi trường truyền thống mô phỏng.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Quay lại Amazon VPC menu. Trong thanh điều hướng bên trái, chọn Endpoints, sau đó click Create Endpoint.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Quay lại Amazon VPC menu. Trong thanh điều hướng bên trái, chọn Endpoints, sau đó click Create Endpoint. ) 
) 
1. Quay lại Amazon VPC menu. Trong thanh điều hướng bên trái, chọn Endpoints, sau đó click Create Endpoint.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Trong Create endpoint console:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Trong Create endpoint console: ) 
) 
2. Trong Create endpoint console:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Đặt tên interface endpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Đặt tên interface endpoint ) 
) 
+ Đặt tên interface endpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Trong Service category, chọn **aws services**    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Trong Service category, chọn **aws services**  ) 
) 
+ Trong Service category, chọn **aws services** 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![name](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![name](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint1.png) ) 
) 
![name](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3.  Trong Search box, gõ S3 và nhấn Enter. Chọn endpoint có tên com.amazonaws.us-east-1.s3. Đảm bảo rằng cột Type có giá trị Interface.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3.  Trong Search box, gõ S3 và nhấn Enter. Chọn endpoint có tên com.amazonaws.us-east-1.s3. Đảm bảo rằng cột Type có giá trị Interface. ) 
) 
3.  Trong Search box, gõ S3 và nhấn Enter. Chọn endpoint có tên com.amazonaws.us-east-1.s3. Đảm bảo rằng cột Type có giá trị Interface.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![service](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint2.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![service](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint2.png) ) 
) 
![service](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint2.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 4. Đối với VPC, chọn VPC Cloud từ drop-down.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 4. Đối với VPC, chọn VPC Cloud từ drop-down. ) 
) 
4. Đối với VPC, chọn VPC Cloud từ drop-down.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo {{% notice warning %}}   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo {{% notice warning %}} ) 
) 
{{% notice warning %}}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Đảm bảo rằng bạn chọn "VPC Cloud" và không phải "VPC On-prem"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Đảm bảo rằng bạn chọn "VPC Cloud" và không phải "VPC On-prem" ) 
) 
Đảm bảo rằng bạn chọn "VPC Cloud" và không phải "VPC On-prem"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo {{% /notice %}}   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo {{% /notice %}} ) 
) 
{{% /notice %}}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Mở rộng **Additional settings** và đảm bảo rằng Enable DNS name *không* được chọn (sẽ sử dụng điều này trong phần tiếp theo của workshop)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Mở rộng **Additional settings** và đảm bảo rằng Enable DNS name *không* được chọn (sẽ sử dụng điều này trong phần tiếp theo của workshop) ) 
) 
+ Mở rộng **Additional settings** và đảm bảo rằng Enable DNS name *không* được chọn (sẽ sử dụng điều này trong phần tiếp theo của workshop)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![vpc](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint3.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![vpc](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint3.png) ) 
) 
![vpc](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint3.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 5. Chọn 2 subnets trong AZs sau: us-east-1a and us-east-1b   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 5. Chọn 2 subnets trong AZs sau: us-east-1a and us-east-1b ) 
) 
5. Chọn 2 subnets trong AZs sau: us-east-1a and us-east-1b

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![subnets](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint4.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![subnets](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint4.png) ) 
) 
![subnets](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint4.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 6. Đối với Security group, chọn SGforS3Endpoint:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 6. Đối với Security group, chọn SGforS3Endpoint: ) 
) 
6. Đối với Security group, chọn SGforS3Endpoint:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![sg](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint5.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![sg](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint5.png) ) 
) 
![sg](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint5.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 7. Giữ default policy - full access và click Create endpoint   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 7. Giữ default policy - full access và click Create endpoint ) 
) 
7. Giữ default policy - full access và click Create endpoint

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![success](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint-success.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![success](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint-success.png) ) 
) 
![success](/images/5-Workshop/5.4-S3-onprem/s3-interface-endpoint-success.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Chúc mừng bạn đã tạo thành công S3 interface endpoint. Ở bước tiếp theo, chúng ta sẽ kiểm tra interface endpoint.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Chúc mừng bạn đã tạo thành công S3 interface endpoint. Ở bước tiếp theo, chúng ta sẽ kiểm tra interface endpoint. ) 
) 
Chúc mừng bạn đã tạo thành công S3 interface endpoint. Ở bước tiếp theo, chúng ta sẽ kiểm tra interface endpoint.
