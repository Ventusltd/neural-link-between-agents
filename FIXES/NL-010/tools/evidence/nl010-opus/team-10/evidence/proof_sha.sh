#!/bin/bash
# proof/edition-sha256.txt: every file of the edition folder except handoff/, proof/handoff/ and this file; sha256sum format, sorted (Edition 4's ./ form)
cd /home/user/estate/kuiper-belt/editions/202611012135 || exit 2
find . -type f ! -path './handoff/*' ! -path './proof/handoff/*' ! -path './proof/edition-sha256.txt' -print0 | LC_ALL=C sort -z | xargs -0 sha256sum > proof/edition-sha256.txt
wc -l proof/edition-sha256.txt
