# VID 01 — Nghiên cứu shot list Lý Tử Thất

Tài liệu đầu vào người dùng cung cấp ngày 12/10/2026: `VID 1 - phan_tich_Ly_Tu_That_471_shots_CORRECTED_FINAL_v3.xlsm`.

**471 cảnh · 22:44.44 · ba sheet · 12 ảnh tĩnh nhúng.** Tệp chưa có tên/URL video để đối chiếu và không bao gồm video chuyển động hoặc audio.

| Tài liệu | Nội dung |
|---|---|
| [Phân tích điện ảnh](Phan_tich_dien_anh.md) | Điểm hay, dẫn chứng shot/timecode, cấu trúc kể chuyện và bài học cho Farm. |
| [QA dữ liệu](Qa_du_lieu.md) | Các mâu thuẫn cụ thể và phạm vi bằng chứng; không sửa bản nguồn. |
| [Shot Analysis CSV](shot_analysis.csv) | 471 dòng và đầy đủ 19 cột của sheet đầu. |
| [AI Reconstruction CSV](ai_reconstruction.csv) | 471 dòng và đầy đủ 32 cột của sheet tái dựng; giữ nguyên cả các trường cần kiểm tra. |
| [Số liệu](metrics.json) | Thời lượng, phân bố nhãn nguồn, 22 pha của nguồn và bốn khối phân tích. |
| [Ảnh minh họa trực tiếp](references/) | Bốn ảnh Shot 001, 003, 006, 010 trích nguyên từ workbook, minh họa các nhận xét bố cục. |
| [Kho bản gốc](source_archive/README.md) | Toàn bộ workbook giữ nguyên byte, lưu thành 41 phần cùng manifest và script khôi phục. |

Các CSV giữ nguyên nội dung ô dạng văn bản, có BOM UTF-8 để thuận tiện mở bằng Excel. Cột hình ảnh trống vì hình được nhúng dưới dạng drawing, không phải nội dung ô; 12 ảnh và định dạng được bảo toàn trong bản gốc.

Quy ước nghiên cứu: phân biệt dữ liệu của bảng, điều đã quan sát trong ảnh và diễn giải chuyên môn. Nhãn cỡ cảnh/góc máy/màu có chỗ chưa nhất quán; chuyển cảnh và audio chưa được xác minh. Không sử dụng các câu mẫu tái dựng như mô tả chắc chắn của mọi cảnh.

Tệp này thuộc dự án **Nghiên Cứu LTT / Farm**, lưu tại repository `ducna841188/yt-ly-tu-that` theo quy ước trong `AGENTS.md`.
