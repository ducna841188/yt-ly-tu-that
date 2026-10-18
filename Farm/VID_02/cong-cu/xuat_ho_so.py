"""Render the current VID_02 JSON into its reader view. No video understanding is performed."""
from pathlib import Path
import json

BASE=Path(__file__).resolve().parents[1]
def load(name):return json.loads((BASE/name).read_text())
def tc(t):return f'{int(t)//60:02d}:{t%60:05.2f}'
def text(value):
    if value is None:return 'Chưa biết'
    if isinstance(value,(list,dict)):return json.dumps(value,ensure_ascii=False)
    return str(value)
def cell(value):return text(value).replace('|','/').replace('\n',' ')

LABELS={
'summary':'Tóm tắt ảnh','subject_count':'Số người trong mẫu','identities':'Nhận diện/phạm vi','action':'Diễn giải hành động','state_start':'Trạng thái ảnh đầu','contact_and_change':'Điểm đỡ/tiếp xúc/biến đổi','state_end':'Trạng thái ảnh cuối','setting':'Bối cảnh','composition':'Các lớp/bố cục','shot_size':'Cỡ cảnh','camera_height_and_angle':'Vị trí/góc máy tương đối','camera_motion':'Chuyển động máy','lens_and_perspective':'Phối cảnh và dữ liệu ống','focus':'Độ rõ/nét','lighting':'Diện mạo ánh sáng','color':'Quan hệ màu','material_texture':'Chất liệu','on_screen_text':'Chữ trong hình','time_treatment':'Tốc độ/xử lý thời gian','cut_in':'Điểm vào','cut_out':'Điểm ra','audio_ambience':'Âm nền','audio_action':'Tiếng thao tác','audio_dialogue':'Lời nói','audio_music':'Nhạc'}
STATUS={'observed':'thấy trên ảnh','interpretation':'diễn giải ảnh','unknown':'chưa kiểm','source_report':'nguồn thuật lại','synthetic':'giả lập'}

def main():
    a=load('phan-tich.json');r=load('tai-tao.json');dna=load('dna.json');source=load('nguon.json');m=load('metrics.json');im=load('anh/manifest.json')
    by_id={s['id']:s for s in a['shots']};rp={s['source_shot_id']:s for s in r['shots']}
    seqs={q['id']:q for q in a['sequences']};contacts={c['shot_id']:c for c in r['contact_studies']}
    atlas={}
    for f in im['frames']:
        if f['atlas'] and '/shot-' in f['atlas']:atlas.setdefault(f['shot_id'],f['atlas'])
    lines=[
      '# VID_02 — Phân tích hình, cấu trúc và tái tạo',
      '',f"Bản {a['version']} · core {a['core_version']} · tệp {tc(a['duration_seconds'])} · **trạng thái partial (chưa đủ hình chuyển động/âm)**.",
      '',f"[Nguồn người dùng](https://www.youtube.com/watch?v=FWMIPukvdsQ) · [Bản JSON chuẩn](phan-tich.json) · [Phiếu tái tạo](tai-tao.json) · [DNA có điều kiện](dna.json) · [Mục lục](README.md)",
      '', '## Cách hiểu độ phủ', '',
      'Đã đọc ảnh theo toàn trục tệp, không phải đã phát trọn video ở tốc độ thật. Có 882 lần hiển thị ảnh theo khoảng cú máy và 476 lần hiển thị ảnh rà dày; một số mốc trùng nhau. Bộ bằng chứng có '+str(m['sampled_evidence_points'])+' mốc ảnh riêng. Bốn nhóm âm, chuyển động máy và tốc độ đều để chưa kiểm khi chưa đủ bằng chứng.',
      '', '**176 là danh sách cú máy làm việc**, sau khi gộp khói bùng 05:59.48 vào cùng góc trước đó. Chưa chứng nhận không còn cut ít tương phản bị bỏ sót. Mốc tính từ đầu tệp tải lên, chưa xác minh offset với phiên bản YouTube.',
      '', 'Mỗi nhận xét có loại bằng chứng. “Diễn giải” là cách đọc ảnh, “đề xuất” là phương án làm phim mới; cả hai không tự thành ý đồ tác giả hoặc hiệu quả đã đo. Trường số người đếm người/thân/tay nhận ra trong ảnh, **không đếm động vật**, không bảo chứng toàn khoảng.',
      '', '## Cách đọc toàn phim', '',
      '**Giả thuyết trục kể:** nhiều công việc nhỏ được đan trong lúc chờ, thành món hoàn chỉnh, rồi được gói/cất và chia sẻ trong một căn nhà đang đầy dần. Thiên nhiên và vật nuôi giữ cảm giác đây là đời sống tiếp diễn. Phần quả thu cuối không tự được coi là nguyên liệu của món nón vàng nếu nguồn không cho thấy mối nối đó.',
      '', '| Phân đoạn | Khoảng | Nhiệm vụ trong cách đọc |', '| --- | --- | --- |',
    ]
    for s in a['segments']:lines.append(f"| {s['id']} | {tc(s['start_seconds'])}–{tc(s['end_seconds'])} | {cell(s['function'])} |")
    lines += ['', '## 26 chuỗi việc', '', 'Chuỗi là đơn vị phân tích tiến trình; một chuỗi có thể chứa nhiều góc hoặc địa điểm. Không đồng nhất 26 chuỗi với 26 cảnh quay sản xuất độc lập.', '', '| Chuỗi | Khoảng | Mục tiêu và thay đổi | Nối tiếp |','| --- | --- | --- | --- |']
    for q in a['sequences']:lines.append(f"| {q['id']} | {tc(q['start_seconds'])}–{tc(q['end_seconds'])} | {cell(q['objective'])}. {cell(q['change'])} | {cell(q['relationship_to_next'])} |")
    lines += ['', '## Nhịp và giới hạn thống kê', '',f"Theo phân hoạch hiện hành: trung bình **{m['mean_shot_seconds']:.2f} giây**, trung vị **{m['median_shot_seconds']:.2f} giây**, ngắn nhất **{m['min_shot_seconds']:.2f}**, dài nhất **{m['max_shot_seconds']:.2f}**. Đây là số mô tả bản dựng dự kiến, không là chuẩn ba giây, điểm cảm xúc hoặc bằng chứng giữ chân.", '', 'Các cú rót/tráng bánh và cảnh cuối dài hơn nhiều cận thay đổi vật liệu. Chuỗi bình rang có chuẩn bị–chờ–khói bùng–kết quả, là một đoạn tương phản về hình; chưa nghe để kết luận cường độ/thiết kế âm của đoạn.', '', '## 12 giả thuyết DNA', '']
    for rule in dna['rules']:
        lines += [f"### {rule['id']} — {rule['title']}",'',rule['observations'],'',f"**Mốc:** {', '.join(rule['shot_refs'])}.", '',f"**Dùng khi:** {' '.join(rule['conditions'])}", '',f"**Tái tạo chức năng:** {rule['reconstruction_recipe']}", '',f"**Ngoại lệ:** {' '.join(rule['exceptions'])}", '',f"**Phép kiểm tiếp:** {rule['next_test']}", '']
    lines += ['## 13 sổ trạng thái sản vật', '', 'Mỗi chuỗi trạng thái nằm trong tai-tao.json với mã cú máy. Không lấp các công đoạn bị lược bằng quan sát bịa thêm.', '']
    for ledger in r['state_ledgers']:
        lines += [f"- **{ledger['title']}:** {' → '.join(x['shot_id'] for x in ledger['entries'])}. {ledger['continuity_limit']}"]
    lines += ['', '## 176 hồ sơ cú máy', '', 'Bấm mở từng mục. Bảng giữ đủ 25 nhóm; trường chưa kiểm vẫn có giá trị null/lý do trong JSON. Ảnh minh chứng là bảng lớn gồm sáu cú máy, tối đa năm ảnh hiển thị mỗi dòng; mốc rà dày nằm ở các bảng tiếp xúc riêng.', '']
    current=None
    for shot in a['shots']:
        q=seqs[shot['sequence_id']]
        if current!=q['id']:
            lines += [f"### {q['id']} — {q['objective']}",''];current=q['id']
        ident=shot['id'];target=rp[ident]
        lines += [f'<a id="{ident.lower()}"></a>',f"<details><summary>{ident} · {tc(shot['start_seconds'])}–{tc(shot['end_seconds'])} · {target['edit_duration_target_seconds']:.2f}s — {shot['observed']['summary']['value']}</summary>", '', f"[Mở ảnh lớn]({atlas[ident]}) · [Phiếu tái tạo của toàn bộ phim](tai-tao.json)", '', '| Nhóm | Nội dung | Trạng thái |', '| --- | --- | --- |']
        for key,v in shot['observed'].items():
            value=cell(v['value']) if v['value'] is not None else cell(v['uncertainty_reason'])
            lines.append(f"| {LABELS[key]} | {value} | {STATUS[v['status']]} |")
        lines += ['', '**Chức năng dự kiến:** '+target['function'],'', '**Cần giữ khi tái tạo:** '+target['protected_elements'][0], '', '**Trạng thái vào–ra:** '+target['start_state']+' → '+target['end_state'], '', '**Độ dài:** là độ dài mục tiêu trong bản dựng; có thể phải sinh dài hơn rồi cắt, tùy công cụ thực. Chưa sinh clip.']
        if ident in contacts:
            lines += ['', '**Rà tiếp xúc bằng ảnh dày:**','']
            for phase in contacts[ident]['phases']:lines.append(f"- {tc(phase['seconds'])}: {phase['description']}")
            names=sorted({f['atlas'] for f in im['frames'] if f['shot_id']==ident and f['atlas'] and 'tiep-xuc-' in f['atlas']})
            lines += ['', ' · '.join(f'[Bảng tiếp xúc {j+1}]({name})' for j,name in enumerate(names))]
        lines += ['', '</details>', '']
    lines += ['## Những việc cần làm để khóa tái tạo', '']
    lines += [f'{i+1}. {q}' for i,q in enumerate(a['open_questions'])]
    lines += ['', 'Chưa có dữ liệu CTR/giữ chân, bình luận được lấy mẫu, khảo sát người xem hoặc video AI đầu ra. Bộ này dùng được làm bản thiết kế và danh sách kiểm; chưa chứng nhận tái tạo hoàn chỉnh.']
    # Keep the overview small; split the full 25-group reader view by the eight
    # film segments, never by review version. JSON remains the single analysis.
    first_detail=lines.index('## 176 hồ sơ cú máy')
    closing=lines.index('## Những việc cần làm để khóa tái tạo')
    blocks={};i=first_detail
    while i<closing:
        if lines[i].startswith('<a id="v02-s'):
            anchor=lines[i].split('"')[1];end=i+1
            while lines[end]!='</details>':end+=1
            blocks[anchor.upper()]=lines[i:end+1];i=end
        i+=1
    detail_dir=BASE/'chi-tiet';detail_dir.mkdir(exist_ok=True)
    overview=lines[:first_detail]+['## Tra từng cú máy','','Mở phần tương ứng để xem đầy đủ 25 nhóm và các mốc tiếp xúc. Tám phần chia theo cấu trúc phim, mỗi phần có một đường dẫn hiện hành.','']
    for segment in a['segments']:
        filename=segment['id'].replace('V02-','')+'.md'
        members=[s for s in a['shots'] if seqs[s['sequence_id']]['segment_id']==segment['id']]
        overview += [f"### {segment['id']} — {segment['function']}",'',f"[Mở phần chi tiết](chi-tiet/{filename})",'', '| Cú máy | Khoảng | Nội dung ảnh |','| --- | --- | --- |']
        details=[f"# {segment['id']} — {segment['function']}",'',f"{tc(segment['start_seconds'])}–{tc(segment['end_seconds'])} · {len(members)} cú máy dự kiến · bản {a['version']} · core {a['core_version']}.", '', '[Mục lục toàn phim](../Phan_tich_dien_anh.md) · [JSON chuẩn](../phan-tich.json) · [Phiếu tái tạo](../tai-tao.json)', '', 'Độ phủ: ảnh theo thời gian, chưa phát trọn chuyển động hoặc nghe âm. Đọc trạng thái/lý do thiếu của từng trường. Số người chỉ đếm ảnh mẫu, không gồm động vật.', '']
        prev=None
        for s in members:
            ident=s['id'];q=seqs[s['sequence_id']]
            overview.append(f"| [{ident}](chi-tiet/{filename}#{ident.lower()}) | {tc(s['start_seconds'])}–{tc(s['end_seconds'])} | {cell(s['observed']['summary']['value'])} |")
            if prev!=q['id']:details += [f"## {q['id']} — {q['objective']}",''];prev=q['id']
            block='\n'.join(blocks[ident]).replace('](anh/','](../anh/').replace('](tai-tao.json)','](../tai-tao.json)')
            details += [block,'']
        overview += ['']
        (detail_dir/filename).write_text('\n'.join(details)+'\n')
    overview += lines[closing:]
    (BASE/'Phan_tich_dien_anh.md').write_text('\n'.join(overview)+'\n')
    readme=f'''# VID_02 — Đồ ăn vặt cho Tết Nguyên đán

**Bản nạp 0.1.0: đã phân tích ảnh theo toàn trục; chưa xem trọn chuyển động hoặc nghe âm.** Tệp dài **10:11.92**, 1280×720, mã hóa 50 fps, có AAC stereo. [Nguồn do người dùng gửi](https://www.youtube.com/watch?v=FWMIPukvdsQ).

**176 cú máy dự kiến · 26 chuỗi việc · 8 phân đoạn · 25 nhóm mỗi cú · 1.328 mốc ảnh riêng · 10 lượt rà tiếp xúc · 13 sổ trạng thái · 12 giả thuyết DNA.** Đây là dữ liệu nghiên cứu có điều kiện, chưa là công thức gây lượt xem.

## Đọc theo thứ tự

1. [Bản phân tích có mục lục và hồ sơ từng cú máy](Phan_tich_dien_anh.md).
2. [JSON phân tích chuẩn](phan-tich.json): quan sát ảnh, diễn giải, nguồn/mốc và phần chưa biết. AI nên đọc từng sequence_id, không cần nạp toàn tệp trong một lượt.
3. [Phiếu tái tạo](tai-tao.json): trạng thái, khung, điểm đỡ, phần phải giữ, yêu cầu tham chiếu, âm đề xuất và dấu duyệt cho từng cú. Đây là thiết kế chưa tạo thử.
4. [DNA có điều kiện](dna.json): bằng chứng, điều kiện, ngoại lệ, cách làm và phép kiểm tiếp.
5. [Nguồn và phương pháp](nguon.json), [mục lục ảnh/checksum](anh/manifest.json), [thống kê](metrics.json), [chỉ mục từng giây](chi-muc-giay.json), [tuyến âm chờ nghe](am-thanh.json).

## Những điểm có thể vận dụng ngay

- Đan công việc trong lúc món khác chờ rồi quay lại trả kết quả: hạt dẻ, lát quả sấy, phôi kẹo và thịt.
- Cho thấy biến đổi bằng điểm tiếp xúc; kết quả tiếp tục được dùng, gói hoặc cất giữ.
- Giữ vật nuôi, người nhận và nơi cất đồ như các phần của đời sống tiếp diễn.
- Bó rơm được làm sớm rồi trở lại làm giá cắm hồ lô; một đạo cụ có công dụng nhìn thấy.
- Không ép mỗi cú máy ba giây: bản phân hoạch hiện tại có trung vị {m['median_shot_seconds']:.2f}s, dao động {m['min_shot_seconds']:.2f}–{m['max_shot_seconds']:.2f}s.

## Phần còn phải xác minh

Chuyển động máy, vận tốc, mọi pha tay/vật giữa ảnh, độ đầy đủ ranh giới và toàn bộ nội dung âm. Đo RMS/sample peak không thay cho nghe nhạc/thoại/SFX hoặc kiểm đồng bộ. 176 cú là danh sách làm việc, không số đếm đã duyệt bằng phát toàn phim.

Mốc 05:59.48 là khói bùng trong cùng góc, đã gộp vào V02-S106. Điểm cắt sang góc rộng dự kiến ở 05:59.64. Các nhận định cảm xúc/công dụng là giả thuyết, chưa có phản hồi người xem. Đọc trường coverage trước sử dụng.

## Lưu trữ và chạy lại

Nguồn 217 MB vẫn là tệp người dùng đã tải lên; [nguon.json](nguon.json) giữ mã tệp và SHA-256, không chép video lớn vào Git. 43 bảng ảnh là ảnh nguồn phục vụ phân tích. [Công cụ xuất bản đọc](cong-cu/xuat_ho_so.py) đọc JSON hiện hành; [công cụ trích lại ảnh](cong-cu/trich_anh.py) cần tệp đúng checksum.

Mọi tệp sửa tại chỗ; lịch sử ở Git và [nhật ký chung](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/CHANGELOG.md). [Thư viện Farm](../Thu_vien_kien_thuc/README.md) · [Core hiện hành](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/README.md).
'''
    (BASE/'README.md').write_text(readme)
    print(json.dumps({'rendered_shots':len(a['shots']),'markdown_bytes':(BASE/'Phan_tich_dien_anh.md').stat().st_size},ensure_ascii=False))

if __name__=='__main__':main()
