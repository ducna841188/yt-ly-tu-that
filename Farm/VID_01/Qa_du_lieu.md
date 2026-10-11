# VID 01 — Kiểm tra dữ liệu và giới hạn bằng chứng

Ngày phân tích: 12/10/2026. Nguồn: workbook `VID 1 - phan_tich_Ly_Tu_That_471_shots_CORRECTED_FINAL_v3.xlsm` do người dùng cung cấp. Không sửa workbook nguồn.

## Phần đã kiểm tra

- Cả hai sheet chính có 471 bản ghi, Shot 001 đến Shot 471, thứ tự liên tục. Mô tả shot của hai sheet trùng nhau ở cả 471 bản ghi.
- Tổng thời lượng là 1.364,44 giây, từ 00:00.00 đến 22:44.44. Thời lượng của từng dòng khớp hiệu hai mốc thời gian; không có khoảng hở hoặc chồng lấn giữa các dòng.
- Đã đọc toàn bộ mô tả, các trường kỹ thuật và sheet `QA & Phương pháp`; đã xem 12 ảnh tĩnh nhúng, tương ứng Shot 001–012 qua anchor tại các hàng 5–16 của sheet `AI Reconstruction`.
- 12 ảnh này là ảnh tham chiếu riêng lẻ, không phải 12 bảng ảnh chứa toàn bộ 471 cảnh. Tệp không cung cấp đủ ảnh để kiểm chứng độc lập toàn bộ mô tả so với video.
- Workbook nói các mô tả đã được kiểm qua frame đầu–giữa–cuối. Đây là tuyên bố phương pháp của tài liệu nguồn, không phải một lượt xem video độc lập trong lần phân tích này.

## Các mâu thuẫn cụ thể cần xử lý trước khi dùng để tái dựng

| Shot / thời gian | Mâu thuẫn trong nguồn | Cách sử dụng trong nghiên cứu hiện tại |
|---|---|---|
| 001 / 00:00.00–00:03.20 | Mô tả và ảnh là hoa đào, mái nhà, núi phủ sương. Các cột O/P/Q lại ghi nắp che → tay nhấc → bên trong lộ ra. | Dùng mô tả cùng ảnh để phân tích phong cảnh; không dùng hành động nhấc nắp. |
| 001 / 00:00.00–00:03.20 | Màu sắc ghi “Xanh lá nền + màu hoa làm điểm nhấn”. Ảnh nổi bật xanh lam–xám lạnh và hồng hoa. | Ghi riêng nhận xét từ ảnh; không lấy chuỗi màu mẫu làm bảng màu đã xác minh. |
| 005 / 00:11.56–00:12.04 | Mô tả và ảnh là vụn/vỏ bào trên mặt sân, không thấy tay cắt. O/P/Q lại mô tả dao đi xuyên nguyên liệu. | Xem đây là cảnh dấu vết sau thao tác theo bằng chứng hiện có; cần video nếu muốn biết diễn tiến đầy đủ. |
| 009 / 00:20.44–00:23.64 | Cột góc máy dùng nhãn “Ngang tầm mắt hoặc hơi cao” chung. Ảnh cho thấy máy ở độ cao thấp gần mặt đất và tầm đầu chó. | Phân biệt độ cao đặt máy với góc ngẩng/cúi; chưa đo góc nghiêng hay tiêu cự. |
| 010 / 00:23.64–00:32.00 | Mô tả nói đổ/tưới từ vật chứa; P lại mặc định “vật chứa nghiêng”. Ảnh thấy bình phun có vòi và tia nước. | Mô tả thao tác tưới/phun theo ảnh, không mặc định phải nghiêng vật chứa trong tái dựng. |
| 011 / 00:32.00–00:35.32 | Mô tả và ảnh là mầm cây; O/P/Q lại có nắp che và tay nhấc. | Giữ chủ thể mầm; chưa kết luận kỹ thuật tua nhanh từ một ảnh tĩnh. |
| 042 / 02:05.96–02:09.08 | Mô tả là mặt ngoài nhà với cửa sổ mở, không thấy rõ người; P ghi tay nhấc phần che. | Đánh dấu mâu thuẫn nội bộ; chưa xác minh cảnh bằng ảnh/video trong lần này. |
| 383 / 18:20.24–18:22.16 | Mô tả là đặt bánh lên khay, chỉnh hàng. O/P/Q lại là dao tiếp cận, cắt và xuất hiện đường cắt. | Dùng mô tả bày bánh cho phân tích quá trình; không dùng trạng thái cắt. |
| 470 / 22:34.52–22:39.20 | Mô tả là góc cao/rộng toàn sân và nhóm người; Shot Size ghi CU / Insert; bố cục ghi pattern/bề mặt và thao tác tay. | Xem các nhãn là chưa thống nhất; chưa tự sửa thành nhãn cuối cùng khi thiếu video. |

Các ví dụ này cho thấy một số cột có dạng câu mẫu và có thể không khớp mô tả riêng. Chúng không đủ để kết luận mọi dòng đều sai, cũng không đủ để coi nhãn “CORRECTED FINAL” là đảm bảo hoàn toàn chính xác.

## Các trường chưa thể dùng như kết luận về bộ phim

| Trường | Tình trạng | Hệ quả |
|---|---|---|
| Camera Movement | 440 dòng ghi tĩnh/gần tĩnh nhưng cần full-motion; 31 dòng chưa phân biệt chủ thể chuyển động với máy tracking/pan. | Không kết luận tỷ lệ máy tĩnh là 440/471. |
| Camera Angle | 440 dòng cùng nhãn “Eye Level / slight High Angle”. | Không chuyển nhãn này thành thống kê góc máy chính xác. |
| Foreground / Midground / Background | 344 dòng dùng cùng ba câu tổng quát: chi tiết gần máy / chủ thể chính / môi trường nhìn thấy. | Không coi các cột này là mô tả bố cục cụ thể đã hoàn tất cho mọi cảnh. |
| Trạng thái đầu / cuối | 341 dòng chỉ nói trạng thái lấy từ frame S/E. Một số dòng cụ thể lại mâu thuẫn mô tả. | Chưa đủ để khóa diễn tiến đầu–giữa–cuối cho sản xuất AI. |
| Ánh sáng / Màu sắc | 340 dòng cùng một bộ mô tả ánh sáng và màu. Một số ảnh mở đầu có bóng nắng và viền sáng rõ. | Không khẳng định mọi cảnh đều ánh sáng mềm/khuếch tán hoặc cùng một palette. |
| Chuyển cảnh | Cả 471 dòng ghi cần xem quanh cut. | Chưa đếm hard cut, dissolve, fade, match cut hay cắt đúng động tác. |
| Âm thanh | Cả 471 dòng ghi chưa phân tích/nghe audio. | Chưa nhận xét cách trộn nhạc, âm môi trường, âm thao tác hoặc cầu nối âm thanh của video này. |
| Mức sẵn sàng AI | 239 dòng A và 232 dòng B; cả hai vẫn ghi cần kiểm chuyển động. | A/B là nhãn của nguồn, không phải chứng nhận sẵn sàng tạo phim. |

## Cách dùng đáng tin cậy

Phân tích thời lượng từ mốc thời gian và các con số đã đối soát. Phân tích nội dung, sự sắp xếp cảnh và hành trình nguyên liệu từ mô tả trong bảng, ghi rõ đó là cơ sở của nhận xét. Phân tích thị giác trực tiếp chỉ áp dụng cho 12 ảnh đã xem. Các nhận xét về tác động cảm xúc và bài học cho Farm là diễn giải chuyên môn, cần thử nghiệm với người xem thực tế.

Một lượt xác minh tiếp theo cần video gốc để xem ranh giới cắt, chuyển động liên tục và nghe âm thanh. Nếu làm lại specification, nên sửa các trường mâu thuẫn theo từng shot thay vì thay câu mẫu hàng loạt. Báo cáo hiện tại giữ các ghi chú này riêng, không ghi đè bản người dùng gửi.
