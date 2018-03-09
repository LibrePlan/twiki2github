#!/bin/bash

#rsync -av  --include=*.md  libreplan.wiki/* testwiki.wiki/.

rm -rf twiki2github.wiki
#git clone   https://github.com/kwoot/testwiki.wiki.git
git clone   https://github.com/LibrePlan/twiki2github.wiki.git

# cleanup
rm  libreplan.wiki/twiki/LibrePlan/*\?*

rsync -avm --include='*\.md' --include='*.gif'  -f 'hide,! */'  libreplan.wiki/*   twiki2github.wiki/.
#cd twiki2github.wiki
#git add *
#git commit -a -m 'auto commit'
#git push
# clean up all files before next run
#git rm -r *
#cd ..

