CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

:root {
    --primary: #0EA5A4;
    --primary-dark: #0F766E;
    --secondary: #2563EB;

    --success: #16A34A;
    --warning: #F59E0B;
    --danger: #EF4444;

    --bg: #EEF3F6;
    --surface: #F8FAFB;
    --surface-raised: #FFFFFF;
    --surface-soft: #F2F6F8;
    --sidebar: #F9FBFC;
    --card: #FFFFFF;

    --text: #111827;
    --muted: #607187;
    --muted-2: #8291A5;

    --line: #D4E0E7;
    --line-2: #C5D3DD;

    --primary-soft: rgba(14, 165, 164, 0.10);
    --shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
}

/* ============================================================
   GLOBAL
============================================================ */

html,
body,
[class*="css"] {
    font-family: "Inter", "Segoe UI", sans-serif !important;
}

html,
body {
    overflow-y: auto !important;
    overflow-x: hidden !important;
    height: auto !important;
    max-height: none !important;
}

.stApp {
    background: linear-gradient(135deg, #EEF3F6 0%, #EAF2F4 52%, #F2F5F7 100%) !important;
    color: var(--text) !important;
    overflow-y: auto !important;
    overflow-x: hidden !important;
    height: auto !important;
    min-height: 100vh !important;
    max-height: none !important;
}

div[data-testid="stElementContainer"]:has(style) {
    display: none !important;
}

#MainMenu,
footer {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    display: none !important;
}

[data-testid="stSidebarCollapseButton"] {
    display: none !important;
}

section[data-testid="stSidebar"] {
    display: none !important;
}

button[title="View fullscreen"] {
    display: none !important;
}

[data-testid="stAppViewContainer"] {
    overflow-y: auto !important;
    overflow-x: hidden !important;
    height: auto !important;
    min-height: 100vh !important;
    max-height: none !important;
}

[data-testid="stMain"],
main {
    overflow-x: hidden !important;
    overflow-y: visible !important;
    height: auto !important;
    max-height: none !important;
}

.block-container {
    --page-gutter: clamp(1.5rem, 2.4vw, 3.5rem);
    width: 100% !important;
    max-width: none !important;
    padding-top: 0 !important;
    padding-left: var(--page-gutter) !important;
    padding-right: var(--page-gutter) !important;
    padding-bottom: 3rem !important;
    overflow: visible !important;
    height: auto !important;
    max-height: none !important;
    box-sizing: border-box !important;
}

/* ============================================================
   TOP NAVIGATION
============================================================ */

.st-key-top_navigation {
    width: calc(100% + min(4.8vw, 7rem)) !important;
    max-width: none !important;
    min-height: 76px;
    padding: 0.7rem var(--page-gutter);
    margin-left: calc(0px - var(--page-gutter));
    margin-right: calc(0px - var(--page-gutter));
    margin-bottom: 1.4rem;
    position: sticky;
    top: 0;
    z-index: 1000;
    background: rgba(249, 251, 252, 0.96);
    border: none;
    border-bottom: 1px solid rgba(148, 163, 184, 0.46);
    border-radius: 0;
    box-shadow:
        0 1px 0 rgba(255, 255, 255, 0.88) inset,
        0 8px 20px -14px rgba(15, 23, 42, 0.42),
        0 14px 34px -26px rgba(14, 165, 164, 0.30);
    backdrop-filter: blur(18px) saturate(125%);
}

.st-key-top_navigation::after {
    content: "";
    position: absolute;
    left: var(--page-gutter);
    right: var(--page-gutter);
    bottom: -1px;
    height: 1px;
    pointer-events: none;
    background: linear-gradient(
        90deg,
        transparent 0%,
        rgba(14, 165, 164, 0.30) 22%,
        rgba(37, 99, 235, 0.24) 78%,
        transparent 100%
    );
}

.st-key-top_navigation > div[data-testid="stVerticalBlock"] {
    gap: 0 !important;
}

.st-key-top_navigation div[data-testid="stHorizontalBlock"] {
    align-items: center;
}

.top-brand {
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    min-width: 0;
    color: var(--text) !important;
    text-decoration: none !important;
}

.top-brand-mark {
    width: 44px;
    height: 44px;
    flex: 0 0 44px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 13px;
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    box-shadow: 0 8px 18px rgba(14, 165, 164, 0.20);
}

.top-brand strong,
.top-brand small {
    display: block;
    letter-spacing: 0;
}

.top-brand strong {
    margin-bottom: 0.15rem;
    color: var(--text);
    font-size: 0.98rem;
    line-height: 1.15;
    font-weight: 900;
    text-transform: uppercase;
}

.top-brand small {
    color: var(--muted);
    font-size: 0.72rem;
    line-height: 1.2;
    font-weight: 650;
}

.st-key-top_navigation div[data-testid="stButton"] button {
    min-height: 52px !important;
    padding: 0 0.7rem !important;
    position: relative !important;
    background: transparent !important;
    border: none !important;
    border-radius: 0 !important;
    box-shadow: none !important;
    color: var(--muted) !important;
    font-size: 0.86rem !important;
    line-height: 1 !important;
    font-weight: 800 !important;
    letter-spacing: 0 !important;
    transform: none !important;
}

.st-key-top_navigation div[data-testid="stButton"] button:hover {
    background: rgba(14, 165, 164, 0.06) !important;
    color: var(--primary-dark) !important;
    border: none !important;
    box-shadow: none !important;
    transform: none !important;
}

.st-key-top_navigation div[data-testid="stButton"] button::after {
    content: "";
    position: absolute;
    left: 0.9rem;
    right: 0.9rem;
    bottom: 0;
    height: 3px;
    border-radius: 3px 3px 0 0;
    background: transparent;
}

.st-key-top_navigation div[data-testid="stButton"] button[kind="primary"] {
    color: var(--primary-dark) !important;
}

.st-key-top_navigation div[data-testid="stButton"] button[kind="primary"]::after {
    background: linear-gradient(90deg, var(--primary), var(--secondary));
}

/* ============================================================
   SIDEBAR FIXED TANPA SCROLLBAR KECIL
============================================================ */

section[data-testid="stSidebar"] {
    width: 285px !important;
    min-width: 285px !important;
    max-width: 285px !important;

    height: 100vh !important;
    min-height: 100vh !important;
    max-height: 100vh !important;

    position: sticky !important;
    top: 0 !important;
    align-self: flex-start !important;

    background: linear-gradient(180deg, #FFFFFF 0%, #FAFCFE 100%) !important;
    border-right: 1px solid var(--line) !important;
    box-shadow: 8px 0 28px rgba(15, 23, 42, 0.04);

    overflow: hidden !important;
    box-sizing: border-box !important;
}

section[data-testid="stSidebar"] * {
    box-sizing: border-box !important;
}

section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
    height: 100vh !important;
    max-height: 100vh !important;

    padding-top: 1rem !important;
    padding-left: 0.95rem !important;
    padding-right: 0.95rem !important;
    padding-bottom: 1rem !important;

    overflow: hidden !important;
    overflow-x: hidden !important;
    overflow-y: hidden !important;

    scrollbar-width: none !important;
    -ms-overflow-style: none !important;
}

section[data-testid="stSidebar"] [data-testid="stSidebarContent"]::-webkit-scrollbar {
    width: 0 !important;
    height: 0 !important;
    display: none !important;
}

section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {
    width: 100% !important;
    max-width: 100% !important;
    padding-top: 0 !important;
    margin-top: 0 !important;
    overflow: visible !important;
}

section[data-testid="stSidebar"] > div:first-child {
    padding-top: 0 !important;
    overflow: hidden !important;
}

section[data-testid="stSidebar"] .element-container {
    width: 100% !important;
    max-width: 100% !important;
    margin-bottom: 0.28rem !important;
    overflow: visible !important;
}

section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] {
    width: 100% !important;
    max-width: 100% !important;
    gap: 0.42rem !important;
    overflow: visible !important;
}

section[data-testid="stSidebar"] iframe {
    max-width: 100% !important;
    overflow: hidden !important;
}

section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] div {
    color: var(--text);
}

/* ============================================================
   BRAND SIDEBAR
============================================================ */

.sb-brand {
    width: 100% !important;
    max-width: 100% !important;

    margin-top: 0 !important;
    margin-bottom: 1.65rem !important;
    padding: 0.82rem 0.84rem !important;

    border-radius: 17px !important;
    background: linear-gradient(135deg, #FFFFFF 0%, #F7FBFC 100%) !important;
    border: 1px solid var(--line) !important;

    display: flex !important;
    align-items: center !important;
    gap: 0.72rem !important;

    box-shadow: 0 14px 30px rgba(15, 23, 42, 0.065);
    overflow: hidden !important;
}

.sb-mark {
    width: 40px !important;
    height: 40px !important;
    min-width: 40px !important;

    border-radius: 14px !important;
    background: linear-gradient(135deg, #0EA5A4 0%, #2563EB 100%) !important;
    color: #FFFFFF !important;

    display: flex !important;
    align-items: center !important;
    justify-content: center !important;

    flex-shrink: 0 !important;
    box-shadow: 0 10px 22px rgba(14, 165, 164, 0.20);
}

.sb-mark svg {
    width: 21px !important;
    height: 21px !important;
    stroke-width: 2.4 !important;
}

.sb-brand-name {
    color: var(--text) !important;
    font-size: 0.92rem !important;
    font-weight: 900 !important;
    letter-spacing: 0.02em !important;
    text-transform: uppercase !important;
    line-height: 1.05 !important;
    white-space: nowrap !important;
}

.sb-brand-sub {
    color: var(--muted) !important;
    font-size: 0.68rem !important;
    font-weight: 700 !important;
    margin-top: 0.18rem !important;
    line-height: 1.25 !important;
    white-space: nowrap !important;
}

/* ============================================================
   SIDEBAR LABEL
============================================================ */

.sb-label {
    color: #64748B !important;
    font-size: 0.68rem !important;
    font-weight: 900 !important;
    letter-spacing: 0.14em !important;
    text-transform: uppercase !important;
    margin-top: 1.75rem !important;
    margin-bottom: 0.72rem !important;
}

.sb-brand + .sb-label {
    margin-top: 0 !important;
}

/* ============================================================
   NAVIGASI
============================================================ */

.nav-active {
    width: 100% !important;
    max-width: 100% !important;
    min-height: 48px !important;

    padding: 0.72rem 0.78rem !important;
    border-radius: 12px !important;

    background: rgba(14, 165, 164, 0.11) !important;
    border: 1.5px solid rgba(14, 165, 164, 0.38) !important;

    color: var(--text) !important;
    font-size: 0.86rem !important;
    font-weight: 850 !important;
    line-height: 1.2 !important;

    margin-top: 0 !important;
    margin-bottom: 1rem !important;

    display: flex !important;
    align-items: center !important;

    text-align: left !important;
    overflow: visible !important;
    box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.35) !important;
}

section[data-testid="stSidebar"] div[data-testid="stButton"] {
    width: 100% !important;
    max-width: 100% !important;
    margin-top: 0.25rem !important;
    margin-bottom: 1rem !important;
    overflow: visible !important;
}

section[data-testid="stSidebar"] div[data-testid="stButton"] button {
    width: 100% !important;
    max-width: 100% !important;
    min-height: 48px !important;

    background: transparent !important;
    color: #334155 !important;

    border: 1px solid rgba(14, 165, 164, 0.22) !important;
    border-radius: 12px !important;

    padding: 0.72rem 0.78rem !important;

    text-align: left !important;
    justify-content: flex-start !important;

    font-size: 0.86rem !important;
    font-weight: 800 !important;
    letter-spacing: 0 !important;
    line-height: 1.2 !important;

    transition: 0.15s ease !important;
    text-transform: none !important;

    box-shadow: none !important;
    transform: none !important;

    overflow: visible !important;
}

section[data-testid="stSidebar"] div[data-testid="stButton"] button div[data-testid="stMarkdownContainer"] {
    width: 100% !important;
    text-align: left !important;
}

section[data-testid="stSidebar"] div[data-testid="stButton"] button p {
    width: 100% !important;
    text-align: left !important;
    color: #334155 !important;
    font-size: 0.86rem !important;
    font-weight: 800 !important;
}

section[data-testid="stSidebar"] div[data-testid="stButton"] button:hover {
    background: rgba(14, 165, 164, 0.08) !important;
    color: var(--text) !important;
    border-color: rgba(14, 165, 164, 0.35) !important;
    transform: none !important;
    box-shadow: none !important;
}

/* ============================================================
   STATUS MODEL
============================================================ */

.status-banner {
    width: 100% !important;
    max-width: 100% !important;

    border: 1px solid rgba(245, 158, 11, 0.35);
    background: rgba(245, 158, 11, 0.09);

    padding: 0.82rem 0.88rem;
    border-radius: 16px;

    display: flex;
    gap: 0.72rem;
    align-items: flex-start;

    margin-top: 0 !important;
    margin-bottom: 1.65rem !important;

    overflow: hidden !important;
}

.status-banner.ok {
    border-color: rgba(22, 163, 74, 0.25);
    background: rgba(22, 163, 74, 0.08);
}

.status-banner .dot {
    width: 10px;
    height: 10px;
    min-width: 10px;
    border-radius: 999px;
    background: var(--warning);
    margin-top: 0.34rem;
    flex-shrink: 0;
}

.status-banner.ok .dot {
    background: var(--success);
}

.status-banner b {
    color: #B45309;
    font-size: 0.72rem;
    font-weight: 900;
    letter-spacing: 0.10em;
    text-transform: uppercase;
}

.status-banner.ok b {
    color: #15803D;
}

.status-banner p {
    color: var(--text);
    font-size: 0.80rem;
    line-height: 1.55;
    margin: 0.22rem 0 0 0;
}

.page-status {
    margin-top: 0.95rem !important;
    margin-bottom: 1.05rem !important;
}

/* ============================================================
   FORM SIDEBAR - FIX ANGKA SLIDER TERPOTONG
============================================================ */

div[data-testid="stSlider"] label,
.stSelectbox label {
    color: var(--text) !important;
    font-size: 0.84rem !important;
    font-weight: 700 !important;
    letter-spacing: 0 !important;
    margin-bottom: 0.35rem !important;
}

/* Container slider dibuat lebih tinggi dan tidak memotong angka bawah */
section[data-testid="stSidebar"] .stSlider {
    width: 100% !important;
    max-width: 100% !important;

    min-height: 92px !important;
    height: auto !important;

    padding-top: 0.04rem !important;
    padding-bottom: 1.55rem !important;

    margin-bottom: 1.85rem !important;

    overflow: visible !important;
    overflow-x: visible !important;
    overflow-y: visible !important;
}

/* Semua anak slider dibuat visible supaya angka 0.05 dan 0.95 tidak kepotong */
section[data-testid="stSidebar"] .stSlider * {
    overflow: visible !important;
}

/* Wrapper element yang berisi slider juga jangan memotong isi */
section[data-testid="stSidebar"] .element-container:has(.stSlider) {
    overflow: visible !important;
    min-height: 104px !important;
    margin-bottom: 1.55rem !important;
}

/* Track slider diberi ruang bawah */
section[data-testid="stSidebar"] div[data-testid="stSlider"] {
    min-height: 92px !important;
    padding-bottom: 1.45rem !important;
    overflow: visible !important;
}

/* Angka min dan max slider */
section[data-testid="stSidebar"] div[data-testid="stSlider"] [data-testid="stTickBar"],
section[data-testid="stSidebar"] div[data-testid="stSlider"] [data-testid="stTickBarMin"],
section[data-testid="stSidebar"] div[data-testid="stSlider"] [data-testid="stTickBarMax"] {
    color: var(--text) !important;
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    overflow: visible !important;
    padding-top: 0.25rem !important;
}

/* Selectbox tetap aman */
section[data-testid="stSidebar"] .stSelectbox {
    width: 100% !important;
    max-width: 100% !important;
    margin-top: 0.55rem !important;
    margin-bottom: 0.85rem !important;
    overflow: visible !important;
}

section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
    width: 100% !important;
    max-width: 100% !important;
    background: #FFFFFF !important;
    border-radius: 12px !important;
}

section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div {
    background: #FFFFFF !important;
    color: #0F172A !important;
    -webkit-text-fill-color: #0F172A !important;
    border-radius: 12px !important;
    border: 1px solid var(--line-2) !important;
    min-height: 42px !important;
}

section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] div,
section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] span,
section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] input {
    color: #0F172A !important;
    -webkit-text-fill-color: #0F172A !important;
    font-weight: 750 !important;
    font-size: 0.86rem !important;
}

section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] svg {
    color: #0F172A !important;
    fill: #0F172A !important;
}

/* ============================================================
   HERO / BERANDA
============================================================ */

.hero-wrap {
    border-radius: 26px !important;
    padding: 2.35rem 2.45rem !important;
    margin-bottom: 1.25rem !important;
    background: linear-gradient(135deg, var(--surface) 0%, #F4F8F9 100%) !important;
    border: 1px solid var(--line) !important;
    box-shadow: var(--shadow);
    position: relative;
    overflow: hidden;
}

.hero-wrap::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 5px;
    height: 100%;
    background: linear-gradient(180deg, var(--primary), var(--secondary));
}

.hero-title {
    color: var(--text);
    font-size: clamp(2.2rem, 4vw, 4rem);
    line-height: 1.05;
    font-weight: 900;
    letter-spacing: -0.06em;
    text-transform: uppercase;
    margin-bottom: 1rem;
}

.hero-title span {
    color: var(--primary);
}

.hero-sub {
    color: var(--muted);
    font-size: 1rem;
    line-height: 1.75;
    max-width: 840px !important;
    margin-bottom: 1.5rem;
}

.eyebrow {
    display: flex;
    align-items: center;
    gap: 0.55rem;
    color: var(--primary-dark);
    font-size: 0.74rem;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 0.13em;
    margin-bottom: 1rem;
}

.eyebrow::before {
    content: "";
    width: 8px;
    height: 8px;
    background: var(--primary);
    border-radius: 2px;
    display: inline-block;
}

.spec-row {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    border: 1px solid var(--line);
    border-radius: 18px;
    overflow: hidden;
    background: var(--surface-raised);
}

.spec-item {
    padding: 1rem;
    border-right: 1px solid var(--line);
}

.spec-item:last-child {
    border-right: none;
}

.spec-label {
    color: var(--muted-2);
    font-size: 0.68rem;
    font-weight: 900;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 0.35rem;
}

.spec-value {
    color: var(--text);
    font-size: 0.9rem;
    font-weight: 800;
}

.hazard-rule {
    height: 4px;
    border-radius: 999px;
    background: linear-gradient(90deg, var(--primary), var(--secondary), transparent);
    margin: 1.4rem 0 1.5rem 0;
}

/* ============================================================
   CARD / SECTION
============================================================ */

.action-panel,
.system-card,
.process-card,
.feat-card {
    background: var(--surface-raised);
    border: 1px solid var(--line);
    border-radius: 22px;
    box-shadow: 0 14px 34px rgba(15, 23, 42, 0.05);
}

.action-panel {
    padding: 1.15rem 1.25rem;
    margin: 1.05rem 0 0.95rem 0;
    position: relative;
    overflow: hidden;
}

.action-panel::before {
    content: "";
    position: absolute;
    inset: 0 auto 0 0;
    width: 4px;
    background: linear-gradient(180deg, var(--primary), var(--secondary));
}

.action-kicker,
.card-label {
    color: var(--primary-dark);
    font-size: 0.72rem;
    font-weight: 900;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
}

.action-title {
    color: var(--text);
    font-size: 1.05rem;
    font-weight: 900;
    margin-bottom: 0.18rem;
}

.action-desc,
.section-desc,
.feat-desc {
    color: var(--muted);
    font-size: 0.88rem;
    line-height: 1.6;
}

.system-card,
.process-card {
    padding: 1.55rem;
    height: 100%;
    transition: 0.18s ease;
}

.system-card:hover,
.process-card:hover,
.feat-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 18px 42px rgba(15, 23, 42, 0.08);
    border-color: rgba(14, 165, 164, 0.38);
}

.system-card h3 {
    color: var(--text);
    font-size: 1.45rem;
    line-height: 1.2;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: -0.04em;
    margin: 0 0 0.85rem 0;
}

.system-card p {
    color: var(--muted);
    font-size: 0.95rem;
    line-height: 1.75;
    margin: 0;
}

.mini-metric-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.75rem;
    margin-top: 1.25rem;
}

.mini-metric {
    background: var(--surface-soft);
    border: 1px solid var(--line);
    border-radius: 15px;
    padding: 0.85rem 0.9rem;
}

.mini-metric span {
    display: block;
    color: var(--muted-2);
    font-size: 0.67rem;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 0.10em;
    margin-bottom: 0.25rem;
}

.mini-metric b {
    color: var(--text);
    font-size: 0.92rem;
    font-weight: 900;
}

.process-item {
    display: flex;
    gap: 1rem;
    align-items: flex-start;
    padding: 1rem 0;
    border-bottom: 1px solid var(--line);
}

.process-item:first-child {
    padding-top: 0;
}

.process-item:last-child {
    border-bottom: none;
    padding-bottom: 0;
}

.process-icon,
.icon-box,
.camera-helper-icon,
.detect-status-icon {
    width: 42px;
    height: 42px;
    border-radius: 14px;
    background: rgba(14, 165, 164, 0.10);
    border: 1px solid rgba(14, 165, 164, 0.24);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.process-item h4 {
    color: var(--text);
    font-size: 1rem;
    font-weight: 900;
    margin: 0 0 0.35rem 0;
}

.process-item p {
    color: var(--muted);
    font-size: 0.88rem;
    line-height: 1.6;
    margin: 0;
}

.section-head {
    color: var(--text);
    font-size: 1.7rem;
    font-weight: 900;
    letter-spacing: -0.04em;
    text-transform: uppercase;
    margin-bottom: 0.35rem;
}

.feat-card {
    padding: 1.35rem;
    height: 100%;
    transition: 0.18s ease;
}

.feat-title {
    color: var(--text);
    font-size: 1rem;
    font-weight: 900;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.tally-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid var(--line);
    padding: 0.55rem 0;
}

.tally-row:last-child {
    border-bottom: none;
}

.tally-name {
    display: flex;
    gap: 0.55rem;
    align-items: center;
    color: var(--muted);
    font-size: 0.86rem;
    font-weight: 650;
}

.tally-swatch {
    width: 9px;
    height: 9px;
    border-radius: 2px;
    display: inline-block;
}

.tally-count {
    color: var(--text);
    font-weight: 900;
}

/* ============================================================
   HALAMAN DETEKSI
============================================================ */

.configuration-heading {
    padding: 1.2rem 1.3rem;
    margin-bottom: 0.8rem;
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 1rem;
    background: var(--surface-raised);
    border: 1px solid var(--line);
    border-radius: 18px;
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.045);
}

.configuration-kicker {
    margin-bottom: 0.35rem;
    color: var(--primary-dark);
    font-size: 0.68rem;
    line-height: 1;
    font-weight: 900;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.configuration-heading h3 {
    margin: 0 0 0.3rem 0;
    color: var(--text);
    font-size: 1.12rem;
    line-height: 1.25;
    font-weight: 900;
    letter-spacing: 0;
}

.configuration-heading p {
    margin: 0;
    color: var(--muted);
    font-size: 0.84rem;
    line-height: 1.5;
}

.configuration-state {
    flex: 0 0 auto;
    padding: 0.52rem 0.7rem;
    display: inline-flex;
    align-items: center;
    gap: 0.48rem;
    border: 1px solid rgba(22, 163, 74, 0.22);
    border-radius: 999px;
    background: rgba(22, 163, 74, 0.07);
    color: #15803D;
    font-size: 0.68rem;
    line-height: 1;
    font-weight: 900;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    white-space: nowrap;
}

.configuration-state span {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #16A34A;
}

.configuration-state.missing {
    border-color: rgba(245, 158, 11, 0.26);
    background: rgba(245, 158, 11, 0.08);
    color: #B45309;
}

.configuration-state.missing span {
    background: var(--warning);
}

.deployment-grid {
    margin-bottom: 0.8rem;
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0.75rem;
}

.deployment-item {
    min-width: 0;
    padding: 1rem;
    display: flex;
    align-items: flex-start;
    gap: 0.8rem;
    background: linear-gradient(135deg, var(--surface-raised) 0%, var(--surface) 100%);
    border: 1px solid var(--line);
    border-radius: 16px;
    box-shadow: 0 10px 26px rgba(15, 23, 42, 0.04);
}

.deployment-icon {
    width: 39px;
    height: 39px;
    flex: 0 0 39px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 11px;
    background: var(--primary-soft);
    border: 1px solid rgba(14, 165, 164, 0.14);
}

.deployment-item span,
.deployment-item strong,
.deployment-item small {
    display: block;
    min-width: 0;
    letter-spacing: 0;
}

.deployment-item span {
    margin-bottom: 0.22rem;
    color: var(--muted);
    font-size: 0.65rem;
    line-height: 1.1;
    font-weight: 850;
    text-transform: uppercase;
}

.deployment-item strong {
    overflow-wrap: anywhere;
    color: var(--text);
    font-size: 0.9rem;
    line-height: 1.3;
    font-weight: 900;
}

.deployment-item small {
    margin-top: 0.2rem;
    color: var(--muted);
    font-size: 0.72rem;
    line-height: 1.35;
    font-weight: 550;
}

div[data-testid="stVerticalBlockBorderWrapper"]:has(.parameter-panel-marker) {
    margin-bottom: 1.15rem;
    background: var(--surface-raised);
    border: 1px solid var(--line-2) !important;
    border-radius: 18px !important;
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.05);
}

.parameter-panel-marker {
    padding-bottom: 0.8rem;
    border-bottom: 1px solid var(--line);
}

.parameter-panel-marker span {
    display: block;
    margin-bottom: 0.22rem;
    color: var(--text);
    font-size: 0.95rem;
    line-height: 1.2;
    font-weight: 900;
    letter-spacing: 0;
}

.parameter-panel-marker p {
    margin: 0;
    color: var(--muted);
    font-size: 0.78rem;
    line-height: 1.45;
}

div[data-testid="stVerticalBlockBorderWrapper"]:has(.parameter-panel-marker) label p {
    color: var(--text) !important;
    font-size: 0.82rem !important;
    font-weight: 800 !important;
    letter-spacing: 0 !important;
}

.detect-hero {
    background: linear-gradient(135deg, var(--surface) 0%, #F4F8F9 100%);
    border: 1px solid var(--line);
    border-radius: 24px;
    padding: 1.55rem 1.65rem;
    margin-bottom: 1.15rem;
    box-shadow: 0 14px 34px rgba(15, 23, 42, 0.05);
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 1rem;
    position: relative;
    overflow: hidden;
}

.detect-hero::before {
    content: "";
    position: absolute;
    inset: 0 auto 0 0;
    width: 5px;
    background: linear-gradient(180deg, var(--primary), var(--secondary));
}

.live-chip {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0.55rem 0.75rem;
    border-radius: 999px;
    background: rgba(22, 163, 74, 0.08);
    border: 1px solid rgba(22, 163, 74, 0.25);
    color: #15803D;
    font-size: 0.72rem;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    white-space: nowrap;
}

.live-chip span {
    width: 8px;
    height: 8px;
    border-radius: 999px;
    background: #16A34A;
    box-shadow: 0 0 0 5px rgba(22, 163, 74, 0.10);
}

.detect-status {
    background: var(--surface-raised);
    border: 1px solid var(--line);
    border-radius: 20px;
    padding: 1rem 1.1rem;
    display: flex;
    align-items: flex-start;
    gap: 0.9rem;
    margin-bottom: 1.15rem;
    box-shadow: 0 14px 34px rgba(15, 23, 42, 0.05);
}

.detect-status.ok {
    border-color: rgba(14, 165, 164, 0.26);
    background: linear-gradient(135deg, var(--surface-raised) 0%, #F1FAF8 100%);
}

.detect-status.warning {
    border-color: rgba(245, 158, 11, 0.30);
    background: linear-gradient(135deg, var(--surface-raised) 0%, #FFF9EA 100%);
}

.detect-status h4 {
    color: var(--text);
    font-size: 0.98rem;
    font-weight: 900;
    margin: 0 0 0.25rem 0;
}

.detect-status p {
    color: var(--muted);
    font-size: 0.88rem;
    line-height: 1.55;
    margin: 0;
}

.camera-panel {
    background: var(--surface-raised);
    border: 1px solid var(--line-2);
    border-radius: 22px;
    overflow: hidden;
    margin-bottom: 0.75rem;
    box-shadow: 0 14px 34px rgba(15, 23, 42, 0.06);
}

.camera-topbar {
    padding: 0.85rem 1rem;
    background: linear-gradient(90deg, var(--surface-soft) 0%, #EAF2F4 100%);
    border-bottom: 1px solid var(--line);
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.camera-topbar span {
    color: var(--muted);
    font-size: 0.72rem;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 0.10em;
}

.camera-topbar b {
    color: var(--primary-dark);
    font-size: 0.72rem;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 0.10em;
}

.camera-helper {
    background: linear-gradient(135deg, var(--surface-raised) 0%, #F1FAF8 100%);
    border: 1px solid rgba(14, 165, 164, 0.28);
    border-radius: 18px;
    padding: 1rem 1.05rem;
    display: flex;
    align-items: flex-start;
    gap: 0.9rem;
    margin: 0.85rem 0 1.25rem 0;
    box-shadow: 0 12px 28px rgba(15, 23, 42, 0.045);
}

.camera-helper h4 {
    color: var(--text);
    font-size: 0.98rem;
    font-weight: 900;
    margin: 0 0 0.3rem 0;
}

.camera-helper p {
    color: var(--muted);
    font-size: 0.88rem;
    line-height: 1.6;
    margin: 0;
}

.detect-metric-title {
    margin-top: 1.35rem !important;
    font-size: 1.45rem !important;
}

/* ============================================================
   WEBRTC
============================================================ */

div[data-testid="stCustomComponentV1"],
div[data-testid="stIFrame"] {
    overflow: visible !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}

/* ============================================================
   METRIK
============================================================ */

.readout-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 22px;
    overflow: hidden;
    box-shadow: 0 14px 34px rgba(15, 23, 42, 0.05);
}

.readout {
    padding: 1.15rem;
    border-right: 1px solid var(--line);
}

.readout:last-child {
    border-right: none;
}

.readout-label {
    color: var(--muted);
    font-size: 0.68rem;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.4rem;
}

.readout-value {
    color: var(--text);
    font-size: 1.45rem;
    font-weight: 900;
}

.readout-value.safe {
    color: var(--success);
}

.readout-value.warn {
    color: var(--warning);
}

.readout-value.bad {
    color: var(--danger);
}

/* ============================================================
   BUTTON UMUM
============================================================ */

div[data-testid="stButton"] button {
    border-radius: 14px !important;
    border: 1px solid rgba(14, 165, 164, 0.42) !important;
    background: linear-gradient(135deg, #0EA5A4, #2563EB) !important;
    color: #FFFFFF !important;
    padding: 0.72rem 1.25rem !important;
    font-weight: 850 !important;
    font-size: 0.88rem !important;
    transition: 0.18s ease !important;
    box-shadow: 0 12px 24px rgba(14, 165, 164, 0.16) !important;
}

div[data-testid="stButton"] button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 16px 30px rgba(37, 99, 235, 0.18) !important;
    color: #FFFFFF !important;
    border-color: rgba(37, 99, 235, 0.45) !important;
}

div[data-testid="stButton"] button:active {
    transform: scale(0.98) !important;
    box-shadow: 0 8px 18px rgba(15, 23, 42, 0.12) !important;
}

div[data-testid="stButton"] button[kind="secondary"] {
    background: var(--surface-raised) !important;
    color: var(--text) !important;
    border: 1px solid var(--line-2) !important;
    box-shadow: 0 10px 22px rgba(15, 23, 42, 0.05) !important;
}

div[data-testid="stButton"] button[kind="secondary"]:hover {
    background: var(--surface-soft) !important;
    color: var(--primary-dark) !important;
    border-color: rgba(14, 165, 164, 0.35) !important;
}

/* tombol sidebar jangan ikut style tombol utama */
section[data-testid="stSidebar"] div[data-testid="stButton"] button {
    background: transparent !important;
    color: #334155 !important;
    border: 1px solid rgba(14, 165, 164, 0.22) !important;
    justify-content: flex-start !important;
    box-shadow: none !important;
    transform: none !important;
}

section[data-testid="stSidebar"] div[data-testid="stButton"] button:hover {
    background: rgba(14, 165, 164, 0.08) !important;
    color: var(--text) !important;
    border-color: rgba(14, 165, 164, 0.35) !important;
    transform: none !important;
    box-shadow: none !important;
}

section[data-testid="stSidebar"] div[data-testid="stButton"] button p {
    color: #334155 !important;
    text-align: left !important;
}

/* ============================================================
   RESPONSIVE
============================================================ */

@media (min-width: 1440px) {
    .st-key-top_navigation {
        min-height: 82px;
        padding: 0.85rem var(--page-gutter);
    }

    .hero-wrap {
        padding: 2.75rem 3rem !important;
    }

    .hero-sub {
        max-width: 1120px !important;
    }

    .system-card,
    .process-card {
        padding: 1.8rem;
    }

    .feat-card {
        padding: 1.45rem;
    }

    .detect-hero {
        padding: 1.8rem 2rem;
    }

    .configuration-heading {
        padding: 1.35rem 1.55rem;
    }

    .deployment-item {
        padding: 1.15rem;
    }
}

@media (max-width: 900px) {
    .block-container {
        --page-gutter: 1rem;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    .st-key-top_navigation {
        width: calc(100% + 2rem) !important;
        position: relative;
        top: 0;
    }

    .spec-row {
        grid-template-columns: repeat(2, 1fr) !important;
    }

    .deployment-grid {
        grid-template-columns: 1fr;
    }

    .mini-metric-grid,
    .readout-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .detect-hero {
        flex-direction: column;
    }
}

@media (max-width: 640px) {
    .block-container {
        --page-gutter: 0.75rem;
        padding-top: 0 !important;
        padding-left: 0.75rem !important;
        padding-right: 0.75rem !important;
    }

    .st-key-top_navigation {
        width: calc(100% + 1.5rem) !important;
        padding: 0.8rem var(--page-gutter);
        border-radius: 0;
    }

    .st-key-top_navigation div[data-testid="stHorizontalBlock"] {
        flex-wrap: wrap;
        gap: 0.45rem !important;
    }

    .st-key-top_navigation div[data-testid="stColumn"]:nth-child(1) {
        flex: 0 0 100% !important;
        width: 100% !important;
    }

    .st-key-top_navigation div[data-testid="stColumn"]:nth-child(2),
    .st-key-top_navigation div[data-testid="stColumn"]:nth-child(3) {
        flex: 1 1 calc(50% - 0.25rem) !important;
        width: calc(50% - 0.25rem) !important;
    }

    .top-brand-mark {
        width: 40px;
        height: 40px;
        flex-basis: 40px;
    }

    .st-key-top_navigation div[data-testid="stButton"] button {
        min-height: 44px !important;
        padding: 0 0.35rem !important;
        border-top: none !important;
        font-size: 0.8rem !important;
    }

    .configuration-heading {
        padding: 1rem;
        flex-direction: column;
    }

    .configuration-state {
        align-self: flex-start;
    }
}
</style>
"""
