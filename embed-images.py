# Inlines every image from the images folder into the case study so the
# encrypted page is fully self contained. Run from inside the private folder:
#   python3 embed-images.py
import base64, mimetypes, os, re
src = open('case-study-source.html', encoding='utf-8').read()
def inline(m):
    path = m.group(1)
    if not os.path.exists(path):
        print('missing, placeholder kept:', path); return m.group(0)
    mime = mimetypes.guess_type(path)[0] or 'image/png'
    data = base64.b64encode(open(path, 'rb').read()).decode()
    print('embedded:', path); return 'src="data:%s;base64,%s"' % (mime, data)
out = re.sub(r'src="(images/[^"]+)"', inline, src)
open('case-study.html', 'w', encoding='utf-8').write(out)
print('wrote case-study.html')
