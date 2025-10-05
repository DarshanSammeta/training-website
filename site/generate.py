#!/usr/bin/env python3
import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SITE = ROOT
PAGES = SITE / 'pages'
ASSETS = SITE / 'assets'

NAV = {
    'services': [
        {'title': 'Online IT Training', 'slug': 'online-it-training'},
        {'title': 'Corporate Training', 'slug': 'corporate-training'},
        {'title': 'Placements', 'slug': 'placements'},
        {'title': 'IT Resources', 'slug': 'it-resources'},
        {'title': 'Quality Services', 'slug': 'quality-services'},
    ],
    'about': [
        {'title': 'Who We Are', 'slug': 'who-we-are'},
        {'title': 'Careers', 'slug': 'careers'},
        {'title': 'Clients', 'slug': 'clients'},
        {'title': 'Contact Us', 'slug': 'contact-us'},
    ],
    'payments': {'title': 'Payments', 'slug': 'payments'},
    'trainings': [
        {'section': 'SAP', 'items': ['SAP FICO','SAP MM','SAP ABAP','SAP SD','SAP PP','SAP HR/HCM','SAP PS','SAP QM','SAP PLM','SAP MDM','SAP GRC','SAP EHS','SAP EPD','SAP WM','SAP BI']},
        {'section': 'Mobile Application', 'items': ['Android Training','iPhone Development Training','Blackberry Training']},
        {'section': 'Datawarehouse', 'items': ['Cognos Planning and Budgeting Online Training','Business Analytics Online Training','Microstrategy Online Training','Datastage Online Training','MSBI Online Training','AB Initio Online Training','BOXI Online Training','Cognos Online Training','Hyperion Interactive Report Online Training','Hyperion EssBase Online Training','Informatica Online Training']},
        {'section': 'Hadoop', 'items': ['Big Data and Hadoop']},
        {'section': 'Microsoft Technical', 'items': ['Biztalk Server Online Training','MS Exchange Server 2003 Online Training','MS Exchange Server 2007 Online Training','MS Exchange Server 2010 Online Training','MS Office Sharepoint 2007 Online Training','MS Office Sharepoint 2010 Online Training','MS SQL Server 2005 Online Training','MS SQL Server 2008 Online Training']},
        {'section': 'Oracle', 'items': ['Oracle 10g/11g Online Training','Oracle APPS Technical Online Training','Siebel Analytics Online Training','Siebel CRM Online Training','WebLogic Online Training','Oracle APPS Functional Online Training','Oracle APPS Financial Online Training','Oracle APPS DBA Online Training']},
        {'section': 'PeopleSoft', 'items': ['Peoplesoft HRMS Functional Online Training','Peoplesoft HRMS Technical Online Training']},
        {'section': 'Cloud Computing', 'items': ['Salesforce']},
        {'section': 'Testing Tools', 'items': ['QA Testing Online Training','QTP Online Training','Load Runner Online Training','ETL Testing Online Training']},
        {'section': 'Databases', 'items': ['Oracle Forms and Reports Online Training','Oracle DBA Online Training','SQL Server Online Training','SQL Server Tuning Online Training']},
        {'section': 'System Admin', 'items': ['MCSE Online Training','CCNA Online Training','CCNP Online Training','SAN Course Training','Solaris Online Training','LINUX Online Training']},
        {'section': 'Middleware Technologies', 'items': ['Tibco Online Training','Web Methods Online Training']},
        {'section': 'SAS', 'items': ['SAS Online Training','SAS Financials Online Training']},
        {'section': 'Cyber Security', 'items': ['Cyber Security']},
        {'section': 'WorkDay', 'items': ['Workday Payroll','Workday HCM Functional','Workday HCM Technical Integration']},
        {'section': 'Business Analytics', 'items': ['Business Analytics']},
    ]
}

def slugify(text: str) -> str:
    text = text.lower().replace('/', '-')
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return re.sub(r'^-|-$', '', text)

BASE_TEMPLATE = """<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>{title} - IT Training</title>
  <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css\" rel=\"stylesheet\">
  <link href=\"{root}/assets/css/styles.css\" rel=\"stylesheet\">
</head>
<body data-root=\"{root}\">
  <nav class=\"navbar navbar-expand-lg navbar-dark bg-dark fixed-top shadow-sm\">
    <div class=\"container\">
      <a class=\"navbar-brand fw-bold\" href=\"{root}/index.html\">IT Training</a>
      <button class=\"navbar-toggler\" type=\"button\" data-bs-toggle=\"collapse\" data-bs-target=\"#nav\"><span class=\"navbar-toggler-icon\"></span></button>
      <div class=\"collapse navbar-collapse\" id=\"nav\">
        <ul class=\"navbar-nav ms-auto mb-2 mb-lg-0\">
          <li class=\"nav-item\"><a class=\"nav-link\" href=\"{root}/index.html\">Home</a></li>
          <li class=\"nav-item dropdown\"><a class=\"nav-link dropdown-toggle\" href=\"#\" data-bs-toggle=\"dropdown\">Services</a><ul class=\"dropdown-menu\" id=\"nav-services\"></ul></li>
          <li class=\"nav-item dropdown\"><a class=\"nav-link dropdown-toggle\" href=\"#\" data-bs-toggle=\"dropdown\">Trainings</a><ul class=\"dropdown-menu\" id=\"nav-trainings\"></ul></li>
          <li class=\"nav-item dropdown\"><a class=\"nav-link dropdown-toggle\" href=\"#\" data-bs-toggle=\"dropdown\">About</a><ul class=\"dropdown-menu\" id=\"nav-about\"></ul></li>
          <li class=\"nav-item\"><a class=\"btn btn-success ms-lg-3\" href=\"{root}/pages/payments.html\">Payments</a></li>
        </ul>
      </div>
    </div>
  </nav>

  <header class=\"hero d-flex align-items-center justify-content-center text-center text-white\">
    <div class=\"container\">
      <h1 class=\"display-5 fw-bold mb-3\">{title}</h1>
      <p class=\"lead mb-4\">{subtitle}</p>
      {cta}
    </div>
  </header>

  <main class=\"mt-5 pt-4\">
    {content}
  </main>

  <footer class=\"py-4 bg-dark text-white text-center\"><div class=\"container\">© <span id=\"year\"></span> IT Training — All rights reserved.</div></footer>
  <script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js\"></script>
  <script src=\"https://unpkg.com/scrollreveal\"></script>
  <script src=\"{root}/assets/js/script.js\"></script>
</body>
</html>
"""

SECTION_CARD = """
<section class=\"container py-5\">
  <div class=\"row g-4\">
    <div class=\"col-12 col-md-6\">
      <img src=\"https://picsum.photos/seed/{seed}/800/520\" class=\"img-fluid rounded shadow reveal\" alt=\"{title}\">
    </div>
    <div class=\"col-12 col-md-6\">
      <h2 class=\"mb-3\">About {title}</h2>
      <p class=\"text-muted\">This is a placeholder description for {title}. Learn with hands-on labs, live sessions, and real-world projects tailored by industry experts.</p>
      <ul class=\"list-unstyled\">
        <li class=\"mb-2\">✔️ Instructor-led live sessions</li>
        <li class=\"mb-2\">✔️ Real projects & case studies</li>
        <li class=\"mb-2\">✔️ Certification guidance</li>
        <li class=\"mb-2\">✔️ Placement assistance</li>
      </ul>
      <a class=\"btn btn-primary\" href=\"#enquire\">Enquire Now</a>
    </div>
  </div>
</section>
<section id=\"enquire\" class=\"bg-light py-5\">
  <div class=\"container\">
    <h3 class=\"mb-3\">Get Syllabus & Schedule</h3>
    <form class=\"row g-3\">
      <div class=\"col-md-6\"><input class=\"form-control\" placeholder=\"Your name\" required></div>
      <div class=\"col-md-6\"><input type=\"email\" class=\"form-control\" placeholder=\"Email\" required></div>
      <div class=\"col-12\"><textarea class=\"form-control\" rows=\"4\" placeholder=\"Tell us about your goals\"></textarea></div>
      <div class=\"col-12\"><button class=\"btn btn-success\" type=\"submit\">Submit</button></div>
    </form>
  </div>
</section>
"""

PAYMENTS_CONTENT = """
<section class=\"container py-5\">
  <div class=\"row justify-content-center\">
    <div class=\"col-lg-8\">
      <div class=\"card shadow reveal\">
        <div class=\"card-body\">
          <h2 class=\"card-title mb-3\">Secure Payments</h2>
          <p class=\"text-muted\">Make payments for your chosen course securely. This is a demo page; integrate your payment gateway (Stripe/Razorpay/PayPal) here.</p>
          <div class=\"d-flex gap-2\">
            <button class=\"btn btn-primary\">Pay with Card</button>
            <button class=\"btn btn-outline-secondary\">PayPal</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

ABOUT_CONTENT = """
<section class=\"container py-5\">
  <div class=\"row g-4\">
    <div class=\"col-md-6\">
      <h2 class=\"mb-3\">{title}</h2>
      <p class=\"text-muted\">This is a placeholder page for {title}. Replace with your company content.</p>
    </div>
    <div class=\"col-md-6\">
      <img src=\"https://picsum.photos/seed/{seed}/800/520\" class=\"img-fluid rounded shadow reveal\" alt=\"{title}\">
    </div>
  </div>
</section>
"""

SERVICE_CONTENT = """
<section class=\"container py-5\">
  <div class=\"row g-4\">
    <div class=\"col-md-6\">
      <img src=\"https://picsum.photos/seed/{seed}/800/520\" class=\"img-fluid rounded shadow reveal\" alt=\"{title}\">
    </div>
    <div class=\"col-md-6\">
      <h2 class=\"mb-3\">{title}</h2>
      <p class=\"text-muted\">Our {title} offering includes tailored solutions, expert consultants, and dedicated support to achieve your business outcomes.</p>
      <a class=\"btn btn-outline-primary\" href=\"{root}/index.html#catalog\">Explore Trainings</a>
    </div>
  </div>
</section>
"""


def ensure_dirs():
    (PAGES / 'services').mkdir(parents=True, exist_ok=True)
    (PAGES / 'trainings').mkdir(parents=True, exist_ok=True)
    (PAGES / 'about').mkdir(parents=True, exist_ok=True)


def write_page(rel_path: Path, title: str, subtitle: str = '', content: str = '', cta_html: str = ''):
    # root prefix depends on depth: pages/* => '..', pages/trainings/* => '../..'
    depth = len(rel_path.parts) - 1  # exclude file name
    root = '.'.join(['.'] + ['.'] * (depth))
    root = '/'.join(['.'] + ['..'] * (depth)) if depth > 0 else '.'

    html = BASE_TEMPLATE.format(
        title=title,
        subtitle=subtitle or 'Hands-on sessions, expert mentors, real outcomes.',
        content=content,
        cta=cta_html,
        root=root,
    )
    out_path = SITE / rel_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding='utf-8')


def generate_services():
    for svc in NAV['services']:
        title = svc['title']
        seed = slugify(title)
        content = SERVICE_CONTENT.format(title=title, seed=seed, root='..')
        rel = Path('pages/services') / f"{svc['slug']}.html"
        write_page(rel, title, content=content)


def generate_trainings():
    for group in NAV['trainings']:
        for item in group['items']:
            title = item
            seed = slugify(title)
            content = SECTION_CARD.format(title=title, seed=seed)
            rel = Path('pages/trainings') / f"{slugify(item)}.html"
            write_page(rel, title, content=content)


def generate_about():
    for page in NAV['about']:
        title = page['title']
        seed = slugify(title)
        content = ABOUT_CONTENT.format(title=title, seed=seed)
        rel = Path('pages/about') / f"{page['slug']}.html"
        write_page(rel, title, content=content)


def generate_payments():
    rel = Path('pages') / 'payments.html'
    write_page(rel, 'Payments', subtitle='Secure checkout for your enrollments', content=PAYMENTS_CONTENT)


def main():
    ensure_dirs()
    generate_services()
    generate_trainings()
    generate_about()
    generate_payments()
    # report
    training_count = sum(len(g['items']) for g in NAV['trainings'])
    total = 1 + len(NAV['services']) + training_count + len(NAV['about']) + 1
    print(f"Generated pages: services={len(NAV['services'])}, trainings={training_count}, about={len(NAV['about'])}, payments=1, home=1, total={total}")

if __name__ == '__main__':
    main()
