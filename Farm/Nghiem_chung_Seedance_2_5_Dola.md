# Farm — Nghiệm chứng Seedance 2.5 qua Dola
- Phiên bản hiện hành: **0.2**, cập nhật 12/10/2026.
- Theo yêu cầu mới: **chỉ cô gái và vườn đã duyệt**, tạm chưa có bà; mỗi cảnh dùng **2,9–3,0 giây**.
- Đã tạo ảnh đầu cảnh; chưa chạy video Seedance/Dola.
- Các cấu hình sáu cảnh × 5 giây có bà ở bản 0.1 thuộc lịch sử Git; dùng bản dưới đây cho lần thử hiện tại.

## Bộ thử hiện hành

[Co_gai_va_vuon_30s](Tests/Co_gai_va_vuon_30s/README.md) có:
- 10 PNG đầu cảnh riêng: S01 giữ nguyên ảnh vườn đã duyệt; S02–S10 tạo từ ảnh cô gái/vườn được người dùng duyệt.
- [Kịch bản 30 giây](Tests/Co_gai_va_vuon_30s/Shot_list_30s.md): 10 cảnh × 3,0 giây, theo dõi một quả vàng từ cây tới chậu rửa.
- [Câu lệnh Seedance](Tests/Co_gai_va_vuon_30s/Seedance_30s.md): đoạn 30 giây và từng cảnh.
- Hai ảnh cô gái và hai ảnh vườn duyệt, giữ nguyên byte trong thư mục references.
- Dữ liệu cảnh JSON, mã kiểm ảnh và nhật ký câu lệnh tạo ảnh.

Chuỗi: **vườn → tới cây → nhìn quả → kê đỡ → cắt cuống → đặt vào rổ → mang ra sân → nghiêng vào nước → rửa → nhìn thành quả**.

Vật liệu thử táo của bản 0.1 được thay bằng quả tròn vỏ vàng có sẵn trong ảnh vườn. Bài hiện tại không có bà, người khác, vật nuôi, cảnh cắt quả hoặc nấu trong bếp. Thiết lập nhân vật sống với bà ở [định hướng dự án](Dinh_huong_chinh_thuc.md) vẫn giữ cho các tập sau.

## Cách thực hiện

1. Dùng đúng file S01.png–S10.png của bộ chọn; S02 là bản đã sửa hướng nhìn vườn.
2. Có thể thử S05 riêng trước để kiểm kéo–cuống–tay đỡ; dùng độ dài Dola thực sự hỗ trợ rồi chọn 3 giây sạch, rõ hành động.
3. Nếu Dola nhận bộ ảnh tương ứng, thử câu lệnh 30 giây với 10 mốc 3 giây. Nếu không nhận đủ, thử hai nhóm 15 giây hoặc từng đoạn riêng; ghi rõ số ảnh thực đã gửi.
4. Kiểm/cắt lại độ dài từng cảnh ở đầu ra, không coi mốc yêu cầu là kết quả đã bảo đảm.
5. Ghép mỗi cảnh 3 giây để có 30 giây; nếu lấy 2,9 giây tất cả thì đoạn thành 29 giây.
6. Giữ âm sinh khi khớp thao tác; người dùng dựng môi trường và nhạc. Video chủ yếu không thoại.

Seedance 2.5 được [ByteDance công bố](https://seed.bytedance.com/en/seedance2_5) hỗ trợ hình/âm thanh đồng thời và đoạn tối đa 30 giây, có liên kết tới Dola. Chưa xác minh giao diện/giới hạn đầu vào trong tài khoản Dola của người dùng. Không tự đặt tên nút hay giả định 3 giây là tùy chọn xuất trực tiếp.

## Tiêu chí kiểm video

- Nhận diện mặt/tóc/trang phục và các đồ vật.
- Tiếp xúc tay–kéo–cuống, trọng lượng quả, đường đi vào rổ và nước.
- Trạng thái: một quả, cuống nguyên trước cắt, cuống ngắn sau cắt, rổ/chậu đổi đúng theo việc.
- Hình giống camera thật, ánh sáng/bóng hợp lý và nhịp tự nhiên.
- Âm thao tác có đúng sự kiện, thời điểm; thoại/nhạc tự thêm được ghi riêng.
- Cảm giác dễ chịu khi xem ở tốc độ bình thường.

Không bù lỗi vật lý/nhận diện bằng màu đẹp hoặc nhạc. Có thể dùng phần hình sạch và thay đoạn lỗi bằng cảnh riêng. Nếu hình đạt nhưng âm sai, giữ hình và thay âm.

## Ghi kết quả thật

| Run | Cảnh/cách | Ảnh & câu lệnh | Độ dài yêu cầu/thực nhận | Giây hình dùng được | Lỗi & timecode | Âm có/đạt | Phút làm việc | Credit/chi phí |
|---|---|---|---|---|---|---|---|---|
| Chưa chạy | — | — | — | — | — | — | — | — |

Tỷ lệ hình dùng được = tổng giây đạt / tổng giây đầu ra.

Chi phí/phút hình dùng được = tổng chi phí thực / (tổng giây đạt / 60). Nếu chưa quy đổi được tiền, giữ credit và thời gian thực, không tự gán giá.

Thử đoạn riêng có phần dư và đoạn 30 giây cần so trên phút hình dùng được cùng công sức chỉnh, không so số giây đầu ra đơn thuần. Một lượt nhỏ chưa chứng minh tỷ lệ thành công ổn định.

## Trạng thái

Bộ ảnh đã tạo và được kiểm về bố cục/chủ thể/trạng thái tĩnh. Chưa có clip Dola nên chưa kết luận độ chân thực chuyển động, giữ nhận diện qua cut hoặc mức giữ chân khán giả. Sau 3–5 video, ưu tiên đã chốt vẫn là giữ chân, người xem quay lại và phản hồi thư giãn.
