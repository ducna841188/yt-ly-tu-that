# Kế hoạch nghiên cứu chín video Lý Tử Thất

Phiên bản kế hoạch 0.3.0; core 1.3.1. Người dùng xác nhận đã chọn đủ tám video bổ sung ngày 18/10/2026. Đã nhận VID_02 (tệp 10:11.92 và URL); còn bảy video bổ sung chưa gửi. Người dùng sẽ nạp từng video. [Bản dữ liệu](ke-hoach-nghien-cuu.json).

## Nguồn cần tiếp nhận

Tiếp nhận từng URL/tệp theo thứ tự người dùng gửi; không cần chờ đủ tám URL mới phân tích. Giữ VID_02 theo số người dùng đã gán. VID_01 vẫn cần bản nguồn để xác minh. Giữ bản nguồn đầy đủ; lượt VID_02 hiện hành bỏ qua âm theo yêu cầu người dùng. Nếu chia đoạn, giữ thứ tự và mốc về bản gốc. Tên gốc, URL, thời lượng, phiên bản và tình trạng âm được ghi trong sổ nguồn; phần chưa có để chưa biết.

VID_01 hiện chỉ có workbook/12 ảnh và phân tích nguồn thuật lại; cần video để xác minh cut, chuyển động, trạng thái và âm. Không coi 471 dòng là 471 shot đã xem độc lập. Nếu chưa có media VID_01, một video mới có thể làm mẫu phương pháp trước.

## Lượt thực hiện

| Lượt | Công việc | Điều cần đạt |
| --- | --- | --- |
| 1 | Xác định bộ nguồn; thử khả năng đọc hình–âm; phân tích đầy đủ một video mẫu | Nhãn, mốc và độ phủ đúng dữ liệu thật |
| 2 | Ba video tiếp theo | Có đối chiếu và ngoại lệ, sửa phương pháp khi cần |
| 3 | Ba video tiếp theo | Tổng bảy video; ghi giả thuyết và dự đoán trước hai phim cuối |
| 4 | Hai video cuối, vẫn phân tích đầy đủ | Kiểm quy tắc trên phần chưa dùng để rút giả thuyết |
| 5 | Các đoạn thử AI và vận dụng sang Farm | Kiểm khả thi, trải nghiệm và chi phí thực dùng |

Phân vai 7+2 khi nhận diện đủ bộ nguồn; giữ tám video người dùng đã chọn. VID_02 là mẫu phương pháp đầu tiên, hiện ở trạng thái partial: 176 phiếu sâu về hình/góc/màu/trạng thái, 26 chuỗi/77 nhịp, 175 liên kết hình, 13 giả thuyết DNA; chưa phát trọn chuyển động. Âm ngoài phạm vi, không chặn lượt hình. Phân tích từ toàn phim tới sự kiện; tuyến âm chỉ triển khai khi thuộc phạm vi yêu cầu. Chỉ mục từng giây là công cụ tra cứu; shot theo ranh giới cắt thực. Khi chia lượt, lưu mốc tiếp tục và phần chưa xem/nghe.

## Ba lớp DNA

1. Phong cách: tổ chức truyện, hình, thời gian, âm và quan hệ đời sống.
2. Hiệu quả: giả thuyết về chọn xem, xem tiếp, hài lòng; ghi đúng dữ liệu có thể tiếp cận.
3. Khả thi AI: tham chiếu, trạng thái, cảnh khó, công đoạn sửa và tiêu chí duyệt.

Mỗi quy tắc có điều kiện, video/shot/mốc, ngoại lệ, cách tái tạo và phép kiểm. Đếm theo phim, shot hoặc thời lượng phải ghi mẫu số. Không lấy số view hoặc hàng nghìn shot từ cùng tác giả làm chứng minh nhân quả.

## Vận dụng và cập nhật

Giữ hướng Farm đã chốt: nhân vật/bối cảnh riêng, tập đầu học gần trình tự nguồn, tập sau phát triển sáng tạo; ưu tiên trải nghiệm nhẹ và chủ yếu không thoại. Cấu hình công cụ, trần chi phí và đoạn thử được chốt khi có bài sản xuất cụ thể. Lần này đã biên soạn lớp phân tích ảnh và phương án tái tạo VID_02; chưa phát trọn chuyển động, tạo clip hoặc kiểm khán giả; âm ngoài phạm vi hiện hành. [Hồ sơ hiện hành](../VID_02/README.md).

Phân tích nguồn giữ đúng thư mục VID; hồ sơ DNA liên kết tới nguồn và core. Tài liệu hiện hành sửa tại chỗ; lịch sử dùng Git và [nhật ký chung](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/CHANGELOG.md). [Sổ tay cho người học](https://github.com/ducna841188/kien-thuc-dien-anh/tree/main/thu-vien/ban-cho-nguoi).
