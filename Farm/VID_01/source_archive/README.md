# Tệp nguồn VID 01 — lưu nguyên vẹn

Tệp người dùng cung cấp: `VID 1 - phan_tich_Ly_Tu_That_471_shots_CORRECTED_FINAL_v3.xlsm`.

Tệp được giữ nguyên toàn bộ **21.416.632 byte**, gồm ba sheet và 12 ảnh nhúng. Lần gửi toàn bộ tệp qua kết nối GitHub không thành công; bản lưu này chia tệp thành 41 phần nhị phân theo thứ tự trong [manifest.json](manifest.json). Đây là các phần của cùng tệp, không phải 41 phiên bản workbook.

Để lấy lại workbook, tải repository bằng **Code → Download ZIP** hoặc clone repository, rồi chạy từ thư mục gốc:

```bash
python Farm/VID_01/source_archive/restore_source.py
```

Script chỉ ghép byte và kiểm tra từng phần cùng toàn bộ tệp; không mở Excel, không thực thi workbook, không sửa nội dung. Kết quả nằm tại `Farm/VID_01/VID_01_LTT_471_shots_CORRECTED_FINAL_v3.xlsm`.

SHA-256 của bản gốc và bản khôi phục:

```text
64ee4244b3a259b09a12ff0af67035aca323a393a15cd4567337f3822aa35a21
```

Bản văn bản để tra cứu ngay trên GitHub nằm ở [shot_analysis.csv](../shot_analysis.csv) và [ai_reconstruction.csv](../ai_reconstruction.csv). Hai CSV là dữ liệu trích xuất, không thay thế các ảnh và định dạng trong workbook nguồn.
