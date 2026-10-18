"""Render the current VID_02 JSON into its reader view. No video understanding is performed."""
from pathlib import Path
import json

BASE=Path(__file__).resolve().parents[1]
def load(name):return json.loads((BASE/name).read_text())
def tc(t):return f'{int(t)//60:02d}:{t%60:05.2f}'
def text(value):
    if value is None:return 'Chưa biết'
    if isinstance(value,dict) and 'relative_reading' in value:return value['relative_reading']+'; vật mốc: '+value['reference_subject']+'; '+value['geometry']
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
      '',f"Bản {a['version']} · core {a['core_version']} · tệp {tc(a['duration_seconds'])} · **phân tích hình theo ảnh có mốc; âm ngoài phạm vi**.",
      '',f"[Nguồn người dùng](https://www.youtube.com/watch?v=FWMIPukvdsQ) · [Bản JSON chuẩn](phan-tich.json) · [Phiếu tái tạo](tai-tao.json) · [DNA có điều kiện](dna.json) · [Mục lục](README.md)",
      '', '## Cách hiểu độ phủ', '',
      'Đã đọc ảnh theo toàn trục tệp, không phải đã phát trọn video ở tốc độ thật. Có 882 lần hiển thị ảnh theo khoảng cú máy và 476 lần hiển thị ảnh rà dày; một số mốc trùng nhau. Bộ bằng chứng có '+str(m['sampled_evidence_points'])+' mốc ảnh riêng. Chuyển động máy và tốc độ thật chưa được chứng nhận từ ảnh. Âm ngoài phạm vi theo người dùng; không phải điều kiện chặn lượt hình.',
      '', '**176 là danh sách cú máy làm việc**, sau khi gộp khói bùng 05:59.48 vào cùng góc trước đó. Chưa chứng nhận không còn cut ít tương phản bị bỏ sót. Mốc tính từ đầu tệp tải lên, chưa xác minh offset với phiên bản YouTube.',
      '', 'Mỗi nhận xét có loại bằng chứng. “Diễn giải” là cách đọc ảnh, “đề xuất” là phương án làm phim mới; cả hai không tự thành ý đồ tác giả hoặc hiệu quả đã đo. Trường số người đếm người/thân/tay nhận ra trong ảnh, **không đếm động vật**, không bảo chứng toàn khoảng.',
      '', '## Cách đọc toàn phim', '',
      '**Giả thuyết trục kể:** nhiều công việc nhỏ được đan trong lúc chờ, thành món hoàn chỉnh, rồi được gói/cất và chia sẻ trong một căn nhà đang đầy dần. Thiên nhiên và vật nuôi giữ cảm giác đây là đời sống tiếp diễn. Phần quả thu cuối không tự được coi là nguyên liệu của món nón vàng nếu nguồn không cho thấy mối nối đó.',
      '', '| Phân đoạn | Khoảng | Nhiệm vụ trong cách đọc |', '| --- | --- | --- |',
    ]
    for s in a['segments']:lines.append(f"| {s['id']} | {tc(s['start_seconds'])}–{tc(s['end_seconds'])} | {cell(s['function'])} |")
    lines += ['', '## 26 chuỗi việc', '', 'Chuỗi là đơn vị phân tích tiến trình; một chuỗi có thể chứa nhiều góc hoặc địa điểm. Không đồng nhất 26 chuỗi với 26 cảnh quay sản xuất độc lập.', '', '| Chuỗi | Khoảng | Mục tiêu và thay đổi | Nối tiếp |','| --- | --- | --- | --- |']
    for q in a['sequences']:lines.append(f"| {q['id']} | {tc(q['start_seconds'])}–{tc(q['end_seconds'])} | {cell(q['objective'])}. {cell(q['change'])} | {cell(q['relationship_to_next'])} |")
    lines += ['', '## Nhịp và giới hạn thống kê', '',f"Theo phân hoạch hiện hành: trung bình **{m['mean_shot_seconds']:.2f} giây**, trung vị **{m['median_shot_seconds']:.2f} giây**, ngắn nhất **{m['min_shot_seconds']:.2f}**, dài nhất **{m['max_shot_seconds']:.2f}**. Đây là số mô tả bản dựng dự kiến, không là chuẩn ba giây, điểm cảm xúc hoặc bằng chứng giữ chân.", '', 'Các cú rót/tráng bánh và cảnh cuối dài hơn nhiều cận thay đổi vật liệu. Chuỗi bình rang có chuẩn bị–chờ–khói bùng–kết quả, là một đoạn tương phản về hình; lượt này chỉ đánh giá diễn tiến hình.', '', '## 13 giả thuyết DNA', '']
    for rule in dna['rules']:
        lines += [f"### {rule['id']} — {rule['title']}",'',rule['observations'],'',f"**Mốc:** {', '.join(rule['shot_refs'])}.", '',f"**Dùng khi:** {' '.join(rule['conditions'])}", '',f"**Tái tạo chức năng:** {rule['reconstruction_recipe']}", '',f"**Ngoại lệ:** {' '.join(rule['exceptions'])}", '',f"**Phép kiểm tiếp:** {rule['next_test']}", '']
    lines += ['## 13 sổ trạng thái sản vật', '', 'Mỗi chuỗi trạng thái nằm trong tai-tao.json với mã cú máy. Không lấp các công đoạn bị lược bằng quan sát bịa thêm.', '']
    for ledger in r['state_ledgers']:
        lines += [f"- **{ledger['title']}:** {' → '.join(x['shot_id'] for x in ledger['entries'])}. {ledger['continuity_limit']}"]
    lines += ['', '## 176 hồ sơ cú máy', '', 'Bấm mở từng mục. JSON giữ đủ 25 nhóm; bản đọc hiện 21 nhóm hình, ẩn bốn trường âm ngoài phạm vi; trường chưa kiểm vẫn có giá trị null/lý do trong JSON. Ảnh minh chứng là bảng lớn gồm sáu cú máy, tối đa năm ảnh hiển thị mỗi dòng; mốc rà dày nằm ở các bảng tiếp xúc riêng.', '']
    current=None
    for shot in a['shots']:
        q=seqs[shot['sequence_id']]
        if current!=q['id']:
            lines += [f"### {q['id']} — {q['objective']}",''];current=q['id']
        ident=shot['id'];target=rp[ident]
        lines += [f'<a id="{ident.lower()}"></a>',f"<details><summary>{ident} · {tc(shot['start_seconds'])}–{tc(shot['end_seconds'])} · {target['edit_duration_target_seconds']:.2f}s — {shot['observed']['summary']['value']}</summary>", '', f"[Mở ảnh lớn]({atlas[ident]}) · [Phiếu tái tạo của toàn bộ phim](tai-tao.json)", '', '| Nhóm | Nội dung | Trạng thái |', '| --- | --- | --- |']
        for key,v in shot['observed'].items():
            if key.startswith('audio_'):continue
            value=cell(v['value']) if v['value'] is not None else cell(v['uncertainty_reason'])
            lines.append(f"| {LABELS[key]} | {value} | {STATUS[v['status']]} |")
        vd=target['visual_decision']
        link=next((x for x in r['visual_study']['visual_cut_links'] if x['from_shot']==ident),None)
        lines += ['', '**Vì sao chọn bộ góc trong chuỗi:** '+vd['angle_reason_in_sequence'], '', '**Cần giữ quan hệ hành động:** '+vd['critical_relationship'], '', '**Công đoạn lược / giới hạn nhân quả:** '+vd['sequence_continuity_and_omissions'], '', '**Nối cú sau:** '+(link['reading'] if link else 'Kết tệp; fade trong cú cuối.'), '', '**Đề xuất hình cho AI:** '+vd['reconstruction_visual_brief']]
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
    # Sequence designs are canonical in tai-tao.json, not independent essays.
    at=lines.index('## 26 chuỗi việc');end=lines.index('## Nhịp và giới hạn thống kê')
    seq_lines=['## 26 chuỗi việc — bóc tách hình và nội dung','',
      'Mỗi chuỗi có câu hỏi người xem, nhịp việc theo trạng thái, lý do bộ góc, màu vật liệu và phần không được tự nối nhân quả. Đây là diễn giải có bằng chứng, chưa là ý đồ tác giả hoặc hiệu quả đã đo.','']
    for q in r['visual_study']['sequence_designs']:
        seq_lines += [f"### {q['id']} — {q['title']}",'',f"**Câu hỏi dẫn:** {q['viewer_question']}",'',
          '| Nhịp nội dung | Cú máy | Khoảng |','| --- | --- | --- |']
        for b in q['beats']:
            seq_lines.append(f"| {cell(b['title'])} | {', '.join(b['shot_refs'])} | {tc(b['start_seconds'])}–{tc(b['end_seconds'])} |")
        seq_lines += ['', '**Góc máy và bố cục:** '+q['angle_logic'], '', '**Màu và chất liệu:** '+q['color_script'], '', '**Cần giữ / phần đã lược:** '+q['continuity_and_omissions'], '', f"[Ảnh lớn đầu chuỗi]({atlas[q['shot_refs'][0]]})", '']
    seq_lines += ['### Các vòng chờ và trả kết quả','','| Gieo trạng thái | Quay lại | Vật mốc | Phần không thấy |','| --- | --- | --- | --- |']
    for x in r['visual_study']['waiting_and_payoff_links']:
        seq_lines.append(f"| {x['setup']} | {x['return']} | {x['object']} | {x['unseen']} |")
    seq_lines += ['', '### Hai mối nối không được bịa thêm','','Bưởi/quýt thu cuối không được cho thấy thành khối quả vàng trong món nón. Nón cuối cũng chưa được chứng minh cùng mẻ với ống bánh trước. Khi làm bản mới có thể thiết kế thêm bước nối, nhưng phải ghi là sáng tạo mới.','']
    lines[at:end]=seq_lines
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
        details=[f"# {segment['id']} — {segment['function']}",'',f"{tc(segment['start_seconds'])}–{tc(segment['end_seconds'])} · {len(members)} cú máy dự kiến · bản {a['version']} · core {a['core_version']}.", '', '[Mục lục toàn phim](../Phan_tich_dien_anh.md) · [JSON chuẩn](../phan-tich.json) · [Phiếu tái tạo](../tai-tao.json)', '', 'Độ phủ: ảnh theo thời gian, chưa phát trọn chuyển động; âm ngoài phạm vi. Đọc trạng thái/lý do thiếu của từng trường. Số người chỉ đếm ảnh mẫu, không gồm động vật.', '']
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

**Bản {a['version']} · tập trung hình ảnh, góc máy, màu sắc và chuỗi hành động. Âm ngoài phạm vi theo người dùng.**

176 hồ sơ cú máy dự kiến · 26 phiếu chuỗi · {m['visual_content_beats']} nhịp nội dung · 175 liên kết trạng thái qua điểm cắt · 13 sổ sản vật · 13 giả thuyết DNA · 43 bảng ảnh nguồn.

## Đọc theo thứ tự

1. [Phân tích có mục lục](Phan_tich_dien_anh.md): bức tranh toàn phim, 26 chuỗi chi tiết, góc/màu/lược việc và đường dẫn từng cú.
2. [Phân tích chuẩn](phan-tich.json): 25 nhóm với bằng chứng; bốn nhóm âm để null vì ngoài phạm vi. Bản đọc chỉ hiện 21 nhóm hình.
3. [Phiếu tái tạo](tai-tao.json): shots[].visual_decision cho từng cú; visual_study.sequence_designs cho chuỗi; visual_study.visual_cut_links cho 175 điểm nối. Các bản thiết kế chưa sinh thử.
4. [DNA có điều kiện](dna.json): 13 giả thuyết, điều kiện, ngoại lệ và phép kiểm. Chưa là công thức gây view.
5. [Nguồn/phương pháp](nguon.json), [ảnh/checksum](anh/manifest.json), [thống kê](metrics.json), [chỉ mục từng giây](chi-muc-giay.json).

## Các kết quả chính

- Góc cao đọc mặt phẳng/vật chứa; tầm mặt vật đọc độ dày, mặt cắt, sợi kéo và cuộn; rộng trả quan hệ người–nơi. Chọn góc theo thông tin.
- Màu có vật mang: chàm áo, nâu tre/gỗ, xanh xám nền, đỏ quả/giấy, vàng bánh. Biến đổi bề mặt kể tiến trình thô–tan–phủ–cắt–chín–gói.
- Hạt dẻ, lát quả, phôi kẹo và thịt có trạng thái chờ rồi được trả; bó rơm có công dụng muộn ở giá hồ lô.
- Không nối bịa bưởi/quýt thành phần quả vàng món cuối, hoặc ống bánh thành cùng mẻ nón nếu chưa có bước/bằng chứng.
- Giữ lực/đỡ/nhả ở dao, xẻng/lò, siro, cán phôi, cuộn, giỏ–đòn–thang và trao món.

## Phạm vi bằng chứng

Tệp tải dài 10:11.92, 1280×720, mã hóa 50fps. 1.328 mốc ảnh riêng theo toàn trục; đây không phải chứng nhận phát trọn chuyển động ở tốc độ thật. 176 cú là phân hoạch làm việc, chưa khóa mọi cut. Không đoán ống kính, khẩu, LUT/Kelvin hoặc tốc độ quay từ ảnh. Chưa có clip AI đầu ra hoặc thử khán giả.

Audio cũ được giữ để truy nguyên, không được phân tích thêm và không chặn lượt hình. Nguồn/checksum, VID_01 và lựa chọn Farm giữ nguyên. Mọi tài liệu sửa tại chỗ; lịch sử ở Git và [nhật ký chung](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/CHANGELOG.md).

[Thư viện Farm](../Thu_vien_kien_thuc/README.md) · [Core hiện hành](https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/README.md).
'''
    (BASE/'README.md').write_text(readme)
    print(json.dumps({'rendered_shots':len(a['shots']),'markdown_bytes':(BASE/'Phan_tich_dien_anh.md').stat().st_size},ensure_ascii=False))

if __name__=='__main__':main()
