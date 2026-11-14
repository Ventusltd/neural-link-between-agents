// Preload: shift the JS clock to FAKE_NOW (ISO) while letting it tick. Test-only evidence tool.
const target = Date.parse(process.env.FAKE_NOW), real = Date.now, off = target - real();
const R = Date;
class FD extends R { constructor(...a) { if (a.length === 0) super(real() + off); else super(...a); } static now() { return real() + off; } }
globalThis.Date = FD;
