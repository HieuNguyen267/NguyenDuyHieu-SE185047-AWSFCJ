# Hướng dẫn Build Hugo Site

## Cách 1: Development Server (Khuyến nghị khi đang chỉnh sửa)

Chạy lệnh sau trong terminal:
```powershell
hugo server
```

Sau đó mở trình duyệt và truy cập:
- **English**: http://localhost:1313/en/
- **Tiếng Việt**: http://localhost:1313/vi/
- **Trang chủ**: http://localhost:1313/

**Ưu điểm:**
- ✅ Tự động reload khi bạn thay đổi file
- ✅ Xem kết quả ngay lập tức
- ✅ Không cần build lại mỗi lần chỉnh sửa

**Dừng server:** Nhấn `Ctrl+C` trong terminal

---

## Cách 2: Build Static Site (Cho Production)

Chạy lệnh:
```powershell
hugo
```

Lệnh này sẽ:
- Tạo các file HTML trong thư mục `public/`
- Copy tất cả file từ `static/` vào `public/`
- Sẵn sàng để deploy lên GitHub Pages hoặc hosting khác

**Sau khi build:**
- File được tạo trong thư mục `public/`
- Có thể upload toàn bộ thư mục `public/` lên hosting

---

## Cách 3: Build với các tùy chọn

### Build chỉ một ngôn ngữ:
```powershell
hugo --environment production
```

### Build với verbose output (xem chi tiết):
```powershell
hugo -v
```

### Build và xóa cache:
```powershell
hugo --cleanDestinationDir
```

---

## Kiểm tra ảnh có hiển thị đúng

Sau khi build, kiểm tra:
1. File ảnh có trong `public/images/2-Proposal/AWS_Architecture.jpg`
2. Trong HTML, đường dẫn ảnh là `/images/2-Proposal/AWS_Architecture.jpg`

---

## Troubleshooting

### Ảnh không hiển thị?
- ✅ Đảm bảo file ảnh nằm trong `static/images/`
- ✅ Đường dẫn trong markdown: `/images/...` (không có `static/`)
- ✅ Build lại site: `hugo` hoặc `hugo server`

### Link không hoạt động?
- ✅ Sử dụng đường dẫn tương đối: `../` hoặc `/path/`
- ✅ Không dùng `content/` trong đường dẫn
- ✅ Đảm bảo file đích tồn tại

---

## Deploy lên GitHub Pages

Sau khi build:
1. Commit và push thư mục `public/` lên GitHub
2. Hoặc sử dụng GitHub Actions để tự động build và deploy

---

## Lưu ý

- File trong `static/` sẽ được copy vào root của `public/`
- File trong `content/` sẽ được render thành HTML
- Theme `hugo-theme-learn` đã được cấu hình trong `config.toml`

