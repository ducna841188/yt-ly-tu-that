"""Re-extract VID_02 screenshot atlases from its exact uploaded source.

Requires FFmpeg, Pillow, DejaVuSans. Does not perform motion playback, listening,
shot detection or semantic labeling. JPEG bytes may differ across encoder versions.
"""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,tempfile
from PIL import Image,ImageDraw,ImageFont

BASE=Path(__file__).resolve().parents[1]
def load(name):return json.loads((BASE/name).read_text())
def tc(t):return f'{int(t)//60:02d}:{t%60:05.2f}'

def main():
    parser=argparse.ArgumentParser();parser.add_argument('video');args=parser.parse_args()
    source=Path(args.video);meta=load('nguon.json');manifest=load('anh/manifest.json');analysis=load('phan-tich.json')
    sha=hashlib.sha256(source.read_bytes()).hexdigest()
    if sha!=meta['uploaded_file']['sha256']:raise SystemExit('Source checksum differs; do not apply old timestamps to another edit.')
    fontdir=Path(os.environ.get('FILM_KB_FONT_DIR','/usr/share/fonts/truetype/dejavu'))
    font=ImageFont.truetype(str(fontdir/'DejaVuSans.ttf'),14);small=ImageFont.truetype(str(fontdir/'DejaVuSans.ttf'),12)
    frames=sorted({x['frame'] for x in manifest['frames']});by_frame={n:i for i,n in enumerate(frames)}
    groups={}
    for f in manifest['frames']:
        if f['atlas']:groups.setdefault(f['atlas'],[]).append(f)
    shots={s['id']:s for s in analysis['shots']}
    with tempfile.TemporaryDirectory(prefix='vid02_frames_') as folder:
        folder=Path(folder)
        filt="select='"+'+'.join(f'eq(n,{n})' for n in frames)+"',scale=640:-1"
        subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-i',str(source),'-vf',filt,'-an','-fps_mode','vfr','-start_number','0','-q:v','2',str(folder/'%05d.jpg')],check=True)
        if len(list(folder.glob('*.jpg')))!=len(frames):raise SystemExit('Extracted frame count mismatch.')
        for name,items in groups.items():
            layout=manifest.get('layouts',{}).get(name)
            if layout:
                canvas=Image.new('RGB',(layout['width'],layout['height']),layout['background']);draw=ImageDraw.Draw(canvas)
                fnt=ImageFont.truetype(str(fontdir/'DejaVuSans.ttf'),layout['font_size'])
                for f in items:
                    x,y,w,h=f['render_box'];im=Image.open(folder/f"{by_frame[f['frame']]:05d}.jpg").resize((w,h),Image.Resampling.LANCZOS)
                    canvas.paste(im,(x,y))
                    if f['caption']:draw.text(tuple(f['caption_xy']),f['caption'],font=fnt,fill=layout['caption_color'])
                canvas.save(BASE/name,quality=92)
                continue
            dense='tiep-xuc-' in name;rows=max(f['row'] for f in items)
            width=1920 if dense else 1600;step=204 if dense else 214;header=28 if dense else 26
            canvas=Image.new('RGB',(width,rows*step+header),'#eeeeee' if dense else '#f3f0e8');draw=ImageDraw.Draw(canvas)
            draw.text((5,3),'VID_02 - anh lay mau; chua phat chuyen dong toc do thuc / chua nghe am',font=font,fill='black')
            labeled=set()
            for f in items:
                x=(f['column']-1)*320;y=(f['row']-1)*step+header
                if not dense and f['row'] not in labeled:
                    s=shots[f['shot_id']];draw.text((5,y+1),f"{s['id']} | {tc(s['start_seconds'])} - {tc(s['end_seconds'])} | {s['end_seconds']-s['start_seconds']:.2f}s",font=font,fill='black');labeled.add(f['row'])
                image=Image.open(folder/f"{by_frame[f['frame']]:05d}.jpg").resize((320,180),Image.Resampling.LANCZOS)
                canvas.paste(image,(x,y+(22 if dense else 31)))
                draw.text((x+4,y+(2 if dense else 17)),f"{f['seconds']:.2f}s",font=font if dense else small,fill='black')
            canvas.save(BASE/name,quality=90)
    manifest['files']=[]
    for name in sorted(groups):
        b=(BASE/name).read_bytes();manifest['files'].append({'path':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
    (BASE/'anh/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'atlases':len(groups),'frames':len(frames),'motion_or_audio_review_performed':False}))

if __name__=='__main__':main()
