---
title: "Bản Đề Xuất Dự Án"
date: 2025-11-10
weight: 1
chapter: false
pre: " <b> 1. </b> "
---
# **Nền Tảng Thương Mại Điện Tử Trang Sức**  
## **Hệ Thống Bán Hàng Trực Tuyến Dựa Trên Đám Mây Sử Dụng React, .NET và MySQL Trên AWS Lightsail**  

---

## **1. Tổng Quan Dự Án**

Nền tảng thương mại điện tử trang sức là một hệ thống bán hàng trực tuyến hiện đại được xây dựng trên hạ tầng điện toán đám mây, hướng đến các doanh nghiệp trang sức vừa và nhỏ. Mục tiêu của dự án là giúp các doanh nghiệp này chuyển đổi từ mô hình kinh doanh truyền thống sang môi trường kỹ thuật số an toàn, linh hoạt và tự động hóa.  

Nền tảng tích hợp giao diện ReactJS, backend .NET Core được lưu trữ trên Amazon Lightsail và cơ sở dữ liệu MySQL để quản lý sản phẩm, người dùng và đơn hàng một cách hiệu quả.  

Các tài sản tĩnh như hình ảnh sản phẩm và nội dung web được lưu trữ trên Amazon S3 và phân phối toàn cầu thông qua Amazon CloudFront, đảm bảo tốc độ và bảo mật tối ưu. Amazon Cognito xử lý xác thực người dùng, trong khi Amazon CloudWatch, AWS CloudTrail và Lightsail Snapshots cung cấp giám sát, kiểm toán và khôi phục thảm họa.  

Dự án này mang lại giải pháp thương mại điện tử tiết kiệm chi phí, dễ vận hành và có khả năng mở rộng cao, phù hợp cho các doanh nghiệp trang sức vừa và nhỏ.  

### **Mục Tiêu Dự Án**
- Phát triển một website thương mại điện tử trang sức thân thiện với người dùng, tương thích trên mọi thiết bị.  
- Tập trung quản lý sản phẩm, kho hàng và đơn hàng.  
- Đảm bảo thời gian hoạt động ≥99.9% thông qua sao lưu và khôi phục tự động.  
- Duy trì chi phí hạ tầng dưới 65 USD/tháng bằng cách sử dụng Lightsail và tài nguyên miễn phí của AWS.  

### **Giá Trị Kinh Doanh**
Các cửa hàng trang sức nhỏ thường gặp khó khăn về chi phí hạ tầng và hạn chế về kỹ thuật. Giải pháp này giúp:  
- Giảm chi phí vận hành với mô hình định giá cố định của Lightsail.  
- Tự động hóa các tác vụ lặp lại, nâng cao hiệu suất.  
- Tăng cường uy tín thương hiệu thông qua hệ thống ổn định và bảo mật dữ liệu mạnh mẽ.  

---

## **2. Phân Tích Vấn Đề**

### **2.1 Hiện Trạng**

Thị trường bán lẻ trang sức đang chuyển mạnh sang kênh trực tuyến, được thúc đẩy bởi nhu cầu cá nhân hóa, minh bạch và trải nghiệm số cao — đặc biệt trong giới trẻ. Tuy nhiên, hầu hết các hệ thống thương mại điện tử hiện nay còn nhiều hạn chế:

- Trải nghiệm người dùng kém: tải trang chậm, thiết kế lỗi thời, thiếu các tính năng tương tác như thử trang sức bằng AR.  
- Thiếu độ tin cậy: khách hàng e ngại khi mua sản phẩm có giá trị cao (vàng, kim cương) vì lo ngại về bảo mật dữ liệu và tính xác thực.  
- Hạ tầng cũ kỹ và không an toàn: nhiều hệ thống cũ lưu trữ mật khẩu hoặc dữ liệu khách hàng ở dạng văn bản thuần, dễ bị tấn công và khó mở rộng.  

---

### **2.2 Thách Thức Chính**

- **Tốc độ và độ tin cậy:**  
  Trang sức cần hình ảnh độ phân giải cao và nội dung tương tác (ví dụ: xem 360°, thử AR). Không có CDN toàn cầu sẽ khiến tải chậm và không ổn định, làm tăng tỷ lệ bỏ giỏ hàng.  

- **Bảo mật và rủi ro gian lận:**  
  Các nền tảng thương mại điện tử là mục tiêu tấn công phổ biến. Không có tường lửa ứng dụng web (WAF), hệ thống dễ bị tấn công SQL injection, XSS hoặc rò rỉ dữ liệu. Việc lưu thông tin xác thực trong mã nguồn là rủi ro nghiêm trọng.  

- **Mất dữ liệu và khôi phục kém:**  
  Giao dịch và tồn kho cần độ chính xác tuyệt đối. Lưu trữ cục bộ có nguy cơ mất dữ liệu vĩnh viễn nếu phần cứng hỏng. Không có lưu trữ bền vững như S3 sẽ khiến hóa đơn và hình ảnh sản phẩm không thể khôi phục.  

- **Thiếu giám sát tập trung:**  
  Không có công cụ như CloudWatch khiến đội ngũ vận hành chỉ phát hiện sự cố khi khách hàng báo, làm tăng thời gian khắc phục (MTTR) và giảm uy tín.  

---

### **2.3 Tác Động Đến Các Bên Liên Quan**

| **Bên Liên Quan** | **Tác Động Chính** |
|--------------------|--------------------|
| Khách hàng | Trải nghiệm mua sắm nhanh, an toàn và minh bạch. |
| Đội ngũ vận hành | Giám sát dễ dàng hơn, sao lưu và khôi phục tự động. |
| Nhà phát triển | Phát triển nhanh hơn với kiến trúc module, API Gateway và Lightsail. |
| Chủ doanh nghiệp | Vận hành liên tục, giảm rủi ro mất dữ liệu, tăng lợi thế cạnh tranh. |

---

### **2.4 Hệ Quả Kinh Doanh**

- **Mất doanh thu:** Hiệu năng kém và UX tệ làm giảm tỷ lệ chuyển đổi.  
- **Rủi ro uy tín và tuân thủ:** Rò rỉ dữ liệu (thiếu WAF hoặc Secrets Manager) có thể gây phạt nặng và tổn hại thương hiệu.  
- **Tăng chi phí vận hành:** Không có giám sát và sao lưu tự động khiến mất nhiều nhân lực và thời gian.  
- **Giới hạn mở rộng:** Hệ thống cũ khó thích nghi với tốc độ tăng trưởng nhanh.  

---

### **3.2 Dịch Vụ AWS Được Sử Dụng**

| **Danh Mục** | **Dịch Vụ AWS** | **Chức Năng Chính** |
|---------------|------------------|----------------------|
| Mạng & Edge | Route 53, CloudFront, WAF, ACM | Định tuyến DNS, phân phối CDN, bảo vệ web, quản lý chứng chỉ SSL |
| Tính toán & API | API Gateway, Lightsail | Quản lý endpoint API và lưu trữ ứng dụng backend |
| Danh tính & Truy cập | Cognito, Secrets Manager | Xác thực / phân quyền và quản lý thông tin nhạy cảm |
| Lưu trữ & CSDL | S3, Lightsail MySQL | Lưu trữ tĩnh và cơ sở dữ liệu quan hệ |
| Dự phòng & Sao lưu | AWS Backup, S3 Versioning, Glacier, Lightsail Snapshots | Sao lưu tự động, lưu trữ dài hạn, kiểm soát phiên bản dữ liệu |
| Giám sát & Kiểm toán | CloudWatch, CloudTrail | Theo dõi hiệu suất theo thời gian thực và ghi nhận hoạt động API |

---

### **3.3 Thiết Kế Thành Phần**

- **Lớp Giao Diện (Frontend):**  
  Website React tĩnh được lưu trữ trên S3 và phân phối qua CloudFront. AWS WAF bảo vệ khỏi các cuộc tấn công phổ biến.

- **Lớp Ứng Dụng (Backend):**  
  API Gateway xác thực token từ Cognito, quản lý các yêu cầu API và giới hạn tốc độ truy cập. Lightsail (Ubuntu) chạy API .NET Core xử lý logic nghiệp vụ (đơn hàng, thanh toán, sản phẩm...).

- **Lớp Dữ Liệu:**  
  MySQL trên Lightsail quản lý dữ liệu giao dịch; thông tin xác thực được lưu an toàn trong Secrets Manager. Amazon S3 lưu trữ hình ảnh, tệp tải lên của người dùng và tài nguyên tĩnh.

---

### **3.4 Kiến Trúc Bảo Mật**

- **Bảo Vệ Ngoại Viên:** WAF lọc yêu cầu độc hại; ACM áp dụng mã hóa HTTPS.  
- **Xác Thực Người Dùng:** Cognito xử lý toàn bộ đăng nhập / đăng ký và cấp token an toàn.  
- **Bảo Mật Hạ Tầng:** Secrets Manager ngăn việc lưu trữ mật khẩu thô.  
- **Kiểm Toán:** CloudTrail ghi lại mọi hành động API phục vụ điều tra và tuân thủ.  

---

### **3.5 Mở Rộng và Quan Sát**

- Mở rộng toàn cầu thông qua bộ nhớ đệm CloudFront.  
- Lưu trữ không giới hạn cho nội dung tĩnh trên S3.  
- CloudWatch cung cấp chỉ số hiệu năng, hỗ trợ điều chỉnh tài nguyên linh hoạt.  

---

## **4. Kế Hoạch Triển Khai Kỹ Thuật**

| **Giai Đoạn** | **Thời Gian** | **Mục Tiêu** | **Sản Phẩm Bàn Giao** | **Tiêu Chí Thành Công** |
|----------------|---------------|---------------|------------------------|--------------------------|
| 1. Thiết lập hạ tầng | Tuần 1–2 | Cấu hình môi trường AWS | S3, CloudFront, Cognito, Route53, SSL | Môi trường ổn định |
| 2. Phát triển Backend | Tuần 3–5 | Xây dựng API .NET và CSDL MySQL | CRUD và cấu trúc DB | Backend hoạt động |
| 3. Kết nối Frontend | Tuần 6–7 | Tích hợp React SPA với API | Giao diện, đăng nhập | UI vận hành |
| 4. Module tải ảnh | Tuần 8–9 | Cho phép tải lên S3 | Test tải ảnh thành công | Pass |
| 5. Giám sát & Sao lưu | Tuần 10–11 | Cấu hình CloudWatch & Snapshot | Cảnh báo & backup | Ổn định hệ thống |
| 6. Kiểm thử & Triển khai | Tuần 12–14 | QA và phát hành chính thức | Demo + tài liệu | Toàn hệ thống ổn định |

---

## **5. Lộ Trình & Cột Mốc Chính**

Dự án kéo dài 14 tuần (tháng 9–12/2025), chia thành 6 sprint Agile–Scrum:

| **Sprint** | **Sản Phẩm** | **Tiêu Chí Thành Công** |
|-------------|---------------|--------------------------|
| Sprint 1 – Nền tảng | Thiết lập Lightsail, S3, CloudFront, Cognito, Route53 | Website HTTPS hoạt động, đăng nhập Cognito thành công |
| Sprint 2 – Backend & DB | API .NET và MySQL | CRUD hoạt động chính xác |
| Sprint 3 – Frontend | Giao diện React kết nối API | Hiển thị sản phẩm & giỏ hàng |
| Sprint 4 – Media | Tích hợp S3 upload | Hiển thị ảnh qua CDN |
| Sprint 5 – Thanh toán | Hoàn thiện quy trình đặt hàng | Thanh toán, xác nhận đơn thành công |
| Sprint 6 – Kiểm thử & Giám sát | Hệ thống hoàn chỉnh | Log & sao lưu hoạt động tốt |

---

## **6. Dự Toán Ngân Sách**

| **Dịch Vụ** | **Mô Tả** | **Chi Phí Ước Tính (USD/tháng)** | **Ghi Chú** |
|--------------|-----------|----------------------------------|--------------|
| Lightsail (.NET API) | 2–4 vCPU, 4–8 GB RAM | $10–$40 | Nên chọn gói ≥$20 |
| Lightsail MySQL | DB quản lý 20–50 GB | $15–$50 | Tách biệt với instance |
| Amazon S3 | Lưu hình ảnh & file tĩnh | $1–$5 | Bao gồm phí request |
| CloudFront | CDN phân phối | $1–$30 | 1TB đầu tiên miễn phí |
| Route53 + ACM | Tên miền & SSL | $1–$4 | ACM miễn phí |
| Cognito | Quản lý người dùng | $0–$10 | 10k người đầu miễn phí |
| CloudWatch + CloudTrail | Giám sát & log | $1–$10 | Tùy log volume |
| Sao lưu | Snapshot & versioning | $1–$10 | Khuyến nghị hàng tuần |

**Tổng ước tính:** 30–160 USD/tháng (~90–480 USD/3 tháng)

### **Mẹo Tối Ưu Chi Phí**
1. Tận dụng AWS Free Tier (Lightsail, S3, CloudFront, Cognito).  
2. Triển khai tại Singapore (ap-southeast-1) để giảm độ trễ.  
3. Dùng Lifecycle chuyển dữ liệu cũ sang Glacier.  
4. Bật cảnh báo chi phí qua AWS Budgets.  
5. Sao lưu định kỳ và bật MFA Delete trên S3.  

---

## **7. Đánh Giá Rủi Ro**

| **ID Rủi Ro** | **Mô Tả** | **Mức Độ** | **Ảnh Hưởng** |
|----------------|------------|--------------|----------------|
| R1 | Lightsail hỏng | Trung bình | Gián đoạn tạm thời |
| R2 | Lỗi hoặc hỏng DB | Cao | Mất dữ liệu giao dịch |
| R3 | Rò rỉ thông tin xác thực | Trung bình | Truy cập trái phép |
| R4 | Lưu lượng tăng đột biến | Trung bình | Giảm tốc độ, treo hệ thống |

### **7.1 Chiến Lược Giảm Thiểu**
- R1: Snapshot hằng ngày và quy trình khôi phục rõ ràng.  
- R2: Backup tự động DB lên S3.  
- R3: Secrets Manager & rotation định kỳ.  
- R4: Tối ưu caching CloudFront, nâng cấp Lightsail khi cần.  

### **7.2 Kế Hoạch Dự Phòng**
- **Khôi phục hệ thống:** Restore từ snapshot trong 4 giờ.  
- **Phục hồi dữ liệu:** Dùng backup MySQL trên S3.  
- **Duy trì hoạt động:** Hiển thị trang bảo trì từ S3 + CloudFront.  
- **Sự cố bảo mật:** Đổi khóa, kiểm tra log CloudTrail.  

### **7.3 Kế Hoạch Giám Sát**
- **Vận hành:** CloudWatch cảnh báo CPU/network.  
- **Bảo mật:** Kiểm tra CloudTrail hàng tuần.  
- **Đánh giá định kỳ:** Rà soát rủi ro mỗi quý.  

---

## **8. Kết Quả Mong Đợi**

### **8.1 Chỉ Số Thành Công (KPI)**

**Kỹ thuật**
- Độ trễ frontend < 200ms (qua CloudFront)  
- Phản hồi API < 350ms (API Gateway + Lightsail)  
- Thời gian hoạt động 99.9%  
- 70%+ request được phục vụ từ CDN cache  
- Không có sự cố bảo mật nghiêm trọng  
- RTO < 30 phút, RPO = 0  

**Kinh doanh**
- Tăng 20–30% tỷ lệ chuyển đổi  
- Giữ chân khách hàng thêm 15–25%  
- Giảm 25–40% chi phí hạ tầng  
- Cải thiện hiệu suất vận hành  

---

### **8.2 Lợi Ích Ngắn Hạn (0–6 tháng)**

- Tốc độ tải nhanh hơn 40–70%  
- Giảm tải backend nhờ CDN  
- Xác thực mạnh mẽ qua Cognito  
- Giám sát và sao lưu tự động  
- Triển khai nhanh hơn nhờ kiến trúc tách rời  

---

### **8.3 Lợi Ích Trung Hạn (6–18 tháng)**

- Giảm chi phí lưu trữ nhờ S3 → Glacier  
- API ổn định khi tải cao  
- Quản lý chi phí dễ dàng qua Cost Explorer  
- Hiệu năng tối ưu qua dashboard CloudWatch  
- Giảm tải công việc bảo trì cho developer  

---

### **8.4 Giá Trị Dài Hạn (18+ tháng)**

- Nền tảng cloud-native sẵn sàng mở rộng sang mobile/app marketplace  
- Sẵn sàng AI/ML cho gợi ý sản phẩm  
- Giảm 80–90% chi phí lưu trữ nhờ Glacier  
- Bảo mật và tuân thủ cấp doanh nghiệp  
- Phủ sóng toàn cầu qua CloudFront Edge Network  
- Hệ thống bền vững, ổn định, dễ mở rộng  

---

### **8.5 Cải Thiện Trải Nghiệm Người Dùng**

- Tốc độ tải hình ảnh nhanh hơn  
- Đăng nhập, theo dõi đơn hàng mượt mà  
- Giảm độ trễ giờ cao điểm  
- Tăng niềm tin khách hàng nhờ độ tin cậy AWS  

---

### **8.6 Năng Lực Chiến Lược Đạt Được**

- Kiến trúc cloud-native, sẵn sàng microservices  
- Quản trị chi phí (FinOps) hiệu quả  
- Giám sát tập trung và báo cáo toàn diện  
- Dễ mở rộng sang ECS, EKS hoặc RDS  
- Tuân thủ bảo mật IAM, Cognito, WAF, Secrets Manager  
- Nền tảng vững chắc cho phân tích dữ liệu và tích hợp AI  
