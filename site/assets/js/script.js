const NAV = {
  services: [
    { title: 'Online IT Training', slug: 'online-it-training' },
    { title: 'Corporate Training', slug: 'corporate-training' },
    { title: 'Placements', slug: 'placements' },
    { title: 'IT Resources', slug: 'it-resources' },
    { title: 'Quality Services', slug: 'quality-services' }
  ],
  about: [
    { title: 'Who We Are', slug: 'who-we-are' },
    { title: 'Careers', slug: 'careers' },
    { title: 'Clients', slug: 'clients' },
    { title: 'Contact Us', slug: 'contact-us' }
  ],
  payments: { title: 'Payments', slug: 'payments' },
  trainings: [
    { section: 'SAP', items: ['SAP FICO','SAP MM','SAP ABAP','SAP SD','SAP PP','SAP HR/HCM','SAP PS','SAP QM','SAP PLM','SAP MDM','SAP GRC','SAP EHS','SAP EPD','SAP WM','SAP BI'] },
    { section: 'Mobile Application', items: ['Android Training','iPhone Development Training','Blackberry Training'] },
    { section: 'Datawarehouse', items: ['Cognos Planning and Budgeting Online Training','Business Analytics Online Training','Microstrategy Online Training','Datastage Online Training','MSBI Online Training','AB Initio Online Training','BOXI Online Training','Cognos Online Training','Hyperion Interactive Report Online Training','Hyperion EssBase Online Training','Informatica Online Training'] },
    { section: 'Hadoop', items: ['Big Data and Hadoop'] },
    { section: 'Microsoft Technical', items: ['Biztalk Server Online Training','MS Exchange Server 2003 Online Training','MS Exchange Server 2007 Online Training','MS Exchange Server 2010 Online Training','MS Office Sharepoint 2007 Online Training','MS Office Sharepoint 2010 Online Training','MS SQL Server 2005 Online Training','MS SQL Server 2008 Online Training'] },
    { section: 'Oracle', items: ['Oracle 10g/11g Online Training','Oracle APPS Technical Online Training','Siebel Analytics Online Training','Siebel CRM Online Training','WebLogic Online Training','Oracle APPS Functional Online Training','Oracle APPS Financial Online Training','Oracle APPS DBA Online Training'] },
    { section: 'PeopleSoft', items: ['Peoplesoft HRMS Functional Online Training','Peoplesoft HRMS Technical Online Training'] },
    { section: 'Cloud Computing', items: ['Salesforce'] },
    { section: 'Testing Tools', items: ['QA Testing Online Training','QTP Online Training','Load Runner Online Training','ETL Testing Online Training'] },
    { section: 'Databases', items: ['Oracle Forms and Reports Online Training','Oracle DBA Online Training','SQL Server Online Training','SQL Server Tuning Online Training'] },
    { section: 'System Admin', items: ['MCSE Online Training','CCNA Online Training','CCNP Online Training','SAN Course Training','Solaris Online Training','LINUX Online Training'] },
    { section: 'Middleware Technologies', items: ['Tibco Online Training','Web Methods Online Training'] },
    { section: 'SAS', items: ['SAS Online Training','SAS Financials Online Training'] },
    { section: 'Cyber Security', items: ['Cyber Security'] },
    { section: 'WorkDay', items: ['Workday Payroll','Workday HCM Functional','Workday HCM Technical Integration'] },
    { section: 'Business Analytics', items: ['Business Analytics'] }
  ]
};

function slugify(text) {
  return text
    .toLowerCase()
    .replace(/\//g, '-')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)/g, '');
}

function getRoot() {
  const fromAttr = document.body.getAttribute('data-root');
  return fromAttr && fromAttr.length ? fromAttr : '.';
}

function buildMenus() {
  const root = getRoot();
  const servicesEl = document.getElementById('nav-services');
  const aboutEl = document.getElementById('nav-about');
  const trainingsEl = document.getElementById('nav-trainings');
  const brand = document.querySelector('.navbar-brand');
  const paymentsBtn = document.querySelector('a.btn.btn-success');

  if (brand) brand.setAttribute('href', `${root}/index.html`);
  if (paymentsBtn) paymentsBtn.setAttribute('href', `${root}/pages/payments.html`);

  if (servicesEl) {
    NAV.services.forEach(item => {
      const li = document.createElement('li');
      li.innerHTML = `<a class="dropdown-item" href="${root}/pages/services/${item.slug}.html">${item.title}</a>`;
      servicesEl.appendChild(li);
    });
  }

  if (aboutEl) {
    NAV.about.forEach(item => {
      const li = document.createElement('li');
      li.innerHTML = `<a class="dropdown-item" href="${root}/pages/about/${item.slug}.html">${item.title}</a>`;
      aboutEl.appendChild(li);
    });
  }

  if (trainingsEl) {
    NAV.trainings.forEach(group => {
      const li = document.createElement('li');
      li.className = 'dropend';
      const submenu = group.items
        .map(it => `<li><a class="dropdown-item" href="${root}/pages/trainings/${slugify(it)}.html">${it}</a></li>`) 
        .join('');
      li.innerHTML = `
        <a class="dropdown-item dropdown-toggle" href="#" data-bs-toggle="dropdown">${group.section}</a>
        <ul class="dropdown-menu">${submenu}</ul>
      `;
      trainingsEl.appendChild(li);
    });
  }
}

function buildCards() {
  const cards = document.getElementById('cards');
  if (!cards) return;
  const root = getRoot();
  const picks = [
    NAV.trainings[0].items[0],
    NAV.trainings[0].items[1],
    NAV.trainings[3].items[0],
    NAV.trainings[8].items[3],
    NAV.trainings[10].items[1],
    NAV.trainings[15].items[0]
  ].map(title => ({ title, slug: slugify(title) }));

  picks.forEach(p => {
    const col = document.createElement('div');
    col.className = 'col-12 col-sm-6 col-lg-4';
    col.innerHTML = `
      <div class="card card-hover h-100 reveal">
        <img src="https://picsum.photos/seed/${p.slug}/600/400" class="card-img-top" alt="${p.title}">
        <div class="card-body">
          <h5 class="card-title">${p.title}</h5>
          <p class="card-text">Master ${p.title} with hands-on labs and expert mentors.</p>
          <a class="btn btn-outline-primary" href="${root}/pages/trainings/${p.slug}.html">View Course</a>
        </div>
      </div>`;
    cards.appendChild(col);
  });
}

function reveal() {
  if (!window.ScrollReveal) return;
  window.ScrollReveal().reveal('.reveal', {
    distance: '40px',
    origin: 'bottom',
    interval: 80,
    cleanup: true
  });
}

function setYear() {
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
}

function init() {
  buildMenus();
  buildCards();
  reveal();
  setYear();
}

document.readyState === 'loading' 
  ? document.addEventListener('DOMContentLoaded', init)
  : init();
