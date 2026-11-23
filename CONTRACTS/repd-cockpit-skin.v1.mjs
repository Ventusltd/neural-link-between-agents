/**
 * REPD Cockpit visual skin — coordination/reference module v1.
 * Source of truth: the existing native V9.73 REPD table CSS and computed styles.
 *
 * This is a read-only design reference in Neural Link, NOT imported by a live
 * Pipeline News release. A release owner must transplant and test it separately.
 * Do not repaint the existing REPD table, gauges, ticker or MAP/A4.
 */
export const REPD_SKIN_CONTRACT_V1 = Object.freeze({
  sourceRepository: 'Ventusltd/globalgrid2050',
  sourceEdition: 'uk_renewables_pipeline/202611222330/',
  anchors: Object.freeze([
    '#repdScroll thead th',
    '#repdScroll tbody .mw',
    '#repdScroll tbody .site',
    '#repdScroll tbody td'
  ]),
  sourceCss: Object.freeze([
    'styles/v7.css',
    'styles/repd-scan.css',
    'styles/repd-expanded.css',
    'styles/hud-v955.css',
    'styles/repd-reports.css'
  ]),
  secondaryScadaReference: Object.freeze({
    repository: 'Ventusltd/gridatlas',
    edition: 'atlas/releases/202608300453-atlas-v9/',
    css: 'ventusv8.css',
    shell: 'index.html',
    liveGenerationAtStudy: '202611222343',
    visualRoles: Object.freeze({
      shell: '#000000',
      hud: '#0a0a0a',
      instrument: '#00ffff',
      news: '#ffae00',
      active: '#00ffff',
      panel: '#050505'
    }),
    constraint: 'SCADA is a secondary stylistic reference; never replace established native REPD table or physics-significant GridAtlas voltage colours.'
  }),
  crossDisciplineAudit: Object.freeze({
    datacentres: Object.freeze({
      source: 'automation/news/datacentre-ui/styles.css',
      mismatch: 'yellow (#f4df73) headers, alternate teal (#62e7ed) and #142328 headings; different input/border colours',
      action: 'new scoped adapter must inherit REPD table header cyan, row text, dark substrate and controls'
    }),
    gridAndOfftakers: Object.freeze({
      source: 'uk_renewables_pipeline/202611222330/scripts/layers/pipeline-layers.css',
      mismatch: 'selected button amber (#ffd24a), unlike native REPD cyan; source counts also amber',
      action: 'normalise controls/labels only; preserve true kV and engineering-layer encoding'
    }),
    prices: Object.freeze({
      source: 'automation/price_daily_ui/78d5360239e1a5fcffa83fcb30d5937c5521acb9/styles.css',
      mismatch: '10px rounded/glowing cards and red (#ff5555) statistical labels unlike REPD restrained cockpit',
      action: 'adopt REPD borders, radii, header and neutral data-label hierarchy; keep genuine alarms red'
    })
  }),
  unchangedTechnologyColors: Object.freeze({
    solar: '#ffff00',
    bess: '#ffae00',
    wind_onshore: '#00ffff',
    wind_offshore: '#0066ff',
    interconnector: '#0066ff'
  }),
  unchangedTickerColor: '#ff3038',
  policy: 'Capture and reuse native computed colours. Never override native REPD selectors. Fail closed if anchors cannot be found.'
});

const ROLES = Object.freeze({
  surface: '--pn-repd-match-surface',
  panel: '--pn-repd-match-panel',
  border: '--pn-repd-match-border',
  headerBackground: '--pn-repd-match-header-bg',
  headerText: '--pn-repd-match-header-text',
  rowText: '--pn-repd-match-row-text',
  projectText: '--pn-repd-match-project-text',
  capacityText: '--pn-repd-match-capacity-text',
  accent: '--pn-repd-match-accent',
  solar: '--pn-repd-match-solar',
  bess: '--pn-repd-match-bess',
  onshore: '--pn-repd-match-onshore',
  offshore: '--pn-repd-match-offshore',
  ticker: '--pn-repd-match-ticker'
});

export function captureNativeRepdSkin(doc) {
  if (!doc || !doc.defaultView || typeof doc.defaultView.getComputedStyle !== 'function') {
    throw new Error('A rendered REPD document is required to capture the native skin');
  }
  const pick = (selector) => {
    const node = doc.querySelector(selector);
    if (!node) throw new Error('Native REPD skin anchor missing: ' + selector);
    return doc.defaultView.getComputedStyle(node);
  };
  const root = pick(':root');
  const header = pick('#repdScroll thead th');
  const mw = pick('#repdScroll tbody .mw');
  const site = pick('#repdScroll tbody .site');
  const row = pick('#repdScroll tbody td');
  const panel = pick('#repdScroll');
  const readVar = (name) => {
    const value = root.getPropertyValue(name).trim();
    if (!value) throw new Error('Missing existing REPD CSS token: ' + name);
    return value;
  };
  const ticker = doc.querySelector('#headlineTicker .pn-ticker-title');
  return Object.freeze({
    surface: readVar('--bg'),
    panel: panel.backgroundColor,
    border: readVar('--line'),
    headerBackground: header.backgroundColor,
    headerText: header.color,
    rowText: row.color,
    projectText: site.color,
    capacityText: mw.color,
    accent: readVar('--accent'),
    solar: readVar('--solar'),
    bess: readVar('--bess'),
    onshore: readVar('--accent'),
    offshore: readVar('--off'),
    ticker: ticker ? doc.defaultView.getComputedStyle(ticker).color : null
  });
}

/**
 * Assigns ONLY scoped custom properties on a NEW report host. It does not
 * change existing table, controls, gauges, ticker, body or other disciplines.
 * Pair with scoped CSS that consumes these --pn-repd-match-* variables.
 */
export function bindNativeRepdSkinToReportHost(host) {
  if (!host || !host.ownerDocument || typeof host.style?.setProperty !== 'function') {
    throw new Error('A rendered report host element is required');
  }
  if (host.matches('#repdScroll, #officialRegister, #repdPanel, body, html')) {
    throw new Error('Refusing to restyle a native REPD container');
  }
  const native = captureNativeRepdSkin(host.ownerDocument);
  for (const [role, property] of Object.entries(ROLES)) {
    if (native[role]) host.style.setProperty(property, native[role]);
  }
  host.dataset.repdSkinContract = 'native-v973-parity-v1';
  return native;
}

export function validateRepdSkinParity(host) {
  const native = captureNativeRepdSkin(host.ownerDocument);
  const missing = [];
  for (const [role, property] of Object.entries(ROLES)) {
    const expected = native[role];
    if (!expected) continue;
    const actual = host.style.getPropertyValue(property).trim();
    if (actual !== expected) missing.push({role, expected, actual});
  }
  return Object.freeze({pass: missing.length === 0, missing, sourceEdition: REPD_SKIN_CONTRACT_V1.sourceEdition});
}
