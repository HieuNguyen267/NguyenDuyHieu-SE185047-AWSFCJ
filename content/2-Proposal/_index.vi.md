---
title: "Proposal"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# Team T1 VN

# Kế hoạch dự án: AWS Jewelry Web Store

## 1. Bối cảnh và động lực

### 1.1 Tóm tắt điều hành
Dự án xây dựng nền tảng thương mại điện tử trang sức. Kiến trúc gồm backend + cơ sở dữ liệu chạy trên **AWS Lightsail**, frontend **React** lưu trữ trên **Amazon S3** và phân phối qua **CloudFront** (HTTPS bằng ACM). Mục tiêu: mở rộng đơn giản, bảo mật cao, tối ưu chi phí với các dịch vụ AWS cốt lõi.

**Các chức năng chính**
- Quản lý sản phẩm trang sức.
- Tải ảnh sản phẩm.
- Giỏ hàng.
- Đăng ký/đăng nhập bằng **Amazon Cognito**.
- API backend trên Lightsail, lưu trữ **MySQL/Postgres**.
- CDN CloudFront + SSL quốc tế.

### 1.2 Tiêu chí thành công
- Hiệu năng: tải trang < 2s nhờ CloudFront.
- Ổn định: API trên Lightsail chịu tải thực tế.
- Toàn vẹn dữ liệu: truy vấn nhanh, an toàn.
- Quản lý người dùng: Cognito ổn định, bảo mật.
- Bảo mật: upload ảnh an toàn lên S3.
- Giám sát: log API đầy đủ qua CloudWatch.

### 1.3 Giả định
- Lưu lượng < 100.000 request/tháng.
- Không yêu cầu autoscaling nâng cao.
- Domain đã có sẵn hoặc mua qua Route 53.
- Đội phát triển thông thạo .NET/React (chuyển từ Node.js sang .NET).

## 2. Kiến trúc giải pháp

### 2.1 Sơ đồ kiến trúc
![alt text](../../static/images/2-Proposal/JewelryDiagram.png)

### 2.2 Kế hoạch kỹ thuật
- Thiết lập S3 hosting + CloudFront, cấu hình HTTPS/ACM, ánh xạ domain Route 53.
- Triển khai API Lightsail, kết nối DB, tích hợp Cognito, đọc secrets từ Secrets Manager.
- Upload ảnh: API cấp presigned URL; S3 private, CloudFront chỉ đọc.
- Log/metrics: CloudWatch.

### 2.3 Kế hoạch dự án
Thời gian ước tính 6–12 tuần tùy phạm vi cuối.

### 2.4 Bảo mật
- Truy cập S3 private, chỉ CloudFront đọc.
- API dùng khóa bí mật lưu trong Secrets Manager.
- HTTPS toàn hệ thống.
- Đăng nhập bảo vệ bằng Cognito.

## 3. Hoạt động và deliverable

| Giai đoạn | Tuần | Hoạt động chính | Deliverable | MD |
|-----------|------|-----------------|-------------|----|
| Assessment | 1 | Thu thập yêu cầu, vẽ kiến trúc, thiết kế DB, liệt kê secrets | Sơ đồ kiến trúc, Schema DB, Danh sách secrets | 5 |
| Hạ tầng cơ bản | 2 | S3 + CloudFront + ACM + Route 53; Lightsail API & DB; Cognito; tạo secrets; bật CloudWatch | Frontend CDN hoạt động, API & DB sẵn sàng, đăng nhập Cognito, secrets được cấu hình | 7 |
| Thành phần 1 – Backend | 3 | API đọc secrets, presigned upload, CRUD sản phẩm, xác thực Cognito, log CloudWatch | API ổn định, upload thành công, login thành công, không hardcode cấu hình | 7 |
| Thành phần 2 – Frontend | 4 | UI shop React, UI login Cognito, UI upload ảnh, gọi API, build & deploy S3+CF | UI hoàn chỉnh, tích hợp API | 7 |
| Kiểm thử & Go-live | 5 | Test tích hợp FE↔BE↔S3↔DB, test bảo mật (IAM + Secrets Manager), E2E | Báo cáo test, checklist bảo mật | 5 |
| Bàn giao | 6 | Hướng dẫn cập nhật secrets, chuyển giao tài khoản, runbook | Runbook đầy đủ, đóng dự án | 5 |

### 3.2 Ngoài phạm vi
- AI/ML, e-commerce phức tạp, xử lý ảnh nâng cao.
- Triển khai đa vùng/DR, admin phức tạp, tích hợp bên thứ ba.
- Autoscaling nâng cao, CI/CD phức tạp.

### 3.3 Lộ trình lên production
- Tối ưu vận hành.
- Harden secrets production.
- Bổ sung xử lý lỗi.
- Triển khai & kiểm chứng production.
- Kế hoạch DR.
- Bàn giao vận hành.

## 4. Chi phí AWS ước tính (tham khảo)

| Dịch vụ | Upfront | Tháng | Region |
|---------|---------|-------|--------|
| S3 | 0.00 USD | 0.26 USD | AP-Singapore |
| CloudFront | 0.00 USD | 0.17 USD | AP-Singapore |
| ACM | 0.00 USD | 0 USD | AP-Singapore |
| Route 53 | 0.00 USD | 0.50–1.00 USD | AP-Singapore |
| Lightsail – DB | 0.00 USD | 10–15 USD | AP-Singapore |
| Cognito | 0.00 USD | 2.00 USD | AP-Singapore |
| Secrets Manager | 0.00 USD | 0.40 USD | AP-Singapore |
| CloudWatch | 0.00 USD | 0.30 USD | AP-Singapore |
| Lightsail – API | 0.00 USD | 5–10 USD | AP-Singapore |

## 5. Đội dự án


| Name | Title | Role | Email / Contact Info |
| :---- | :---- | :---- | :---- |
| Nguyễn Duy Hiếu  | Product Owner | Project Manager (BE) | Hieundse185047@fpt.edu.vn |
| Lưu Ngọc Ngân Giang | Software Developer | Developer (BE) | luungocngangiang25@gmail.com |
| Nguyễn Huy Hoàng  | Software Developer | Developer (FE) | Hoangnhse185092@fpt.edu.vn |
| Trần Hồ Phương Khanh | Software Developer | Developer (FE) | khanhthpse185070@fpt.edu.vn |
| Tăng Khanh Nhi | Software Developer | Developer (FE) | tangkhanhnhi111@gmail.com |
## 6. Nhân lực & ước tính chi phí

| Tài nguyên | Trách nhiệm | Tỷ lệ (USD) / Giờ |
| :---- | :---- | ----- |
| Solution Architects \[số lượng được phân công\] | - Thiết kế và kiến trúc hệ sinh thái hạ tầng AWS, tích hợp các dịch vụ như S3, CloudFront, Lightsail, ACM, Route 53, và Secrets Manager. - Tư vấn chiến lược về giao thức bảo mật và tối ưu chi phí vận hành. - Thực hiện đánh giá toàn diện các quy trình triển khai để đảm bảo tuân thủ các thực hành tốt nhất trong ngành. | 12 |
| Engineers \[số lượng được phân công\] | - Thực hiện cung cấp và triển khai các thành phần hạ tầng cốt lõi, bao gồm S3, CloudFront, Route 53, ACM, và Lightsail. - Thiết lập pipeline CI/CD và hỗ trợ triển khai frontend lên Amazon S3. - Triển khai và cấu hình môi trường runtime API .NET trong hạ tầng AWS Lightsail. - Cấu hình quản lý thông tin xác thực an toàn qua AWS Secrets Manager và thiết lập cơ chế logging bằng Amazon CloudWatch. | 6 |
| Khác (Vui lòng chỉ rõ) | - Thực hiện kiểm chứng hệ thống nghiêm ngặt sau triển khai và kiểm thử tích hợp. - Cung cấp tư vấn kỹ thuật liên tục và dịch vụ hỗ trợ khách hàng chuyên dụng. | 0 |

\* Lưu ý: Tham khảo phần "hoạt động & deliverable" để xem danh sách các giai đoạn dự án

| Giai đoạn dự án | Solution Architects | Engineers | Khác (Vui lòng chỉ rõ) | Tổng giờ |
| :---: | :---: | :---: | :---: | :---: |
| S3 + CloudFront | 1 | 2 |  | 3 |
| Lightsail API + DB | 1 | 4 |  | 4 |
| Cognito | 1 | 2 |  | 5 |
| Logging & Monitoring | 1 | 1 |  | 3 |
| Tổng giờ | 4 | 12 |  | 15 |
| Tổng chi phí |  |  |  |  |

Bạn có thể tìm ước tính ngân sách trên [AWS Pricing Calculator](https://calculator.aws/#/estimate?id=621f38b12a1ef026842ba2ddfe46ff936ed4ab01).

| Tên dịch vụ | Chi phí Upfront | Chi phí hàng tháng | Mô tả | Region | Tóm tắt cấu hình |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AWS Secrets Manager | 0.00 USD | 0.13 USD | Quản lý mật khẩu DB | Asia Pacific (Singapore) | Số lượng secrets (1), Thời gian trung bình mỗi secret (10 ngày), Số lượng API calls (1/tháng) |
| AWS Certificate Manager | 15.00 USD | 0.00 USD | Chứng chỉ SSL | Asia Pacific (Singapore) | Số lượng FQDN (1) |
| Amazon S3 | 0.00 USD | 0.03 USD | Host React + Lưu trữ ảnh | Asia Pacific (Singapore) | S3 Standard storage (1 GB/tháng), Data Transfer In/Out (0 TB/tháng) |
| Amazon Route 53 | 0.00 USD | 3.50 USD | Quản lý Domain | Asia Pacific (Singapore) | Hosted Zones (1) |
| Amazon Lightsail | 0.00 USD | 3.20 USD | API + Database Server | Asia Pacific (Singapore) | 1 Bundle, Storage (100GB), Data Transfer (250GB), Additional storage (8 GB) |
| Amazon Cognito | 0.00 USD | 0.05 USD | User Login/Auth | Asia Pacific (Singapore) | MAU (1), Advanced security features (Enabled) |
| Amazon CloudWatch | 0.00 USD | 0.30 USD | API Logging | Asia Pacific (Singapore) | Metrics requested (1), Widget Image (1), Other API requests (1), Custom Metrics (1) |
| Amazon CloudFront | 0.00 USD | 0.00 USD | Frontend CDN | Asia Pacific (Singapore) | Free Plan (1) |
| TỔNG | 15.00 USD | \~7.21 USD |  |  |  |

Phân bổ đóng góp chi phí giữa Partner, Customer, AWS:

| Bên | Đóng góp (USD) | % Đóng góp của Tổng |
| :---- | :---- | :---- |
| Customer |  |  |
| Partner |  |  |
| AWS |  |  | 

## 7. Điều kiện nghiệm thu
- Website chạy ổn định trên domain thật.
- API kết nối DB hoàn chỉnh.
- Upload ảnh hoạt động.
- CloudWatch log & Cognito login chạy tốt.
- Được khách hàng/chủ dự án chấp nhận.

## File TEMPLETE DOCX: [DOWLOAD Proposal (DOCX)](https://drive.google.com/drive/folders/1TLXOU4XDvSqv1hfWYhXhWilc5G53iN2H?usp=sharing)