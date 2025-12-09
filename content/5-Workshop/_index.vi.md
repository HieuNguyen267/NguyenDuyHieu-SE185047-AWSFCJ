---
title: "Workshop"
weight: 2
chapter: false
pre: "<b>5. </b>"
---

# Workshop AWS Jewelry Web

![Architecture](/images/5-Workshop/architecture.png)
<p align="center"><em>Sơ đồ kiến trúc AWS Jewelry Web (CloudFront + S3, Lightsail API/DB, Cognito, Secrets, CloudWatch).</em></p>

#### Tổng quan

Workshop này ghi lại dự án AWS Jewelry Web: một stack thương mại điện tử trang sức bảo mật, tối ưu chi phí, dùng dịch vụ AWS managed.

- **Frontend**: React SPA trên **S3 + CloudFront** với TLS ACM và domain Route 53.
- **Backend**: **Lightsail** chạy API .NET; **Lightsail MySQL/Postgres** cho dữ liệu.
- **Identity**: **Amazon Cognito** User Pool cho signup/login và verify JWT ở API.
- **Media**: Bucket **S3** private cho ảnh; upload qua **presigned PUT**; CloudFront đọc object.
- **Secrets & Observability**: **AWS Secrets Manager** cho mật khẩu DB + cấu hình bucket; **CloudWatch Logs** cho sự kiện API/nghiệp vụ.

Mục tiêu thiết kế:

- Tải trang <2s toàn cầu nhờ CloudFront.
- API ổn định với tải dự kiến (<100k req/tháng).
- DB an toàn, không hardcode secrets (chỉ dùng Secrets Manager).
- Upload an toàn; log API đầy đủ cho vận hành và analytics cơ bản.

#### Bản đồ nội dung

1. **[5.1. Mục tiêu & Phạm vi](5.1-objectives--scope/)**  
2. **[5.2. Walkthrough Kiến trúc](5.2-architecture-walkthrough/)**  
3. **[5.3. Triển khai Clickstream Ingestion](5.3-implementing-clickstream-ingestion/)**  
4. **[5.4. Xây dựng lớp phân tích riêng tư](5.4-building-private-analytics-layer/)**  
5. **[5.5. Trực quan hóa với Shiny Dashboards](5.5-visualizing-analytics-with-shiny-dashboards/)**  
6. **[5.6. Tổng kết & Dọn dẹp](5.6-summary-cleanup/)**

