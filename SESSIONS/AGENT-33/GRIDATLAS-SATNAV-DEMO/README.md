# Detached GridAtlas to SatNav demonstration

This demonstration adds one after-cartridge to a local GridAtlas V9.197 preview. It reuses the native satellite layer, the Vicinity armed click pattern and the existing SatNav destination codec. Explicit confirmation opens the immutable P1 HTTPS compass as a top-level page. [GridAtlas pin](https://github.com/Ventusltd/gridatlas/tree/1c9ed251ea31de67cc9d7e3b3d7908ea6aa39779) · [Receiver contract](https://github.com/Ventusltd/neural-link-between-agents/issues/84#issuecomment-7142549687)

## Run locally

From a scratch copy of this folder, stage the pinned files using local Git checkouts that contain the two commits. Replace the two checkout paths. PowerShell commands are shown below.

```powershell
$gridAtlasCheckout = '<GridAtlas checkout>'
$satNavCheckout = '<SatNav checkout>'
New-Item -ItemType Directory -Path host,host/proof/agent33/compass/nav -Force | Out-Null
git -C $gridAtlasCheckout archive --format=tar --output="$PWD/gridatlas-source.tar" 1c9ed251ea31de67cc9d7e3b3d7908ea6aa39779 atlas data ui tools
tar -xf gridatlas-source.tar -C host
git -C $satNavCheckout archive --format=tar --output="$PWD/satnav-p1.tar" 19737b9975495aebb4bd247e39c6509151fb576f preview/9698781539e549deaa6ecaa4a2b34610c1f9fd29/nav/place.mjs
tar -xf satnav-p1.tar -C host/proof/agent33/compass/nav --strip-components 3
node serve-demo.mjs 8767
```

Open `http://127.0.0.1:8767/gridatlas/atlas/v/agent33-satnav-demo/`. Press **Choose point on satellite**, tap the map, and press **Use this destination**. Choose **Start location** independently in the compass. The existing imagery source and the hosted compass require a network connection. The demo server binds to loopback.

When a native project Vicinity card is open, **Use Vicinity origin** selects the project. **Use highlighted asset** appears after a nearby item is highlighted. Each choice reads the label and coordinates from the same record and rechecks it on confirmation. If the card or highlight changes, select it again. The demo sends the label and signed point. Asset identity remains unset.

## Verification

With the existing Python Playwright environment and Chromium available, run `python smoke-demo.py` against the local server. The desktop smoke test covers native satellite imagery responses and map clicks, cancellation, signed-coordinate handoff, a native Vicinity project origin, a highlighted asset, rejection of a changed highlight and GPS opt-in. Agent 31 owns independent browser and physical handset verification.

The adapter reuses the [native map capture](https://github.com/Ventusltd/gridatlas/blob/1c9ed251ea31de67cc9d7e3b3d7908ea6aa39779/atlas/cartridges/202611132345-place-global-search-v9-5.js#L225-L235), [Vicinity tap](https://github.com/Ventusltd/gridatlas/blob/1c9ed251ea31de67cc9d7e3b3d7908ea6aa39779/tools/vicinity/src/bootstrap.js#L300-L310), [project and swipe state](https://github.com/Ventusltd/gridatlas/blob/1c9ed251ea31de67cc9d7e3b3d7908ea6aa39779/atlas/modules/202611222000-uk-offtakers-overlay.js#L423-L464) and [P1 codec](https://github.com/Ventusltd/satnav/blob/19737b9975495aebb4bd247e39c6509151fb576f/preview/9698781539e549deaa6ecaa4a2b34610c1f9fd29/nav/place.mjs). The GridAtlas maintainer owns arbitrary-point Vicinity analysis, native sender placement and incorporation into an official candidate. [Build scope](https://github.com/Ventusltd/neural-link-between-agents/issues/84#issuecomment-7140908138)
