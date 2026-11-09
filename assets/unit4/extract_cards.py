"""Rebuild Unit 4 raster cards from preserved user sheets. Requires Pillow."""
from pathlib import Path
import hashlib
import json
from PIL import Image


def main():
    root = Path(__file__).resolve().parents[2]
    manifest = json.loads((root / 'assets/unit4/manifest.json').read_text())
    # Validate all sources before writing any output.
    sources = {}
    for item in manifest['items']:
        path = root / item['source_image']
        if hashlib.sha256(path.read_bytes()).hexdigest() != item['source_sha256']:
            raise ValueError(f'Source checksum changed: {path}')
        if path not in sources:
            with Image.open(path) as image:
                sources[path] = image.convert('RGB')
        left, top, right, bottom = item['crop_box']
        width, height = sources[path].size
        if not (0 <= left < right <= width and 0 <= top < bottom <= height):
            raise ValueError(f'Invalid crop: {item["slug"]}')
    for item in manifest['items']:
        crop = sources[root / item['source_image']].crop(item['crop_box'])
        png, webp = root / item['image'], root / item['webp']
        png.parent.mkdir(parents=True, exist_ok=True)
        webp.parent.mkdir(parents=True, exist_ok=True)
        crop.save(png, optimize=True)
        crop.save(webp, 'WEBP', quality=88, method=6)
    print(f'Rebuilt {len(manifest["items"])} PNG/WebP pairs.')


if __name__ == '__main__':
    main()
