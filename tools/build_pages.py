"""Sinh các trang dịch vụ tĩnh (chạy: python3 tools/build_pages.py).

Sửa nội dung trong PAGES rồi chạy lại để cập nhật các file */index.html.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://haiquan.shop"
MAPS = "https://www.google.com/maps/search/?api=1&query=Ch%E1%BB%A3+V%C4%A9nh+%C4%90i%E1%BB%87n%2C+%C4%90i%E1%BB%87n+B%C3%A0n"
FB = "https://www.facebook.com/hai.nguyenduy.3745"
AREA = ["Điện Bàn", "Vĩnh Điện", "Đà Nẵng", "Quảng Nam"]

PAGES = [
    {
        "slug": "xe-tai-dien-ban",
        "share": "share-xe-tai.jpg",
        "nav": "Chở hàng",
        "title": "Xe tải chở hàng Điện Bàn – Thuê xe tải, xe lôi | Hải Quân",
        "desc": "Thuê xe tải chở hàng ở Điện Bàn, Vĩnh Điện: chở đồ đạc, dọn nhà, vật liệu xây dựng, hàng cồng kềnh, tuyến gần – xa. Gọi anh Hải 0707 477 243, anh Quân 0783 346 050.",
        "h1": "Xe tải chở hàng ở Điện Bàn",
        "lede": "Thuê xe tải, xe con, xe lôi, xe bò chở đồ đạc, vật liệu xây dựng và hàng cồng kềnh. Xe xuất phát từ bãi gần Chợ Vĩnh Điện, tuyến gần – xa đều nhận.",
        "phone": ("0707477243", "0707 477 243", "Gọi anh Hải"),
        "hero": ("xe-tai-cho-do.webp", 900, 1200, "Xe tải Hải Quân chở đầy đồ đạc dọn nhà, đậu trước bãi hàng ở Vĩnh Điện"),
        "service": "Vận chuyển hàng hóa bằng xe tải",
        "body": """
<h2>Chở những gì</h2>
<ul>
  <li>Đồ đạc trong nhà, dọn nhà, chuyển phòng trọ</li>
  <li>Vật liệu xây dựng: cát, đá, gạch, xi măng, ván</li>
  <li>Dàn giáo, mâm sắt, ván cho công trình</li>
  <li>Hàng cồng kềnh, hàng nặng, hàng nhẹ số lượng lớn</li>
  <li>Đất, xà bần bằng xe lôi vào hẻm nhỏ</li>
</ul>
<p>Nhận chở cho cá nhân, hộ gia đình và doanh nghiệp, theo yêu cầu, tuyến gần trong Điện Bàn hay tuyến xa hơn.</p>

<h2>Bốn loại xe</h2>
<ul class="rows">
  <li><b>Xe tải</b><span>hàng nặng, vật liệu, dàn giáo</span></li>
  <li><b>Xe con</b><span>hàng nhẹ, cần đi nhanh</span></li>
  <li><b>Xe lôi (ba gác)</b><span>hẻm nhỏ, đất, xà bần</span></li>
  <li><b>Xe bò</b><span>quãng ngắn trong công trình</span></li>
</ul>

<h2 style="margin-top:40px">Đặt xe thế nào</h2>
<ol class="steps">
  <li>Gọi hoặc nhắn Zalo anh Hải 0707 477 243 (hoặc anh Quân 0783 346 050).</li>
  <li>Báo chỗ lấy hàng, chỗ giao, loại hàng và khối lượng ước chừng.</li>
  <li>Nghe báo giá chuyến, chốt giờ, xe tới đúng hẹn.</li>
</ol>
""",
        "photos": [
            ("xi-mang-gach.webp", 700, 933, "Xe tải đậu cạnh bao xi măng và gạch chờ chở đi"),
            ("do-dat-xe-loi.webp", 900, 1200, "Xe lôi đổ đất xuống sân nhà khách"),
        ],
        "faq": [
            ("Thuê xe tải chở hàng ở Điện Bàn giá bao nhiêu?",
             "Giá tính theo chuyến, tùy quãng đường, loại xe và loại hàng. Gọi 0707 477 243 báo điểm đi, điểm đến để nghe giá trước khi chở."),
            ("Có nhận chở dọn nhà không?",
             "Có. Hải Quân nhận chở đồ đạc cho hộ gia đình, dọn nhà, chuyển phòng trọ bằng xe tải hoặc xe lôi tùy lượng đồ."),
            ("Có chở đi xa ngoài Điện Bàn không?",
             "Có, tuyến gần – xa đều nhận. Báo điểm giao khi gọi để được sắp xe phù hợp."),
            ("Xe xuất phát từ đâu?",
             "Từ bãi hàng gần Chợ Vĩnh Điện, Điện Bàn (TP. Đà Nẵng, trước đây thuộc Quảng Nam)."),
        ],
    },
    {
        "slug": "cho-thue-dan-giao-dien-ban",
        "share": "share-dan-giao.jpg",
        "nav": "Dàn giáo",
        "title": "Cho thuê, mua bán dàn giáo (dàn tiệp) Điện Bàn | Hải Quân",
        "desc": "Cho thuê và mua bán dàn giáo, dàn tiệp mới và cũ ở Điện Bàn, gần Chợ Vĩnh Điện. Có sẵn ở bãi, mâm sắt, ván, chở tới công trình. Gọi 0363 569 319.",
        "h1": "Cho thuê, mua bán dàn giáo ở Điện Bàn",
        "lede": "Dàn giáo (dân mình hay gọi là dàn tiệp) mới và cũ, có sẵn ở bãi gần Chợ Vĩnh Điện. Bán, cho thuê, thu mua lại, kèm mâm sắt và ván. Gọi là chở tới công trình.",
        "phone": ("0363569319", "0363 569 319", "Gọi hỏi giá"),
        "hero": ("khung-dan-giao.webp", 900, 1200, "Khung dàn giáo mạ kẽm dựng thành hàng ở bãi Hải Quân, Điện Bàn"),
        "service": "Cho thuê và mua bán dàn giáo",
        "body": """
<h2>Có gì ở bãi</h2>
<ul class="rows">
  <li><b>Khung dàn giáo (dàn tiệp) mới</b><span>bán · cho thuê</span></li>
  <li><b>Dàn giáo cũ còn dùng tốt</b><span>bán · thu mua</span></li>
  <li><b>Mâm sắt</b><span>bán · cho thuê</span></li>
  <li><b>Ván</b><span>bán</span></li>
</ul>
<p style="margin-top:20px">Hàng xếp sẵn ở bãi, xem tận nơi được. Công trình đang thiếu dàn giáo thì gọi, Hải Quân chở tới bằng xe tải hoặc xe ba gác.</p>

<h2 style="margin-top:40px">Thuê dàn giáo thế nào</h2>
<ol class="steps">
  <li>Gọi 0363 569 319 hoặc nhắn Zalo 0707 477 243.</li>
  <li>Báo số bộ cần, thời gian thuê và địa chỉ công trình.</li>
  <li>Nghe báo giá, hẹn ngày giao. Hết hạn thuê, xe tới thu về.</li>
</ol>
""",
        "photos": [
            ("bai-dan-giao.webp", 900, 1200, "Dàn giáo dựng dọc tường bãi, xe ba gác chở dàn giáo phía sau"),
            ("dan-giao-ven-duong.webp", 900, 1200, "Dàn giáo bày ven đường trước biển hiệu Hải bán"),
        ],
        "faq": [
            ("Dàn tiệp và dàn giáo có khác nhau không?",
             "Là một. Ở Điện Bàn, Quảng Nam nhiều người gọi dàn giáo là dàn tiệp. Biển ở bãi ghi cả mua bán và cho thuê dàn tiệp."),
            ("Thuê dàn giáo ở Điện Bàn tính giá thế nào?",
             "Báo theo số bộ và thời gian thuê. Gọi 0363 569 319 để nghe giá hôm nay."),
            ("Có thu mua dàn giáo cũ không?",
             "Có. Hải Quân mua bán dàn giáo cả mới và cũ, gọi mô tả số lượng và tình trạng để được báo giá."),
            ("Có chở dàn giáo tới công trình không?",
             "Có. Dàn giáo sẵn kho, gọi là chở tới bằng xe của Hải Quân."),
        ],
    },
    {
        "slug": "vat-lieu-xay-dung-dien-ban",
        "share": "share-vat-lieu.jpg",
        "nav": "Vật liệu",
        "title": "Vật liệu xây dựng Điện Bàn – Cát, đá, gạch, xi măng | Hải Quân",
        "desc": "Bán cát, đá, gạch, xi măng, ván ở Điện Bàn, gần Chợ Vĩnh Điện. Chở tận nơi bằng xe tải, xe lôi. Gọi 0363 569 319.",
        "h1": "Cát, đá, gạch, xi măng ở Điện Bàn",
        "lede": "Vật liệu xây dựng cho nhà dân và công trình nhỏ, lấy tại bãi gần Chợ Vĩnh Điện hoặc chở tận nơi bằng xe tải, xe lôi của Hải Quân.",
        "phone": ("0363569319", "0363 569 319", "Gọi hỏi giá"),
        "hero": ("boc-gach-len-xe.webp", 700, 933, "Bốc gạch lên xe tải để giao cho khách ở Điện Bàn"),
        "service": "Bán vật liệu xây dựng",
        "body": """
<h2>Vật liệu có bán</h2>
<ul class="rows">
  <li><b>Gạch</b><span>theo xe</span></li>
  <li><b>Xi măng</b><span>theo bao</span></li>
  <li><b>Cát</b><span>theo khối</span></li>
  <li><b>Đá</b><span>theo khối</span></li>
  <li><b>Ván ép, ván gỗ</b><span>theo tấm</span></li>
</ul>
<p style="margin-top:20px">Mua kèm dàn giáo và thuê xe chở cùng một chỗ, đỡ phải gọi nhiều nơi.</p>

<h2 style="margin-top:40px">Đặt vật liệu thế nào</h2>
<ol class="steps">
  <li>Gọi 0363 569 319, báo loại vật liệu và số lượng.</li>
  <li>Báo địa chỉ giao, đường có vào được xe tải hay cần xe lôi.</li>
  <li>Nghe báo giá cả hàng lẫn tiền chở, hẹn giờ giao.</li>
</ol>
""",
        "photos": [
            ("xi-mang-gach.webp", 700, 933, "Bao xi măng và gạch xếp sẵn chờ giao"),
            ("van-ep.webp", 700, 933, "Ván ép phủ phim lót kín thùng xe"),
        ],
        "faq": [
            ("Có giao vật liệu tận nơi ở Điện Bàn không?",
             "Có. Hải Quân có xe tải và xe lôi, giao được cả nhà trong hẻm nhỏ."),
            ("Giá cát, đá, gạch, xi măng hôm nay bao nhiêu?",
             "Giá thay đổi theo đợt hàng. Gọi 0363 569 319 để nghe giá hôm nay, kèm tiền chở tới chỗ bạn."),
            ("Bãi vật liệu ở đâu?",
             "Gần Chợ Vĩnh Điện, Điện Bàn (TP. Đà Nẵng, trước đây thuộc Quảng Nam)."),
        ],
    },
]

NAV = [("/cho-thue-dan-giao-dien-ban/", "Dàn giáo"), ("/vat-lieu-xay-dung-dien-ban/", "Vật liệu"),
       ("/xe-tai-dien-ban/", "Chở hàng"), ("/#lien-he", "Liên hệ")]


def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def page(p):
    url = f"{SITE}/{p['slug']}/"
    tel, tel_txt, tel_label = p["phone"]
    img, w, h, alt = p["hero"]
    nav = "\n".join(
        f'        <li><a href="{href}"{" aria-current=\"page\"" if label == p["nav"] else ""}>{label}</a></li>'
        for href, label in NAV)
    photos = "\n".join(
        f'      <figure class="ph"><img src="/images/{f}" width="{fw}" height="{fh}" loading="lazy" alt="{esc(a)}"></figure>'
        for f, fw, fh, a in p["photos"])
    faq_html = "\n".join(f"      <h3>{q}</h3>\n      <p>{a}</p>" for q, a in p["faq"])
    others = "\n".join(
        f'      <a href="/{o["slug"]}/"><b>{o["h1"]}</b><span>{o["lede"].split(".")[0]}.</span></a>'
        for o in PAGES if o is not p)
    ld = [
        {"@context": "https://schema.org", "@type": "Service", "name": p["service"],
         "serviceType": p["service"], "url": url, "description": p["desc"],
         "image": f"{SITE}/images/{img}",
         "provider": {"@id": f"{SITE}/#business"},
         "areaServed": [{"@type": "City", "name": a} for a in AREA]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Hải Quân", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": p["h1"], "item": url}]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in p["faq"]]},
    ]
    return f"""<!doctype html>
<html lang="vi" data-type="place">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p['title']}</title>
<meta name="description" content="{esc(p['desc'])}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#f6f4ef">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:locale" content="vi_VN">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Hải Quân Điện Bàn">
<meta property="og:title" content="{esc(p['title'])}">
<meta property="og:description" content="{esc(p['desc'])}">
<meta property="og:image" content="{SITE}/images/{p['share']}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(p['h1'])} – Hải Quân, gọi {tel_txt}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=1)}
</script>
</head>
<body>
<a class="skip" href="#main">Bỏ qua, tới nội dung</a>

<header class="nav">
  <div class="wrap">
    <a class="mark" href="/"><i aria-hidden="true"></i>Hải Quân</a>
    <nav aria-label="Mục lục">
      <ul>
{nav}
      </ul>
    </nav>
    <a class="btn" href="tel:{tel}">{tel_label} {tel_txt}</a>
  </div>
</header>

<main id="main">

<section class="hero">
  <div class="wrap grid" data-enter>
    <div class="hero-text">
      <p class="crumbs"><a href="/">Hải Quân</a> / {p['nav']}</p>
      <h1>{p['h1']}</h1>
      <p class="lede">{p['lede']}</p>
      <div class="hero-actions">
        <a class="btn" href="tel:{tel}">{tel_label} {tel_txt}</a>
        <a class="link" href="https://zalo.me/0707477243" target="_blank" rel="noopener">Nhắn Zalo 0707 477 243 <span class="arr">→</span></a>
      </div>
    </div>
    <figure class="ph hero-ph">
      <img src="/images/{img}" width="{w}" height="{h}" alt="{esc(alt)}" fetchpriority="high">
    </figure>
  </div>
</section>

<section class="alt">
  <div class="wrap grid">
    <div class="prose">
{p['body']}
    </div>
    <aside class="aside">
      <div class="visit-panel">
        <p class="label" style="margin:0 0 12px">Bãi hàng gần Chợ Vĩnh Điện</p>
        <ul class="phones">
          <li><span>Dàn giáo, vật liệu</span><a href="tel:0363569319">0363 569 319</a></li>
          <li><span>Anh Hải (Zalo)</span><a href="tel:0707477243">0707 477 243</a></li>
          <li><span>Anh Quân</span><a href="tel:0783346050">0783 346 050</a></li>
        </ul>
        <a class="link" href="{MAPS}" target="_blank" rel="noopener">Xem đường tới bãi <span class="arr">→</span></a>
      </div>
    </aside>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="pair">
{photos}
    </div>
  </div>
</section>

<section class="alt" aria-labelledby="h-faq">
  <div class="wrap">
    <h2 id="h-faq">Câu hỏi hay gặp</h2>
    <div class="faq">
{faq_html}
    </div>
  </div>
</section>

<section aria-labelledby="h-more">
  <div class="wrap">
    <h2 id="h-more" style="margin-bottom:32px">Hải Quân còn làm</h2>
    <div class="more-services">
{others}
      <a href="/"><b>Xem tất cả ở trang chủ</b><span>Ảnh bãi hàng và số điện thoại.</span></a>
    </div>
  </div>
</section>

</main>

<footer>
  <div class="wrap grid">
    <p class="f-addr"><a href="{MAPS}" target="_blank" rel="noopener">Gần Chợ Vĩnh Điện,<br>Điện Bàn, Đà Nẵng</a></p>
    <div class="f-col">
      <p class="label">Gọi</p>
      <p><a href="tel:0363569319">0363 569 319</a> · dàn giáo</p>
      <p><a href="tel:0707477243">0707 477 243</a> · anh Hải</p>
      <p><a href="tel:0783346050">0783 346 050</a> · anh Quân</p>
    </div>
    <div class="f-col">
      <p class="label">Dịch vụ</p>
      <p><a href="/cho-thue-dan-giao-dien-ban/">Cho thuê dàn giáo Điện Bàn</a></p>
      <p><a href="/vat-lieu-xay-dung-dien-ban/">Vật liệu xây dựng Điện Bàn</a></p>
      <p><a href="/xe-tai-dien-ban/">Xe tải chở hàng Điện Bàn</a></p>
      <p><a href="{FB}" target="_blank" rel="noopener">Facebook</a></p>
    </div>
    <p class="legal">© 2026 Hải Quân · haiquan.shop</p>
  </div>
</footer>

<nav class="actionbar" aria-label="Gọi nhanh">
  <a href="tel:{tel}">Gọi ngay</a>
  <a href="https://zalo.me/0707477243" target="_blank" rel="noopener">Nhắn Zalo</a>
</nav>
</body>
</html>
"""


def sitemap():
    urls = [f"{SITE}/"] + [f"{SITE}/{p['slug']}/" for p in PAGES]
    body = "\n".join(f"  <url><loc>{u}</loc><lastmod>2026-11-21</lastmod></url>" for u in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n'


if __name__ == "__main__":
    for p in PAGES:
        d = os.path.join(ROOT, p["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(page(p))
        print("wrote", p["slug"])
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap())
    print("wrote sitemap.xml")
