---
title: "Worklog Tuần 9"
date: 2025-11-07
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---
### Mục tiêu Tuần 9:

* Cấu hình Amazon S3 an toàn cho upload hình ảnh (bucket policy, CORS, ACL).
* Xây dựng upload service với presigned URL tích hợp vào backend API.

### Các nhiệm vụ trong Tuần 9

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
|-----|-----------|--------------|-----------------|--------------------|
| 1   | Tạo bucket S3 cho hình sản phẩm; đặt private, bật versioning. | 03/11/2025 | 03/11/2025 | Tài liệu AWS S3 |
| 2   | Cấu hình CORS cho CloudFront/SPA và giới hạn MIME types. | 04/11/2025 | 04/11/2025 | Tài liệu AWS S3 |
| 3   | Implement service tạo presigned URL (PUT/GET), kiểm tra size/type. | 05/11/2025 | 05/11/2025 | AWS SDK docs |
| 4   | Tích hợp endpoint upload vào backend; gắn metadata (uploader, productId). | 06/11/2025 | 06/11/2025 | Đề xuất `AWSJewelry` |
| 5   | Kiểm thử E2E upload từ React: lấy URL → PUT ảnh → xem qua CDN. | 07/11/2025 | 07/11/2025 | Postman, CloudFront |

### Thành tựu Tuần 9:
* Bucket S3 được harden (private, versioning, CORS tối thiểu cho SPA).
* Service presigned URL có kiểm soát content-type/kích thước và metadata tagging.
* Upload API gắn ngữ cảnh sản phẩm, trả về object key sẵn sàng CDN.
* Frontend kiểm thử thành công: upload ảnh và phân phối qua CloudFront.
