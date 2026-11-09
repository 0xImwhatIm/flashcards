# Unit 4 — What Time Is The Concert?

35 supplied dinosaur illustrations are integrated: Unit 4-1 (20), Unit 4-2 (15).
Each item.image maps to its PNG and the existing renderer selects the matching
WebP under assets/optimized/unit4. No SVG redraw or unrelated artwork is used.

## Source and extraction

Four original 1280×960 JPEG sheets are preserved byte-for-byte in source/.
Their sheet order is the reverse of attachment order (photo 4 = sheet 1).
manifest.json records every word, source hash, integer crop box, dimensions,
and PNG/WebP hashes. Crops exclude headings and labels below the illustrations;
embedded lettering is retained, including weekdays, English, today and p.m.
Those images can reveal spelling hints in Spell mode; the supplied art is unchanged.

PNG preserves the decoded source pixels; WebP uses quality 88, method 6.
No enlargement or redrawing. Rebuild with Pillow installed:

    python3 assets/unit4/extract_cards.py

The script verifies source checksums and writes only the 70 mapped derivatives.
If changing source artwork or crop boxes, update manifest hashes after review.

Free means available/not busy, fan means a music fan, and sign means autograph.
Unit 3's notice-sign art remains independent. Filenames use pm, am and oclock;
the vocabulary retains p.m., a.m., and o'clock.
