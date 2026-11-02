  // ==== SECTION C begin (OPUS-6 builder): EXPORT, the EDIT paste field, the Backspace rule, copy-or-show
  // Keys: GridAtlas's export and clipboard method, gridatlas@5ec7f62 atlas/modules/202609031958-menu-bar.js:707-733
  // (copy, else show the payload in full), :794-811 (export this view; the image is checked before it is offered),
  // :813-816 exportStamp (UTC to the minute), :1082-1097 looksBlank (sample a 40x40 probe), :1120-1137 capture INSIDE a
  // render frame, :1354-1365 every export control named by id and data-*-export. The Kuiper's WebGL context is
  // {antialias:false, alpha:false} with no preserveDrawingBuffer (editions/202611012135/index.html:122), so a read outside
  // the frame is opaque black, not transparent: the blank test here is "every probe pixel one colour" (alpha 0 included),
  // GridAtlas's sample taken one step further for an opaque canvas. The capture runs as the last painter of KY.draw.add,
  // after the engine's wafer (index.html:332-363) and overlay (:384 ff.) in the same task.
  var C = (function () {
    var KYc = null, Hc = null, Lk = null, st = { exports: [], copies: [], pastes: [], backspace: 0, capture: null };
    var COPIED_MS = 4000, CAPTURE_ORDER = 1e9, CAPTURE_WAIT_MS = 4000;
    var LICENCE_LINE = 'code Apache-2.0, text and data CC BY 4.0';           // editions/README.md:27
    var BLANK_WORDS = 'the image came back blank; try again after the wafer has drawn';
    function mk(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }

    // ---- copy, never silent (6.1 LINK; 6.L1). rowEl: the row that asked; text: the payload.
    function payloadField(rowEl) { return rowEl.parentNode ? rowEl.parentNode.querySelector('input.ky-file-payload[data-for="' + rowEl.id + '"]') : null; }
    var PAYLOAD_CSS = 'ky-file-payload-css';
    function payloadStyle() {                                         // a 44 px field in the shell's face (MB:221 rows >= 44 px)
      if (document.getElementById(PAYLOAD_CSS)) return; var c = mk('style'); c.id = PAYLOAD_CSS;
      c.textContent = 'input.ky-file-payload{display:block;box-sizing:border-box;width:100%;min-height:44px;margin:0;padding:10px 12px;'
        + 'font:12px/1.4 ui-monospace,Menlo,Consolas,monospace;color:#fff;background:#05070c;border:1px solid #2ee6e6;border-radius:0;'
        + '-webkit-user-select:text;user-select:text}';
      document.head.appendChild(c);
    }
    function showPayload(rowEl, text, why) {
      payloadStyle();
      var f = payloadField(rowEl);
      if (!f) { f = mk('input', 'ky-file-payload'); f.type = 'text'; f.readOnly = true; f.setAttribute('data-for', rowEl.id);
        f.setAttribute('aria-label', 'the clipboard is not available here: select and copy this by hand');
        f.addEventListener('click', function (e) { e.stopPropagation(); f.select(); });
        f.addEventListener('focus', function () { f.select(); });
        rowEl.parentNode.insertBefore(f, rowEl.nextSibling); }
      f.value = text; f.title = why;
      try { f.focus({ preventScroll: true }); } catch (e) { try { f.focus(); } catch (e2) {} }
      try { f.select(); f.setSelectionRange(0, text.length); } catch (e) {}
      st.copies.push({ row: rowEl.id, ok: false, why: why, text: text });
      return false;
    }
    function copyText(rowEl, text) {
      var label = rowEl.querySelector('.ky-file-label') || rowEl.firstChild || rowEl;
      if (!rowEl.hasAttribute('data-label')) rowEl.setAttribute('data-label', label.textContent);
      var was = rowEl.getAttribute('data-label'), clip = navigator.clipboard;
      if (!clip || typeof clip.writeText !== 'function') return Promise.resolve(showPayload(rowEl, text, 'navigator.clipboard is not available on this page'));
      var p; try { p = clip.writeText(text); } catch (e) { return Promise.resolve(showPayload(rowEl, text, 'the clipboard refused: ' + (e && e.message || e))); }
      return Promise.resolve(p).then(function () {
        var f = payloadField(rowEl); if (f) f.remove();
        label.textContent = '✓ Copied'; st.copies.push({ row: rowEl.id, ok: true, text: text });
        clearTimeout(rowEl._kyCopied); rowEl._kyCopied = setTimeout(function () { label.textContent = was; }, COPIED_MS);
        return true;
      }, function (e) { return showPayload(rowEl, text, 'the clipboard refused: ' + (e && e.message || e)); });
    }

    // ---- EXPORT (6.1): the capture, the blank test, the stamp
    function looksBlank(canvas) {                                    // GridAtlas :1082 generalised for an opaque canvas
      try {
        var probe = mk('canvas'); probe.width = 40; probe.height = 40;
        var c = probe.getContext('2d'); c.drawImage(canvas, 0, 0, 40, 40);
        var d = c.getImageData(0, 0, 40, 40).data, r = d[0], g = d[1], b = d[2], a = d[3], anyAlpha = false;
        for (var i = 0; i < d.length; i += 4) { if (d[i + 3] !== 0) anyAlpha = true; if (d[i] !== r || d[i + 1] !== g || d[i + 2] !== b || d[i + 3] !== a) return false; }
        return true;                                                   // one colour (or wholly transparent)
      } catch (e) { return false; }                                    // a tainted canvas is not blank (GridAtlas :1090-1094)
    }
    function utcStamp(now) { return now.toISOString().replace('T', ' ').slice(0, 16) + ' UTC'; }      // GridAtlas :813-816
    function editionName() {
      var m = String(Hc.big && Hc.big.textContent || '').match(/Kuiper Edition \d+/i);
      return (m ? m[0] : 'Kuiper edition') + ' · ' + KYc.edition;
    }
    function viewLink() {
      try { if (Lk && typeof Lk.hashText === 'function') { var h = Lk.hashText(); return location.origin + location.pathname + (h ? '#' + h : ''); } } catch (e) {}
      return location.origin + location.pathname + location.hash;
    }
    // the foot every exported artefact carries: edition, stamp, UTC time, licence, and the link that reopens the view
    function footLines(now) { return [editionName() + ' · ' + utcStamp(now), LICENCE_LINE, viewLink()]; }
    var pending = null;
    function capturePainter() {                                       // runs inside draw(), after the wafer and the overlay
      if (!pending) return; var p = pending; pending = null; clearTimeout(p.timer);
      try {
        var cv = Hc.cv, ov = Hc.ov, W = cv.width, Hh = cv.height;
        if (!W || !Hh) { p.done(null, 'the wafer has no size to capture'); return; }
        var view = mk('canvas'); view.width = W; view.height = Hh;
        var v = view.getContext('2d'); v.drawImage(cv, 0, 0); v.drawImage(ov, 0, 0, W, Hh);
        p.done(view, null);
      } catch (e) { p.done(null, 'the capture failed: ' + (e && e.message || e)); }
    }
    function capture() {                                              // -> Promise<{view} | {refused}>
      return new Promise(function (res) {
        if (pending) { clearTimeout(pending.timer); pending.done(null, 'a newer capture was asked for'); }
        pending = { done: function (view, why) { res(view ? { view: view } : { refused: why }); },
          timer: setTimeout(function () { if (pending) { pending = null; res({ refused: BLANK_WORDS }); } }, CAPTURE_WAIT_MS) };
        KYc.redraw();
      });
    }
    function stamped(view, now) {                                     // innerWidth x min(dpr, 2) wide, the foot below the view
      var s = Math.min(window.devicePixelRatio || 1, 2), W = Math.round(innerWidth * s), Hv = Math.round(innerHeight * s);
      var lines = footLines(now), fs = Math.round(11 * s), lh = Math.round(16 * s), pad = Math.round(8 * s), footH = pad * 2 + lh * lines.length;
      var out = mk('canvas'); out.width = W; out.height = Hv + footH;
      var o = out.getContext('2d'); o.imageSmoothingEnabled = true;
      o.fillStyle = '#000'; o.fillRect(0, 0, W, Hv); o.drawImage(view, 0, 0, W, Hv);
      o.fillStyle = '#05070c'; o.fillRect(0, Hv, W, footH);
      o.fillStyle = '#2ee6e6'; o.fillRect(0, Hv, W, Math.max(1, Math.round(s)));          // the instrument's line (PALETTE.md)
      o.font = fs + 'px ui-monospace, Menlo, Consolas, monospace'; o.textBaseline = 'top'; o.fillStyle = '#c9d3e6';
      lines.forEach(function (t, i) { o.fillText(t, pad, Hv + pad + i * lh, W - 2 * pad); });
      return { canvas: out, foot: { lines: lines, height: footH, scale: s } };
    }
    function say(rowEl, words) {                                      // the row's own second line says what happened
      var h = rowEl.querySelector('.ky-file-why'); if (!h) { h = mk('span', 'gm-hint ky-file-why'); rowEl.appendChild(h); }
      h.textContent = words; rowEl.setAttribute('data-ky-state', words === '' ? '' : words.slice(0, 40));
    }
    function fileName(now) { return 'kuiper-' + KYc.edition + '-' + now.toISOString().slice(0, 16).replace(/[-:]/g, '') + 'Z.png'; }
    function exportImage(rowEl) {
      var now = new Date(); say(rowEl, 'capturing inside the next frame…');
      return capture().then(function (r) {
        if (r.refused) { st.exports.push({ kind: 'image', ok: false, why: r.refused, at: now.toISOString() }); say(rowEl, r.refused); return null; }
        if (looksBlank(r.view)) { st.exports.push({ kind: 'image', ok: false, why: BLANK_WORDS, at: now.toISOString() }); say(rowEl, BLANK_WORDS); return null; }
        var s = stamped(r.view, now);
        return new Promise(function (res) {
          s.canvas.toBlob(function (blob) {
            if (!blob) { say(rowEl, BLANK_WORDS); st.exports.push({ kind: 'image', ok: false, why: 'toBlob returned nothing' }); res(null); return; }
            var url = URL.createObjectURL(blob), a = mk('a'); a.href = url; a.download = fileName(now); a.style.display = 'none';
            document.body.appendChild(a); a.click(); a.remove(); setTimeout(function () { URL.revokeObjectURL(url); }, 60000);
            var rec = { kind: 'image', ok: true, file: a.download, bytes: blob.size, width: s.canvas.width, height: s.canvas.height,
              view_height: s.canvas.height - s.foot.height, foot: s.foot.lines, at: now.toISOString() };
            st.exports.push(rec); say(rowEl, '✓ saved ' + a.download + ' · ' + blob.size + ' bytes'); res(rec);
          }, 'image/png');
        });
      });
    }
    // Print: the same image and foot in a print stylesheet; the browser's print-to-PDF is the PDF (no PDF writer copied)
    var PRINT_ID = 'ky-file-print', PRINT_CSS = 'ky-file-print-css';
    function printView(rowEl) {
      var now = new Date(); say(rowEl, 'capturing inside the next frame…');
      return capture().then(function (r) {
        var why = r.refused || (looksBlank(r.view) ? BLANK_WORDS : null);
        if (why) { st.exports.push({ kind: 'print', ok: false, why: why, at: now.toISOString() }); say(rowEl, why); return null; }
        var s = stamped(r.view, now), old = document.getElementById(PRINT_ID); if (old) old.remove();
        if (!document.getElementById(PRINT_CSS)) { var css = mk('style'); css.id = PRINT_CSS;
          css.textContent = '#' + PRINT_ID + '{display:none}@media print{body>*:not(#' + PRINT_ID + '){display:none!important}'
            + '#' + PRINT_ID + '{display:block!important;position:static;background:#fff;color:#000}#' + PRINT_ID + ' img{width:100%;height:auto;display:block}'
            + '@page{margin:10mm}}'; document.head.appendChild(css); }
        var box = mk('div'); box.id = PRINT_ID; box.setAttribute('aria-hidden', 'true');
        var img = mk('img'); img.alt = s.foot.lines[0]; img.src = s.canvas.toDataURL('image/png'); box.appendChild(img);
        document.body.appendChild(box);
        var rec = { kind: 'print', ok: true, width: s.canvas.width, height: s.canvas.height, foot: s.foot.lines, at: now.toISOString() };
        st.exports.push(rec); say(rowEl, '✓ sent to the browser’s print · ' + s.foot.lines[0]);
        var go = function () { try { window.print(); } catch (e) { say(rowEl, 'this browser refused to print: ' + (e && e.message || e)); } };
        if (img.complete) go(); else img.onload = go;
        return rec;
      });
    }
    function exportRows(group, row) {                                 // row(label, onTap, id): the lead's row factory
      var img = row('⤓ Save an image of this view', function (el) { exportImage(el); return true; }, 'kuiper-export-image');
      img.setAttribute('data-ky-export', 'image');
      var pr = row('⎙ Print', function (el) { printView(el); return true; }, 'kuiper-export-print');
      pr.setAttribute('data-ky-export', 'print');
      group.appendChild(img); group.appendChild(pr); return [img, pr];
    }

    // ---- EDIT (6.5): the find box also takes a pasted Kuiper or See Through link; `Paste a link…` opens the same field
    var PLACEHOLDER_LINK = 'a key, a repository, a period, or a pasted link';
    function looksLikeLink(t) { return /^(https?:\/\/|\.{0,2}\/|[#?])/i.test(t) || /^(key|line|repo|period|layers|edition|app|sub|space)=/.test(t); }
    function takePaste(text) {                                        // true when the text was a link and was handled
      var t = String(text || '').trim(); if (!t || !looksLikeLink(t) || !Lk || typeof Lk.read !== 'function') return false;
      var r = Lk.read(t);
      if (!r) { st.pastes.push({ text: t, ok: false, why: 'not a link' }); return false; }
      st.pastes.push({ text: t, ok: true, target: r.target || 'kuiper', fields: r.fields, refused: r.refused });
      if (r.target === 'see-through' || r.target === 'other') { location.href = r.url; return true; }   // navigation, same tab
      if (typeof Lk.apply === 'function') Lk.apply(r.fields, { from: 'paste' });
      return true;
    }
    function wireFind() {
      var gin = Hc.gin, gbox = Hc.gbox;
      // capture phase on #goto runs before the engine's own keydown on #gotoin (index.html:605)
      gbox.addEventListener('keydown', function (e) {
        if (e.key !== 'Enter' || e.target !== gin) return;
        var t = gin.value.trim(); if (!looksLikeLink(t)) return;      // the find grammar (index.html:606-613) stays the engine's
        e.preventDefault(); e.stopImmediatePropagation(); e.stopPropagation();
        gbox.style.display = 'none'; takePaste(t);
      }, true);
      if (gin.placeholder !== PLACEHOLDER_LINK) { st.placeholder_was = gin.placeholder; gin.placeholder = PLACEHOLDER_LINK; }
    }
    function openPaste() {                                            // `Paste a link…`: the find box, named for a link
      var gbox = Hc.gbox, gin = Hc.gin;
      try { var sh = KYc.modules && KYc.modules['kuiper-shell'] && KYc.modules['kuiper-shell'].api; if (sh && sh.close) sh.close(); } catch (e) {}
      gbox.style.display = 'block'; gin.value = ''; gin.setAttribute('enterkeyhint', 'go');
      try { gin.focus(); } catch (e) {}
    }
    function pasteRow(editPanel, row) {
      if (!editPanel) return null;
      var r = row('Paste a link…', function () { openPaste(); return true; }, 'ky-edit-paste');
      r.setAttribute('data-ky-edit', 'paste');
      editPanel.appendChild(r); return r;
    }

    // ---- Backspace (whole wafer) clears every field but `layers` (6.3, 6.5)
    function wireBackspace() {
      addEventListener('keydown', function (e) {
        if (e.key !== 'Backspace' || Hc.gbox.style.display === 'block') return;
        var t = e.target; if (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) return;
        st.backspace++;
        if (Lk && typeof Lk.clear === 'function') Lk.clear(['layers']);
      });
    }

    return {
      install: function (K, link) { KYc = K; Hc = K.hooks; Lk = link; K.draw.add(capturePainter, CAPTURE_ORDER); wireFind(); wireBackspace(); },
      exportRows: exportRows, pasteRow: pasteRow, copyText: copyText, exportImage: exportImage, printView: printView,
      takePaste: takePaste, looksBlank: looksBlank, footLines: footLines,
      inspect: function () { return JSON.parse(JSON.stringify(st)); },
      strings: { blank: BLANK_WORDS, licence: LICENCE_LINE, placeholder: PLACEHOLDER_LINK }
    };
  })();
  // ==== SECTION C end
