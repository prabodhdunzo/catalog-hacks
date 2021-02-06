# catalog-hacks

Perfect script to hack catalog related stuff for dropshop.

Few handy scripts to fetch data from prod SKU.

```
declare -a b=("BREAKFAST%20%26%20DAIRY" "PROVISIONS" "CONDIMENTS" "SNACKS%20%26%20FROZEN%20FOOD" "CHOCOLATES%20%26%20ICE-CREAM" "PERSONAL%20CARE" "CLEANING%20%26%20HOUSEHOLD")
```

```
for bb in "${b[@]}"                                                                                                                                                   
    for a in {1..15}
    curl 'https://www.dunzo.com/v3/sku/listing/67c00343-077a-4482-8622-368ab7f16bfe/tab/'$bb'?subTag=Grocery&page='"$a"'&size=1000' \
  -H 'authority: www.dunzo.com' \
  -H 'pragma: no-cache' \
  -H 'cache-control: no-cache' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'dnt: 1' \                                                                                                               
  -H 'x-app-version: 2.0.0' \
  -H 'x-app-type: PWA_WEB' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.dunzo.com/bangalore/dropshop-kalyan-nagar' \
  -H 'accept-language: en-US,en;q=0.9,hi;q=0.8' \
  -H 'cookie: dz_e=ZGYxODhiZmItOGM0Yi00MWNjLTkyZGMtYTVmNWQyYWI2MDNjX3Yx; connect.sid=s%3AQlNb7WFtGGaQL5n_sIzzLeQmHuXIvYmE.LUCqao8dk3YqBIRt60UR0QayF1UPx2UpcsuVXedc8BE; lux_uid=161254666507357577; _gcl_au=1.1.2127912523.1612546665; WZRK_G=02e3218ec2af4ffb8d7ef0b0fea7b8bb; WZRK_S_46R-KR9-WZ5Z=%7B%22p%22%3A1%2C%22s%22%3A1612546665%2C%22t%22%3A1612546665%7D; _gid=GA1.2.1992568000.1612546665; _gat_UA-74154936-4=1; _ga=GA1.1.241025125.1599471971; _fbp=fb.1.1612546665855.1652718174; _ga_MH9JSX933B=GS1.1.1612546513.43.1.1612546703.0' \
  --compressed | jq -r -S ".data.skuList.subCategories | .[] | .products | .[] | {(.skuId):[.imageUrl, .subTitle]}" >> pc
```
