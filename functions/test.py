import re

def remove_m3u8_urls(script):
    # Regex to match .m3u8 URLs
    regex = re.compile(r'http[s]?://[^\s"]+\.m3u8')
    # Remove all occurrences of .m3u8 URLs from the script
    cleaned_script = re.sub(regex, '', script)
    return cleaned_script

# Example usage
script = """
<script type='text/javascript'>eval(function(p,a,c,k,e,d){while(c--)if(k[c])p=p.replace(new RegExp('\\b'+c.toString(a)+'\\b','g'),k[c]);return p}('q 5m=[];1a("cm").cl({ck:"1",cj:[{3e:"1t://ci.ch.1s/cg/cf/ce/cd,n,h,x,.cc/cb.ca?t=c9&s=c8&e=c7&f=5c&c6=3g&i=0.0&c5=c4&c3=3g&c2=3g&c1=c0"}],bz:"1t://5o.1s/by.3d",4f:"3f%",4e:"3f%",bx:"bw",bv:"5p.34",bu:\'bt\',bs:{br:{5q:"#1n",bq:"#1n"},bp:{bo:"#1n"},bn:{5q:"#1n"}},bm:"1p",y:[{3e:"/5e?5d=bl&1i=5p&bk=1t://5o.1s/bj.3d",bi:"bh"}],3q:{bg:1,bf:\'#1n\',be:\'#bd\',bc:"bb",ba:30,b9:\'3f\',},"b8":{"b7":"5k","b6":"b5"},\'b4\':{"b3":"b2","b1":"b0","az":"ay"},ax:"5n",aw:"1t://av.1s",au:{3e:"/at-39/as.3d",3b:"1t://5n.1s",1g:"ar-aq",ap:"5",2a:1p},ao:{},an:1p,3p:[0.25,0.5,0.75,1,1.25,1.5,2]});q 3a,3c;q am=0,al=0,ak=0;q o=1a();q 5h=0,aj=0,ai=0,1d=0;$.ah({ag:{\'af-ae\':\'ad-ac\'}});o.1e(\'5l\',k(x){j(5>0&&x.1g>=5&&3c!=1){3c=1;$(\'1o.ab\').aa(\'a9\')}5m.a8(1h=>{j(1h.5l<=x.1g&&1h.5i==0){j(1h.a7==\'5k\'){o.a6(1h.3b)}3n{q a=5j.a5(\'a4\');a.a3=1h.3b;5j.a2.a1(a);}1h.5i=1}});j(x.1g>=1d+5||x.1g<1d){1d=x.1g;38.a0(\'37\',9z.9y(1d),{9x:60*60*24*7})}});o.1e(\'2e\',k(x){5h=x.1g});o.1e(\'9w\',k(x){5g(x)});o.1e(\'9v\',k(){$(\'1o.5f\').9u();38.9t(\'37\')});o.1e(\'9s\',k(x){});k 5g(x){$(\'1o.5f\').2a();$(\'#9r\').2a();j(3a)2k;3a=1;2i=0;j(3t.9q===9p){2i=1}$.5b(\'/5e?5d=9o&9n=3s&9m=5c-9l-28-9k-9j&9i=1&9h=&2i=\'+2i,k(39){$(\'#9g\').9f(39)});q 1d=38.5b(\'37\');j(1d>0){1a().2e(1d)}}k 9e(){q y=o.2l(5a);59.58(y);j(y.1i>1){3k(i=0;i<y.1i;i++){j(y[i].3j==5a){59.58(\'!!=\'+i);o.3h(i)}}}}o.1e(\'9d\',k(){1a().1v(\'<p 29="26://23.22.1z/36/p" 4t="b-p-1f b-p-1f-9c" 35="0 0 2g 2g" 4s="1j"><1r d="m 25.9b,57.9a v 99.3 c 0.98,2.97 2.94,4.93 4.8,4.8 h 62.7 v -19.3 h -48.2 v -96.4 56 92.91 v 19.3 c 0,5.3 3.6,7.2 8,4.3 l 41.8,-27.9 c 2.90,-1.8z 4.8y,-5.8x 2.7,-8 -0.8w,-1.8v -1.8u,-2.8t -2.7,-2.7 l -41.8,-27.9 c -4.4,-2.9 -8,-1 -8,4.3 v 19.3 56 30.8s c -2.8r,0.8q -4.8p,2.8o -4.9,4.9 z m 8n.8m,73.8l c -3.55,-6.54 -10.53,-10.52 -17.7,-10.6 -7.50,0.4z -13.4y,4.4x -17.7,10.6 -8.2h,14.4w -8.2h,32.4v 0,46.3 3.55,6.54 10.53,10.52 17.7,10.6 7.50,-0.4z 13.4y,-4.4x 17.7,-10.6 8.2h,-14.4w 8.2h,-32.4v 0,-46.3 z m -17.7,47.2 c -7.8,0 -14.4,-11 -14.4,-24.1 0,-13.1 6.6,-24.1 14.4,-24.1 7.8,0 14.4,11 14.4,24.1 0,13.1 -6.5,24.1 -14.4,24.1 z m -47.8k,9.8j v -51 l -4.8,4.8 -6.8,-6.8 13,-12.8i c 3.8h,-3.8g 8.8f,-0.8e 8.2,3.4 v 62.8d z"></1r></p>\',"8c 10 4m",k(){1a().2e(1a().4l()+10)},"4u");$("1o[4k=4u]").4i().4h(\'.b-1f-2b\');1a().1v(\'<p 29="26://23.22.1z/36/p" 4t="b-p-1f b-p-1f-2b" 35="0 0 2g 2g" 4s="1j"><1r d="8b.2,8a.89.1c,21.1c,0,0,0-17.7-10.6,21.1c,21.1c,0,0,0-17.7,10.6,44.2f,44.2f,0,0,0,0,46.3,21.1c,21.1c,0,0,0,17.7,10.6,21.1c,21.1c,0,0,0,17.7-10.6,44.2f,44.2f,0,0,0,0-46.88-17.7,47.2c-7.8,0-14.4-11-14.4-24.87.6-24.1,14.4-24.1,14.4,11,14.4,24.86.4,4r.85,95.5,4r.84-43.4,9.7v-83-4.8,4.8-6.8-6.8,13-82.8,4.8,0,0,1,8.2,3.81.7l-9.6-.80-7z.7y.7x.4q,4.4q,0,0,1-4.8,4.7w.6v-19.7u.2v-96.7t.7s.7r,5.3-3.6,7.2-8,4.3l-41.8-27.7q.4p,6.4p,0,0,1-2.7-8,5.4o,5.4o,0,0,1,2.7-2.7p.8-27.7o.4-2.9,8-1,8,4.7n.7m.7k.4n,4.4n,0,0,1,7j.1,57.7i"></1r></p>\',"7h 10 4m",k(){q 2d=1a().4l()-10;j(2d<0)2d=0;1a().2e(2d)},"4j");$("1o[4k=4j]").4i().4h(\'.b-1f-2b\');$("1o.b-1f-2b").2a()});1a().1v(\'<p 29="26://23.22.1z/36/p" 29:4g="26://23.22.1z/7g/4g" 4f="7f" 4e="7e" 35="0 0 20 21" 7d="1.1"><g 7c="7b"><1r 7a=" 79:78;33-77:76;33:#1n;33-74:1;" d="2r 18.45 20.1q 16 1.4c 20.1q w 0.4d 20.1q 0 20.49 0 19.4a 16 0 14 w 0 13.1y 0.4d 12.1m 1.4c 12.1m w 2.72 12.1m 2.31 13.1y 2.31 14 16 2.31 18.4b 16 17.2z 18.4b 16 17.2z 14 w 17.2z 13.1y 17.71 12.1m 18.1x 12.1m w 19.2y 12.1m 19.1w 13.1y 19.1w 14 16 19.1w 19.4a w 20.70 20.49 19.6z 20.1q 18.45 20.1q 3v 2r 10.3u 12.2q w 10.2w 13.42 9.6y 13.42 9.6x 12.2q 16 4.3z 8.6w w 4.40 8.6u 4.40 7.2s 4.3z 7.2y w 5.6t 6.2t 5.6s 6.6r 6.6q 7.2y 16 8.1x 9.6p 16 8.1x 1.2w w 8.1x 0.3y 9.6o 0.2x 9.1w 0.2x w 10.6n 0.2x 11.2u 0.3y 11.2u 1.2w 16 11.2u 9.6m 16 13.6l 7.3x w 14.6k 6.2t 14.6j 6.2t 15.3w 7.3x w 15.2s 7.6i 15.2s 8.6h 15.3w 8.6g 3v 2r 10.3u 12.2q "/></g></p>\',"6f",k(){q 3r=3t.2p(\'/f/3s\',\'6e\');3r.6d()},"6c");o.1e("1b",k(6b){q y=o.2l();j(y.1i<2)2k;$(\'.b-u-6a-69\').68(k(){$(\'#b-u-r-1b\').2m(\'b-u-r-1u\');$(\'.b-r-1b\').1l(\'1k-2n\',\'1j\')});o.1v("/67/66.p","65 64",k(){$(\'.b-3o\').63(\'b-u-2p\');$(\'.b-u-3q, .b-u-3p\').1l(\'1k-2o\',\'1j\');j($(\'.b-3o\').61(\'b-u-2p\')){$(\'.b-r-1b\').1l(\'1k-2o\',\'1p\');$(\'.b-r-1b\').1l(\'1k-2n\',\'1p\');$(\'.b-u-r-5z\').2m(\'b-u-r-1u\');$(\'.b-u-r-1b\').5y(\'b-u-r-1u\')}3n{$(\'.b-r-1b\').1l(\'1k-2o\',\'1j\');$(\'.b-r-1b\').1l(\'1k-2n\',\'1j\');$(\'.b-u-r-1b\').2m(\'b-u-r-1u\')}},"5x");j(!5w.5v(\'5u\'))5t("3m(\'5s\')",5r)});q 2j;k 3m(3i){q y=o.2l();j(y.1i>1){3k(i=0;i<y.1i;i++){j(y[i].3j==3i){j(i==2j){2k}2j=i;o.3h(i)}}}}',36,455,'|||||||||||jw||||||||if|function||||player|svg|var|submenu|||settings||C||tracks||||||||L||||jwplayer|audioTracks|589|lastt|on|icon|position|item|length|false|aria|attr|617188|FFFFFF|div|true|976562|path|com|https|active|addButton|980469|5625|222656|org|||w3|www|||http|||xmlns|hide|rewind||tt|seek|769|240|60009|adb|current_audio|return|getAudioTracks|removeClass|expanded|checked|open|953125|M|816406|894531|394531||40625|0234375|355469|144531||832031||fill||viewBox|2000|tt0gpnm7280p3i|ls|data|vvplay|link|vvad|jpg|file|100|z13jtbat10fa85i|setCurrentAudioTrack|audio_name|name|for||audio_set|else|controls|playbackRates|captions|win|0gpnm7280p3i|window|902344|Z|320312|335938|628906|636719|140625||390625|||625||||371094|59375|191406|417969|621094|height|width|xlink|insertAfter|detach|ff00|button|getPosition|sec|974|887|013|867|178|focusable|class|ff11|06475|23525|29374|97928|30317|31579||29683|38421|30626|72072|H||log|console|track_name|get|2465|op|dl|video_ad|doPlay|prevt|loaded|document|vast|time|uas|StreamWish|roseimgs|10924|text|300|हिन्दी|setTimeout|default_audio|getItem|localStorage|dualSound|addClass|quality||hasClass||toggleClass|Track|Audio|dualy|images|mousedown|buttons|topbar|event|download11|focus|_blank|Download|929688|46875|777344|808594|011719|519531|242188|773438|183594|261719|4375|917969|921875|128906|507812||949219|097656|613281|421875|042969|769531|210938||opacity||nonzero|rule|none|stroke|style|surface1|id|version|21px|20px|1999|Rewind|778Z|214|2A4||3H209|3v19|9c4|7l41|9a6|3c0|1v19|4H79|3h48||8H146|3a4|2v125|130|1Zm162|4v62|13a4|51l|278Zm|278|1S103|1s6|3Zm|078a21|131|M113|Forward|69999|88605|21053|03598|02543|99999|72863|77056|04577|422413|163|210431|860275|03972|689569|893957|124979|52502|174985|57502|04363|13843|480087|93574|99396|160|76396|164107|||63589|03604|125|778|993957|rewind2|ready|set_audio_track|html|fviews|referer|embed|a071c5e14515002cef14d301708146f5|1726477081|104|hash|file_code|view|undefined|cRAds1|over_player_msg|pause|remove|show|complete|play|ttl|round|Math|set|appendChild|body|src|script|createElement|playAd|xtype|forEach|slow|fadeIn|video_ad_fadein|cache|no|Cache|Content|headers|ajaxSetup|v2done|tott|pop3done|vastdone2|vastdone1|playbackRateControls|cast|margin|left|top|logo_40|upload|logo|streamwish|aboutlink|abouttext|480p|517|720p|1060|1080p|2260|qualityLabels|insecure|vpaidmode|client|advertising|fontOpacity|backgroundOpacity|Tahoma|fontFamily|303030|backgroundColor|color|userFontScale|thumbnails|kind|0gpnm7280p3i0000|url|get_slides|androidhls|menus|progress|timeslider|icons|controlbar|skin|auto|preload|duration|uniform|stretching|0gpnm7280p3i_xt|image|13335|asn|p2|p1|500|sp|srv|129600|1726477082|Je0tMzHz699pMMGQ7JO_Wqt_DmF2eYm9FmvALNIMkF4|m3u8|master|urlset|0gpnm7280p3i_|00000|01|hls2|pradoi|e9ccawf5esyyffhp|sources|debug|setup|vplayer'.split('|')))
</script>
"""

cleaned_script = remove_m3u8_urls(script)
print(cleaned_script)