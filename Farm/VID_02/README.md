# VID_02 — Đồ ăn vặt cho Tết Nguyên đán

**Bản 0.2.0 · tập trung hình ảnh, góc máy, màu sắc và chuỗi hành động. Âm ngoài phạm vi theo người dùng.**

176 hồ sơ cú máy dự kiến · 26 phiếu chuỗi · 77 nhịp nội dung · 175 liên kết trạng thái qua điểm cắt · 13 sổ sản vật · 13 giả thuyết DNA · 43 bảng ảnh nguồn.

## Đọc theo thứ tự

1. [Phân tích có mục lục](Phan_tich_dien_anh.md): bức tranh toàn phim, 26 chuỗi chi tiết, góc/màu/lược việc và đường dẫn từng cú.
2. [Phân tích chuẩn](phan-tich.json): 25 nhóm với bằng chứng; bốn nhóm âm để null vì ngoài phạm vi. Bản đọc chỉ hiện 21 nhóm hình.
3. [Phiếu tái tạo](tai-tao.json): shots[].visual_decision cho từng cú; visual_study.sequence_designs cho chuỗi; visual_study.visual_cut_links cho 175 điểm nối. Các bản thiết kế chưa sinh thử.
4. [DNA có điều kiện](dna.json): 13 giả thuyết, điều kiện, ngoại lệ và phép kiểm. Chưa là công thức gây view.
5. [Nguồn/phương pháp](nguon.json), [ảnh/checksum](anh/manifest.json), [thống kê](metrics.json), [chỉ mục từng giây](chi-muc-giay.json).

## Các kết quả chính

- Góc cao đọc mặt phẳng/vật chứa; tầm mặt vật đọc độ dày, mặt cắt, sợi kéo và cuộn; rộng trả quan hệ người–nơi. Chọn góc theo thông tin.
- Màu có vật mang: chàm áo, nâu tre/gỗ, xanh xám nền, đỏ quả/giấy, vàng bánh. Biến đổi bề mặt kể tiến trình thô–tan–phủ–cắt–chín–gói.
- Hạt dẻ, lát quả, phôi kẹo và thịt có trạng thái chờ rồi được trả; bó rơm có công dụng muộn ở giá hồ lô.
- Không nối bịa bưởi/quýt thành phần quả vàng món cuối, hoặc ống bánh thành cùng mẻ nón nếu chưa có bước/bằng chứng.
- Giữ lực/đỡ/nhả ở dao, xẻng/lò, siro, cán phôi, cuộn, giỏ–đòn–thang và trao món.

## Phạm vi bằng chứng

Tệp tải dài 10:11.92, 1280×720, mã hóa 50fps. 1.328 mốc ảnh riêng theo toàn trục; đây không phải chứng nhận phát trọn chuyển động ở tốc độ thật. 176 cú là phân hoạch làm việc, chưa khóa mọi cut. Không đoán ống kính, khẩu, LUT/Kelvin hoặc tốc độ quay từ ảnh. Chưa có clip AI đầu ra hoặc thử khán giả.

Audio cũ được giữ để truy nguyên, không được phân tích thêm và không chặn lượt hình. Nguồn/checksum, VID_01 và lựa chọn Farm giữ nguyên. Mọi tài liệu sửa tại chỗ; lịch sử ở Git và [nhật ký chung](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/CHANGELOG.md).

[Thư viện Farm](../Thu_vien_kien_thuc/README.md) · [Core hiện hành](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/README.md).
