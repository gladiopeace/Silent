echo "~ Lib for GLOBAL ~"
echo "Loading..."
sleep 1

echo "鈻讹笍 starting PUBG MOBILE"
am start -n com.vng.pubgmobile/com.epicgames.ue4.SplashActivity

sleep 2





mv /data/data/com.vng.pubgmobile/lib/libUE4.so /storage/emulated/0/OriG/
mv /data/data/com.vng.pubgmobile/lib/libtprt.so /storage/emulated/0/OriG/







mv /storage/emulated/0/LibMod/libUE4.so /data/data/com.vng.pubgmobile/lib
mv /storage/emulated/0/LibMod/libtprt.so /data/data/com.vng.pubgmobile/lib



chmod -R 755 /data/data/com.vng.pubgmobile/lib/libUE4.so 
chmod -R 755 /data/data/com.vng.pubgmobile/lib/libtprt.so 
chmod -R 755 /data/data/com.vng.pubgmobile/lib/libgcloud.so 
