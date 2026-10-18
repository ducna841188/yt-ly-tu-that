# FARM — Nhánh kiến thức đời sống nông thôn yên bình

Phiên bản 1.1.2, ngày 18/10/2026. Dùng [FILM-KB hiện hành](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/README.md); đọc manifest trên main trước khi áp dụng. core_dependency.version là bản đã đối chiếu gần nhất, commit = null để không khóa hướng dẫn vào bản cũ.

**10 quy tắc ứng dụng · 3 ứng viên nghiên cứu · 1 ví dụ dữ liệu từ báo cáo VID_01.** Chưa tiếp nhận video mới hoặc kiểm nghiệm video/khán giả trong lần tạo nhánh này.

## Đọc theo thứ tự

1. [Hồ sơ ngách](ho-so-ngach.json).
2. [Định hướng đã chốt](https://github.com/ducna841188/yt-ly-tu-that/blob/main/Farm/Dinh_huong_chinh_thuc.md) và [hồ sơ khán giả](https://github.com/ducna841188/yt-ly-tu-that/blob/main/Farm/Ho_so_khan_gia.md).
3. [Chuẩn phân tích chung](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/02_CHUAN_PHAN_TICH.md) và [chuẩn quyết định](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/03_RA_QUYET_DINH.md).
4. [Nguồn và giới hạn VID_01](https://github.com/ducna841188/yt-ly-tu-that/blob/main/Farm/VID_01/Qa_du_lieu.md).
5. [Ví dụ chuyển hai shot từ báo cáo vào schema](vi-du-vid01-tu-bao-cao.json).

## Những điều đang dùng

- Lời hứa thư giãn trong một thế giới làng quê xanh; công việc có tiến triển và thành quả.
- Mục tiêu nữ 35–55 ở đô thị Mỹ là hồ sơ hướng tới, chưa phải kết quả xác nhận khán giả.
- Chủ yếu không thoại; âm thao tác, môi trường và nhạc được tổ chức theo trải nghiệm.
- Thế giới nhân vật có cô gái, bà, vật nuôi và quan hệ tiếp diễn. Số người của từng shot theo bản yêu cầu, không áp một người cho toàn loạt.
- Camera, màu, nhịp và âm lấy từ nguyên lý chung rồi lựa chọn theo ngách; không sao tỷ lệ/thời lượng của một video thành công thức.

## Trạng thái bằng chứng VID_01

Nguồn có 471 bản ghi, độ dài theo bảng 22:44.44 và 12 ảnh tĩnh nhúng. Những cột camera/chuyển cảnh/audio còn hạn chế đã được ghi trong QA. Lần này chỉ kế thừa báo cáo và chuyển hai shot làm ví dụ cấu trúc; chưa xác minh toàn chuyển động hoặc nghe audio.

Các ứng viên gửi về core có trạng thái candidate. Cần bằng chứng phù hợp và xem điều kiện/phản ví dụ trước khi nâng mức; không tự đảo nguyên tắc đã dùng.

## Khi tiếp nhận video mới

Ghi asset, tệp, mốc gốc, offset từng phần và độ phủ. Phân tích toàn phim → phân đoạn → chuỗi → shot → sự kiện theo cùng schema. Lưu mỗi video/asset thật với một hồ sơ phân tích hiện hành; sửa đúng tệp đó, không tạo thư mục bản sao theo version. Tổng hợp sau một lượt nhập.

[Dấu vết nguồn đã đọc](nguon.json) · [Quy tắc làm việc](AGENTS.md) · [Nhật ký chung](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/CHANGELOG.md).

Tài liệu làm việc trỏ main để đọc bản hiện hành. Revision trong nguồn/phân tích ghi lại bằng chứng lúc phân tích, không là bản sao tài liệu cần đọc thêm. Lịch sử cập nhật thư viện và Farm nằm trong một nhật ký chung; chi tiết trước–sau dùng Git.
