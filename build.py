#!/usr/bin/env python3
"""The Plain Bar — template-v2 T1 site builder (9 files, 7 core pages).
Facts only, source-gated (card t_46a9eb44): Longview News-Journal Business Beat 2026-11-16.
Pre-launch site: opening planned mid-January 2027, hours/phone/menu unpublished -> omitted, never guessed.
"""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "public")

SITE = "The Plain Bar"
CITY = "Longview, TX"
ORIGIN = "https://the-plain-bar-demo.up.railway.app"   # pinned demo host (canonical/sitemap)
ADDR_STREET = "3500 McCann Rd STE H07B"
ADDR_FULL = "3500 McCann Rd STE H07B, Longview, TX 75604"
ADDR_CITY = "Longview, TX 75604"
EMAIL = "demarkus@acktl.com"
LAT, LON = 32.5385423, -94.7501096                    # Nominatim: 3500 McCann Rd (Longview Mall anchors)
NEWS_URL = "https://news-journal.com/2026-11-16/business-beat-robroy-starts-renovations-at-new-longview-facility/"
MAP_Q = "3500%20McCann%20Rd%20STE%20H07B%2C%20Longview%2C%20TX%2075604"
DIRS = "https://www.google.com/maps/dir/?api=1&destination=3500%20McCann%20Rd%20STE%20H07B%2C%20Longview%2C%20TX%2075604"
BUILT = "BUILT-2026-11-18"

# ------------------------------------------------------------------ shared parts
def head(title, desc, path, noindex=False):
    canonical = ORIGIN + path
    robots = '\n  <meta name="robots" content="noindex">' if noindex else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<!-- {BUILT} -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">{robots}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{ORIGIN}/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{ORIGIN}/og.png">
<link rel="icon" href="/favicon.svg">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header>
  <div class="wrap headrow">
    <a class="brand" href="/">The Plain Bar<span class="brandtag">Longview Mall · opening soon</span></a>
    <nav aria-label="Main">
      <a href="/">Home</a>
      <a href="/events">Events</a>
      <a href="/sunday-brunch">Brunch</a>
      <a href="/book-nights">Book nights</a>
      <a href="/cocktail-classes">Classes</a>
      <a class="btn ghost sm" href="/contact">Say hello</a>
    </nav>
  </div>
</header>
<main id="main">
"""

FOOTER = f"""</main>
<footer>
  <div class="wrap">
    <div class="fgrid">
      <div>
        <h4>The Plain Bar</h4>
        <address class="nap">New neighborhood bar · inside Longview Mall · opening soon<br>
        {ADDR_STREET}<br>{ADDR_CITY}<br>
        <a href="mailto:{EMAIL}">{EMAIL}</a></address>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="/events">Events</a></li>
          <li><a href="/sunday-brunch">Sunday brunch</a></li>
          <li><a href="/book-nights">Book nights</a></li>
          <li><a href="/cocktail-classes">Cocktail classes</a></li>
          <li><a href="/contact">Contact &amp; directions</a></li>
          <li><a href="/privacy">Privacy</a></li>
        </ul>
      </div>
      <div>
        <h4>Find Us</h4>
        <ul>
          <li><a href="{DIRS}" target="_blank" rel="noopener">Get directions</a></li>
          <li><a href="https://www.google.com/maps?q={MAP_Q}" target="_blank" rel="noopener">See the map</a></li>
          <li><a href="mailto:{EMAIL}">Email the owner</a></li>
        </ul>
      </div>
    </div>
    <div class="footline"><span>© 2026 The Plain Bar · {ADDR_STREET}, {ADDR_CITY}</span>
    <span>Opening planned for mid-January 2027</span></div>
  </div>
</footer>
</body>
</html>
"""

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>\n'

def breadcrumb(trail):
    items = ", ".join(f'{{"@type":"ListItem","position":{i+1},"name":{json.dumps(n)},"item":{json.dumps(ORIGIN+p)}}}' for i,(n,p) in enumerate(trail))
    return ld({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":json.loads("["+items+"]")})

def faq(pairs):
    q = [{"@type":"Question","name":n,"acceptedAnswer":{"@type":"Answer","text":a}} for n,a in pairs]
    return {"@type":"FAQPage","mainEntity":q}

def crumbbar(trail):
    parts = ' › '.join(f'<a href="{p}">{n}</a>' if i < len(trail)-1 else n for i,(n,p) in enumerate(trail))
    return f'<nav class="crumbs" aria-label="Breadcrumb">{parts}</nav>\n'

def cta_band(head_txt, sub_txt):
    return f"""  <section class="band">
    <div class="wrap bandrow">
      <div>
        <h2>{head_txt}</h2>
        <p>{sub_txt}</p>
      </div>
      <p class="bandcta"><a class="btn" href="/contact">Contact the bar</a></p>
    </div>
  </section>
"""

def mapbox(title_attr):
    return f"""      <div class="map">
        <iframe src="https://www.google.com/maps?q={MAP_Q}&amp;output=embed" title="{title_attr}" loading="lazy"></iframe>
      </div>
"""

MAP_TITLE = "Map: The Plain Bar, 3500 McCann Rd STE H07B, Longview, TX 75604"

# ------------------------------------------------------------------ home
home = head(
    "The Plain Bar — New Neighborhood Bar, Longview TX",
    "A new bar inside Longview Mall, 3500 McCann Rd STE H07B, Longview TX — Sunday brunches, book nights and date-night cocktail classes planned for opening, targeted mid-January 2027.",
    "/") + f"""  <section class="hero">
    <div class="wrap">
      <p class="eyebrow">Opening soon · Longview Mall · Longview, Texas</p>
      <h1>A plain name for a bar built around getting together.</h1>
      <p class="lede">The Plain Bar is a new neighborhood bar inside Longview Mall at 3500 McCann Road. Sunday brunches, book nights and date-night cocktail classes are already on the plan — the doors are targeted to open mid-January 2027.</p>
      <p class="herocta"><a class="btn" href="/contact">Say hello before we open</a> <a class="btn ghost" href="/events">See what's planned</a></p>
    </div>
  </section>

  <section class="strip">
    <div class="wrap striprow">
      <p><span class="k">Where</span> Inside Longview Mall — {ADDR_STREET}, {ADDR_CITY}</p>
      <p><span class="k">When</span> Opening targeted mid-January 2027 — hours post the week we open</p>
      <p><span class="k">Who</span> Owner DeMarkus King · licensed by TABC (permit MB200168843)</p>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <p class="eyebrow">01 · What's already on the plan</p>
      <h2>Three things the owner has promised before a single door has opened.</h2>
      <div class="cards">
        <a class="card" href="/sunday-brunch">
          <h3>Sunday brunches</h3>
          <p>A midday Sunday table at the bar — food, drinks, and somewhere to sit with people you like.</p>
          <span class="more">Details →</span>
        </a>
        <a class="card" href="/book-nights">
          <h3>Book nights</h3>
          <p>Regular evenings for readers — one of the first events planned for the bar.</p>
          <span class="more">Details →</span>
        </a>
        <a class="card" href="/cocktail-classes">
          <h3>Cocktail classes</h3>
          <p>Date-night classes designed for two, planned as part of the opening lineup.</p>
          <span class="more">Details →</span>
        </a>
      </div>
    </div>
  </section>

  <section class="sec alt">
    <div class="wrap">
      <p class="eyebrow">02 · The story so far</p>
      <h2>Renovation is already underway.</h2>
      <p>Owner DeMarkus King is turning a 900-square-foot space inside Longview Mall into the kind of bar Longview can walk into without a plan — and filling the calendar before the opening: brunch on Sundays, book nights, and classes for people who want to get better at making a drink. The team is just forming; the bar is hiring its first bar manager now.</p>
      <p class="src">Announced in the Longview News-Journal Business Beat, November 16, 2026 — <a href="{NEWS_URL}" target="_blank" rel="noopener">read the report</a>.</p>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <p class="eyebrow">03 · Find the space</p>
      <h2>Inside Longview Mall, off McCann Road.</h2>
      <div class="visit">
        <div class="visitcopy">
          <p>Unit H07B, on the mall side of 3500 McCann Road. Entrance and parking notes will post here the week we open.</p>
          <p class="honest">No phone line yet — email reaches the owner directly: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
        </div>
{mapbox(MAP_TITLE)}      </div>
    </div>
  </section>
""" + cta_band("Questions before opening? Ask.", "The form on the contact page emails the bar directly — the owner answers.") + """  <section class="ldwrap">
""" + ld({
    "@context": "https://schema.org",
    "@type": "BarOrPub",
    "name": SITE,
    "image": ORIGIN + "/og.png",
    "description": "New neighborhood bar inside Longview Mall — Sunday brunches, book nights and date-night cocktail classes planned for opening, targeted mid-January 2027.",
    "address": {"@type": "PostalAddress", "streetAddress": ADDR_STREET, "addressLocality": "Longview", "addressRegion": "TX", "postalCode": "75604", "addressCountry": "US"},
    "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LON},
    "url": ORIGIN + "/",
    "email": EMAIL,
    "openingDate": "2027-01-15",
    "parentOrganization": {"@type": "Organization", "name": "Longview Mall"}
}) + """</section>
""" + FOOTER

# ------------------------------------------------------------------ events hub
events = head(
    "Events — The Plain Bar, Longview TX",
    "The planned event lineup at The Plain Bar, a new bar inside Longview Mall: Sunday brunches, book nights and date-night cocktail classes, opening targeted mid-January 2027.",
    "/events") + crumbbar([("Home","/"),("Events","/events")]) + f"""  <section class="hero slim">
    <div class="wrap">
      <p class="eyebrow">Events · The Plain Bar · Longview Mall</p>
      <h1>What's planned, before it's promised.</h1>
      <p class="lede">The bar has not opened yet, so this is the honest list: three kinds of gatherings the owner has already announced for the calendar. Schedules, menus and prices post here the week we open — whatever lands here is true.</p>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <div class="cards">
        <a class="card" href="/sunday-brunch">
          <h3>Sunday brunches</h3>
          <p>Announced plan: a regular Sunday brunch — a midday table with food and drinks at the bar.</p>
          <span class="more">Brunch details →</span>
        </a>
        <a class="card" href="/book-nights">
          <h3>Book nights</h3>
          <p>Announced plan: regular evenings built around reading — a home for Longview readers at the bar.</p>
          <span class="more">Book night details →</span>
        </a>
        <a class="card" href="/cocktail-classes">
          <h3>Date-night cocktail classes</h3>
          <p>Announced plan: classes for two — come with someone and learn how the drinks get made.</p>
          <span class="more">Class details →</span>
        </a>
      </div>
      <p class="note">The lineup will grow — event ideas are announced on this page first, and the opening date itself posts here the moment it is set.</p>
    </div>
  </section>
""" + cta_band("Want something to happen here?", "Brunch, books, classes — or your own idea for the calendar. Tell the bar.") + """  <section class="ldwrap">
""" + ld({"@context": "https://schema.org", "@graph": [
    {"@type": "ItemList", "name": "Events at The Plain Bar", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Sunday brunches", "url": ORIGIN + "/sunday-brunch"},
        {"@type": "ListItem", "position": 2, "name": "Book nights", "url": ORIGIN + "/book-nights"},
        {"@type": "ListItem", "position": 3, "name": "Date-night cocktail classes", "url": ORIGIN + "/cocktail-classes"}]}
]}) + """</section>
""" + FOOTER

# ------------------------------------------------------------------ service detail helper
def detail(fname, title, desc, path, eyebrow, h1, paras, faq_pairs, service_name, graph_type_extra=None):
    body = head(title, desc, path) + crumbbar([("Home","/"),("Events","/events"),(h1.split(" — ")[0] if "—" in h1 else service_name, path)])
    body += f"""  <section class="hero slim">
    <div class="wrap">
      <p class="eyebrow">{eyebrow}</p>
      <h1>{h1}</h1>
      <p class="lede">{paras[0]}</p>
    </div>
  </section>

  <section class="sec">
    <div class="wrap narrow">
"""
    for p in paras[1:]:
        body += f"      <p>{p}</p>\n"
    body += f"""      <p class="honest">Start times, menus and prices are not set yet — the bar is targeting a mid-January 2027 opening and details post when they exist. <a href="/contact">Ask the bar</a> and you'll get a straight answer.</p>
    </div>
  </section>

  <section class="sec alt">
    <div class="wrap narrow">
      <p class="eyebrow">Questions people ask</p>
      <h2>Before it opens</h2>
      <dl class="faqlist">
"""
    for q, a in faq_pairs:
        body += '        <div class="faq"><dt>' + q + "</dt><dd>" + a + "</dd></div>\n"
    body += """      </dl>
    </div>
  </section>
""" + cta_band("Be there when it starts.", "Email the bar through the contact form — the owner answers directly.") + "  <section class=\"ldwrap\">\n"
    graph = [
        {"@type": "Service", "name": service_name, "serviceType": service_name,
         "provider": {"@type": "BarOrPub", "name": SITE, "address": {"@type": "PostalAddress", "streetAddress": ADDR_STREET, "addressLocality": "Longview", "addressRegion": "TX", "postalCode": "75604", "addressCountry": "US"}},
         "areaServed": {"@type": "City", "name": "Longview, TX"},
         "url": ORIGIN + path}
    ]
    if graph_type_extra:
        graph.extend(graph_type_extra)
    body += ld({"@context": "https://schema.org", "@graph": graph}) + "</section>\n" + FOOTER
    return body

sunday_brunch = detail(
    "sunday-brunch.html",
    "Sunday Brunch — The Plain Bar, Longview TX",
    "A planned Sunday brunch at The Plain Bar, the new bar inside Longview Mall, 3500 McCann Rd STE H07B, Longview TX — a midday Sunday table with food and drinks, opening targeted mid-January 2027.",
    "/sunday-brunch",
    "Planned event · The Plain Bar · Longview Mall",
    "Sunday brunch in Longview, coming to Longview Mall",
    ["The Plain Bar's opening plan includes a regular Sunday brunch — the bar's version of a midday Sunday table: something to eat, something to drink, and room to sit with people you like without leaving the mall.",
     "Announced by owner DeMarkus King in the News-Journal Business Beat as one of the bar's first commitments. The menu, the start time and whether Sundays are all-day will be set with the opening — targeted mid-January 2027 — and posted on this page the week they're decided."],
    [("When does Sunday brunch start?",
      "With the bar itself. The Plain Bar's opening is targeted for mid-January 2027, and the exact brunch start time will be posted on this site as soon as it is set."),
     ("Where is The Plain Bar?",
      "Inside Longview Mall at 3500 McCann Rd STE H07B, Longview, TX 75604."),
     ("Is there a brunch menu yet?",
      "Not yet. The menu is being planned and will be published here before opening — nothing on this site is guessed."),
     ("Do I need a reservation for brunch?",
      "That isn't decided yet. Email the bar through the contact form and the owner will tell you where things stand when you ask.")],
    "Sunday brunch")

book_nights = detail(
    "book-nights.html",
    "Book Nights — The Plain Bar, Longview TX",
    "Book nights are planned at The Plain Bar, the new bar inside Longview Mall, 3500 McCann Rd STE H07B, Longview TX — regular evenings for readers, opening targeted mid-January 2027.",
    "/book-nights",
    "Planned event · The Plain Bar · Longview Mall",
    "Book nights in Longview — a reading crowd at a mall bar",
    ["One of the first events announced for The Plain Bar is a book night: a regular evening at the bar built around what people are reading — a place for Longview readers to show up with a book and leave with opinions.",
     "The format — which night, how often, whether there's a theme or a featured title — is part of the opening plan owner DeMarkus King announced in the News-Journal Business Beat, and the specifics will post here as soon as they're locked in. The bar's opening is targeted for mid-January 2027."],
    [("When is book night?",
      "The day and time aren't set yet — they come with the opening, targeted for mid-January 2027, and will be posted here the week they're announced."),
     ("Do I have to bring a book?",
      "That's the spirit of it. The exact format — hosted or open, themed or free — is still being planned; ask the bar and the owner will tell you what's decided."),
     ("Where is The Plain Bar?",
      "Inside Longview Mall at 3500 McCann Rd STE H07B, Longview, TX 75604."),
     ("Will book nights serve alcohol?",
      "Yes — The Plain Bar is a licensed bar, permitted by the Texas Alcoholic Beverage Commission under permit MB200168843.")],
    "Book nights")

cocktail_classes = detail(
    "cocktail-classes.html",
    "Cocktail Classes — The Plain Bar, Longview TX",
    "Date-night cocktail classes are planned at The Plain Bar, the new bar inside Longview Mall, 3500 McCann Rd STE H07B, Longview TX — classes for two, opening targeted mid-January 2027.",
    "/cocktail-classes",
    "Planned event · The Plain Bar · Longview Mall",
    "Date-night cocktail classes in Longview",
    ["The Plain Bar's announced opening lineup includes cocktail classes built as date nights: two people, a bartender, and an evening learning how the drinks actually get made — shake, stir, measure, taste.",
     "Owner DeMarkus King announced the classes in the News-Journal Business Beat as part of the bar's event plans. Pricing, the schedule and how signups work will be published with the opening — targeted mid-January 2027."],
    [("Are the cocktail classes just for couples?",
      "They're planned as date nights — that's the announced idea. Whether single seats are offered isn't decided yet; the contact form reaches the owner directly."),
     ("How much will a class cost?",
      "Prices aren't published yet — the bar hasn't opened. Class pricing posts on this site when it's set."),
     ("Do I need any experience?",
      "No experience is implied by the plan — these are classes to learn from, not tests. Format details come with the opening."),
     ("Where will classes take place?",
      "At the bar: inside Longview Mall, 3500 McCann Rd STE H07B, Longview, TX 75604.")],
    "Date-night cocktail classes")

# ------------------------------------------------------------------ contact
contact = head(
    "Contact & Directions — The Plain Bar, Longview TX",
    "Contact The Plain Bar, the new bar inside Longview Mall at 3500 McCann Rd STE H07B, Longview TX 75604 — form, owner email, directions and the map. Opening targeted mid-January 2027.",
    "/contact") + crumbbar([("Home","/"),("Contact & directions","/contact")]) + f"""  <section class="hero slim">
    <div class="wrap">
      <p class="eyebrow">Contact · The Plain Bar · Longview Mall</p>
      <h1>Talk to the bar before it opens.</h1>
      <p class="lede">Questions about opening dates, the events, private gatherings — or you want the bar manager job — this reaches owner DeMarkus King. There's no phone line yet; email and this form are how the bar answers right now.</p>
    </div>
  </section>

  <section class="sec">
    <div class="wrap grid2">
      <div>
        <h2>Send a note</h2>
        <form class="cform" action="/contact" method="post">
          <label for="f-name">Your name</label>
          <input id="f-name" name="name" type="text" maxlength="120" required autocomplete="name">
          <label for="f-phone">Phone <span class="opt">(optional)</span></label>
          <input id="f-phone" name="phone" type="tel" maxlength="60" autocomplete="tel">
          <label for="f-email">Email <span class="opt">(optional)</span></label>
          <input id="f-email" name="email" type="email" maxlength="120" autocomplete="email">
          <label for="f-msg">Message</label>
          <textarea id="f-msg" name="message" rows="5" maxlength="4000" required placeholder="What do you want the bar to know?"></textarea>
          <p><button class="btn" type="submit">Send to the bar</button></p>
        </form>
        <p class="note">Messages from this form email the bar directly. Prefer plain mail? <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
      </div>
      <div class="visitcopy">
        <h2>Visit &amp; apply</h2>
        <address class="nap big">The Plain Bar<br>
        {ADDR_STREET}<br>{ADDR_CITY}<br>
        <a href="mailto:{EMAIL}">{EMAIL}</a><br>
        <a href="{DIRS}" target="_blank" rel="noopener">Get directions</a></address>
        <p>The space is inside Longview Mall off McCann Road, unit H07B. Hours post the week of opening — currently targeted mid-January 2027.</p>
        <p><span class="k">Now hiring</span> The bar is hiring its first bar manager. Send a short note through the form or email the owner to apply.</p>
        <p class="honest">Licensed by the Texas Alcoholic Beverage Commission — permit MB200168843.</p>
{mapbox(MAP_TITLE)}      </div>
    </div>
  </section>
""" + """  <section class="ldwrap">
""" + ld({"@context": "https://schema.org", "@graph": [
    {"@type": "BarOrPub", "name": SITE,
     "address": {"@type": "PostalAddress", "streetAddress": ADDR_STREET, "addressLocality": "Longview", "addressRegion": "TX", "postalCode": "75604", "addressCountry": "US"},
     "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LON},
     "url": ORIGIN + "/contact", "email": EMAIL, "openingDate": "2027-01-15",
     "contactPoint": {"@type": "ContactPoint", "contactType": "customer service", "email": EMAIL, "availableLanguage": "English"}}
]}) + """</section>
""" + FOOTER

# ------------------------------------------------------------------ privacy
privacy = head(
    "Privacy Policy — The Plain Bar, Longview TX",
    "Privacy at The Plain Bar's website: what the contact form collects, how the Google map embed works, and the fact that this site runs no analytics and sets no cookies. New bar inside Longview Mall, Longview TX.",
    "/privacy") + crumbbar([("Home","/"),("Privacy","/privacy")]) + f"""  <section class="hero slim">
    <div class="wrap">
      <p class="eyebrow">Privacy · The Plain Bar</p>
      <h1>What this site knows about you.</h1>
      <p class="lede">Short version: only what you type into the contact form, plus whatever Google's map embed does on its own. No analytics, no tracking scripts, no cookies set by this site.</p>
    </div>
  </section>

  <section class="sec">
    <div class="wrap narrow">
      <h2>The contact form</h2>
      <p>If you use the form, you send the bar your name, an optional phone number, an optional email address, and your message. That information is used for one thing: answering you. Messages are emailed to the bar's inbox and kept as long as needed to reply and to remember what was asked.</p>
      <h2>No trackers</h2>
      <p>This site loads no analytics, no advertising scripts and no third-party cookies of its own, and it sets no cookies itself. The only outside content on the site is the embedded Google Map on the home and contact pages, which loads from Google — Google may set its own cookies under its own privacy policy once the map renders.</p>
      <h2>Your mail comes from the bar</h2>
      <p>Replies go out as <a href="mailto:{EMAIL}">{EMAIL}</a>. If you'd rather not be emailed about the bar at all, say so in any reply or email the owner and the bar will stop.</p>
      <h2>Removing your details</h2>
      <p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> and ask — the bar will delete what the form kept about you.</p>
      <p class="honest">This page describes the site as it stands today, November 2026, before opening. If practices change at launch, this page changes with them.</p>
    </div>
  </section>
""" + cta_band("Anything else?", "One question, one sentence — the form works.") + """  <section class="ldwrap">
""" + ld({"@context": "https://schema.org", "@type": "PrivacyPolicy", "name": "Privacy Policy — The Plain Bar", "url": ORIGIN + "/privacy"}) + """</section>
""" + FOOTER

# ------------------------------------------------------------------ thanks / 404
thanks = head(
    "Thanks — The Plain Bar, Longview TX",
    "Your message reached The Plain Bar, the new bar inside Longview Mall. The owner answers notes from Longview directly — the bar is targeting a mid-January 2027 opening.",
    "/thanks", noindex=True) + f"""  <section class="hero slim">
    <div class="wrap">
      <p class="eyebrow">Message sent</p>
      <h1>Your note is on its way to the bar.</h1>
      <p class="lede">The owner reads everything that comes in — while the space is still under renovation, replies may take a day or two. The opening calendar posts on this site first.</p>
      <p class="herocta"><a class="btn" href="/">Back to the front page</a> <a class="btn ghost" href="/events">See what's planned</a></p>
    </div>
  </section>
""" + FOOTER

notfound = head(
    "Page Not Found — The Plain Bar, Longview TX",
    "That page isn't on The Plain Bar's site — the new bar inside Longview Mall, Longview TX, is still getting ready for its planned mid-January 2027 opening.",
    "/404", noindex=True) + f"""  <section class="hero slim">
    <div class="wrap">
      <p class="eyebrow">404</p>
      <h1>That page isn't here.</h1>
      <p class="lede">The bar hasn't opened yet — there's a lot of site still to write. Try the front page, the events plan, or tell the bar what you were looking for.</p>
      <p class="herocta"><a class="btn" href="/">Front page</a> <a class="btn ghost" href="/events">Events</a> <a class="btn ghost" href="/contact">Contact</a></p>
    </div>
  </section>
""" + FOOTER

# ------------------------------------------------------------------ static files
CSS = """:root{
  --ink:#17120e; --ink2:#231b13; --ink3:#2c2317;
  --cream:#f1e7d4; --brass:#c8a24b; --amber:#e2b45e; --mute:#a3947c;
  --line:rgba(200,162,75,.34); --line2:rgba(241,231,212,.14);
  --serif:Georgia,"Iowan Old Style","Palatino Linotype","Times New Roman",serif;
  --sans:"Avenir Next",Avenir,"Helvetica Neue",Helvetica,sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html{color-scheme:dark}
body{background:var(--ink);color:var(--cream);font:17px/1.65 var(--serif)}
a{color:var(--amber)}
a:hover{color:var(--cream)}
.wrap{max-width:1060px;margin:0 auto;padding:0 24px}
.narrow{max-width:720px}
.skip{position:absolute;left:-9999px}
.skip:focus{left:12px;top:12px;background:var(--brass);color:#17120e;padding:8px 14px;z-index:9}

header{border-bottom:1px solid var(--line);background:var(--ink)}
.headrow{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:10px 22px;padding-top:14px;padding-bottom:14px}
.brand{font:700 23px/1.1 var(--serif);color:var(--cream);text-decoration:none;display:flex;flex-direction:column;letter-spacing:.01em}
.brandtag{font:600 10px/1.6 var(--sans);letter-spacing:.22em;text-transform:uppercase;color:var(--mute);margin-top:4px}
nav{display:flex;flex-wrap:wrap;align-items:center;gap:4px 20px;font:600 13px/1 var(--sans);letter-spacing:.12em;text-transform:uppercase}
nav a{color:var(--cream);text-decoration:none;padding:8px 0;border-bottom:1px solid transparent}
nav a:hover{color:var(--amber)}
nav a[aria-current="page"]{color:var(--amber);border-bottom-color:var(--brass)}

.btn{display:inline-block;background:var(--brass);color:#17120e;font:700 14px/1.2 var(--sans);letter-spacing:.08em;text-transform:uppercase;text-decoration:none;padding:14px 22px;border:1px solid var(--brass);border-radius:2px;cursor:pointer}
.btn:hover{background:var(--amber);border-color:var(--amber);color:#17120e}
.btn.ghost{background:transparent;color:var(--cream);border-color:var(--line)}
.btn.ghost:hover{border-color:var(--amber);color:var(--amber)}
.btn.sm{padding:9px 14px;font-size:12px}
button.btn{font-family:var(--sans)}

.eyebrow{font:700 12px/1.8 var(--sans);letter-spacing:.24em;text-transform:uppercase;color:var(--brass)}
h1{font:700 clamp(34px,5.4vw,58px)/1.08 var(--serif);letter-spacing:-.01em;margin:14px 0 18px;max-width:21ch}
h2{font:700 clamp(23px,3.4vw,33px)/1.2 var(--serif);margin:0 0 18px;max-width:26ch}
h3{font:700 21px/1.3 var(--serif);margin-bottom:10px}
p{margin:14px 0;max-width:70ch}
.lede{color:var(--cream);font-size:clamp(17px,2.2vw,20px);line-height:1.6;max-width:62ch}

.hero{border-bottom:1px solid var(--line2);padding:74px 0 62px}
.hero.slim{padding:52px 0 42px}
.herocta{margin-top:26px;display:flex;flex-wrap:wrap;gap:12px}
.crumbs{font:600 11.5px/1.8 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--mute);padding:22px 0 0}
.crumbs a{color:var(--mute);text-decoration:none}
.crumbs a:hover{color:var(--amber)}

.strip{border-bottom:1px solid var(--line);background:var(--ink2)}
.striprow{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px 34px;padding-top:26px;padding-bottom:26px}
.striprow p{margin:0;font:15px/1.6 var(--sans);color:var(--cream);max-width:none}
.k{display:inline-block;font:700 10.5px/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--brass);border:1px solid var(--line);padding:5px 8px;margin-right:10px;vertical-align:1px}

.sec{padding:64px 0;border-bottom:1px solid var(--line2)}
.sec.alt{background:var(--ink2);border-bottom-color:var(--line)}
.src{font:14px/1.6 var(--sans);color:var(--mute)}
.note{font:14.5px/1.6 var(--sans);color:var(--mute)}
.honest{font:14.5px/1.6 var(--sans);color:var(--mute)}

.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));border:1px solid var(--line);margin-top:28px}
.card{display:block;background:var(--ink);border:1px solid var(--line);padding:26px 24px;text-decoration:none;color:var(--cream);min-height:190px}
.card h3{color:var(--cream)}
.card p{font:15px/1.6 var(--sans);color:var(--mute);margin:8px 0 14px;max-width:none}
.more{font:700 11.5px/1 var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--brass)}
.card:hover{background:var(--ink3)}
.card:hover h3{color:var(--amber)}

.visit{display:grid;grid-template-columns:1fr 1.1fr;gap:34px;align-items:start;margin-top:8px}
.visitcopy p{margin:12px 0}
.map{width:100%;border:1px solid var(--line);background:var(--ink2)}
.map iframe{display:block;width:100%;height:340px;border:0}

.grid2{display:grid;grid-template-columns:1fr 1fr;gap:44px;align-items:start}
.cform{margin-top:6px}
.cform label{display:block;font:700 11.5px/1 var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--brass);margin:18px 0 8px}
.cform label:first-child{margin-top:0}
.opt{color:var(--mute);font-weight:600;letter-spacing:.06em;text-transform:none}
.cform input,.cform textarea{display:block;width:100%;background:var(--ink);color:var(--cream);border:1px solid var(--line);border-radius:2px;padding:13px 14px;font:16px/1.5 var(--sans)}
.cform input:focus,.cform textarea:focus{outline:2px solid var(--brass);border-color:var(--brass)}
.cform button{margin-top:22px}
.nap{font-style:normal;font:15.5px/1.8 var(--sans)}
.nap.big{font-size:16px;margin-bottom:18px;color:var(--cream)}

.faqlist{margin-top:8px;border-top:1px solid var(--line)}
.faq{padding:20px 0;border-bottom:1px solid var(--line2)}
.faq dt{font:700 17px/1.4 var(--serif);color:var(--cream);margin-bottom:8px}
.faq dd{font:15px/1.65 var(--sans);color:var(--mute);max-width:66ch}

.band{border-bottom:1px solid var(--line);background:var(--ink3)}
.bandrow{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:18px 34px;padding-top:44px;padding-bottom:44px}
.band h2{margin:0}
.band p{margin:0;color:var(--mute);font:15px/1.6 var(--sans);max-width:46ch}
.bandcta{margin:0}

.ldwrap{padding:0;margin:0}

footer{background:var(--ink);border-top:1px solid var(--line);padding:48px 0 34px}
.fgrid{display:grid;grid-template-columns:1.2fr 1fr 1fr;gap:34px}
footer h4{font:700 12px/1 var(--sans);letter-spacing:.22em;text-transform:uppercase;color:var(--brass);margin-bottom:16px}
footer address,footer ul{font:14.5px/1.9 var(--sans);color:var(--mute)}
footer ul{list-style:none}
footer a{color:var(--mute);text-decoration:none;border-bottom:1px solid transparent}
footer a:hover{color:var(--amber)}
.footline{display:flex;flex-wrap:wrap;gap:8px 28px;justify-content:space-between;border-top:1px solid var(--line2);margin-top:36px;padding-top:18px;font:12.5px/1.7 var(--sans);color:var(--mute)}

@media (max-width:820px){
  .visit,.grid2,.fgrid{grid-template-columns:1fr}
  .hero{padding:46px 0 38px}
  .sec{padding:44px 0}
  nav{gap:2px 14px;font-size:12px}
  .bandrow{padding-top:34px;padding-bottom:34px}
}
"""

SITEMAP_PAGES = ["/", "/events", "/sunday-brunch", "/book-nights", "/cocktail-classes", "/contact", "/privacy"]
sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{ORIGIN}{p}</loc><lastmod>2026-11-18</lastmod></url>\n" for p in SITEMAP_PAGES)
    + "</urlset>\n")

robots = f"""User-agent: *
Allow: /

Sitemap: {ORIGIN}/sitemap.xml
"""

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#17120e"/><rect x="4" y="4" width="56" height="56" fill="none" stroke="#c8a24b" stroke-width="2"/><text x="32" y="44" font-family="Georgia,serif" font-size="34" font-weight="bold" fill="#f1e7d4" text-anchor="middle">P</text></svg>
"""

PAGES = {
    "index.html": home, "events.html": events,
    "sunday-brunch.html": sunday_brunch, "book-nights.html": book_nights,
    "cocktail-classes.html": cocktail_classes,
    "contact.html": contact, "privacy.html": privacy,
    "thanks.html": thanks, "404.html": notfound,
}

def main():
    os.makedirs(OUT, exist_ok=True)
    for name, doc in PAGES.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(doc)
        print(name, len(doc.encode()), "bytes")
    with open(os.path.join(OUT, "style.css"), "w", encoding="utf-8") as f: f.write(CSS)
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f: f.write(sitemap)
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f: f.write(robots)
    with open(os.path.join(OUT, "favicon.svg"), "w", encoding="utf-8") as f: f.write(FAVICON)
    print("static files written")

if __name__ == "__main__":
    main()
