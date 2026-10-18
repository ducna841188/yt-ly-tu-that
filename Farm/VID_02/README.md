# VID_02 — Đồ ăn vặt cho Tết Nguyên đán

**Bản nạp 0.1.0: đã phân tích ảnh theo toàn trục; chưa xem trọn chuyển động hoặc nghe âm.** Tệp dài **10:11.92**, 1280×720, mã hóa 50 fps, có AAC stereo. [Nguồn do người dùng gửi](https://www.youtube.com/watch?v=FWMIPukvdsQ).

**176 cú máy dự kiến · 26 chuỗi việc · 8 phân đoạn · 25 nhóm mỗi cú · 1.328 mốc ảnh riêng · 10 lượt rà tiếp xúc · 13 sổ trạng thái · 12 giả thuyết DNA.** Đây là dữ liệu nghiên cứu có điều kiện, chưa là công thức gây lượt xem.

## Đọc theo thứ tự

1. [Bản phân tích có mục lục và hồ sơ từng cú máy](Phan_tich_dien_anh.md).
2. [JSON phân tích chuẩn](phan-tich.json): quan sát ảnh, diễn giải, nguồn/mốc và phần chưa biết. AI nên đọc từng sequence_id, không cần nạp toàn tệp trong một lượt.
3. [Phiếu tái tạo](tai-tao.json): trạng thái, khung, điểm đỡ, phần phải giữ, yêu cầu tham chiếu, âm đề xuất và dấu duyệt cho từng cú. Đây là thiết kế chưa tạo thử.
4. [DNA có điều kiện](dna.json): bằng chứng, điều kiện, ngoại lệ, cách làm và phép kiểm tiếp.
5. [Nguồn và phương pháp](nguon.json), [mục lục ảnh/checksum](anh/manifest.json), [thống kê](metrics.json), [chỉ mục từng giây](chi-muc-giay.json), [tuyến âm chờ nghe](am-thanh.json).

## Những điểm có thể vận dụng ngay

- Đan công việc trong lúc món khác chờ rồi quay lại trả kết quả: hạt dẻ, lát quả sấy, phôi kẹo và thịt.
- Cho thấy biến đổi bằng điểm tiếp xúc; kết quả tiếp tục được dùng, gói hoặc cất giữ.
- Giữ vật nuôi, người nhận và nơi cất đồ như các phần của đời sống tiếp diễn.
- Bó rơm được làm sớm rồi trở lại làm giá cắm hồ lô; một đạo cụ có công dụng nhìn thấy.
- Không ép mỗi cú máy ba giây: bản phân hoạch hiện tại có trung vị 3.24s, dao động 0.70–9.22s.

## Phần còn phải xác minh

Chuyển động máy, vận tốc, mọi pha tay/vật giữa ảnh, độ đầy đủ ranh giới và toàn bộ nội dung âm. Đo RMS/sample peak không thay cho nghe nhạc/thoại/SFX hoặc kiểm đồng bộ. 176 cú là danh sách làm việc, không số đếm đã duyệt bằng phát toàn phim.

Mốc 05:59.48 là khói bùng trong cùng góc, đã gộp vào V02-S106. Điểm cắt sang góc rộng dự kiến ở 05:59.64. Các nhận định cảm xúc/công dụng là giả thuyết, chưa có phản hồi người xem. Đọc trường coverage trước sử dụng.

## Lưu trữ và chạy lại

Nguồn 217 MB vẫn là tệp người dùng đã tải lên; [nguon.json](nguon.json) giữ mã tệp và SHA-256, không chép video lớn vào Git. 43 bảng ảnh là ảnh nguồn phục vụ phân tích. [Công cụ xuất bản đọc](cong-cu/xuat_ho_so.py) đọc JSON hiện hành; [công cụ trích lại ảnh](cong-cu/trich_anh.py) cần tệp đúng checksum.

Mọi tệp sửa tại chỗ; lịch sử ở Git và [nhật ký chung](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/CHANGELOG.md). [Thư viện Farm](../Thu_vien_kien_thuc/README.md) · [Core hiện hành](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/README.md).
