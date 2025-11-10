
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Kiểm tra Gateway Endpoint"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Kiểm tra Gateway Endpoint" ) 
) 
title : "Kiểm tra Gateway Endpoint"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo date :  "`r Sys.Date()`"    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo date :  "`r Sys.Date()`"  ) 
) 
date :  "`r Sys.Date()`" 

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
echo pre : " <b> 5.3.2 </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.3.2 </b> " ) 
) 
pre : " <b> 5.3.2 </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Tạo S3 bucket   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Tạo S3 bucket ) 
) 
#### Tạo S3 bucket

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Đi đến S3 management console   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Đi đến S3 management console ) 
) 
1. Đi đến S3 management console

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Trong Bucket console, chọn **Create bucket**   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Trong Bucket console, chọn **Create bucket** ) 
) 
2. Trong Bucket console, chọn **Create bucket**

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Create bucket](/images/5-Workshop/5.3-S3-vpc/create-bucket.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Create bucket](/images/5-Workshop/5.3-S3-vpc/create-bucket.png) ) 
) 
![Create bucket](/images/5-Workshop/5.3-S3-vpc/create-bucket.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Trong Create bucket console   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Trong Create bucket console ) 
) 
3. Trong Create bucket console

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Đặt tên bucket: chọn 1 tên mà không bị trùng trong phạm vi toàn cầu (gợi ý: lab\<số-lab\>\<tên-bạn\>)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Đặt tên bucket: chọn 1 tên mà không bị trùng trong phạm vi toàn cầu (gợi ý: lab\<số-lab\>\<tên-bạn\>) ) 
) 
+ Đặt tên bucket: chọn 1 tên mà không bị trùng trong phạm vi toàn cầu (gợi ý: lab\<số-lab\>\<tên-bạn\>)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Bucket name](/images/5-Workshop/5.3-S3-vpc/bucket-name.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Bucket name](/images/5-Workshop/5.3-S3-vpc/bucket-name.png) ) 
) 
![Bucket name](/images/5-Workshop/5.3-S3-vpc/bucket-name.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Giữ nguyên giá trị của các fields khác (default)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Giữ nguyên giá trị của các fields khác (default) ) 
) 
+ Giữ nguyên giá trị của các fields khác (default)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Kéo chuột xuống và chọn **Create bucket**   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Kéo chuột xuống và chọn **Create bucket** ) 
) 
+ Kéo chuột xuống và chọn **Create bucket**

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Create](/images/5-Workshop/5.3-S3-vpc/create-button.png)       | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Create](/images/5-Workshop/5.3-S3-vpc/create-button.png)     ) 
) 
![Create](/images/5-Workshop/5.3-S3-vpc/create-button.png)    

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Tạo thành công S3 bucket   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Tạo thành công S3 bucket ) 
) 
+ Tạo thành công S3 bucket

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Success](/images/5-Workshop/5.3-S3-vpc/bucket-success.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Success](/images/5-Workshop/5.3-S3-vpc/bucket-success.png) ) 
) 
![Success](/images/5-Workshop/5.3-S3-vpc/bucket-success.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Kết nối với EC2 bằng session manager   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Kết nối với EC2 bằng session manager ) 
) 
#### Kết nối với EC2 bằng session manager

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Trong workshop này, bạn sẽ dùng AWS Session Manager để kết nối đến các EC2 instances. Session Manager là 1 tính năng trong dịch vụ Systems Manager được quản lý hoàn toàn bởi AWS. System manager cho phép bạn quản lý Amazon EC2 instances và các máy ảo on-premises (VMs)thông qua 1 browser-based shell. Session Manager cung cấp khả năng quản lý phiên bản an toàn và có thể kiểm tra mà không cần mở cổng vào, duy trì máy chủ bastion host hoặc quản lý khóa SSH.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Trong workshop này, bạn sẽ dùng AWS Session Manager để kết nối đến các EC2 instances. Session Manager là 1 tính năng trong dịch vụ Systems Manager được quản lý hoàn toàn bởi AWS. System manager cho phép bạn quản lý Amazon EC2 instances và các máy ảo on-premises (VMs)thông qua 1 browser-based shell. Session Manager cung cấp khả năng quản lý phiên bản an toàn và có thể kiểm tra mà không cần mở cổng vào, duy trì máy chủ bastion host hoặc quản lý khóa SSH. ) 
) 
+ Trong workshop này, bạn sẽ dùng AWS Session Manager để kết nối đến các EC2 instances. Session Manager là 1 tính năng trong dịch vụ Systems Manager được quản lý hoàn toàn bởi AWS. System manager cho phép bạn quản lý Amazon EC2 instances và các máy ảo on-premises (VMs)thông qua 1 browser-based shell. Session Manager cung cấp khả năng quản lý phiên bản an toàn và có thể kiểm tra mà không cần mở cổng vào, duy trì máy chủ bastion host hoặc quản lý khóa SSH.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + First cloud journey [Lab](https://000058.awsstudygroup.com/1-introduce/) để hiểu sâu hơn về Session manager.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + First cloud journey [Lab](https://000058.awsstudygroup.com/1-introduce/) để hiểu sâu hơn về Session manager. ) 
) 
+ First cloud journey [Lab](https://000058.awsstudygroup.com/1-introduce/) để hiểu sâu hơn về Session manager.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Trong AWS Management Console, gõ Systems Manager trong ô tìm kiếm và nhấn Enter:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Trong AWS Management Console, gõ Systems Manager trong ô tìm kiếm và nhấn Enter: ) 
) 
1. Trong AWS Management Console, gõ Systems Manager trong ô tìm kiếm và nhấn Enter:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![system manager](/images/5-Workshop/5.3-S3-vpc/sm.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![system manager](/images/5-Workshop/5.3-S3-vpc/sm.png) ) 
) 
![system manager](/images/5-Workshop/5.3-S3-vpc/sm.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Từ **Systems Manager** menu, tìm **Node Management** ở thanh bên trái và chọn **Session Manager**:   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Từ **Systems Manager** menu, tìm **Node Management** ở thanh bên trái và chọn **Session Manager**: ) 
) 
2. Từ **Systems Manager** menu, tìm **Node Management** ở thanh bên trái và chọn **Session Manager**:

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![system manager](/images/5-Workshop/5.3-S3-vpc/sm1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![system manager](/images/5-Workshop/5.3-S3-vpc/sm1.png) ) 
) 
![system manager](/images/5-Workshop/5.3-S3-vpc/sm1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Click Start Session, và chọn EC2 instance tên **Test-Gateway-Endpoint**.    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Click Start Session, và chọn EC2 instance tên **Test-Gateway-Endpoint**.  ) 
) 
3. Click Start Session, và chọn EC2 instance tên **Test-Gateway-Endpoint**. 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo {{% notice info %}}   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo {{% notice info %}} ) 
) 
{{% notice info %}}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Phiên bản EC2 này đã chạy trong "VPC cloud" và sẽ được dùng để kiểm tra khả năng kết nối với Amazon S3 thông qua điểm cuối Cổng mà bạn vừa tạo (s3-gwe). {{% /notice %}}   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Phiên bản EC2 này đã chạy trong "VPC cloud" và sẽ được dùng để kiểm tra khả năng kết nối với Amazon S3 thông qua điểm cuối Cổng mà bạn vừa tạo (s3-gwe). {{% /notice %}} ) 
) 
Phiên bản EC2 này đã chạy trong "VPC cloud" và sẽ được dùng để kiểm tra khả năng kết nối với Amazon S3 thông qua điểm cuối Cổng mà bạn vừa tạo (s3-gwe). {{% /notice %}}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Start session](/images/5-Workshop/5.3-S3-vpc/start-session.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Start session](/images/5-Workshop/5.3-S3-vpc/start-session.png) ) 
) 
![Start session](/images/5-Workshop/5.3-S3-vpc/start-session.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Session Manager sẽ mở browser tab mới với shell prompt: sh-4.2 $   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Session Manager sẽ mở browser tab mới với shell prompt: sh-4.2 $ ) 
) 
Session Manager sẽ mở browser tab mới với shell prompt: sh-4.2 $

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Success](/images/5-Workshop/5.3-S3-vpc/start-session-success.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Success](/images/5-Workshop/5.3-S3-vpc/start-session-success.png) ) 
) 
![Success](/images/5-Workshop/5.3-S3-vpc/start-session-success.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Bạn đã bắt đầu phiên kết nối đến EC2 trong VPC Cloud thành công. Trong bước tiếp theo, chúng ta sẽ tạo một  S3 bucket và một tệp trong đó.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Bạn đã bắt đầu phiên kết nối đến EC2 trong VPC Cloud thành công. Trong bước tiếp theo, chúng ta sẽ tạo một  S3 bucket và một tệp trong đó. ) 
) 
Bạn đã bắt đầu phiên kết nối đến EC2 trong VPC Cloud thành công. Trong bước tiếp theo, chúng ta sẽ tạo một  S3 bucket và một tệp trong đó.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Create a file and upload to s3 bucket   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Create a file and upload to s3 bucket ) 
) 
#### Create a file and upload to s3 bucket

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Đổi về ssm-user's thư mục bằng lệnh "cd ~"    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Đổi về ssm-user's thư mục bằng lệnh "cd ~"  ) 
) 
1. Đổi về ssm-user's thư mục bằng lệnh "cd ~" 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Change user's dir](/images/5-Workshop/5.3-S3-vpc/cli1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Change user's dir](/images/5-Workshop/5.3-S3-vpc/cli1.png) ) 
) 
![Change user's dir](/images/5-Workshop/5.3-S3-vpc/cli1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Tạo 1 file để kiểm tra bằng lệnh "fallocate -l 1G testfile.xyz", 1 file tên "testfile.xyz" có kích thước 1GB sẽ được tạo.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Tạo 1 file để kiểm tra bằng lệnh "fallocate -l 1G testfile.xyz", 1 file tên "testfile.xyz" có kích thước 1GB sẽ được tạo. ) 
) 
2. Tạo 1 file để kiểm tra bằng lệnh "fallocate -l 1G testfile.xyz", 1 file tên "testfile.xyz" có kích thước 1GB sẽ được tạo.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Create file](/images/5-Workshop/5.3-S3-vpc/cli-file.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Create file](/images/5-Workshop/5.3-S3-vpc/cli-file.png) ) 
) 
![Create file](/images/5-Workshop/5.3-S3-vpc/cli-file.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Tải file mình vừa tạo lên S3 với lệnh "aws s3 cp testfile.xyz s3://your-bucket-name". Thay your-bucket-name bằng tên S3 bạn đã tạo.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Tải file mình vừa tạo lên S3 với lệnh "aws s3 cp testfile.xyz s3://your-bucket-name". Thay your-bucket-name bằng tên S3 bạn đã tạo. ) 
) 
3. Tải file mình vừa tạo lên S3 với lệnh "aws s3 cp testfile.xyz s3://your-bucket-name". Thay your-bucket-name bằng tên S3 bạn đã tạo.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Uploaded](/images/5-Workshop/5.3-S3-vpc/uploaded.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Uploaded](/images/5-Workshop/5.3-S3-vpc/uploaded.png) ) 
) 
![Uploaded](/images/5-Workshop/5.3-S3-vpc/uploaded.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Bạn đã tải thành công tệp lên bộ chứa S3 của mình. Bây giờ bạn có thể kết thúc session.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Bạn đã tải thành công tệp lên bộ chứa S3 của mình. Bây giờ bạn có thể kết thúc session. ) 
) 
Bạn đã tải thành công tệp lên bộ chứa S3 của mình. Bây giờ bạn có thể kết thúc session.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Kiểm tra object trong S3 bucket   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Kiểm tra object trong S3 bucket ) 
) 
#### Kiểm tra object trong S3 bucket

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 1. Đi đến S3 console.     | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 1. Đi đến S3 console.   ) 
) 
1. Đi đến S3 console.  

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 2. Click tên s3 bucket của bạn   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 2. Click tên s3 bucket của bạn ) 
) 
2. Click tên s3 bucket của bạn

E:\thuctap\report mau\fcj-workshop-template-main>(
echo 3. Trong Bucket console, bạn sẽ thấy tệp bạn đã tải lên S3 bucket của mình   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo 3. Trong Bucket console, bạn sẽ thấy tệp bạn đã tải lên S3 bucket của mình ) 
) 
3. Trong Bucket console, bạn sẽ thấy tệp bạn đã tải lên S3 bucket của mình

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Check S3](/images/5-Workshop/5.3-S3-vpc/check-s3-bucket.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Check S3](/images/5-Workshop/5.3-S3-vpc/check-s3-bucket.png) ) 
) 
![Check S3](/images/5-Workshop/5.3-S3-vpc/check-s3-bucket.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Tóm tắt   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Tóm tắt ) 
) 
#### Tóm tắt

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Chúc mừng bạn đã hoàn thành truy cập S3 từ VPC. Trong phần này, bạn đã tạo gateway endpoint cho Amazon S3 và sử dụng AWS CLI để tải file lên. Quá trình tải lên hoạt động vì gateway endpoint cho phép giao tiếp với S3 mà không cần Internet gateway gắn vào "VPC Cloud". Điều này thể hiện chức năng của gateway endpoint như một đường dẫn an toàn đến S3 mà không cần đi qua pub    lic Internet.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Chúc mừng bạn đã hoàn thành truy cập S3 từ VPC. Trong phần này, bạn đã tạo gateway endpoint cho Amazon S3 và sử dụng AWS CLI để tải file lên. Quá trình tải lên hoạt động vì gateway endpoint cho phép giao tiếp với S3 mà không cần Internet gateway gắn vào "VPC Cloud". Điều này thể hiện chức năng của gateway endpoint như một đường dẫn an toàn đến S3 mà không cần đi qua pub    lic Internet. ) 
) 
Chúc mừng bạn đã hoàn thành truy cập S3 từ VPC. Trong phần này, bạn đã tạo gateway endpoint cho Amazon S3 và sử dụng AWS CLI để tải file lên. Quá trình tải lên hoạt động vì gateway endpoint cho phép giao tiếp với S3 mà không cần Internet gateway gắn vào "VPC Cloud". Điều này thể hiện chức năng của gateway endpoint như một đường dẫn an toàn đến S3 mà không cần đi qua pub    lic Internet.
