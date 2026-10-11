"""Restore the unchanged uploaded workbook from its ordered binary parts."""
from pathlib import Path
import hashlib
import json


def restore():
    folder = Path(__file__).resolve().parent
    manifest = json.loads((folder / 'manifest.json').read_text(encoding='utf-8'))
    source = bytearray()
    for item in manifest['parts']:
        name = item['path']
        if Path(name).name != name:
            raise ValueError('Invalid part filename')
        data = (folder / name).read_bytes()
        if len(data) != item['bytes'] or hashlib.sha256(data).hexdigest() != item['sha256']:
            raise ValueError(f'Part integrity check failed: {name}')
        source.extend(data)
    if len(source) != manifest['bytes'] or hashlib.sha256(source).hexdigest() != manifest['sha256']:
        raise ValueError('Complete workbook integrity check failed')
    output = folder.parent / manifest['archived_filename']
    if output.exists():
        if hashlib.sha256(output.read_bytes()).hexdigest() == manifest['sha256']:
            print(f'Already restored and verified: {output}')
            return
        raise FileExistsError(f'Refusing to replace another file: {output}')
    output.write_bytes(source)
    print(f'Restored and SHA-256 verified: {output}')


if __name__ == '__main__':
    restore()
