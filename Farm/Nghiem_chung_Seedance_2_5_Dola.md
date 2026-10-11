# Farm — Bài nghiệm chứng Seedance 2.5 qua Dola
- Phiên bản: **0.1 — chuẩn bị thử, chưa có kết quả**.
- Ngày: **12/10/2026**, theo giờ Việt Nam.
- Dựa trên [Định hướng chính thức](Dinh_huong_chinh_thuc.md).
- Mục đích: kiểm tra hình trông như camera thật, thao tác có tiếp xúc/trọng lượng, tính liền mạch giữa các cảnh, tương tác với bà và khả năng giữ âm thao tác.
- Đây là bài thử kỹ thuật ngắn, không phải kịch bản tập đầu đã được người dùng duyệt.

## 1. Vì sao thử hai cách

**A:** tạo sáu đoạn riêng, mỗi đoạn mục tiêu 5 giây, rồi ghép theo thứ tự.

**B:** tạo một đoạn mục tiêu 30 giây chứa đúng sáu cảnh và cùng chuỗi công việc.

Cả hai dùng cùng tạo hình, trang phục, nơi chốn, nông sản, đồ vật, hướng sáng và trạng thái. So sánh lượng hình dùng được và công sức sửa thay vì chỉ số giây mô hình sinh ra.

Một lượt A + B tương đương bảy yêu cầu tạo, mục tiêu tổng 60 giây đầu ra. Số này chỉ là quy mô thử đề xuất, không phải số lần tạo đã chạy hay hạn mức tài khoản. Nếu Dola không cho chọn đúng độ dài, ghi cả độ dài yêu cầu và độ dài thực nhận; không coi phép so sánh là đã kiểm soát đủ.

Đầu tiên chỉ chạy **T02** một lần để kiểm tra thao tác hái quả. Sau khi xem kết quả mới quyết định có cần sửa ảnh/prompt trước khi làm các cảnh còn lại. Không lập lại nhiều lần một prompt chưa hiểu lỗi.

## 2. Thông tin công cụ đã đối chiếu

[Trang Seedance 2.5 của ByteDance](https://seed.bytedance.com/en/seedance2_5) công bố tạo hình/âm thanh đồng thời và đoạn tối đa 30 giây, đồng thời dẫn “Try Dola”. [Bài giới thiệu chính thức](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) mô tả tham chiếu nhiều ảnh và kiểm soát theo mốc thời gian, đồng thời thừa nhận còn hạn chế với chuyển động phức tạp và tương tác nhiều chủ thể.

Đây là năng lực công bố của mô hình, không phải chứng minh bộ cảnh Farm đạt yêu cầu. Trang Dola công khai hiện chuyển tới https://www.dola.com/chat/ nhưng không cung cấp nội dung giao diện đọc được qua công cụ tra cứu. Vì vậy chưa xác minh các nút, số ảnh cho phép hoặc cài đặt có trong tài khoản của người dùng. Hướng dẫn dưới đây không tự đặt tên các nút chưa quan sát.

## 3. Chuẩn bị ảnh — bước quyết định trước khi tạo video

Dùng đúng bộ tham chiếu của người dùng:
1. Cô gái: mặt, cơ thể, tóc và một bộ trang phục cho toàn bài thử.
2. Bà: ảnh tham chiếu riêng, nếu dùng cảnh hai người.
3. Bối cảnh: vườn, khu rửa, bếp và bàn ăn thuộc cùng một thế giới; không trộn vị trí cửa, mái hoặc vật dụng từ các bản khác.
4. Đồ vật và nông sản: cùng rổ, chậu, dao, thớt, nồi, bát ở các cảnh cần tiếp nối.

Từ các ảnh master đó tạo **sáu ảnh đầu cảnh**, mỗi ảnh chỉ thể hiện một khung hình hoàn chỉnh, một góc nhìn và trạng thái trước hành động. Bảng nhiều góc của nhân vật dùng làm tham chiếu để tạo ảnh; không mặc định dùng nguyên một bảng nhiều ô làm ảnh đầu của cảnh đơn, vì mô hình có thể giữ bố cục nhiều ô.

Đề xuất khung ngang **16:9**. Ảnh cần rõ vùng tay/dụng cụ/vật chịu tác động khi cảnh có thao tác. Không ép ảnh mềm, da nhẵn hoặc xóa nền đến mức mất quan hệ không gian.

**Nông sản thử đề xuất: táo.** Lý do là có thể theo dõi quả nguyên → rửa → cắt → miếng trong nồi → bát thành phẩm. Đây là vật liệu kiểm tra hình/chuyển động, chưa chốt cây trồng hay món ăn cho tập đầu và không gán táo cho một vùng/mùa thực tế nào của dự án. Có thể thay bằng nông sản người dùng chọn, nhưng phải sửa đồng bộ cả ảnh, trạng thái và prompt.

Trạng thái bộ ảnh trong lần chuẩn bị này: **chưa được xác nhận/đính kèm vào bài thử**. Không tự dùng ảnh Lý Tử Thất làm ảnh nhân vật của Farm.

## 4. Sáu cảnh và điều cần quan sát

| Mã | Ảnh trước hành động | Hành động trong 5 giây | Trạng thái kết thúc | Kiểm tra chính |
|---|---|---|---|---|
| T01 | Vườn có táo chín, lá xanh, các lớp gần–xa; không có người | Lá và cành nhỏ lay nhẹ trong gió | Bố cục, cây, quả và ánh sáng ổn định | Lá/quả không biến dạng; màu xanh tự nhiên; cảm giác nơi chốn |
| T02 | Cô gái trước cành; một quả còn gắn vào cuống; rổ trong tầm với | Đỡ quả, xoay nhẹ/tách cuống, đặt vào rổ | Quả ở trong rổ; vị trí cũ trên cành đã trống | Mặt, tay, tiếp xúc, cuống, lực và đường đi của quả |
| T03 | Rổ vài quả táo ở trên chậu nước; tay giữ rổ | Nghiêng rổ, táo rơi xuống chậu với nước bắn nhẹ | Táo nằm/nổi trong chậu; rổ nhẹ hơn | Quỹ đạo, va chạm, nước và âm đổ |
| T04 | Một táo nguyên trên thớt; tay giữ an toàn; dao sẵn để cắt | Một lần cắt qua quả | Hai phần táo nằm trên thớt, mặt cắt nhìn rõ | Dao có tiếp xúc; vật tách theo đường cắt; tay/vật không xuyên nhau |
| T05 | Nồi chứa miếng táo đã qua thời gian đun; muỗng gỗ trong tay | Khuấy chậm một vòng trong nồi sôi nhẹ | Miếng vẫn cùng loại, chỉ đổi vị trí; hơi nước đi lên | Vật liệu, trọng lượng, muỗng, hơi và nước sôi |
| T06 | Cô gái và bà cạnh bàn; cô gái cầm bát táo đã chế biến | Cô gái đặt bát trước bà; bà nhìn bát rồi mỉm cười nhẹ | Bát trên bàn; hai người thư thái | Hai khuôn mặt ổn định; đặt bát có trọng lượng; tương tác tự nhiên |

T04 → T05 có lược thời gian chế biến; không diễn tả táo chín tức thì trong năm giây. Bài thử chỉ có cô gái và bà để đọc rõ tương tác. Chó/mèo, nhiều khách và các việc như cuốc/vót tre sẽ được thử riêng sau khi có kết quả, không cùng lúc tăng mọi độ khó.

## 5. Thao tác trên Dola

1. Mở chức năng tạo video trong Dola mà người dùng đang sử dụng; xác nhận đúng **Seedance 2.5** theo thông tin giao diện nếu có.
2. Với cách A, đưa **ảnh đầu cảnh tương ứng** vào chức năng tạo video từ ảnh. Nếu giao diện cho thêm ảnh tham chiếu, gán rõ vai trò mặt/trang phục/bối cảnh; ảnh đầu vẫn phải là đúng cảnh đang làm.
3. Chọn 16:9 và 5 giây nếu có các lựa chọn đó. Nếu độ dài tự động, ghi lại và yêu cầu độ dài trong prompt.
4. Nếu có lựa chọn tạo âm thanh, bật để thử tiếng thao tác; prompt yêu cầu không thoại, không nhạc. Nếu không có tùy chọn, vẫn có thể thử prompt nhưng phải kiểm video có audio thật hay không.
5. Tạo T02 trước bằng prompt ở dưới. Xem ở tốc độ bình thường, rồi xem chậm vùng tay–quả–rổ.
6. Giữ ảnh, prompt và video gốc. Ghi kết quả trước khi thay đổi.
7. Khi T02 có đoạn dùng được, tạo các cảnh còn lại. Cách B chỉ chạy khi có thể cung cấp đủ ảnh/tham chiếu để giữ cùng tạo hình và thế giới; nếu giới hạn đầu vào khác A, ghi rõ và không diễn giải chênh lệch chỉ do độ dài 30 giây.

Chưa có hướng dẫn nút bấm chi tiết đã xác minh cho tài khoản Dola này. Nếu giao diện không khớp các bước tổng quát, cần xem ảnh giao diện hiện tại để điều chỉnh, không chuyển qua dịch vụ khác khi người dùng chưa chọn.

## 6. Prompt cho từng đoạn riêng — cách A

Các prompt dưới đây là tiếng Việt. “Ảnh tham chiếu” là **ảnh đầu đúng mã cảnh đã chuẩn bị**, không phải một ảnh bất kỳ. Khi giao diện có ký hiệu tham chiếu riêng, dùng đúng ký hiệu nó cấp; không giả định cú pháp @Image bắt buộc ở Dola.

### T01 — Không gian vườn, 5 giây

Tạo một video ngang 16:9 dài 5 giây từ ảnh tham chiếu. Giữ nguyên bố cục, các cây, vị trí quả táo, lớp lá gần máy và vùng cây phía xa. Một cảnh toàn ổn định như camera thật đặt trên chân máy trong vườn. Gió nhẹ làm lá và những cành nhỏ lay chậm; các quả vẫn bám cuống, không thay kích thước hay mọc thêm. Ánh sáng tự nhiên cùng hướng như ảnh, chi tiết lá và bề mặt quả rõ vừa phải, sắc xanh tươi có nhiều mức sáng tối. Không tự di chuyển máy, không chuyển cảnh, không làm bóng nhựa hoặc xóa mờ toàn khung. Chỉ tiếng lá và gió nhẹ, chim xa nhỏ; không lời nói, không nhạc, không chữ.

### T02 — Hái một quả, 5 giây

Tạo một video ngang 16:9 dài 5 giây từ ảnh tham chiếu. Giữ đúng cô gái, khuôn mặt, tóc, trang phục, cành táo và chiếc rổ trong ảnh. Một trung cảnh máy ổn định, đủ thấy gương mặt, hai tay, quả và rổ. Cô gái đỡ một quả táo còn gắn trên cành, xoay nhẹ để tách khỏi cuống, rồi đặt chính quả đó vào rổ. Chuyển động chậm vừa, có sức nặng và tiếp xúc thật; cành nhúc nhích nhẹ theo lực tay. Quả phải đi liên tục từ cành qua bàn tay tới rổ, không tự biến mất hoặc có thêm quả. Cô gái tập trung, nét mặt dễ chịu, không nhìn vào camera. Giữ ánh sáng và màu từ ảnh, bề mặt da, vải, lá và quả như hình quay thật. Không đổi mặt, không chuyển cảnh, không cử động máy. Chỉ tiếng lá và chạm nhẹ vào rổ, âm vườn nhỏ; không thoại, không nhạc, không chữ.

### T03 — Đổ táo vào chậu nước, 5 giây

Tạo một video ngang 16:9 dài 5 giây từ ảnh tham chiếu. Giữ đúng rổ, táo, tay áo, chậu nước và vị trí khu rửa. Một cận cảnh máy ổn định nhìn chếch vào rổ và chậu. Hai tay nghiêng rổ vừa đủ để vài quả táo lần lượt lăn và rơi vào chậu dưới tác dụng trọng lực. Táo va nhẹ vào nước và nhau, làm nước bắn ít và gợn lan ra; tay đưa rổ về vị trí cân bằng sau khi đổ. Quả giữ hình và màu; không xuyên chậu, không biến thành loại khác, không tự tăng số lượng. Chi tiết giọt nước và độ ướt trên quả như camera quay thật. Không chuyển cảnh, không tự thêm mặt người hoặc vật mới. Có tiếng táo chạm nước và tiếng nước gợn đồng bộ, không tiếng nói, không nhạc, không chữ.

### T04 — Dao cắt táo, 5 giây

Tạo một video ngang 16:9 dài 5 giây từ ảnh tham chiếu. Giữ nguyên quả táo, tay, tay áo, dao, thớt và hướng sáng. Một cận cảnh đủ thấy bàn tay, lưỡi dao và toàn quả trên thớt; camera ổn định. Tay giữ quả ở vị trí hợp lý, tay cầm dao thực hiện một đường cắt có tiếp xúc từ phần trên xuống thớt. Quả tách thành hai phần theo đúng đường dao và hai phần nằm lại trên thớt, nhìn rõ mặt cắt ẩm. Giữ số ngón và hình bàn tay ổn định; lưỡi dao không xuyên bàn tay, không cắt trước khi chạm quả; quả không đổi hình giữa thao tác. Nhịp làm tự nhiên, không tăng tốc hay rung hình. Chỉ tiếng cắt quả và dao chạm thớt nhỏ, không thoại, không nhạc, không chữ.

### T05 — Khuấy nồi, 5 giây

Tạo một video ngang 16:9 dài 5 giây từ ảnh tham chiếu. Giữ đúng cô gái nếu thấy mặt, tay áo, bếp, nồi, muỗng gỗ và các miếng táo đã được đun trong ảnh. Một trung cận hoặc cận theo đúng ảnh, máy ổn định. Tay khuấy chậm một vòng bằng muỗng; các miếng táo dịch chuyển theo dòng chất lỏng và giữ hình hợp lý. Nồi sôi nhẹ, hơi nước mỏng đi lên và tan dần, không phun mạnh vào camera. Muỗng chạm đúng chất lỏng và thành nồi, không xuyên vật. Ánh sáng từ cửa và bếp giữ như ảnh, vật liệu gỗ, kim loại/gốm và thức ăn có bề mặt tự nhiên. Không đổi món hoặc sinh thêm nguyên liệu. Chỉ tiếng sôi nhỏ và muỗng chạm nồi đồng bộ, không thoại, không nhạc, không chữ.

### T06 — Cô gái và bà, 5 giây

Tạo một video ngang 16:9 dài 5 giây từ ảnh tham chiếu. Giữ đúng hai người, khuôn mặt cô gái và bà, tóc, trang phục, bàn, bát và bối cảnh. Một trung cảnh hai người, camera ổn định. Cô gái nhẹ nhàng đặt bát táo đã chế biến trước bà; đáy bát chạm bàn và đứng yên. Bà nhìn bát rồi nhìn cô gái, mỉm cười nhỏ; cô gái đáp lại bằng nét mặt thư thái. Cử chỉ ít, tự nhiên, có cảm giác quen thuộc; không diễn quá mức hay nhìn thẳng camera. Hai khuôn mặt giữ nguyên trong toàn cảnh, tay không xuyên bát hoặc người kia, không đổi vị trí ghế/bàn. Ánh sáng và màu từ ảnh có cảm giác ấm áp vừa phải, không phủ vàng toàn khung. Chỉ tiếng bát chạm bàn nhỏ và âm nơi sống nhẹ, không lời nói, không nhạc, không chữ.

## 7. Prompt một đoạn nhiều cảnh 30 giây — cách B

Đưa cùng bộ ảnh đầu cảnh T01–T06 và bộ tham chiếu được phép vào Dola. Nếu tài khoản chỉ nhận một ảnh hoặc không gán được vai trò, ghi rõ hạn chế trước khi thử; không xem đây là so sánh có cùng lượng thông tin đầu vào. Các mốc sau là chỉ dẫn mong muốn, không bảo đảm mô hình cắt đúng từng phần trăm giây.

Tạo video ngang 16:9 dài 30 giây, hình và chuyển động như camera thật quay trong một thế giới làng quê. Dùng đúng các ảnh T01–T06 để giữ cô gái, bà, trang phục, vườn, khu rửa, bếp, bàn ăn, táo và các vật dụng. Cùng một tạo hình và ánh sáng hợp lý trong từng không gian. Mỗi cảnh chỉ có một hành động chính, máy ổn định, chuyển sang góc tiếp theo bằng cắt thẳng đơn giản, không hiệu ứng biến hình giữa người/đồ vật.

0–5 giây: toàn cảnh vườn theo T01, lá lay nhẹ, táo bám cuống, các lớp không gian rõ.
5–10 giây: trung cảnh T02, cô gái đỡ một táo trên cành, xoay nhẹ/tách cuống và đặt chính quả đó vào rổ.
10–15 giây: cận cảnh T03, nghiêng rổ để táo rơi vào chậu nước, có va chạm và nước gợn tự nhiên.
15–20 giây: cận cảnh T04, một táo trên thớt được cắt thành hai phần, lưỡi dao có tiếp xúc thật và hai phần nằm trên thớt.
20–25 giây: cảnh T05 tại bếp, nồi đã qua thời gian đun chứa các miếng táo, tay khuấy một vòng và hơi nước mỏng đi lên. Đây là lược thời gian công đoạn, không biến quả nguyên tức thì thành món chín.
25–30 giây: trung cảnh T06, cô gái đặt bát táo đã chế biến trước bà, bà và cô gái trao ánh nhìn và nụ cười nhỏ, bát chạm bàn và đứng yên.

Giữ mặt, tóc, trang phục và vật dụng nhất quán. Táo giữ đúng loại và trạng thái của công đoạn; chỉ thay đổi do thao tác thấy được hoặc do thời gian chế biến đã lược qua. Các chuyển động có trọng lượng, tay và dụng cụ chạm đúng vật. Sắc xanh nhiều lớp, màu thức ăn và da tự nhiên, không bóng nhựa. Chỉ tiếng thao tác đồng bộ và môi trường nhỏ; không tự thêm thoại, giọng kể, nhạc, chữ hoặc logo.

## 8. Cách chấm và chọn hình dùng được

Xem lần đầu ở tốc độ bình thường để đánh giá cảm giác. Xem lại chậm những chỗ tay chạm vật, cắt, đổ, đặt bát và các thời điểm đổi cảnh. Không chọn chỉ từ ảnh thumbnail hoặc một frame đẹp.

Thang dưới đây là quy ước thử của dự án, không phải chuẩn ngành hay tiêu chuẩn chính thức của Seedance:
- **0:** lỗi thấy rõ, phá hành động/nhận diện; chưa dùng đoạn chứa lỗi.
- **1:** có khuyết điểm; ghi chính xác đoạn có thể cắt dùng hoặc cần sửa.
- **2:** đoạn xem được ở tốc độ bình thường, đạt tiêu chí đang xét.
- **N/A:** không xuất hiện yếu tố để đánh giá, ví dụ cảnh lá không có mặt người; không tự cho 2.

| Tiêu chí | Quan sát |
|---|---|
| Nhận diện | Mặt, tóc, cơ thể, trang phục không tự đổi; cả bà và cô gái đều giữ đúng nếu xuất hiện |
| Vật lý/thao tác | Tay–vật–dụng cụ có tiếp xúc; vật có trọng lượng/quỹ đạo; không xuyên nhau hoặc tự xuất hiện |
| Tính liền mạch | Đúng vật liệu, vật chứa, trạng thái trước/sau, vị trí bối cảnh và hướng sáng |
| Cảm giác camera thật | Bề mặt tự nhiên, chuyển động không co giãn bất thường, ánh sáng/bóng hợp lý, khung hình ổn định |
| Nhịp thư giãn | Hành động rõ, đủ thời gian đọc, cử chỉ không giật/gấp hoặc diễn quá; đánh giá ở tốc độ bình thường |
| Âm thao tác | Đúng sự kiện và đúng lúc; không tự có thoại/nhạc; có hay không có âm được ghi riêng |

Một lỗi nhận diện hoặc vật lý không được bù bằng màu đẹp hay nhạc dễ chịu. Tuy vậy, đoạn lỗi không buộc bỏ cả video nếu có khoảng hình sạch sử dụng được. Chọn phần hành động có đầu–diễn tiến–kết quả rõ; thời lượng dùng có thể ngắn hơn độ dài lần tạo.

Nếu hình đạt nhưng âm sai/nhạc tự xuất hiện: giữ hình, bỏ âm sinh và để người dùng dựng âm theo phân công. Đây là kết quả “hình đạt, audio cần thay”, không gộp thành mô hình đã làm âm đạt.

## 9. Ghi lại mỗi lần thử

| Run | Mã/cách | Ảnh và phiên bản prompt | Độ dài yêu cầu/thực nhận | Giây hình dùng được | Lỗi và timecode | Audio có/đạt | Phút làm việc | Credit/chi phí thực |
|---|---|---|---|---|---|---|---|---|
| Chưa chạy | — | — | — | — | — | — | — | — |

Tính từ dữ liệu thực:
- **Tỷ lệ hình dùng được = tổng số giây đạt / tổng số giây đầu ra.**
- **Chi phí/phút hình dùng được = tổng chi phí thực / (tổng giây đạt / 60).**
- Theo dõi thời gian tạo ảnh, đợi sinh, xem/chọn, tạo lại và dựng.
- Nếu chưa có giá/credit quy đổi, giữ credit cùng phút làm việc; không tự gán tiền.
- Với một lượt thử nhỏ, kết quả chỉ mô tả bộ cảnh đã chạy, chưa suy ra tỷ lệ thành công ổn định của mô hình.

## 10. Quyết định sau phép thử

- Cách A đạt, B khó giữ người/vật: ưu tiên ảnh rõ và đoạn riêng cho thao tác; đoạn dài dùng khi có bằng chứng phù hợp.
- Cách B đạt và giảm công sức: dùng đoạn nhiều cảnh cho các chuỗi đã kiểm, vẫn có thể thay một đoạn lỗi bằng cảnh riêng.
- T02 hoặc T04 lỗi: kiểm ảnh có cung cấp đủ tay/dụng cụ/vật và trạng thái đầu không; sửa một yếu tố rồi thử lại.
- T06 lỗi: kiểm bộ tham chiếu hai người và đường đặt bát; giảm cử chỉ/tương tác phức tạp trước khi thêm họ hàng.
- Cảnh nào đẹp nhưng không có tiến trình rõ: sửa hành động/cách dựng; không chỉ thêm từ “cinematic”.
- Chưa đạt độ chân thực người dùng yêu cầu: chưa kéo dài thành tập hoàn chỉnh; dùng kết quả để xác định điểm cần thay trong ảnh, prompt hoặc loại cảnh.

Độ dài sinh và độ dài cảnh dùng trong bản dựng được quyết định riêng. Mốc 5/30 giây là để so sánh phương pháp, không phải nhịp cắt cố định của Farm.

## 11. Thử trải nghiệm với người xem

Sau khi có hình đạt, người dùng dựng bản âm thanh dự định. Cho một nhóm nhỏ phù hợp hồ sơ mục tiêu xem bản có âm và thông tin rằng hình được tạo bằng AI. Hỏi ngắn:
- Người xem có thấy dễ chịu hơn sau đoạn này không; đoạn nào khiến họ bị kéo ra khỏi cảm giác yên bình?
- Họ có muốn xem tiếp công việc và thành quả không?
- Điều gì khiến họ muốn quay lại với cô gái và bà?

Đây là phản hồi thăm dò về trải nghiệm, chưa là chứng minh tác dụng sức khỏe hoặc phép đo đại diện cho khán giả Mỹ. Sau 3–5 video mới đối chiếu các ưu tiên đã chốt bằng dữ liệu giữ chân, quay lại và phản hồi thực.

## 12. Trạng thái hiện tại

- Đã chuẩn bị sáu cảnh, prompt riêng, prompt 30 giây và cách ghi kết quả.
- Chưa có bộ ảnh đầu cảnh được xác nhận cho bài thử.
- Chưa chạy Dola; chưa tạo/đánh giá video nào trong bài này.
- Cần đầu ra thực để quyết định cách 5 giây/30 giây, mức sửa và dự toán. Không tuyên bố đã nghiệm chứng chỉ từ tài liệu mô hình.
