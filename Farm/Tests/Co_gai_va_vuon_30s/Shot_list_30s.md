# Test 02 — Cô gái và khu vườn, 30 giây
- Bản kịch bản: **0.2**, cập nhật ngày 12/10/2026.
- Theo yêu cầu mới: chỉ thử cô gái và khu vườn, tạm chưa có bà; mỗi cảnh mục tiêu **2,9–3,0 giây**.
- Bản dựng mẫu dùng **10 cảnh × 3,0 giây = 30,0 giây**.
- Nhân vật/thế giới dài hạn vẫn có bà; phạm vi bài thử này không thay đổi thiết lập đó.
- Bộ đầu vào: bốn ảnh cô gái/vườn được người dùng duyệt trong tin nhắn ngày 12/10/2026.
- Bộ đầu ra: **10 PNG riêng**, trong đó S01 giữ nguyên ảnh vườn duyệt và S02–S10 được tạo bằng công cụ tạo ảnh tích hợp.
- Đã tạo ảnh; **chưa tạo video Seedance/Dola**.

## Ý tưởng của đoạn thử

Cô gái tới cây quả trong khu vườn đã duyệt, đỡ và cắt cuống một quả, đặt vào rổ, mang ra mép sân để rửa, rồi nhìn thành quả với nét mặt nhẹ nhàng.

Dùng quả tròn vỏ vàng sẵn trong ảnh vườn, thay vật liệu thử táo của bản 0.1. Đây là mô tả thị giác, chưa xác định tên giống/cây hoặc mùa vụ thực tế từ ảnh AI.

## Bảng cảnh

| Cảnh | Thời gian | Cỡ/góc cảnh | Trạng thái ảnh đầu | Động tác trong 3 giây | Trạng thái cuối | Âm thanh |
|---|---|---|---|---|---|---|
| [S01](images/S01.png) | 00:00–00:03 | Toàn cảnh rộng; Góc hơi cao, đúng ảnh vườn duyệt | Vườn không có người; cây quả vàng, giàn quả xanh dài và lối đá đúng ảnh. | Lá và cành nhỏ lay nhẹ trong gió. | Quả vẫn gắn trên cây; bố cục và ánh sáng ổn định. | Gió lá, chim xa nhỏ. |
| [S02](images/S02.png) | 00:03–00:06 | Trung toàn / thấy toàn thân; Gần ngang tầm mắt, từ sân nhìn vào vườn | Cô gái ở miệng lối đá, cầm rổ trống và nhìn về cây bên cạnh. | Bước nhỏ tới cây quả, rổ trống đung đưa rất nhẹ. | Cô gái dừng cạnh cây; mặt, trang phục, rổ giữ nguyên. | Bước trên đá, áo/rổ khẽ động. |
| [S03](images/S03.png) | 00:06–00:09 | Cận quả / đặc tả; Ngang tầm quả | Một quả tròn vỏ vàng còn nối với cành bằng cuống nguyên. | Lá cạnh quả lay nhẹ; máy giữ yên. | Cuống vẫn nguyên; quả không tự rơi. | Lá xào xạc nhỏ. |
| [S04](images/S04.png) | 00:09–00:12 | Trung cảnh; Ngang tầm, thấy mặt nghiêng 3/4 | Tay đã khẽ kê dưới quả; kéo còn ở ngang bụng, chưa chạm cuống. | Kê/nâng đáy quả rất nhẹ để đỡ trọng lượng, khoảng 1 cm. | Quả vẫn còn trên cành, tay đỡ chắc; chưa cắt. | Lá và vải áo khẽ động. |
| [S05](images/S05.png) | 00:12–00:15 | Cận tay, kéo và cuống; Chếch ngang, vùng lưỡi kéo–cuống rõ | Một tay đỡ quả; kéo mở ôm cuống còn nguyên. | Khép kéo một lần để cắt cuống; tay đỡ chịu trọng lượng quả. | Quả tách khỏi cành; có cuống ngắn; không cắt vỏ quả. | Tiếng kéo khép/cắt nhỏ, lá khẽ động. |
| [S06](images/S06.png) | 00:15–00:18 | Cận / nhìn xuống rổ; Góc cao chếch | Quả đã cắt cuống ở trên tay, còn cách đáy rổ trống. | Hạ chính quả đó xuống rổ, nhả tay nhẹ. | Trong rổ có đúng một quả; tay rời ra ít. | Quả chạm rổ tre, tiếng đan tre nhỏ. |
| [S07](images/S07.png) | 00:18–00:21 | Trung toàn / thấy toàn thân; Từ sân nhìn vào vườn | Cô gái xách rổ có một quả; chậu và ghế thấp ở mép sân. | Đi một bước nhỏ về phía chậu rửa. | Rổ vẫn một quả, cô gái gần chỗ rửa. | Bước chân, rổ tre khẽ động. |
| [S08](images/S08.png) | 00:21–00:24 | Cận rổ và chậu; Nhìn xuống chếch | Quả vẫn ở trong rổ hơi nghiêng; chậu có nước, chưa có quả. | Nghiêng rổ thêm chút để một quả lăn nhẹ vào chậu. | Quả ở trong chậu, rổ trống, nước gợn nhỏ. | Quả chạm nước và gợn nước. |
| [S09](images/S09.png) | 00:24–00:27 | Cận tay và nước; Chếch trên miệng chậu | Một tay đỡ quả trong nước; tay còn lại vừa chạm vỏ. | Xoa một đường nhẹ trên vỏ để rửa. | Quả vẫn nguyên và ướt, hai tay ổn định. | Nước và tay chạm vỏ nhỏ. |
| [S10](images/S10.png) | 00:27–00:30 | Trung cận / thấy mặt và quả; Ngang tầm, cô gái ở ghế thấp cạnh chậu | Cô gái đỡ quả ướt phía trên chậu; rổ bên cạnh đã trống. | Nâng quả thêm vài cm và nhìn thành quả với nụ cười nhẹ. | Giữ quả phía trên chậu, nước nhỏ vài giọt, nét mặt thư thái. | Giọt nước và nền vườn nhỏ. |

## Quy tắc liền mạch

- Cùng khuôn mặt, tóc, búi thấp, áo trắng cổ đứng, tay áo xắn, tạp dề chàm họa tiết vòng chấm trắng, quần xám dài và giày vải đen của ảnh duyệt.
- Góc chung là từ sân nhìn vào vườn: cây quả vàng bên trái, giàn quả xanh dài bên phải, lối đá và đèn thấp đúng bố cục chính của ảnh vườn. Ảnh nhìn ngược được giữ làm tham chiếu bổ sung, không trộn hai hướng trong cùng khung.
- Theo dõi **một quả**: còn trên cây → cắt cuống → vào rổ → vào nước → rửa → nâng nhìn. Rổ chỉ có một quả sau S06, trống sau S08.
- Cuống nguyên ở S03–S05 trước động tác cắt; cuống ngắn ở các cảnh sau.
- Rổ tre một quai vòng, chậu kim loại và ghế gỗ thấp giữ cùng loại/hình giữa các cảnh. Chậu và ghế là đồ đặt tạm trên phần sân, không thêm công trình mới.
- S04 đã có tay kê dưới quả trong ảnh; câu lệnh chỉ nâng đỡ nhẹ. Không yêu cầu tay tự xuất hiện từ vị trí khác.
- Mỗi cảnh có một thao tác chính. Các chuyển vị trí nhỏ như đặt rổ xuống/lấy quai/xếp lại chỗ ngồi có thể được lược giữa hai góc cắt, không diễn tả chúng như biến hình.
- Không có bà, người khác, chó/mèo hoặc cảnh trong bếp trong bài thử hiện tại.

## Độ dài cần hiểu đúng

**3 giây là thời lượng cảnh dùng trong bản dựng.** Có hai cách chạy:
1. Một đoạn 30 giây gồm 10 cảnh theo mốc trên.
2. Các đoạn riêng từ từng PNG, dùng độ dài Dola thực sự cho phép rồi lấy 2,9–3,0 giây rõ hành động nhất.

Nếu Dola chỉ cho độ dài tối thiểu dài hơn 3 giây, không ép thông số không tồn tại. Có thể tạo 4–5 giây rồi cắt. Không tăng tốc động tác để nhét nhiều việc vào 3 giây.

Các mốc trong câu lệnh nhiều cảnh là chỉ dẫn mong muốn; khi nhận video phải kiểm/cắt lại thời lượng thực của từng cảnh. Nếu tất cả lấy 2,9 giây thì đoạn ghép là 29 giây; bản này dùng 3,0 giây để có 30 giây.

## Cách chạy đầu tiên

Có thể kiểm S05 riêng trước vì đây là cảnh có tương tác tay–kéo–cuống khó nhất. Sau đó thử đoạn 30 giây với bộ ảnh, dùng [câu lệnh Seedance](Seedance_30s.md). Nếu một cảnh bị lỗi, thay bằng đoạn riêng từ đúng PNG; không tự thay loại quả/bối cảnh/nhân vật để che lỗi.

Video chủ yếu không thoại. Câu lệnh yêu cầu âm thao tác và âm vườn nhẹ; người dùng tự dựng nhạc/âm nền. Nếu hình tốt nhưng âm sinh sai, có thể giữ hình và thay âm.

## Tình trạng kiểm tra

Đã xem các ảnh riêng để kiểm chủ thể, bố cục chính, trang phục, số lượng quả và trạng thái đồ vật. Đã sửa hướng nhìn của bản S02 ban đầu; chỉ file S02 hiện trong bộ này là bản chọn.

Các PNG chưa chứng minh chuyển động, tiếp xúc hay nhận diện sẽ giữ ổn định trong video. Cần kiểm đầu ra Dola ở tốc độ bình thường và xem chậm vùng tay, kéo, cuống, rổ, nước. Chi tiết nhỏ của cây/rổ/họa tiết có thể thay đổi trong ảnh sinh; không coi đây là bản sao hình học chính xác của vườn.

[Quay lại bộ ảnh](README.md) · [Dữ liệu cảnh JSON](shotlist.json) · [Câu lệnh tạo ảnh đã dùng](Cau_lenh_tao_anh.md)

