#!/bin/sh 
rm config.site
echo ac_cv_file__dev_ptmx=yes >> config.site 
echo ac_cv_file__dev_ptc=yes >> config.site 
export CONFIG_SITE=config.site
./configure CC=/opt/arm-2009q3-4.4.1/bin/arm-none-linux-gnueabi-gcc CXX=/opt/arm-2009q3-4.4.1/bin/arm-none-linux-gnueabi-g++ AR=/opt/arm-2009q3-4.4.1/bin/arm-none-linux-gnueabi-ar RANLIB=/opt/arm-2009q3-4.4.1/bin/arm-none-linux-gnueabi-ranlib READELF=/opt/arm-2009q3-4.4.1/bin/arm-none-linux-gnueabi-readelf --host=arm-none-linux --disable-ipv6 --build=i686-linux-gnu --prefix=/opt/python/Python-3.4.3/build --silent --target=arm-none-linux-gnueabi --enable-shared
