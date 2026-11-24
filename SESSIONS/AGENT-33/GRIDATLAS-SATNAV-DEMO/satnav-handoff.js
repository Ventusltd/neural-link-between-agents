/* Detached GridAtlas/SatNav compatibility proof. */
void async function () {
  const proofRoot = new URL('../../../proof/agent33/', location.href);
  const compass = new URL('https://ventusltd.github.io/satnav/preview/9698781539e549deaa6ecaa4a2b34610c1f9fd29/nav/');
  const { buildDestination } = await import(new URL('compass/nav/place.mjs', proofRoot));
  const { normaliseOrigin } = await import(new URL('../../../tools/vicinity/src/model.mjs', location.href));
  const style = document.createElement('style');
  style.textContent = `
    #agent33-satnav { position:absolute; z-index:1200; left:12px; top:52px;
      width:min(380px,calc(100% - 24px)); box-sizing:border-box; padding:12px;
      border:1px solid #367078; border-radius:6px; background:#08141bed;
      color:#e4f7f7; font:14px/1.45 ui-monospace,monospace; }
    #agent33-satnav h2 { margin:0 0 8px; font:inherit; font-weight:bold; color:#00ffff; }
    #agent33-satnav p { margin:8px 0 0; overflow-wrap:anywhere; }
    #agent33-satnav .actions { display:flex; flex-wrap:wrap; gap:6px; }
    #agent33-satnav button { min-height:44px; max-width:100%; padding:6px 9px;
      border:1px solid #367078; border-radius:3px; background:#07191f;
      color:#bff7f9; font:inherit; cursor:pointer; text-align:left; }
    #agent33-satnav button:disabled { color:#8ba0a2; cursor:default; }
    #agent33-satnav button:focus-visible { outline:2px solid #fff; outline-offset:1px; }
    #agent33-satnav [hidden] { display:none; }
  `;
  document.head.append(style);
  const panel = document.createElement('section');
  panel.id = 'agent33-satnav';
  panel.setAttribute('aria-labelledby', 'agent33-satnav-title');
  const heading = document.createElement('h2');
  heading.id = 'agent33-satnav-title';
  heading.textContent = 'SatNav handoff demo';
  const actions = document.createElement('div');
  actions.className = 'actions';
  const confirmation = document.createElement('div');
  confirmation.className = 'actions';
  const status = document.createElement('p');
  status.setAttribute('role', 'status');
  status.textContent = 'Waiting for the GridAtlas map…';
  function button(id, name, parent = actions) {
    const element = document.createElement('button');
    element.type = 'button';
    element.id = `agent33-${id}`;
    element.textContent = name;
    parent.append(element);
    return element;
  }
  const pick = button('pick', 'Choose point on satellite');
  const origin = button('origin', 'Use Vicinity origin');
  const asset = button('asset', 'Use highlighted asset');
  const confirm = button('confirm', 'Use this destination', confirmation);
  const cancel = button('cancel', 'Cancel', confirmation);
  panel.append(heading, actions, status, confirmation);
  document.body.append(panel);

  const samePoint = (a, b) => a?.length === 2 && b?.length === 2 && a[0] === b[0] && a[1] === b[1];
  const satellite = () => document.querySelector('#scada-ui-container input[name="bm"][value="sat"]');
  let map, marker, armed = false, pending = null;

  // Read the exact current project or swiped item from the native Vicinity card.
  function currentCardPoint(kind) {
    const card = window.__GRIDATLAS_MODULES__?.ukOfftakers?.state.pp;
    if (!card?.project) return null;
    if (kind === 'origin') return { card, name: card.r.n, at: card.r.a };
    const swipe = card.swipe;
    const entry = swipe?.entries[swipe.index];
    const highlight = swipe?.marker?.getLngLat();
    if (!entry || !highlight || !samePoint([highlight.lng, highlight.lat], entry.at)) return null;
    return { card, index: swipe.index, name: entry.name, at: entry.at };
  }

  function reset(message) {
    armed = false;
    pending = null;
    marker?.remove();
    marker = null;
    status.textContent = message;
    render();
  }

  function render() {
    pick.disabled = !map?.getLayer('l-sat') || !satellite();
    pick.setAttribute('aria-pressed', String(armed));
    origin.disabled = !currentCardPoint('origin');
    asset.disabled = !currentCardPoint('asset');
    origin.hidden = origin.disabled;
    asset.hidden = asset.disabled;
    confirmation.hidden = !armed && !pending;
    confirm.hidden = !pending;
  }

  function stage(kind, selection) {
    if (!selection) return;
    reset('');
    try {
      const value = normaliseOrigin({ at: selection.at, name: selection.name, type: 'map-point' });
      pending = { kind, selection: { ...selection, at: value.at }, value };
      if (kind === 'map') marker = new window.maplibregl.Marker({ color: '#00ffff' }).setLngLat(value.at).addTo(map);
      status.textContent = `${value.name} · ${value.at[1].toFixed(6)}, ${value.at[0].toFixed(6)}`;
      render();
      confirm.focus();
    } catch {
      reset('Choose a valid map point.');
    }
  }

  // Same armed MapLibre click and [longitude, latitude] order as Vicinity bootstrap.
  function mapClick(event) {
    if (armed && event.lngLat) stage('map', { name: 'Chosen map point', at: [event.lngLat.lng, event.lngLat.lat] });
  }

  pick.onclick = () => {
    if (armed) { reset('Selection cancelled.'); return; }
    reset('Tap a point on the satellite map.');
    const input = satellite();
    if (!input.checked) input.click();
    armed = true;
    render();
  };
  origin.onclick = () => stage('origin', currentCardPoint('origin'));
  asset.onclick = () => stage('asset', currentCardPoint('asset'));
  cancel.onclick = () => { reset('Selection cancelled.'); pick.focus(); };
  confirm.onclick = () => {
    if (!pending) return;
    const { kind, selection, value } = pending;
    if (kind !== 'map') {
      const current = currentCardPoint(kind);
      if (!current || current.card !== selection.card || current.index !== selection.index ||
          current.name !== selection.name || !samePoint(current.at, value.at)) {
        reset('The Vicinity selection changed. Select it again.');
        pick.focus();
        return;
      }
    }
    const query = buildDestination({ name: value.name, coordinates: value.at, mode: 'compass' });
    location.assign(new URL(query, compass));
  };
  panel.addEventListener('keydown', event => {
    if (event.key === 'Escape' && (armed || pending)) { event.preventDefault(); cancel.click(); }
  });
  for (const type of ['click', 'dblclick', 'mousedown', 'pointerdown', 'touchstart']) {
    panel.addEventListener(type, event => event.stopPropagation());
  }

  function refresh() {
    const nativeMap = window.__GRIDATLAS_V9_MAP__;
    if (nativeMap && nativeMap !== map && nativeMap.getLayer('l-sat')) {
      map?.off('click', mapClick);
      map = nativeMap;
      map.getContainer().append(panel);
      map.on('click', mapClick);
      status.textContent = 'Choose a point or use an open Vicinity card.';
    }
    render();
  }
  refresh();
  let timer = setInterval(refresh, 250);
  window.addEventListener('pagehide', () => {
    clearInterval(timer);
    map?.off('click', mapClick);
    reset('Choose a point or use an open Vicinity card.');
    map = null;
  });
  window.addEventListener('pageshow', event => {
    if (!event.persisted) return;
    refresh();
    timer = setInterval(refresh, 250);
  });
}().catch(error => console.error('Detached SatNav handoff failed', error));
