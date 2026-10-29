# Farm — Đặc tả nhiệm vụ và đầu ra cho 9 skill sản xuất

- Phiên bản: **1.0.0**.
- Ngày biên soạn: **29/10/2026**, giờ Việt Nam.
- Trạng thái: **đề xuất để xây skill Codex; chưa cài đặt hoặc chạy thử các skill**.
- Phạm vi: Kịch bản → kiểm chứng thực tế → mỹ thuật và tính liên tục → thiết kế quay → prompt → kiểm tra trước chạy → tạo video → kiểm tra thành phẩm → dựng.
- Đây là đề xuất tổ chức thực hiện, chưa thay thế các quyết định đã duyệt của Farm. Chín khâu là chín chức năng; một người hoặc một phiên Codex có thể đảm nhiệm nhiều chức năng.

## 1. Căn cứ và cách dùng

Đọc [AGENTS.md](../../AGENTS.md), [định hướng chính thức](../Dinh_huong_chinh_thuc.md), [hồ sơ khán giả](../Ho_so_khan_gia.md) và yêu cầu hiện hành trước khi làm. Giữ lời hứa thư giãn trong thế giới làng quê, ưu tiên Mỹ, chủ yếu không thoại, nhân vật và đời sống tiếp diễn. Người dùng phụ trách âm môi trường và nhạc. Công cụ dự kiến là Seedance 2.5 qua Dola; khả năng thực có của tài khoản cần được kiểm tra.

Đã đối chiếu FILM-KB hiện hành trên main: **1.3.1**, commit quan sát `ac1077c2444fc9351528da64ca109f0ba7869d28`. Các đường dẫn làm việc luôn trỏ main:

- [Hướng dẫn AI](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/00_HUONG_DAN_AI.md), [chuẩn phân tích](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/02_CHUAN_PHAN_TICH.md), [chuẩn quyết định](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/03_RA_QUYET_DINH.md).
- [Vận hành sản xuất](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/06_VAN_HANH_SAN_XUAT.md); các quy trình kịch bản, danh sách shot, câu lệnh AI và chẩn đoán lỗi trong `thu-vien/quy-trinh/`.
- Các mục đã đọc trực tiếp: **AI-002@1.0.0**, **AI-003@1.1.0**, **AI-010@1.3.0**, **AI-011@1.1.0**, **AI-013@1.1.0**, **QC-004@1.2.0**, **QC-010@1.3.0**.
- [Hồ sơ ứng dụng Farm](../Thu_vien_kien_thuc/ho-so-ngach.json), bản 1.4.0. Các giả thuyết biên tập vẫn là giả thuyết, không trở thành kết quả thử khán giả.

Khi xây skill, kiểm manifest core trên main lại một lần để phát hiện thay đổi. Ghi phiên bản thực đọc trong sản phẩm. Các tên skill, tệp và trường mới dưới đây là **hợp đồng đề xuất của quy trình Farm**, không phải các tính năng đã có của Codex hoặc Dola.

## 2. Quyền điều phối và điều kiện chuyển khâu

| Vai trò | Trách nhiệm và quyền |
| --- | --- |
| Chủ dự án — người dùng | Chốt định hướng, phạm vi, ngân sách, thay đổi lớn và bản được phát hành. Quyền đã cấp trong tác vụ tiếp tục có hiệu lực; không hỏi lại cho từng prompt hoặc thao tác trong phạm vi đó. |
| Đạo diễn | Chịu trách nhiệm sáng tạo xuyên suốt; nghiệm thu chuyên môn, chọn phương án trong phạm vi được giao, giải quyết xung đột giữa các bộ phận. Nếu chưa có người được giao vai này, Codex chỉ ghi đề nghị duyệt. |
| Bộ phận / skill thực hiện | Hoàn thành đầu ra đúng khâu; tự kiểm và ghi giới hạn; sửa phần thuộc trách nhiệm. |
| Bộ phận kiểm tra | Đối chiếu tiêu chí với bằng chứng, nêu lỗi và đề nghị chuyển khâu. Không tự giả lập phê duyệt của người dùng hoặc một người khác. |

Một phiên Codex có thể đổi vai tuần tự. Khi đó phải ghi `review_mode: self_review`; không mô tả đây là đánh giá độc lập. Việc dùng nhiều agent chỉ thực hiện khi có chỉ dẫn cho phép tương ứng; đặc tả này không tự yêu cầu tạo agent.

Các mốc cần quyết định của chủ dự án: brief và phạm vi đầu tư; phương án sản xuất trước khi tiêu credit; thay đổi vượt phạm vi đã duyệt; bản phát hành. Dùng lại ủy quyền còn hiệu lực, chỉ hỏi phần còn thiếu đang chặn công việc. Viết nháp, kiểm tài liệu và chuẩn bị gói chạy vẫn có thể tiếp tục khi chưa chốt chi phí tạo video.

### 2.1. Trạng thái dùng chung

Tách các chiều trạng thái để tránh nhầm “đã viết” với “đã chạy”:

| Trường | Giá trị và ý nghĩa |
| --- | --- |
| `work_status` | `draft`, `ready_for_review`, `needs_revision`, `blocked`, `complete`: tiến độ thực hiện. |
| `gate_status` | `not_checked`, `pass`, `fail`, `blocked`, `stale`: kết quả kiểm điều kiện chuyển khâu trên đúng đầu vào. |
| `approval_status` | `not_required`, `pending`, `approved`, `rejected`: quyết định của người có thẩm quyền, kèm phạm vi và bằng chứng ủy quyền/phê duyệt. |
| `execution_status` | `not_run`, `running`, `succeeded`, `failed`: thao tác thực thi, dùng khi có tạo, xử lý hoặc xuất tệp. |
| Trạng thái từng phép kiểm | `pass`, `fail`, `not_checked`, `not_applicable`; trường hợp không áp dụng phải có lý do. |

Chỉ chuyển sang thực thi khâu sau khi gate phụ thuộc đã `pass`, còn hiệu lực và có đủ quyền thực hiện. Khâu sau được chuẩn bị nháp từ dữ liệu tạm, nhưng phải gắn rõ phụ thuộc chưa đạt; không tiêu credit dựa trên bản nháp đó.

`complete` có nghĩa đã hoàn thành phạm vi ghi trong phiếu; không tự có nghĩa đủ quyền phát hành. Một tác vụ tạo video có thể `execution_status: succeeded` trong khi take đó không đạt kiểm tra chất lượng.

### 2.2. Mức lỗi và quy tắc nghiệm thu đề xuất

- **Critical:** sai người/vật bắt buộc, sai thao tác quyết định, mâu thuẫn thực tế làm sai nghĩa, tự đổi nội dung đã duyệt, đầu vào/đầu ra không truy nguyên, hoặc chạy khi thiếu quyền/chi phí. Chặn khâu bị ảnh hưởng.
- **Major:** thiếu góc cần dựng, sai liên tục quan trọng, ảnh đầu không khả thi, lỗi chuyển động/âm khiến việc không đọc được. Phải sửa hoặc có phương án thay thế đáp ứng cùng yêu cầu, được nghiệm thu.
- **Minor:** sai khác nhỏ không làm thay đổi nhận diện, hành động, thông tin hoặc điểm nối. Ghi rõ vị trí, ảnh hưởng và người chấp nhận trong phạm vi được giao.

Gate `pass` khi tất cả phép kiểm bắt buộc đã kiểm và đạt, không còn lỗi critical/major chưa giải quyết, đầu ra truy nguyên được, và lỗi minor còn lại đã được chấp nhận hợp lệ. Không cộng điểm hình đẹp để bù lỗi hành động. Không đặt “đạt 95%”, số lần tạo hay thời lượng cảnh cố định làm chuẩn chung.

### 2.3. Hợp đồng bàn giao cho mọi skill

Mỗi khâu bàn giao **tệp sản phẩm + phiếu kiểm + việc tiếp theo**. Phiếu có tối thiểu:

| Nhóm trường | Nội dung bắt buộc |
| --- | --- |
| Nhận diện | `episode_id`, `stage_id`, `item_ids`, `artifact_id`, `artifact_version`, `producer_role`, người/công cụ thực hiện. |
| Phụ thuộc | `input_refs`: đường dẫn/URI, ID, phiên bản và checksum nội dung đầu vào; commit khi phù hợp. |
| Ràng buộc | `protected_elements`, phạm vi đã duyệt, ngân sách/ủy quyền nếu có thực thi tốn phí. |
| Sản phẩm | `output_refs`: vị trí tệp thật, loại tệp, checksum; hoặc trạng thái chưa tạo cùng lý do. |
| Kiểm tra | `checks`: mã tiêu chí, kỳ vọng, kết quả, bằng chứng và phạm vi đã kiểm. |
| Vấn đề | `issues`: mức lỗi, item/timecode, triệu chứng, bằng chứng, khâu nhận sửa, cách kiểm lại. |
| Quyết định | Các trạng thái ở mục 2.1; người duyệt thực tế, `review_mode`, phạm vi quyền và bằng chứng quyết định. |
| Chuyển việc | `next_stage`, `blocked_items`, phần độc lập có thể tiếp tục, hành động cụ thể cần làm. |

Thông tin chưa biết dùng `null` và lý do; không điền giá trị giả để hoàn tất biểu mẫu. Mẫu và tình huống minh họa luôn ghi `synthetic`. Thời gian ghi đơn vị giây, khoảng `[start, end)` và trục nguồn; frame index phải có fps hoặc timestamp tương ứng. Không biến timecode của clip thành timecode của timeline mà thiếu ánh xạ.

Một ID/đường dẫn giữ một bản tài liệu hiện hành, cập nhật version tại chỗ; Git giữ lịch sử. Mỗi lần sinh thật có `run_id`/`take_id` riêng vì đó là sản phẩm khác nhau. Giữ file nguồn nguyên vẹn, liên kết checksum và không ghi đè take khác. Các tệp lớn dùng nơi lưu được hỗ trợ và manifest; không mặc định đưa toàn bộ video lên Git. Nhật ký thư viện/Farm dùng nhật ký chung hiện có, không tạo CHANGELOG riêng.

Khi đầu vào thay đổi, đánh dấu `stale` cho các gate phụ thuộc trực tiếp và gián tiếp, liệt kê phạm vi ảnh hưởng rồi kiểm lại. Giữ nguyên các sản phẩm đã tạo để truy nguyên; không tự xóa hay tạo lại cả tập. Một take cũ chỉ được dùng với đầu vào mới khi có kết quả đối chiếu mới.

### 2.4. Cấu trúc sản phẩm dự kiến cho một tập

Đây là quy ước đầu ra khi xây skill; tác vụ này chưa tạo tập phim mới:

```text
<thu-muc-tap>/
  brief.md
  script.json
  reality-check.json
  art-continuity.json
  shot-plan.json
  generation-requests.json
  preflight.json
  runs.json
  take-review.json
  edit-plan.json
  delivery.json
  gates.json
```

`script.json`, `shot-plan.json` và từng yêu cầu tạo sử dụng schema core tương ứng. Trường điều phối bổ sung đặt trong `gates.json` hoặc tệp liên quan, không tự thêm trường vào schema core có `additionalProperties: false`. `generation-requests.json` là mảng các đối tượng theo schema yêu cầu tạo. Markdown là bản đọc xuất từ dữ liệu khi cần, không duy trì hai nguồn nội dung độc lập.

## 3. Skill 01 — Kịch bản

**Tên đề xuất:** `farm-kich-ban`. **Chủ trách nhiệm:** biên kịch, dưới chỉ đạo của đạo diễn. **Kích hoạt:** viết hoặc sửa câu chuyện, phân đoạn, nhịp hành động của một tập Farm.

**Đầu vào:** brief; định hướng hiện hành; mục tiêu trải nghiệm; tài sản đã duyệt; nguồn tham chiếu đã chỉ định; các giới hạn thời lượng, phạm vi và chi phí đã có. Giới hạn chưa chốt được ghi là biến mở, không tự nhận là quyết định của người dùng.

**Nhiệm vụ:**

1. Viết trục tập: công việc gì, vì sao đáng theo, điều gì thay đổi, thành quả được dùng/chia sẻ thế nào.
2. Chia phân đoạn và nhịp: trạng thái đầu → hành động/tác động → trạng thái mới; ghi thông tin người xem nhận được.
3. Phân vai hình và âm, ghi lời thoại chỉ khi brief cho phép. Cho mỗi cảnh quan/đoạn nghỉ một chức năng cụ thể.
4. Đánh dấu chi tiết cần kiểm chứng thực tế, tài sản thiếu, hành động khó và khoảng thời gian được lược.
5. Soát mở đầu–thành quả–kết, sự tiếp diễn của thế giới và phần phải giữ khi sửa.

**Tiêu chí:**

- `KB-01`: mỗi nhịp có đóng góp về thông tin, hành động, quan hệ hoặc trải nghiệm; tránh lặp cùng thông tin vô cớ.
- `KB-02`: người xem có thể hiểu công việc và nhận ra thay đổi qua hình/âm; thành quả có nguyên nhân trong mạch kể.
- `KB-03`: kết và phần mở đầu phù hợp lời hứa đã chọn; không thêm xung đột mạnh trái định hướng chỉ để tạo chú ý.
- `KB-04`: danh tính, số người và phạm vi từng bài đúng yêu cầu. Bài thử chỉ cô gái/vườn không tự thêm bà; các tập khác vẫn giữ thế giới có bà theo brief.
- `KB-05`: cảm giác thư giãn là ý đồ cần thử; thời lượng là mục tiêu, không coi 3 giây/cảnh hay số cảnh của nguồn là định mức toàn dự án.

**Đầu ra:** `script.json` theo [script.schema.json](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/schema/script.schema.json), kèm danh sách câu hỏi kiểm chứng và phiếu gate 01. Có các ID phân đoạn/nhịp, chức năng, trạng thái, hình/âm, giả định, ràng buộc và tiêu chí kiểm. `viewer_tested` phản ánh dữ liệu thật.

**Điều kiện chuyển:** kịch bản rõ việc, đúng brief và các chỗ cần kiểm chứng được định vị. Gate này xác nhận đủ để kiểm chứng, chưa chứng nhận quy trình trồng/nấu đúng. Nếu brief mâu thuẫn, làm rõ đúng mâu thuẫn; phần nháp độc lập vẫn tiếp tục.

## 4. Skill 02 — Kiểm chứng thực tế

**Tên đề xuất:** `farm-kiem-chung-thuc-te`. **Chủ trách nhiệm:** nghiên cứu thực tế/chuyên môn. **Kích hoạt:** kiểm thao tác, nông sản, dụng cụ, mùa vụ, chế biến và các quan hệ nhân quả trong kịch bản.

**Đầu vào:** kịch bản và câu hỏi; bối cảnh địa lý/thời gian nếu cần; nguồn gốc; các phần đã được người dùng xác nhận. Kiểm sơ bộ có thể diễn ra ngay khi viết; đây là mốc kiểm chính thức trước thiết kế sản xuất.

**Nhiệm vụ:**

1. Tách những khẳng định có thể kiểm thành từng mục gắn beat/segment ID.
2. Đối chiếu nguồn đáng tin đúng vấn đề: tài liệu chuyên môn, hướng dẫn chính thức, người am hiểu hoặc video thao tác có thể quan sát.
3. Phân biệt quan sát trực tiếp, nguồn thuật lại, suy luận và phần chưa biết; ghi vị trí/mốc nguồn hỗ trợ đúng kết luận.
4. Kiểm thứ tự công đoạn, dụng cụ, tư thế, thời gian biến đổi, số lượng/trạng thái và chỗ lược cần tín hiệu.
5. Đề xuất chỉnh ít nhất phần cần thiết; khi phải đổi câu chuyện, trả biên kịch/đạo diễn quyết định.

**Tiêu chí:**

- `TT-01`: mọi chi tiết trọng yếu được kiểm có nguồn và kết luận đúng phạm vi; URL tồn tại riêng lẻ chưa đủ làm bằng chứng.
- `TT-02`: thao tác chủ đạo có tác nhân, điểm tiếp xúc/đỡ, đường đi và kết quả hợp lý; dụng cụ phù hợp công việc.
- `TT-03`: mùa vụ, vật liệu, thời gian và chuỗi chế biến không mâu thuẫn làm sai nội dung; khoảng chờ/lược được thiết kế rõ khi cần.
- `TT-04`: nguồn mâu thuẫn được ghi và xử lý; còn bất định trọng yếu thì chặn đúng cảnh, không tuyên bố đã kiểm xong cả tập.
- `TT-05`: lựa chọn hư cấu/thẩm mỹ được ghi riêng; quan sát AI tạo ra không được dùng làm nguồn chứng minh thao tác đời thực.

**Đầu ra:** `reality-check.json`, gồm mỗi mục: `claim_id`, beat liên quan, điều cần kiểm, nguồn/locator, loại bằng chứng, kết luận `supported|contradicted|uncertain`, lý do, ảnh hưởng và đề xuất sửa. Kèm gate 02 và danh sách điều bắt buộc giữ khi chuyển sang thiết kế.

**Điều kiện chuyển:** các vấn đề thực tế ảnh hưởng cảnh được giải quyết hoặc được thay bằng phương án phù hợp đã duyệt. Thiếu chuyên gia/nguồn cho chi tiết trọng yếu thì `blocked` cảnh đó; tiếp tục kiểm phần khác. Codex không tự nhận là chuyên gia đã nghiệm thu khi chỉ tổng hợp tài liệu.

## 5. Skill 03 — Mỹ thuật và tính liên tục

**Tên đề xuất:** `farm-my-thuat-lien-tuc`. **Chủ trách nhiệm:** mỹ thuật và giám sát liên tục. **Kích hoạt:** lập hồ sơ hình ảnh/thế giới, chuẩn bị ảnh tham chiếu/ảnh đầu và kiểm trạng thái nối giữa các cảnh.

**Đầu vào:** kịch bản đã sửa theo kiểm chứng; tài sản đã duyệt; quyền tham chiếu của mỗi ảnh; các thiết kế hiện hành của Farm.

**Nhiệm vụ:**

1. Cấp asset ID cho nhân vật, địa điểm, trang phục, dụng cụ và vật liệu cần theo dõi; ghi file, checksum, phiên bản, trạng thái duyệt.
2. Phân quyền tham chiếu: ảnh nào quyết định mặt, áo, không gian, dụng cụ, màu hay chuyển động; xử lý xung đột trước tạo.
3. Lập sơ đồ nhà–vườn–sân–bếp và các quan hệ cần giữ; thiết kế vật liệu, ánh sáng/màu theo bối cảnh.
4. Lập sổ trạng thái theo nhịp: vị trí, người giữ, lượng, mức hoàn tất, độ ướt/bẩn, tác nhân thay đổi; ghi cả đoạn che rồi lộ.
5. Đánh giá phần hình còn thiếu. Khi thiết kế quay chọn khung, quay lại khâu này để chuẩn bị/kiểm ảnh đầu cụ thể và cập nhật liên tục theo shot ID.

**Tiêu chí:**

- `MT-01`: tham chiếu dùng đúng vai trò, đúng file đã duyệt; biến thể mới có trạng thái riêng, không tự thay ảnh chuẩn.
- `MT-02`: nhận diện và thiết kế ổn định; trạng thái được phép đổi đúng tác động. Không khóa quả luôn khô khi cảnh yêu cầu rửa.
- `MT-03`: mỗi thay đổi quan trọng từ nhịp/cảnh trước sang sau có nguyên nhân hoặc khoảng lược rõ.
- `MT-04`: ảnh đầu có người/vật/dụng cụ và quan hệ khả thi; chi tiết nằm ngoài ảnh được ghi thiếu thay vì tự coi đã xác nhận.
- `MT-05`: thiết kế đủ thông tin phục vụ shot, không thêm chi tiết làm đổi thế giới đã duyệt.

**Đầu ra:** `art-continuity.json`: asset registry, reference authority, sơ đồ/ảnh thiết kế được liên kết, sổ trạng thái theo beat rồi theo shot, thuộc tính giữ/được đổi, vùng chưa biết và gate 03. Tệp hình có thật được lưu/liên kết với checksum; tệp chưa tạo phải ghi rõ.

**Điều kiện chuyển:** đủ thiết kế và trạng thái để lập bộ góc. Ảnh đầu theo shot có thể hoàn thiện sau khâu 04 nhưng phải được kiểm trước khâu 06. Mâu thuẫn thao tác trả khâu 02; mâu thuẫn câu chuyện trả khâu 01.

## 6. Skill 04 — Thiết kế quay

**Tên đề xuất:** `farm-thiet-ke-quay`. **Chủ trách nhiệm:** đạo diễn hình ảnh, phối hợp người dựng. **Kích hoạt:** chuyển nhịp kịch bản thành bộ shot có thể dựng và phù hợp sản xuất AI.

**Đầu vào:** kịch bản, kiểm chứng thực tế, mỹ thuật/liên tục, năng lực công cụ đã biết và giới hạn đã có.

**Nhiệm vụ:**

1. Chỉ ra bằng chứng khán giả cần thấy/nghe ở từng nhịp trước khi chọn góc máy.
2. Thiết kế cỡ/góc, bố cục, vùng nét, dàn cảnh, ánh sáng và chuyển động máy/chủ thể theo chức năng.
3. Viết trạng thái vào → pha tiếp xúc/biến đổi → trạng thái ra; chỉ ra điểm quan trọng phải nhìn được.
4. Chọn bộ góc tối thiểu đủ dựng; lập nối hướng nhìn, hướng chuyển động, không gian và trạng thái qua cut. Tạo cảnh dự phòng có lý do.
5. Tách shot trong bản dựng khỏi job tạo video; ghi thời lượng dựng mục tiêu, phần dư cần thiết và khả năng chia job.
6. Lập storyboard/animatic khi có công cụ và dữ liệu; nếu mới có bảng ảnh/thời gian, ghi đúng loại sản phẩm đó.

**Tiêu chí:**

- `QY-01`: mỗi shot liên kết với nhịp và có thông tin/chức năng rõ; bộ góc đủ để hiểu hành động quan trọng.
- `QY-02`: không để góc máy/che khuất làm mất bằng chứng tiếp xúc mà cảnh phải cho thấy; phần ngoài khung có thể lược khi mạch vẫn rõ.
- `QY-03`: hướng và trạng thái nối được; trường hợp đổi trục/nhảy thời gian có phương án giúp người xem định hướng.
- `QY-04`: thời lượng đủ cho hành động và điểm cắt dự kiến; ghi là thiết kế cho tới khi có take thật.
- `QY-05`: camera, ánh sáng và màu có mô tả thực hiện được; thông số máy thật chỉ là ý đồ khi chưa có công cụ/metadata bảo đảm.
- `QY-06`: đã xác định shot rủi ro để thử trước, tránh tạo hàng loạt trước khi biết cảnh quyết định có làm được hay không.

**Đầu ra:** `shot-plan.json` theo [shot-plan.schema.json](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/schema/shot-plan.schema.json); storyboard/animatic nếu thực sự đã tạo; mapping beat–shot–job và gate 04 trong phiếu điều phối. Mỗi shot có ID, trạng thái, hành động, góc/bố cục, hình–âm, tham chiếu, liên tục và acceptance checks.

**Điều kiện chuyển:** có bộ shot đủ dựng và tiêu chí cụ thể để viết prompt. Nếu cần đổi vị trí, đạo cụ hoặc ảnh đầu, trả khâu 03 để cập nhật; thay hành động quan trọng quay về kiểm chứng/kịch bản tương ứng.

## 7. Skill 05 — Prompt

**Tên đề xuất:** `farm-viet-prompt`. **Chủ trách nhiệm:** thiết kế yêu cầu tạo AI. **Kích hoạt:** viết hoặc sửa yêu cầu tạo theo shot và công cụ thực tế.

**Đầu vào:** shot plan, ảnh đầu/tham chiếu đúng bản, sổ liên tục, phần phải giữ, hồ sơ năng lực công cụ có bằng chứng và tiêu chí nghiệm thu.

**Nhiệm vụ:**

1. Tách ý đồ điện ảnh, nội dung/trạng thái, vai trò tham chiếu và thiết lập thực nhập vào dịch vụ.
2. Viết câu lệnh tập trung vào chủ thể, trạng thái đầu, hành động chính, tiếp xúc/đường đi, kết quả, camera và môi trường liên quan.
3. Kiểm câu chữ khớp ảnh đầu. Ảnh đã có tay kê quả thì yêu cầu tiếp tục kê/đỡ phù hợp, không đồng thời yêu cầu bắt đầu vươn tay từ xa.
4. Soạn bản để dán theo ngôn ngữ được chọn, kèm diễn giải tiếng Việt để rà ý; không mặc định tiếng Anh luôn tốt hơn.
5. Liệt kê ảnh nào nhập vào trường nào, thứ tự gì, thiết lập nào có thật; negative prompt/seed/ảnh cuối chỉ ghi như điều khiển khi đã xác minh được hỗ trợ.
6. Khi sửa, ghi lỗi cần giải, giả thuyết, biến đổi và phần giữ; không chỉ thêm nhiều tính từ chất lượng.

**Tiêu chí:**

- `PR-01`: không mâu thuẫn với ảnh đầu, shot plan và trạng thái vào/ra; bảo vệ đúng phần đã duyệt.
- `PR-02`: nội dung có hành động quan sát được, không chỉ “cinematic”, “vật lý hoàn hảo”, “chữa lành”.
- `PR-03`: tham số đã quan sát/thử được tách khỏi công bố tài liệu và điều chưa biết; thông số không hỗ trợ có phương án xử lý.
- `PR-04`: một job có mục tiêu thực hiện rõ; nhiều hành động/shot chỉ gộp khi công cụ và bài thử hỗ trợ cách đó.
- `PR-05`: thời lượng yêu cầu sinh và thời lượng dùng trong dựng được ghi riêng; ý định cắt 3 giây không biến thành cài đặt sinh 3 giây.
- `PR-06`: yêu cầu âm phù hợp brief; với trường hợp hiện hành, không tự thêm thoại/nhạc, ghi tiếng thao tác cần kiểm.

**Đầu ra:** `generation-requests.json`, mỗi mục theo [generation-request.schema.json](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/schema/generation-request.schema.json). Phiếu kèm mapping ID yêu cầu–shot–ảnh, checksum prompt/ảnh, ngôn ngữ, thiết lập, phần chưa hỗ trợ và gate 05. `tested` chỉ đổi khi có lượt thử thực phù hợp.

**Điều kiện chuyển:** gói prompt đủ để kiểm trước chạy. Đây chưa phải giấy phép chạy và chưa xác nhận video sẽ đạt. Thiếu cách điều khiển một ràng buộc then chốt thì chuyển thành bài thử nhỏ hoặc phương án chia việc, không hứa prompt khóa tuyệt đối.

## 8. Skill 06 — Kiểm tra trước chạy

**Tên đề xuất:** `farm-kiem-tra-truoc-chay`. **Chủ trách nhiệm:** kiểm tra sản xuất, đạo diễn giải quyết đánh đổi. **Kích hoạt:** trước lượt tạo tốn phí, trước chạy lô hoặc sau khi đầu vào/công cụ thay đổi.

**Đầu vào:** toàn bộ gói 01–05 đúng bản; file ảnh thật; giao diện/chế độ thật nếu tiếp cận được; chi phí và phạm vi đã được phép.

**Nhiệm vụ:**

1. Kiểm gate đầu vào, ID, file tồn tại/đọc được, checksum, số/thứ tự ảnh, ảnh nào là ảnh đầu/tham chiếu.
2. Xem ảnh đầu thực tế: đúng mặt/đồ/bối cảnh; tay nào giữ gì, tay nào rảnh, điểm đỡ, vùng cắt ảnh, đường đi và che khuất.
3. So chéo kịch bản–thực tế–liên tục–shot–prompt để tìm mâu thuẫn trước khi tiêu credit.
4. Xác minh dịch vụ/chế độ và các trường cần nhập; phân biệt tài liệu quảng bá với tính năng của tài khoản đang dùng.
5. Kiểm phạm vi ủy quyền, hạn mức credit/chi phí, số job, quy tắc dừng và bài thử rủi ro. Chưa biết giá thì ghi chưa biết, không tự điền giá tiền.
6. Chốt danh sách job được chạy cùng checksum gói; tách job bị chặn khỏi các job độc lập đủ điều kiện.

**Tiêu chí:**

- `PC-01`: không còn lỗi critical/major ở gói đầu vào; các gate phụ thuộc đang có hiệu lực.
- `PC-02`: ảnh đầu khả thi về cơ thể, dụng cụ, tiếp xúc và đường đi; chỉnh prompt không được dùng để bỏ qua lỗi ảnh đầu.
- `PC-03`: model/chế độ, số ảnh và thiết lập cần thiết đủ bằng chứng sử dụng; điều chưa biết chỉ được thử trong job thăm dò có phạm vi rõ.
- `PC-04`: có quyền thực hiện và giới hạn chi phí/lượt chạy phù hợp. Tận dụng quyền hiện có, chỉ hỏi phần thiếu thực sự chặn việc.
- `PC-05`: có tiêu chí kiểm sản phẩm và đường sửa khi thất bại; job chạy lại không trùng một job đang chờ xử lý.

**Đầu ra:** `preflight.json` theo từng request/job: snapshot/checksum đầu vào, checklist, lỗi, job đủ điều kiện, job bị chặn, hạn mức, căn cứ ủy quyền, điều kiện dừng và gate 06. Chỉ job `pass` với quyền hợp lệ mới được nộp chạy.

**Điều kiện chuyển:** gói được kiểm đúng bản và đủ quyền. Thiếu công cụ truy cập Dola thì hoàn thành phần kiểm tĩnh, ghi phần giao diện `not_checked`, bàn giao gói thao tác cho người thực hiện; không báo `pass` toàn gói hoặc đã nộp job. Có thể duyệt riêng job thăm dò chỉ để xác minh giao diện/năng lực nếu được phép.

## 9. Skill 07 — Tạo video

**Tên đề xuất:** `farm-tao-video`. **Chủ trách nhiệm:** vận hành sản xuất AI. **Kích hoạt:** nộp job đã qua preflight, nhận kết quả hoặc nhập take do người dùng chạy.

**Đầu vào:** các job `pass` còn hiệu lực, tài khoản/công cụ được hỗ trợ, ủy quyền phù hợp, hạn mức và nơi lưu kết quả.

**Nhiệm vụ:**

1. Kiểm lại checksum gói trước nộp. Dùng đúng dịch vụ, ảnh, prompt, thiết lập và phạm vi đã duyệt.
2. Ghi `run_id`, job ID từ dịch vụ nếu có, thời điểm, người/công cụ vận hành, model/chế độ thực, đầu vào và thiết lập thực.
3. Theo dõi trạng thái, kiểm job hiện có trước retry để tránh tạo trùng/tính phí hai lần.
4. Nhận tệp, kiểm file mở được, đo metadata, lưu take nguyên gốc và checksum. Ghi credit/chi phí thực nếu có; chưa có thì `null`.
5. Với mỗi lần tạo lại, ghi nguyên nhân/giả thuyết; dừng theo hạn mức đã có hoặc khi cần quyết định thay phương án.
6. Nếu Codex không có tích hợp/browser phù hợp, cung cấp gói thao tác cụ thể cho người dùng; sau khi nhận tệp và thông tin chạy thì nhập manifest với đúng provenance.

**Tiêu chí:**

- `TV-01`: mọi take truy được về đúng request, ảnh/prompt và cấu hình đã nộp; trường không quan sát được phải ghi chưa biết.
- `TV-02`: tệp thực tồn tại, đọc được, có thời lượng/kích thước/fps hoặc timestamp đo từ file; không lấy thời lượng yêu cầu thay thời lượng đầu ra.
- `TV-03`: giữ nguyên nguồn, không ghi đè, không tự đổi model/nội dung hoặc vượt hạn mức; mọi lần chạy đều được tính vào thống kê thực.
- `TV-04`: phân biệt chờ chạy, lỗi dịch vụ, đã nhận tệp và take đạt chất lượng. Nộp thành công chưa có nghĩa đạt hình/chuyển động.

**Đầu ra:** `runs.json`, tệp video nguyên gốc hoặc URI truy cập được kèm checksum; request/run/take mapping; metadata đo; trạng thái job; đầu vào thực; credit/chi phí/thời gian; lỗi thực thi. Gate 07 xác nhận bàn giao tệp đủ để kiểm, không xác nhận chất lượng nội dung.

**Điều kiện chuyển:** có take thật đọc được để khâu 08 kiểm. Khi không có khả năng thao tác dịch vụ, ghi `execution_status: not_run` và điểm chặn chính xác; giữ gói chạy sẵn sàng. Không tự tạo API, nút giao diện, seed hoặc job ID giả.

## 10. Skill 08 — Kiểm tra thành phẩm từng take và chuỗi

**Tên đề xuất:** `farm-kiem-tra-thanh-pham`. **Chủ trách nhiệm:** giám sát liên tục/QC; đạo diễn nghiệm thu chuyên môn. **Kích hoạt:** khi có take thật, sau sửa hình hoặc cần chọn đoạn đưa vào dựng.

**Đầu vào:** video thật; manifest/checksum; request/shot/tiêu chí; sổ liên tục; các take liền kề khi đã có.

**Nhiệm vụ:**

1. Xác định khả năng xem/nghe của công cụ. Đo metadata và kiểm file; xem toàn take tốc độ thường khi có phương tiện phù hợp, sau đó rà chậm/frame ở mốc rủi ro.
2. Kiểm riêng vẻ hình, nhận diện/ổn định theo thời gian, chuyển động, đúng hành động/vật lý, liên tục và âm; ghi khoảng thực đã kiểm.
3. Rà tiếp xúc–chuyển lực–nhả, số lượng qua che/lộ, dụng cụ, vật liệu, nền, bóng và phản chiếu theo yêu cầu của shot.
4. Chọn khoảng dùng được theo source timecode, điểm vào/ra, phần dư và trạng thái đầu/cuối; đối chiếu với take liền kề.
5. Phân loại dùng được toàn take, dùng được một phần, sửa hậu kỳ hoặc tạo lại. Chỉ giữ phần đáp ứng chức năng, không cắt mất bằng chứng bắt buộc để che lỗi.
6. Trả lỗi về khâu có nguyên nhân phù hợp: ảnh đầu, prompt, thiết kế quay, thao tác thực tế, vận hành hay dựng; đánh dấu đó là giả thuyết cho tới khi kiểm lại.

**Tiêu chí:**

- `TP-01`: đúng nhân vật, vật và số lượng cần giữ trong toàn khoảng dự định sử dụng; khác biệt hợp lý do hành động/ánh sáng được phân biệt với lỗi.
- `TP-02`: hành động bắt buộc thực sự xảy ra đúng thứ tự và đọc được; video đứng yên/mượt nhưng không làm việc vẫn chưa đạt.
- `TP-03`: không còn lỗi hình học, xuyên/treo/nhân đôi, trôi vân hoặc flicker gây sai nghĩa hay phá trải nghiệm trong khoảng chọn.
- `TP-04`: trạng thái ra nối được với shot tiếp; chưa có shot tiếp thì ghi đánh giá liên tục chuỗi chưa hoàn tất.
- `TP-05`: âm được nghe và đối chiếu nếu kết luận đồng bộ. Hình đạt/âm sai có thể giao hình cùng chỉ dẫn bỏ/thay âm, đúng phạm vi người dùng phụ trách.
- `TP-06`: báo cáo phân biệt ảnh mẫu, khoảng chuyển động và khoảng âm đã tiếp cận. Metadata/ảnh trích không chứng nhận đã xem toàn chuyển động hoặc đã nghe.

**Đầu ra:** `take-review.json`: take ID/checksum, từng phép kiểm và evidence span, lỗi/timecode, khoảng được dùng, trạng thái vào/ra, âm dùng/bỏ/chưa kiểm, kết luận `accept|accept_range|repair|regenerate|blocked`, khâu sửa và gate 08 theo take/đoạn. Nếu kết luận bị giới hạn bởi khả năng xem/nghe, ghi rõ phạm vi chưa kiểm; đoạn chưa đủ kiểm không được coi là đã đạt toàn bộ.

**Điều kiện chuyển:** dựng chính thức dùng các khoảng đã được nghiệm thu đúng phạm vi. Dựng nháp có thể dùng placeholder gắn nhãn rõ; không trộn placeholder vào bản giao như clip đã đạt. Sau upscale, nội suy, sửa vùng hoặc ghép phải kiểm lại phần chịu tác động.

## 11. Skill 09 — Dựng và bàn giao

**Tên đề xuất:** `farm-dung-phim`. **Chủ trách nhiệm:** dựng phim/hoàn thiện hình; phối hợp người dùng về âm và đạo diễn về tổng thể. **Kích hoạt:** dựng sơ, dựng nội dung, hoàn thiện hoặc xuất bản giao từ các take đã kiểm.

**Đầu vào:** kịch bản/shot plan hiện hành; khoảng take được dùng; gate 08; kế hoạch hình–âm; tài sản âm có thật nếu được cung cấp; thông số bản giao được chọn.

**Nhiệm vụ:**

1. Lập timeline theo thông tin và tiến trình công việc; chọn điểm cắt, phần lược, khoảng nghỉ và cơ hội nhận thành quả.
2. Kiểm cả ba quy mô: take, chuỗi, toàn phim. Phát hiện cảnh thiếu và yêu cầu đúng bộ phận tạo bổ sung.
3. Quản lý ánh xạ timeline → take → source in/out; giữ fps/timebase rõ, không đổi tốc độ làm sai hành động đã duyệt.
4. Phối hợp với người dùng về tiếng thao tác, môi trường và nhạc; phân biệt âm tạm với âm cuối; kiểm đồng bộ, chuyển nền và mức âm.
5. Cân màu/sáng giữa các cảnh, xử lý cục bộ có kiểm, chốt hình rồi hoàn thiện; thay đổi lớn sau khóa hình phải ghi tác động.
6. Xuất bằng công cụ thực có; mở lại tệp xuất để kiểm hình/âm, đầu–cuối, khung đen, file lỗi và đoạn cần thiết. Gửi đạo diễn nghiệm thu, chủ dự án quyết định phát hành.

**Tiêu chí:**

- `DG-01`: người xem theo được người/vật/công việc qua cut; không ghép các take đạt riêng lẻ thành chuỗi sai trạng thái.
- `DG-02`: nhịp phục vụ ý đồ thư giãn và tiến trình; đoạn nghỉ có chức năng, thành quả được nhìn/dùng/nhận theo kịch bản. Đây là đánh giá biên tập, chưa là phản hồi khán giả.
- `DG-03`: không làm mất bước/bằng chứng quan trọng để che lỗi; khoảng lược không tạo hiểu sai công việc.
- `DG-04`: hình và âm đúng phạm vi yêu cầu; không có nhạc/thoại phát sinh trái brief. Chưa có âm cuối thì chỉ bàn giao bản khóa hình/nháp và ghi âm còn thiếu.
- `DG-05`: thông số file được chọn theo mục đích và khả năng nguồn. Resolution, fps, codec, audio sample rate và mục tiêu loudness/true peak nếu dùng phải ghi rõ; không tự upscale hay gán 24 fps/-14 LUFS thành chuẩn mọi tập.
- `DG-06`: tệp xuất thực được mở/kiểm lại. Nếu công cụ chỉ làm được kế hoạch dựng/EDL, bàn giao đúng loại đó và ghi bước dựng/xuất chưa thực hiện.
- `DG-07`: bản cuối chỉ `ready_for_release` khi đủ hình/âm, kiểm bản xuất đã đạt và có nghiệm thu theo quyền được giao. Trạng thái đã phát hành cần bằng chứng thao tác phát hành riêng.

**Đầu ra:** `edit-plan.json` chứa timeline/EDL và ánh xạ nguồn; project dựng nếu công cụ hỗ trợ; master thật khi đã xuất; `delivery.json` chứa vị trí/checksum, metadata, phiên bản nội dung, phạm vi kiểm hình/âm, lỗi còn lại và quyết định nghiệm thu. Gate 09 ghi rõ `rough_cut|picture_lock|master` là loại bản giao, cùng trạng thái duyệt/phát hành tách biệt.

**Điều kiện hoàn tất:** giao đúng loại sản phẩm người dùng yêu cầu, có bằng chứng kiểm tương ứng. Lỗi bản dựng/bản xuất đi qua lượt kiểm của khâu 08 trên đúng file rồi quay lại khâu 09 để sửa; không kết thúc quy trình ở việc xuất file thành công. Phát hành chỉ khi người dùng đã cho phép.

## 12. Cách trả lỗi và bảo vệ phần đã đạt

| Hiện tượng | Khâu cần điều tra/sửa trước | Phần cần giữ |
| --- | --- | --- |
| Thành quả xuất hiện nhưng thiếu nguyên nhân trong câu chuyện | 01; phối hợp 02 nếu liên quan quy trình thật | Nhân vật, định hướng và các nhịp đã có chức năng. |
| Trình tự chế biến hoặc dụng cụ sai | 02 → 01/03/04 theo phạm vi | Tài sản và cảnh không bị ảnh hưởng. |
| Đổi mặt, áo, kiến trúc hoặc trạng thái vật | 03; đối chiếu đầu vào thực ở 07 | Hành động, nhịp và hình đạt ngoài vùng lỗi. |
| Góc quay không thấy tiếp xúc cần chứng minh | 04 → 03/05 | Mục tiêu hành động và không gian đã duyệt. |
| Prompt yêu cầu khác tư thế ảnh đầu | 05 hoặc 03 sau kiểm 06 | Tham chiếu đúng và phần câu lệnh không mâu thuẫn. |
| Tạo đúng gói nhưng liên tục lỗi cùng pha khó | 03/04/05 theo giả thuyết, thử có giới hạn ở 07 | Ràng buộc nội dung, chi phí và kết quả đã dùng được. |
| Take đúng hình nhưng có nhạc/âm sai | 08 → 09, phối hợp người dùng làm âm | Phần hình đạt, nếu âm có thể thay mà vẫn đúng yêu cầu. |
| Clip đạt riêng nhưng nối sai trong timeline | 09; quay 03/04 khi thiếu thông tin | Các source range đã đạt nếu vẫn phù hợp. |
| File master sai màu/âm/timebase so với timeline | 09 → kiểm lại 08 | Nguồn gốc và lựa chọn dựng đã duyệt. |

Mỗi yêu cầu sửa có: lỗi và bằng chứng → giả thuyết nguyên nhân → thay đổi đề nghị → phần phải giữ → tiêu chí kiểm lại → phạm vi phụ thuộc cần làm mới. Không tự chạy lại cả chuỗi khi chỉ một cảnh bị ảnh hưởng.

## 13. Ví dụ xuyên suốt — cắt một quả vàng khỏi cành

**Ví dụ thiết kế từ bài thử S05 hiện có; chưa có take Dola để nghiệm thu.**

| Khâu | Quyết định/đầu ra kỳ vọng |
| --- | --- |
| 01 | Nhịp chuyển từ quả còn trên cây sang quả đã thu hoạch; cần thấy cô gái làm chủ công việc. |
| 02 | Kiểm thao tác kéo cắt cuống và tay đỡ; thông tin loài quả chưa rõ phải giữ giới hạn, không tự đổi thành táo hoặc xác nhận kỹ thuật theo loài. |
| 03 | Cùng một quả, rổ và nhân vật; cuống nguyên trước cắt, cuống ngắn sau cắt; ảnh đầu có tay đỡ và kéo đúng vị trí. |
| 04 | Góc cận đủ đọc lưỡi kéo–cuống–tay đỡ; đường nối sang cảnh đặt quả vào rổ. |
| 05 | Yêu cầu khép kéo cắt cuống một lần, quả được tay đỡ; giữ nhận diện, hình quả và hướng máy. |
| 06 | Xem ảnh thật để xác nhận kéo ôm cuống, không ôm vỏ; kiểm số tay, điểm đỡ, khả năng công cụ và quyền chạy. |
| 07 | Lưu take thật, cấu hình/đầu vào và metadata; số giây dùng được còn chờ kiểm. |
| 08 | Xem diễn tiến chạm–cắt–tách, không cắt vào vỏ, không tự rơi/nhân đôi; ghi khoảng dùng được và điểm nối. |
| 09 | Giữ bằng chứng cắt cần thiết, nối quả đã tách vào cảnh hạ quả; đồng bộ tiếng kéo khi có âm đạt. |

Nếu ảnh đẹp nhưng kéo chỉ đóng trong không khí rồi quả tự tách, tiêu chí hành động chưa đạt. Nếu hình đạt mà tiếng kéo lệch, có thể giữ hình và giao sửa âm đúng phạm vi.

## 14. Chuyển đặc tả thành skill Codex

Khi người dùng yêu cầu xây/cài đặt, dùng chín tên ở trên làm chín gói skill, với frontmatter `name` và `description` nêu đúng lúc kích hoạt. Mỗi `SKILL.md` cần ngắn, đọc thêm hợp đồng chung và tài liệu chuyên môn theo nhu cầu. Đường dẫn tới hợp đồng phải được đóng gói hoặc giải quyết theo vị trí cài thực tế, không giả định đường dẫn tương đối từ repo sang thư mục skill luôn đúng.

Mỗi skill có tám phần thực thi:

1. Mục tiêu và tình huống dùng.
2. Đọc chỉ dẫn hiện hành, kiểm đầu vào và phụ thuộc.
3. Nhiệm vụ theo thứ tự, phần được tự quyết và quyền đã có.
4. Cách kiểm cụ thể gắn với mã tiêu chí trong tài liệu này.
5. Mẫu sản phẩm, schema và phiếu gate.
6. Cách xử lý dữ liệu thiếu, công cụ thiếu, nguồn mâu thuẫn và trạng thái chưa kiểm.
7. Trả lỗi đúng khâu, giữ phần đạt, làm mới gate phụ thuộc.
8. Báo cáo ngắn: đã làm gì, đầu ra ở đâu, kiểm gì, còn vướng gì, bước tiếp theo.

Nếu cần điều phối, trước hết dùng một manifest quy trình chứa thứ tự/phụ thuộc và trạng thái. Chưa cần thêm vai sáng tạo mới. Việc gọi skill, dùng tác vụ tuần tự hay agent song song phải theo khả năng thực của Codex và chỉ dẫn hiện hành.

### Bộ tình huống nghiệm thu hành vi khi xây skill

Các ca dưới đây là **tiêu chuẩn thử sau khi xây**, chưa phải kết quả đã chạy:

| Ca | Tình huống đưa vào | Hành vi phải thấy |
| --- | --- | --- |
| T01 — kịch bản | Brief không thoại nhưng mẫu nguồn có lời thuyết minh | Giữ brief, chuyển thông tin sang hình/âm phù hợp; không chép thoại mặc định. |
| T02 — thực tế | Chưa rõ loại quả, nguồn hướng dẫn chỉ dành cho loài khác | Ghi chưa chắc đúng phần, tìm nguồn phù hợp hoặc chặn kết luận đó; không xác nhận thao tác theo loài. |
| T03 — liên tục | Vật đi sau tay rồi xuất hiện với số lượng khác | Phát hiện cần kiểm qua che/lộ; không coi đầu/cuối đẹp là đủ. |
| T04 — quay | Cận đẹp nhưng không thấy pha tiếp xúc bắt buộc | Đề xuất đổi góc/dàn cảnh hoặc bổ sung góc đúng chức năng; giữ mục tiêu thao tác. |
| T05 — prompt | Ảnh đầu đã kê quả, yêu cầu lại bắt đầu vươn tay từ xa | Nêu mâu thuẫn và sửa đúng ảnh hoặc câu lệnh theo phần đã duyệt. |
| T06 — preflight | Có prompt nhưng ảnh sai checksum, hoặc quyền chạy chưa bao phủ chi phí | Chặn đúng job, không tiêu credit; hoàn tất phần kiểm độc lập. |
| T07 — tạo | Không có công cụ Dola; hoặc job đang pending bị yêu cầu retry | Giao gói thao tác/kiểm job hiện có; không bịa đã tạo và không nộp trùng. |
| T08 — QC | Chỉ có vài ảnh trích hoặc công cụ không nghe được audio | Báo đúng độ phủ; không xác nhận toàn chuyển động/âm; nêu phần cần người/công cụ kiểm. |
| T09 — dựng | Hai take đạt riêng nhưng vật đổi trạng thái qua cut | Phát hiện lỗi chuỗi, sửa điểm cắt/coverage; không dùng nhạc để coi mạch đã đạt. |
| T10 — phụ thuộc | Prompt/ảnh được sửa sau khi preflight pass | Đánh dấu gate liên quan stale, yêu cầu kiểm lại đúng gói trước chạy. |
| T11 — quyền duyệt | Codex tự viết và tự rà nhưng không có người duyệt khác | Ghi self_review; không tự điền tên người dùng vào phê duyệt. |
| T12 — bản giao | Xuất file thành công nhưng chưa kiểm lại hình/âm hoặc thiếu âm cuối | Ghi đúng loại bản nháp/khóa hình và phần chưa kiểm; chưa đề nghị phát hành như master hoàn chỉnh. |

Khi nghiệm thu skill, ghi từng ca đã chạy, sản phẩm nhận được, kết quả và giới hạn. Kiểm cấu trúc/schema chỉ chứng minh dữ liệu hợp lệ; khả năng xem video, thao tác Dola, chất lượng hình–âm và phản hồi người xem cần bằng chứng riêng.

## 15. Phạm vi đã hoàn thành của tài liệu này

Đã biên soạn hợp đồng bàn giao chung, nhiệm vụ/tiêu chí/đầu ra của chín khâu, quyền quyết định, vòng sửa lỗi và tình huống thử. Chưa tạo hoặc cài `SKILL.md`, chưa thực thi ca thử hành vi, chưa chạy Dola, chưa tạo tập phim và chưa có số liệu khán giả. Các chuẩn nghiệm thu đề xuất cần áp dụng thử vào một đoạn đại diện trước khi mở rộng sản xuất.
