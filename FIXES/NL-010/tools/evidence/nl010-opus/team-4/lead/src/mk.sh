#!/bin/bash
# rebuild: patched page, loader reference, the patch, MODULE.sha256
set -e
L=/tmp/nl010-opus/team-4/lead; E=/home/user/estate/kuiper-belt/editions/202611012135; H=$E/handoff/04-loader
python3 $L/src/build.py $L/work/patched.html
awk '/<script type="module">/{f=1;next} /<\/script>/{f=0} f' $L/work/patched.html > $L/work/page.mjs; node --check $L/work/page.mjs
{ head -6 $E/modules/202611012145-loader.js; cat $L/src/block.js; } > $L/work/loader.js && mv $L/work/loader.js $E/modules/202611012145-loader.js
node --check $E/modules/202611012145-loader.js 2>/dev/null || true
cd /home/user/estate/kuiper-belt
cp $L/work/patched.html $L/work/b.html
diff -u --label a/editions/202611012135/index.html --label b/editions/202611012135/index.html editions/202611012135/index.html $L/work/patched.html > $H/index.html.patch || true
git apply --check $H/index.html.patch && echo PATCH_APPLIES
(cd $E && sha256sum modules/202611012145-hello.js modules/202611012145-loader.js) > $H/MODULE.sha256
sha256sum $H/index.html.patch | sed "s#$H/##" >> $H/MODULE.sha256
cat $H/MODULE.sha256
