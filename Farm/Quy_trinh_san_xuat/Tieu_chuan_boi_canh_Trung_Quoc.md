# Farm — Tiêu chuẩn bối cảnh Trung Quốc và tính đúng mùa

- Phiên bản: **1.1.0**; cập nhật **29/10/2026**, giờ Việt Nam.
- Yêu cầu đã xác nhận: **nông thôn Vân Nam, Trung Quốc**; vật dụng, màu sắc, hành động, cảnh quan và sinh hoạt phù hợp bối cảnh địa phương; kiểm soát theo mùa; lấy video **Lý Tử Thất làm ý tưởng và hướng tới motif/concept tương tự**.
- Phần đề xuất triển khai: hồ sơ, trường dữ liệu, mã kiểm và cách bàn giao trong tài liệu này. Chưa cài skill, chưa xác minh một vùng cụ thể hoặc nghiệm thu ảnh/video hiện có.
- Đọc cùng [định hướng chính thức](../Dinh_huong_chinh_thuc.md) và [đặc tả chín skill](Dac_ta_skill_doan_phim.md). Đây là lớp tiêu chuẩn bắt buộc dùng chung, không thêm một khâu độc lập sau khi đã tạo xong video.

## 1. Mục tiêu kiểm soát

Mỗi shot phải thuộc về **một nơi sống tại Vân Nam, Trung Quốc, trong một thời kỳ và một giai đoạn mùa xác định đủ cho nội dung đang kể**. Hình đẹp, mái ngói, tre, đèn lồng hoặc dòng chữ “Chinese countryside” không tự chứng minh điều đó.

Kiểm theo quan hệ: **địa phương/khí hậu → thời gian/mùa → cảnh quan và nông sản → nhà cửa và vật dụng → trang phục và hành động → ánh sáng/màu → liên tục giữa các shot**. Các bằng chứng phải cùng hỗ trợ một thế giới sống được, thay vì gom những dấu hiệu được cho là “Á Đông”.

Một vật dụng dùng chung nhiều nước vẫn có thể phù hợp với đời sống địa phương Trung Quốc. Tiêu chí là sự phù hợp có căn cứ với hồ sơ đã chọn, không phải vật nào cũng phải có nguồn gốc độc quyền Trung Quốc. Không suy quốc gia của một chiếc rổ hoặc dân tộc của nhân vật chỉ từ vẻ ngoài.

## 2. Hồ sơ bối cảnh bắt buộc trước sản xuất

Khâu 01–03 cùng lập `world-profile.json`. Bản đầu có thể còn biến mở để nghiên cứu; trước chạy chính thức phải giải quyết các biến ảnh hưởng trực tiếp đến job đó. Chỉ ghi “Trung Quốc, mùa xuân” có thể chưa đủ khi cảnh phụ thuộc khí hậu, loại cây hoặc phong tục riêng.

| Trường / nhóm | Nội dung cần ghi |
| --- | --- |
| Nhận diện | `profile_id`, `version`, `country: CN`, `province: Yunnan`, yêu cầu người dùng và căn cứ quyết định; Vân Nam là phần đã chốt. |
| Địa phương | Tiểu vùng/làng mẫu tại Vân Nam hoặc phạm vi tham chiếu đủ cụ thể; địa hình, độ cao/khí hậu khi cần. Không tự chốt tên làng thật cho một làng hư cấu hoặc mặc định một tiểu vùng đại diện toàn tỉnh. |
| Thời kỳ | Hiện đại, giai đoạn lịch sử hoặc đời sống đương đại giữ nghề truyền thống; mức hiện diện của điện, nhựa, kim loại, máy móc theo brief và nguồn. Chưa chọn thì để mở. |
| Văn hóa | Sinh hoạt/ẩm thực/nghề của địa phương, phong tục có dùng trong câu chuyện; nhóm văn hóa cụ thể chỉ ghi khi có nguồn và lựa chọn phù hợp. |
| Lịch tập | Mùa, giai đoạn trong mùa, khoảng tháng nếu có căn cứ, giờ trong ngày, thời tiết; lịch dương/âm/tiết khí phải ghi rõ loại lịch nếu sử dụng. |
| Sinh thái và mùa vụ | Loài/giống cây khi cần, giai đoạn trồng–ra hoa–đậu quả–thu hoạch–bảo quản; vật nuôi và trạng thái cảnh quan liên quan. |
| Không gian | Địa hình, cây nền, đường, tường/rào, mái/cửa, nhà–sân–vườn–bếp, vật liệu và sơ đồ quan hệ cố định. |
| Đời sống và đạo cụ | Dụng cụ, bếp, đồ chứa, đồ ăn/uống, bàn ghế, trang phục theo việc và thời tiết; thiết kế, chất liệu, cách sử dụng. |
| Màu và ánh sáng | Màu có vật mang: tường/đá/gỗ, lá, đất, nước, nông sản, áo, món ăn; nguồn/hướng sáng, bề mặt ướt/khô và giới hạn chỉnh màu. |
| Tham chiếu | ID, URI/file, checksum, tác giả/nguồn khi biết, địa điểm/thời gian có bằng chứng, phạm vi hỗ trợ, quyền tham chiếu và trạng thái duyệt. |
| Giới hạn | Phần đã xác minh, suy luận, thiết kế và chưa biết; chi tiết không phù hợp hoặc cần kiểm thêm, cùng lý do. |

Không bắt điền độ cao, ngày chính xác hoặc thông số khí hậu nếu không cần cho quyết định. Mọi giá trị chưa biết dùng `null` kèm lý do; không bịa để đủ hồ sơ. Một tập có nhiều mùa dùng một lịch nhiều giai đoạn và các liên kết chuyển thời gian, không ép một mùa cho cả tập.

Tham chiếu ảnh AI dùng để truyền thiết kế; nguồn thực địa/tài liệu chuyên môn dùng để kiểm xác thực. Một ảnh AI đã được chọn không tự là chứng cứ văn hóa đúng. Với tài sản hiện có, thêm kết quả đối chiếu vào manifest/hồ sơ, giữ file gốc và quyền tham chiếu của nó.

## 3. Tiêu chuẩn theo từng nhóm nội dung

| Nhóm | Cần kiểm trong thiết kế và đầu ra | Dấu hiệu cần điều tra |
| --- | --- | --- |
| Kiến trúc và làng quê | Kiểu mái/cửa/tường, vật liệu, sân, bếp, đường, hàng rào và quan hệ với địa hình của vùng/thời kỳ đã chọn. | Cùng căn nhà đổi ngôn ngữ thiết kế giữa các góc; ghép các phong cách vùng khác nhau mà không có căn cứ trong hồ sơ. |
| Vật dụng | Kiểu dáng/chất liệu/công năng của rổ, thúng, dao, kéo, cuốc, đồ gốm, nồi/chảo, đồ dùng bàn ăn; cách cầm và sử dụng. | Đúng hình thức trang trí nhưng dùng sai việc; một đạo cụ tự đổi thiết kế; vật hiện đại xuất hiện trái thời kỳ/brief. |
| Trang phục | Nhân vật, công việc, thời tiết, mức độ ướt/bẩn và sự tiếp diễn; chi tiết trang phục có nguồn nếu mang ý nghĩa địa phương. | Tự chuyển thành cổ trang, trang phục nghi lễ hoặc thay mặt đã duyệt chỉ để tăng cảm giác “Trung Quốc”. |
| Hành động và sinh hoạt | Trình tự trồng/thu/chế biến, nhóm dụng cụ, cách bảo quản, chuẩn bị bữa ăn, trao/nhận và tương tác gia đình đúng bối cảnh chọn. | Dùng một phong tục như chuẩn cho toàn quốc; đưa nghi lễ hoặc động tác biểu tượng vào cảnh thường ngày không có lý do. |
| Nông sản và thực vật | Loài/giống khi cần, trạng thái sinh trưởng, nguồn nguyên liệu, khả năng trồng/thu tại vùng và mùa; cây nền cũng được kiểm. | Hoa, quả chín và lá nền trái lịch đã xác minh; nguyên liệu tươi được ngầm coi là vừa thu dù thực tế câu chuyện dùng hàng dự trữ. |
| Thời tiết và bề mặt | Mưa/nắng, sương, tuyết nếu có căn cứ, đất ẩm, nước, mái/sân, quần áo và hoạt động tương ứng. | Mưa vừa dứt nhưng mọi vật tự khô ngay; tuyết chỉ được thêm để tượng trưng mùa đông dù không có căn cứ địa phương. |
| Màu sắc | Màu vật liệu và sinh học theo thời điểm; ánh sáng có nguyên nhân; giữ màu nhận diện và trạng thái khi cân màu. | Cả mùa thu bị tô vàng/cam, mọi mùa đông bị xanh lạnh; dùng đỏ/đèn lồng mặc định để “Trung Quốc hóa” toàn khung. |
| Chữ và biểu tượng | Chữ nhìn thấy phải đúng nội dung, dạng chữ, vị trí, vùng/thời kỳ; biển hiệu, nhãn, câu đối và vật nghi lễ chỉ dùng khi hợp cảnh. | Chữ giả, ký tự bị biến dạng, biển/biểu tượng không được giải thích trong hồ sơ. Không tự biến mọi chữ ngoài Hán tự thành lỗi nếu thực tế bối cảnh cho phép. |
| Âm khi có trong phạm vi | Tiếng thao tác đúng vật liệu/công cụ; môi trường phù hợp cảnh; nhạc do người dùng chọn, phối hợp đúng định hướng. | Âm gợi một nơi/mùa/hoạt động khác với hình; tự thêm nhạc “phong cách Trung Quốc” để thay thế kiểm bối cảnh. |

Một yếu tố giống phong cách của nước/vùng khác là **đầu mối kiểm**, không tự là kết luận loại bỏ. Đối chiếu cụ thể với bộ tham chiếu địa phương và chức năng của yếu tố đó; nếu đúng với đời sống đã chọn, ghi căn cứ để giữ.

## 4. Kiểm theo mùa và lịch câu chuyện

Đây là bảng câu hỏi kiểm, **không phải lịch nông vụ đã xác minh cho mọi vùng Trung Quốc**:

| Giai đoạn | Những quan hệ phải kiểm |
| --- | --- |
| Xuân | Trạng thái chồi/lá/hoa đúng loài và địa phương; gieo/trồng/thu thực tế; độ ẩm, thời tiết và áo quần phù hợp giai đoạn. Không mặc định mọi cây đều nở hoa. |
| Hạ | Mức phát triển cây/quả, mưa/nắng, sinh hoạt ngoài trời, che nắng và bảo quản nguyên liệu theo điều kiện cụ thể; không tự coi mọi vụ thu đều vào mùa hè. |
| Thu | Loại cây/giống đến kỳ thu, hoạt động sơ chế/phơi/cất nếu hợp nguồn; lá đổi màu theo loài/khí hậu, không tô vàng toàn bộ cây nền. |
| Đông | Cây thường xanh/rụng lá, độ lạnh, hoạt động bếp và nguồn nguyên liệu tươi/dự trữ; tuyết/băng/sương giá cần căn cứ, không thêm như quy tắc bắt buộc. |
| Chuyển mùa hoặc nhiều tháng | Có thời gian trôi được thiết kế; cây, ruộng/vườn, thời tiết, trang phục, lượng dự trữ và công việc tiến triển đồng bộ; nhà/đạo cụ giữ nhận diện. |

Lịch mùa vụ phải gắn với vùng, giống, giai đoạn và điều kiện canh tác. Nhà kính, nguyên liệu mua, sấy/ướp hoặc dự trữ là khả năng cần kiểm và thể hiện đúng nguồn gốc trong câu chuyện; không tự viện dẫn chúng để hợp thức hóa một lỗi sau khi tạo.

Ngày lễ/âm lịch/tiết khí không tự đồng nghĩa thời tiết chính xác. Nếu câu chuyện dùng mốc lịch, kiểm năm và quan hệ với địa phương khi cần. Không tự thêm Tết, đèn lồng hoặc nghi lễ chỉ vì đoạn đang ở mùa đông.

## 5. Phiếu bối cảnh cho từng shot

`shot-context.json` là bảng bổ sung theo `shot_id`, không sửa cấu trúc schema core. Mỗi hàng có:

1. `shot_id`, `world_profile_ref` gồm ID/phiên bản/checksum; beat/sequence và giai đoạn lịch đang dùng.
2. Vị trí cụ thể, giờ/thời tiết; các cảnh trước/sau liên quan.
3. Asset ID và trạng thái của kiến trúc, cảnh quan/cây nền, đạo cụ, trang phục, nguyên liệu và món ăn thực sự nhìn thấy.
4. Hành động và các yêu cầu văn hóa/đời sống cần đúng; phần nào có thể dùng chung, phần nào đặc thù địa phương.
5. Màu chủ đạo có vật mang, quan hệ sáng/bóng, vật ướt/khô và thay đổi được phép.
6. `required_visible_features`: dấu hiệu cụ thể cần có trong khung; `incompatible_features`: chi tiết trái hồ sơ kèm lý do. Không cần nhồi dấu hiệu nhận diện quốc gia vào mọi shot cận.
7. `evidence_refs`, dữ liệu thiếu và `context_check_ids` áp dụng; có lý do cho mục không áp dụng.
8. Kết quả kiểm ảnh đầu, kiểm take và kiểm điểm nối là các phép kiểm riêng, kèm file/checksum, vị trí/timecode và người/công cụ thực hiện.

Mỗi tiêu chí chỉ đánh giá phần có thể kiểm: cận tay không thấy mái nhà thì ghi kiến trúc không hiện trong khung và kế thừa hồ sơ địa điểm, không bịa đã quan sát mái. Các checklist nhìn thấy phải bao phủ cả tiền cảnh, nhân vật/hành động và hậu cảnh khi chúng xuất hiện.

## 6. Mười hai tiêu chí dùng chung

| Mã | Điều kiện đạt | Bộ phận dẫn kiểm |
| --- | --- | --- |
| **CN-01** | Hồ sơ giữ đúng **Vân Nam, Trung Quốc** và đủ tiểu vùng/thời kỳ/giai đoạn mùa cho cảnh; biến chưa biết không làm vô hiệu kết luận được đưa ra. | Kịch bản + kiểm chứng. |
| **CN-02** | Kiến trúc, vật liệu, địa hình và quan hệ nhà–sân–vườn phù hợp hồ sơ và giữ liên tục ở các góc. | Mỹ thuật. |
| **CN-03** | Vật dụng đúng thiết kế, vật liệu, công năng và cách dùng có căn cứ trong đời sống vùng/thời kỳ đó. | Kiểm chứng + mỹ thuật. |
| **CN-04** | Trang phục phù hợp việc, thời tiết và nhân vật; giữ tham chiếu đã duyệt; không tự áp cổ trang/nghi lễ. | Mỹ thuật. |
| **CN-05** | Hành động lao động, chế biến, ăn uống và tương tác văn hóa phù hợp ngữ cảnh; chi tiết đặc thù có nguồn, không khái quát cho toàn Trung Quốc. | Kiểm chứng. |
| **CN-06** | Cây, giống/giai đoạn khi cần, nông sản và nguồn nguyên liệu phù hợp địa phương–mùa–lịch truyện; cảnh nền cũng được rà. | Kiểm chứng + mỹ thuật. |
| **CN-07** | Thời tiết, đất/nước/bề mặt, phục trang và hoạt động nhất quán; biến đổi có tác nhân hoặc khoảng thời gian hợp lý. | Liên tục + QC. |
| **CN-08** | Màu và ánh sáng xuất phát từ vật liệu, cây, thời tiết và thời điểm; grade không làm sai nhận diện mùa hoặc bản chất món/nguyên liệu. | Mỹ thuật + hình ảnh + dựng. |
| **CN-09** | Chữ/biểu tượng nhìn thấy được đối chiếu nội dung, hình dạng và tính phù hợp; không có dấu hiệu trang trí sai bối cảnh chưa giải quyết. | Mỹ thuật + QC. |
| **CN-10** | Mỗi điểm nối giữ đúng địa điểm/giai đoạn hoặc thể hiện chuyển thời gian hợp lý; các thay đổi theo mùa đồng bộ với tiến trình công việc. | Liên tục + dựng. |
| **CN-11** | Âm thuộc phạm vi nghiệm thu phù hợp vật liệu, môi trường và hành động; phần chưa nghe hoặc chờ người dùng làm âm được ghi đúng trạng thái. | Âm thanh + QC. |
| **CN-12** | Ảnh, prompt, hồ sơ và take dùng đúng bản; xung đột văn hóa/mùa với ảnh đã duyệt có phiếu xử lý, giữ nguồn và không tự thay tài sản. | Preflight + vận hành + QC. |

Mỗi phép kiểm ghi kỳ vọng cụ thể từ hồ sơ, kết quả `pass|fail|not_checked|not_applicable`, nguồn/evidence, mức lỗi và phạm vi sửa. Tất cả mục bắt buộc áp dụng phải đạt mới chuyển khâu tương ứng. Một cảnh đúng vật lý nhưng sai địa phương/mùa vẫn chưa đạt bối cảnh.

## 7. Phân công xuyên suốt chín khâu

| Khâu | Nhiệm vụ bổ sung | Sản phẩm/điều kiện phải bàn giao |
| --- | --- | --- |
| 01 — Kịch bản | Đặt nơi sống tại Vân Nam; gắn lịch mùa và nguồn nguyên liệu với công việc, gia đình và thành quả; lập concept/motif từ video tham chiếu đã chọn. | Brief và lịch tập; câu hỏi tiểu vùng/thời kỳ/mùa; mapping nhịp–giai đoạn và bản đối chiếu tham chiếu. |
| 02 — Kiểm chứng | Xác minh chi tiết địa phương, công năng vật dụng, thao tác/sinh hoạt và mùa vụ; phân biệt nguồn thật với ảnh tạo. | Bằng chứng cho world profile và CN-01/03/05/06; danh sách mâu thuẫn/chưa biết. |
| 03 — Mỹ thuật/liên tục | Xây bộ thiết kế kiến trúc–đạo cụ–áo–cây–màu theo vùng và mùa; giữ asset ID, sổ trạng thái. | `world-profile.json`, ảnh chuẩn/thiết kế có thật và `shot-context.json` phần mỹ thuật. |
| 04 — Thiết kế quay | Chọn khung thấy đủ thông tin công việc và môi trường cần thiết; giữ bối cảnh cả ngoài hành động chính. | Mapping shot với phiếu bối cảnh và dấu hiệu cần thấy; kế hoạch nối/chuyển mùa. |
| 05 — Prompt | Chuyển hồ sơ thành chi tiết nhìn thấy/hành động đúng shot, dùng tham chiếu thực; giữ lịch và vật liệu. | Gói tạo gắn world profile và shot-context, điều kiện giữ/loại có lý do. “Chinese rural” riêng lẻ chưa đủ. |
| 06 — Preflight | So ảnh đầu thật với vùng/mùa, tiền–trung–hậu cảnh, prompt và quyền tham chiếu; xử lý thiếu hồ sơ ảnh hưởng cảnh. | Kết quả CN áp dụng trên đúng gói; job sai/thiếu dữ liệu thiết yếu chưa được chạy chính thức. |
| 07 — Tạo video | Giữ nguyên gói đã kiểm, ghi đúng profile/ảnh/prompt thực dùng; không đổi đạo cụ/mùa để dễ sinh. | Run/take manifest truy ngược profile; file thật để kiểm. Chưa kết luận chất lượng văn hóa. |
| 08 — Kiểm thành phẩm | So diễn tiến thật với hồ sơ, rà cả nền và che/lộ; đánh dấu sai vùng, đồ, màu, sinh hoạt hoặc mùa theo thời gian. | Kết quả CN trên take/source range; lỗi/timecode và khâu sửa. |
| 09 — Dựng | Rà địa lý–mùa vụ qua cut, cảnh chuyển mùa và màu/âm; kiểm master sau grade/ghép. | Biên bản bối cảnh toàn chuỗi/toàn phim, ánh xạ shot–giai đoạn, kết quả bản xuất. |

## 8. Cách viết yêu cầu tạo và kiểm trước chạy

Gói tạo diễn đạt theo cấu trúc sau; đây là mẫu ý đồ, không phải cú pháp hoặc tham số Dola đã xác minh:

> Địa điểm và giai đoạn lấy từ hồ sơ [profile ID]; ảnh tham chiếu [asset ID] có quyền quyết định [thuộc tính]. Trong shot này thấy [chi tiết đã kiểm]. Nhân vật dùng [dụng cụ] thực hiện [hành động] từ [trạng thái đầu] tới [trạng thái cuối]. Cây/nền, trang phục, bề mặt và ánh sáng giữ đúng [giai đoạn]. Giữ [phần đã duyệt]; xử lý [chi tiết không tương thích có căn cứ] bằng [phương án].

Phần không xuất hiện trong khung chỉ giữ ở metadata/phụ thuộc, tránh prompt quá tải. Negative prompt hoặc field khóa vùng/mùa chỉ dùng như điều khiển khi công cụ thật có hỗ trợ. Chữ “authentic”, tên tỉnh hoặc mã màu không bảo đảm đầu ra đúng; ảnh đầu và video phải được kiểm riêng.

Nếu ảnh chuẩn có điểm chưa khớp với hồ sơ mới: chỉ rõ vùng ảnh/asset, yêu cầu mâu thuẫn và phương án bảo vệ phần đạt. Giải quyết ở thiết kế trước chạy; không ghi đè ảnh người dùng đã duyệt hoặc tự thay nhân vật. Không coi toàn bộ bộ thử 30 giây đã đạt lớp tiêu chuẩn mới khi chưa đối chiếu.

## 9. Mức lỗi và xử lý

- **Critical:** đổi quốc gia/thế giới hoặc địa phương đã chốt ngoài phạm vi; thay tài sản đã duyệt trái quyền; cảnh trọng tâm có hành động/văn hóa/mùa sai làm thay nghĩa tập. Chặn sản phẩm bị ảnh hưởng.
- **Major:** kiến trúc/đạo cụ/trang phục/cây hoặc thời tiết mâu thuẫn rõ với hồ sơ; pha đổi mùa không được giải thích; màu hậu kỳ làm sai nhận diện trạng thái/mùa. Sửa hoặc thay bằng phương án được nghiệm thu trước dùng chính thức.
- **Minor:** sai khác không làm thay đổi nơi chốn, thời kỳ, mùa, công việc hoặc nhận diện, có căn cứ chấp nhận trong phạm vi được giao. Ghi rõ người chấp nhận và ảnh hưởng.

Thiếu bằng chứng là `not_checked`/`blocked` đúng mục, không tự thành `fail` về sự thật cũng không thành `pass`. Căn cứ chưa đủ thì tiếp tục nghiên cứu/thiết kế phần độc lập. Màu đẹp, nhạc hay hoặc nhãn “phong cách Lý Tử Thất” không bù được lỗi bối cảnh bắt buộc.

Đạo diễn nghiệm thu tính thống nhất toàn phim; kiểm chứng và mỹ thuật chịu trách nhiệm hồ sơ/bằng chứng; QC báo lỗi trên sản phẩm thật. Người dùng chốt thay đổi lớn, đầu tư và phát hành theo quyền hiện hành.

## 10. Tình huống thử bổ sung khi xây skill

Đây là các ca giả lập để kiểm hành vi, chưa phải kết quả thử:

| Ca | Đầu vào giả lập | Hành vi đúng |
| --- | --- | --- |
| T13 | Dự án đã chốt Vân Nam nhưng một tài liệu/ảnh mẫu mặc định tỉnh khác | Giữ Vân Nam; chỉ tiểu vùng còn mở. Đối chiếu chi tiết và điều chỉnh theo hồ sơ, không đổi tỉnh theo nguồn mẫu. |
| T14 | Nhà, bếp và đạo cụ lấy từ nhiều nguồn khác vùng nhưng chưa có căn cứ cùng xuất hiện | Kiểm nguồn và tính tương thích cụ thể, lập bộ thống nhất; không đánh đồng là đều Trung Quốc nên tự đạt. |
| T15 | Hai shot liền hành động có mưa/đất ướt rồi khô ngay không có thời gian trôi | Ghi lỗi liên tục mùa/thời tiết và sửa đúng thiết kế hoặc take. |
| T16 | Cây nền và nông sản trái lịch địa phương đã xác minh | Chặn mục mâu thuẫn, kiểm nguồn nguyên liệu/giai đoạn; không tự thêm nhà kính hoặc hàng mua để chữa lời kể. |
| T17 | Áp màu vàng cho toàn cảnh thu hoặc thêm tuyết vào đông không có căn cứ | Trả về palette vật liệu và dữ liệu địa phương; không coi biểu tượng bốn mùa là lịch thật. |
| T18 | Shot cận rổ tre dùng chung nhiều nước, không thấy kiến trúc | Kiểm thiết kế/công năng với hồ sơ; không kết luận sai quốc gia chỉ vì vật không độc quyền Trung Quốc; ghi đúng phạm vi quan sát. |
| T19 | Ảnh đã duyệt xuất hiện chi tiết mâu thuẫn lớp bối cảnh mới | Giữ file gốc, lập phiếu xung đột và phương án; không tự thay mặt/vườn hoặc báo đã đạt văn hóa. |
| T20 | Từng take đúng mùa nhưng dựng ghép nhảy mùa không có quan hệ thời gian | Kiểm CN-10 ở chuỗi/master, sửa timeline/chuyển thời gian và kiểm lại sau grade. |

## 11. Phần cần tiếp tục xác định theo tập

**Vân Nam, Trung Quốc** và mục tiêu motif/concept tương tự video Lý Tử Thất đã được người dùng xác nhận. Tiểu vùng/làng mẫu, thời kỳ, mùa/giai đoạn của từng tập, giống cây, bộ ảnh có nguồn và palette tương ứng còn cần nghiên cứu/lựa chọn khi triển khai. Không hỏi lại tỉnh đã chốt; chỉ làm rõ chi tiết thực sự chặn cảnh cụ thể. Tài liệu này chưa chọn một tiểu vùng, lịch bốn mùa, bản sắc dân tộc hoặc thay đổi bộ nhân vật/bối cảnh đã duyệt.

## 12. Học motif và concept từ Lý Tử Thất, triển khai trong thế giới Vân Nam

### 12.1. Hai lớp phải cùng đạt

1. **Lớp concept/motif:** xác định điều muốn học từ tập nguồn — ý tưởng trung tâm, vòng công việc, sự biến đổi sản vật, cách cho thấy năng lực/thành quả, quan hệ gia đình, nhịp nghỉ–làm–nhận kết quả và các hình ảnh/hành động được lặp có chức năng. Đây là những nội dung cần đọc từ nguồn cụ thể hoặc ghi là thiết kế đề xuất; chưa quan sát thì chưa báo là đặc điểm của tập đó.
2. **Lớp bối cảnh thực hiện:** thể hiện ý tưởng bằng nhân vật và tài sản Farm, với nhà–vườn–bếp, vật dụng, nguyên liệu, sinh hoạt, ánh sáng và mùa phù hợp Vân Nam. Chi tiết nào dùng chung có căn cứ thì giữ; chi tiết nào mâu thuẫn phải điều chỉnh có lý do và giữ chức năng cảnh.

Theo lựa chọn hiện hành, tập đầu vẫn ưu tiên giữ gần trình tự tham chiếu để học làm; các tập sau nâng cấp/sáng tạo hơn. Nếu điều chỉnh theo thực tế Vân Nam buộc đổi phần đã chốt của trình tự hay nội dung, ghi rõ tác động và xử lý theo quyền hiện có. Không tự bỏ lựa chọn giữ gần trình tự hoặc tự chuyển cả thế giới sang địa phương của nguồn.

### 12.2. Bản đối chiếu nguồn → concept/motif → cảnh Farm

Tạo `reference-adaptation.json` theo tập. Đây là hợp đồng dữ liệu đề xuất của Farm, không phải schema core đã có. Có phần concept/motif toàn tập và các hàng theo chuỗi/nhịp/shot:

| Nhóm | Cần ghi |
| --- | --- |
| Nguồn và độ phủ | Video/asset ID, bản nguồn/checksum khi có, URL và locator/timecode; đã xem hình, nghe âm hay chỉ đọc báo cáo/ảnh; phần chưa kiểm. |
| Ý tưởng tập | Concept nguồn được quan sát/thuật lại/diễn giải, concept Farm lựa chọn, mục tiêu trải nghiệm và phần người dùng đã chốt. |
| Motif | Hình ảnh/hành động/âm hoặc quan hệ trở lại có chức năng gì, xuất hiện ở đâu, dự kiến biến đổi/được trả kết quả thế nào trong Farm. Một chủ đề chung chưa tự là motif lặp. |
| Chức năng nguồn | Chuỗi/shot nguồn cho thấy điều gì, vì sao cần trong mạch; bằng chứng hay giả thuyết về chức năng được ghi đúng loại. |
| Chuyển sang Farm | Beat/shot ID, phần giữ về concept/motif/trình tự, phần đổi sang Vân Nam và lý do; liên kết world profile và shot-context. |
| Kiểm thực tế | Kiến trúc, đồ dùng, thao tác, món/nguyên liệu, mùa vụ hoặc biểu tượng cần đối chiếu; nguồn kiểm địa phương và kết quả. |
| Nghiệm thu | Dấu hiệu phải thấy/nghe, phần đã duyệt cần giữ, đánh đổi, trạng thái quyết định và bằng chứng sản phẩm thật khi đã có. |

Không dùng bảng này để tuyên bố đã xem toàn bộ một tập từ shot list hoặc ảnh trích. Không tự gán tỷ lệ giống, cảm xúc người xem hoặc ý đồ tác giả như dữ kiện đã đo. Mức tương đồng được mô tả bằng các lựa chọn cụ thể có thể kiểm, đồng thời tuân thủ CN-01 đến CN-12.

### 12.3. Trách nhiệm bổ sung cho chín khâu

- **01:** lập concept tập và đường đi motif; mapping nhịp/trình tự với nguồn đã chọn, ghi rõ phần giữ/điều chỉnh.
- **02:** đối chiếu từng chi tiết phụ thuộc địa phương/mùa với Vân Nam; ghi mâu thuẫn và phương án thực tế.
- **03:** xây asset/không gian/đạo cụ/palette thực hiện được concept tại Vân Nam, giữ bộ nhân vật đã duyệt.
- **04:** chuyển chức năng cảnh nguồn thành bộ góc Farm đọc được hành động, chất liệu, tiến trình và thành quả; ghi lựa chọn giống/đổi cùng lý do.
- **05:** prompt mô tả nội dung và hành động cụ thể từ bản đối chiếu; tên Lý Tử Thất riêng lẻ không thay nội dung, ảnh đầu hoặc bộ tham chiếu.
- **06:** so nguồn → bản đối chiếu → hồ sơ Vân Nam → ảnh/prompt; chặn mâu thuẫn nội dung/văn hóa/mùa còn ảnh hưởng job.
- **07:** chạy đúng gói, liên kết run/take với bản đối chiếu và profile đã dùng; không sửa ý tưởng hoặc tỉnh trong lúc vận hành.
- **08:** kiểm take thực hiện đúng chức năng shot và giữ motif/phần phải giữ; đồng thời kiểm bối cảnh Vân Nam trên vùng nhìn/nghe được.
- **09:** nghiệm thu concept/motif ở cấp chuỗi/toàn tập: tiến trình rõ, motif có chỗ trở lại/biến đổi phù hợp thiết kế, thành quả và quan hệ được thể hiện; hình–âm không phá bối cảnh/mùa. Nhận xét biên tập chưa phải kết quả khán giả.

### 12.4. Ca nghiệm thu bổ sung

| Ca | Đầu vào giả lập | Hành vi đúng |
| --- | --- | --- |
| T21 | Concept từ tập nguồn được giữ nhưng một công đoạn/đạo cụ chưa được xác minh cho Vân Nam | Giữ chức năng/ý tưởng đã chọn, kiểm chi tiết địa phương rồi giữ hoặc điều chỉnh có căn cứ; không tự coi nguồn là chứng nhận Vân Nam. |
| T22 | Prompt chỉ ghi “giống Lý Tử Thất, Vân Nam” nhưng thiếu hành động, vật liệu và điểm nối | Trả về concept/motif, world profile và shot plan để viết yêu cầu cụ thể; chưa coi đủ điều kiện chạy. |
| T23 | Các take riêng đẹp nhưng motif hoặc tiến trình đã duyệt mất trong bản dựng | Định vị phần thiếu ở timeline, sửa cấu trúc/coverage đúng phạm vi; kiểm lại cả concept và CN, không chấm giống bằng vẻ ảnh đơn lẻ. |
