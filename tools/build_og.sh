#!/bin/zsh
# Tạo ảnh chia sẻ Facebook/Zalo 1200x630 cho từng trang: zsh tools/build_og.sh
set -e
cd "$(dirname "$0")/.."
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT=8766
python3 -m http.server $PORT >/dev/null 2>&1 &
SRV=$!
trap "kill $SRV" EXIT
sleep 1
PROFILE=$(mktemp -d)

shot() { # out img pos title phone sub
  local url="http://127.0.0.1:$PORT/tools/og.html?img=/images/$2&pos=$3&t=$(python3 -c 'import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1]))' "$4")&p=$5&s=$(python3 -c 'import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1]))' "$6")"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --user-data-dir="$PROFILE" \
    --window-size=1200,630 --virtual-time-budget=4000 --screenshot="/tmp/og-$1.png" "$url" >/dev/null 2>&1
  sips -s format jpeg -s formatOptions 82 "/tmp/og-$1.png" --out "images/share-$1.jpg" >/dev/null
  echo "images/share-$1.jpg"
}

shot home hai-va-dan-giao.webp "50% 45%" "Xe tải chở hàng, dàn giáo, vật liệu ở Điện Bàn" "0363 569 319" "Zalo 0707 477 243|Bán, cho thuê, chở"
shot xe-tai xe-tai-cho-do.webp "50% 60%" "Xe tải chở hàng ở Điện Bàn" "0707 477 243" "Anh Hải, có Zalo|Quân 0783 346 050"
shot dan-giao khung-dan-giao.webp "center" "Cho thuê, mua bán dàn giáo Điện Bàn" "0363 569 319" "Dàn tiệp mới, cũ|Có sẵn ở bãi"
shot vat-lieu boc-gach-len-xe.webp "center" "Cát, đá, gạch, xi măng ở Điện Bàn" "0363 569 319" "Chở tận nơi bằng|xe tải, xe lôi"
