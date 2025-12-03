from pathlib import Path
import re
import base64


def main() -> None:
    # Thư mục chứa hai file markdown Blog1
    base = Path("content/3-BlogsTranslated/3.1-Blog1")
    md_files = ["_index.md", "_index.vi.md"]

    # Nơi lưu ảnh trích ra (Hugo sẽ phục vụ dưới đường dẫn /images/...)
    out_dir = Path("static/images/3-BlogImage/Blog1-Extracted")
    out_dir.mkdir(parents=True, exist_ok=True)

    # Bắt các dòng dạng:
    # [image1]: <data:image/png;base64,AAAA...>
    # Lưu ý: trong raw string chỉ cần escape 1 lần cho dấu [ ]
    pattern = re.compile(
        r'^\[image(\d+)\]:\s*<data:image/(png|jpe?g);base64,([^>]+)>',
        re.MULTILINE,
    )

    for name in md_files:
        md_path = base / name
        text = md_path.read_text(encoding="utf-8")

        def replace(match: re.Match) -> str:
            idx = int(match.group(1))
            mime = match.group(2)
            b64_data = match.group(3)

            ext = "jpg" if mime.startswith("jp") else "png"
            filename = f"blog1-{idx}.{ext}"
            img_path = out_dir / filename

            # Ghi file ảnh ra đĩa
            img_bytes = base64.b64decode(b64_data)
            img_path.write_bytes(img_bytes)

            # Trả lại dòng markdown mới trỏ tới file ảnh
            return f"[image{idx}]: /images/3-BlogImage/Blog1-Extracted/{filename}"

        new_text = pattern.sub(replace, text)
        md_path.write_text(new_text, encoding="utf-8")
        print(f"Updated {md_path}")


if __name__ == "__main__":
    main()


