#!/usr/bin/env bash
set -e
export OFFICIAL_BUILD=true
export RETROFIT=false
source script/envsetup.sh
breakfast lineage_guacamole user
m target-files-package
m otatools-package
folder=out/target/product/guacamole/obj/PACKAGING/target_files_intermediates/
for file in ${folder}lineage_*
do
    file_name=${file##*/}
    new_path=$folder${file_name:8}
    mv -- "$file" "$new_path"
done
script/release.sh guacamole
echo "$BUILD_NUMBER successfully built"
