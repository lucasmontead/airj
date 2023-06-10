import subprocess
import hashlib
import base64
import json
import os
import re

POST_DESCRIPTION = 'Baixe ou assista online o episódio "{}" de {} em PT-BR e em alta qualidade.'
SEASON_DESCRIPTION = 'Baixar a {} de {} em alta qualidade.'

def limit_entries(entry_list):
    entries = entry_list.copy()
    numbers = []
    n = 100
    loop = 0
    
    while entries:
        limited_entries = []
        
        for i in entries[:100]:
            if 'Cartoon Network' in i['tags']:
                i['tags'].remove('Cartoon Network')
            
            try:
                description = i['description']
            
            except KeyError:
                description = ''
            
            limited_entries.append({
                'published': i['published'],
                'tags': i['tags'],
                'title': i['title'],
                'slug': i['slug'],
                'display_url': i['display_url'],
                'author': i['author'],
                'high_thumbnail': i['high_thumbnail'],
                'low_thumbnail': i['low_thumbnail'],
                'description': description
            })
        
        del entries[:100]
        
        with open(os.getcwd() + f'\\postagens\\{n}.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps({
                'data': base64.b64encode(json.dumps(limited_entries).encode('ascii')).decode()
            }))
        
        if not loop:
            with open(os.getcwd() + f'\\postagens\\10.json', 'w', encoding='utf-8') as e:
                e.write(json.dumps({
                    'data': base64.b64encode(json.dumps(limited_entries[:10]).encode('ascii')).decode()
                }))
        
        numbers.append(n)
        n += 100
        loop += 1
    
    pagination_guide = []
    pagination_guide.append({})
    pagination_guide.append({})
    
    pagination_guide[0]['type'] = 'pagination_guide'
    pagination_guide[1][f'{numbers[0]}.json'] = []
    
    for idx, val in enumerate(entry_list, start=1):
        if idx > numbers[0]:
            numbers.pop(0)
            pagination_guide[1][f'{numbers[0]}.json'] = []
        
        if not idx % 10:
            pagination_guide[1][f'{numbers[0]}.json'].append(idx)
        
        if len(entry_list) == idx:
            if idx % 10:
                if pagination_guide[1][f'{numbers[0]}.json'] == []:
                    pagination_guide[1][f'{numbers[0]}.json'].append(numbers[0] - 90)
                
                else:
                    pagination_guide[1][f'{numbers[0]}.json'].append(pagination_guide[1][f'{numbers[0]}.json'][-1] + 10)
                
                print(pagination_guide)
    
    with open(os.getcwd() + f'\\postagens\\{hashlib.md5(b"pagination_guide").hexdigest()}.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps({
            'data': base64.b64encode(json.dumps(pagination_guide).encode('ascii')).decode()
        }))
    
    """
    for i in range(len(pagination_guide[1].keys())):
        with open(os.getcwd() + f'\\postagens\\', 'w', encoding
    """

def gen_entries(type, entry_list):
    for entry in entry_list:
        entry_data = []
        tags = entry['tags']
        
        if 'Cartoon Network' in tags:
            tags.remove('Cartoon Network')
        
        try:
            description = entry['description']
        
        except KeyError:
            description = ''
        
        entry_data.append({
            'type': type,
            'published': entry['published'],
            'tags': entry['tags'],
            'title': entry['title'],
            'slug': entry['slug'],
            'display_url': entry['display_url'],
            'html': entry['html'],
            'author': entry['author'],
            'description': description
        })
        
        with open(os.getcwd() + f'\\postagens\\{entry["slug"]}.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps({
                'data': base64.b64encode(json.dumps(entry_data).encode('ascii')).decode()
            }))

# BEM-VINDOS AO SUBMUNDO (PARTE 1)
DISPLAY_URL = '/2019/10/cartoon-network-ao-vivo.html'
# DISPLAY_URL = '/2019/10/victor-e-valentino-s01e19.html'

HTML = '\n<style>\n.sidebar-right {display: none;}\n.static_page .post-head {\n    border-bottom: 0px;\n}\n\n.meta-details {\n    text-align: left;\n}\n</style>\n<img src="https://3.bp.blogspot.com/-D2pqG_yTfs8/W8UQSJ93iJI/AAAAAAAAFg4/rMn007hmvsApkNmbe7Hx9cEM-Y-cROsggCLcBGAs/s1000/cn-aovivo.png" style="display: none;"></img>\n<style>.playeriframe {  width: 896px;  height: 504px; }  @media screen and (max-width:1020px) {  .playeriframe {   width: 640px;   height: 360px;  } }  @media screen and (max-width:767px) {  .playeriframe {   width: 384px;   height: 216px;  } }  @media screen and (max-width:479px) {  .playeriframe {   width: 256px;   height: 144px;  } } </style><style>#chat_embed {  width: 896px;  height: 300px; }  @media screen and (max-width:1020px) {  #chat_embed {   width: 640px;   height: 300px;  } }  @media screen and (max-width:767px) {  #chat_embed {   width: 384px;   height: 300px;  } }  @media screen and (max-width:479px) {  #chat_embed {   width: 256px;   height: 300px;  } } </style>\n<center><iframe src="https://player.twitch.tv/?channel=aovivocn" class="playeriframe" scrolling="no" frameborder="0" allowfullscreen="true"></iframe><br><iframe frameborder="0" class="playeriframe" scrolling="no" id="chat_embed" src="https://www.twitch.tv/embed/aovivocn/chat"></iframe></center>\n'

#HTML = "\n<div style=\"text-align: center;\">\n    <div class=\"separator\" style=\"clear: both; text-align: center;\"><img alt=\"OK, K.O.! Vamos ser Her\u00f3is - Entrega Especial\" height=\"225\" src=\"https://lh3.googleusercontent.com/-IhvveTrrewU/XdBcbsLFlVI/AAAAAAAAC5A/ylp2JvYpnuoF2GybRnnCsbEHLmklMbd3QCLcBGAsYHQ/s1000/vlcsnap-2019-11-16-16h08m37s623.png\" width=\"400\" /></div>\n    <a name='more'></a>\n    <br />Idioma: Portugu\u00eas / Ingl\u00eas\n    <br />Legendas: Sem legendas\n    <br />Formato: MKV\n    <br />Qualidade: WEB-DL\n    <br />Release: CTOON\n    <br />Ripador: BombA\n    <br />Encoder / Uploader: BombA\n    <br />\n    <br /><b><span style=\"font-size: x-large;\">DOWNLOAD</span></b>\n    <br /><span style=\"font-size: large;\"><a href=\"https://mega.nz/#!SvAgWSDT!Gxcgnf5SEnyar9gX8U3vr4BXWMa0pbilN6k8tvDXA1c\" rel=\"nofollow\" target=\"_blank\">Op\u00e7\u00e3o 1 (MEGA)</a></span>\n    <br /><span style=\"font-size: large;\"><a href=\"https://drive.google.com/open?id=1VKk2I8roofK1AbziB8f8McD2U-Kefkum\" rel=\"nofollow\" target=\"_blank\">Op\u00e7\u00e3o 2 (Google Drive)</a></span>\n    <br />\n    <br /><span style=\"font-size: x-large;\"><b>ASSISTA ONLINE</b></span>\n    <br />\n    <!-- Download: <a href=\"https://drive.google.com/open?id=1lDVLAZUHw-ZzBWGA9K_Yekn-yLNjXUoG\" rel=\"nofollow\" target=\"_blank\">Google Drive</a> | <a class=\"assistir-online_2-02\" href=\"#!\">Assistir Online</a><br /><div style=\"display: none;\" id=\"player_2-02\"><br /><video poster=\"https://1.bp.blogspot.com/-k_pR7J1rqBQ/XP7pEUH2kZI/AAAAAAAARS8/XPqRubLIEzgJhwJOcfO4fBQ62IuSBmb_gCLcBGAs/s1280/vlcsnap-2019-06-10-20h29m46s617.png\" id=\"video-player_2-02\" class=\"video-js vjs-default-skin\" preload=\"none\" controls data-setup='{\"fluid\": true}'><source src=\"https://2.bp.blogspot.com/-oNBH17S34h0/XP7rfW0kI_I/AAAAAAAACc0/b_se95VPq4oRESu5ms06N3NyOGN12u4oQCKgBGAs/m22/\" type=\"video/mp4\" label=\"720p\" res=\"720\" /><source src=\"https://2.bp.blogspot.com/-oNBH17S34h0/XP7rfW0kI_I/AAAAAAAACc0/b_se95VPq4oRESu5ms06N3NyOGN12u4oQCKgBGAs/m18/\" type=\"video/mp4\" label=\"360p\" res=\"360\" /><script>videojs('video-player_2-02').videoJsResolutionSwitcher();  $(document).ready(function(){     $(\".assistir-online_2-02\").click(function(){         $(\"#player_2-02\").slideToggle(\"slow\");     }); }); </script></video></div>-->\n    <video poster=\"https://lh3.googleusercontent.com/-IhvveTrrewU/XdBcbsLFlVI/AAAAAAAAC5A/ylp2JvYpnuoF2GybRnnCsbEHLmklMbd3QCLcBGAsYHQ/s1000/vlcsnap-2019-11-16-16h08m37s623.png\" id=\"video-player\" class=\"video-js vjs-default-skin\" controls data-setup='{\"fluid\": true}'>\n        <source src=\"https://lh3.googleusercontent.com/-YQjtpcTlMPg/XdBd8V7D__I/AAAAAAAAC5M/sM46lZ8b3yEXcmetevwpYRdmpCosFXWZQCEwYBhgL/m37/\" type=\"video/mp4\" label=\"1080p\" res=\"1080\" />\n        <source src=\"https://lh3.googleusercontent.com/-YQjtpcTlMPg/XdBd8V7D__I/AAAAAAAAC5M/sM46lZ8b3yEXcmetevwpYRdmpCosFXWZQCEwYBhgL/m22/\" type=\"video/mp4\" label=\"720p\" res=\"720\" />\n        <source src=\"https://lh3.googleusercontent.com/-YQjtpcTlMPg/XdBd8V7D__I/AAAAAAAAC5M/sM46lZ8b3yEXcmetevwpYRdmpCosFXWZQCEwYBhgL/m18/\" type=\"video/mp4\" label=\"360p\" res=\"360\" />\n    </video>\n    <script>\n        videojs('video-player').videoJsResolutionSwitcher()\n    </script>\n</div>\n<!--updateupdateupdateupdateupdateupdateupdateupdateupdateupdateupdateupdateupdateupdateupdateupdateupdateupdateupdateupdateupdateupdateupdateupdateupdateupdate-->"

IMAGE = 'https://3.bp.blogspot.com/-D2pqG_yTfs8/W8UQSJ93iJI/AAAAAAAAFg4/rMn007hmvsApkNmbe7Hx9cEM-Y-cROsggCLcBGAs/s1000/cn-aovivo.png'

#HTML = '''
'''
<div style="text-align: center;">
    <div class="separator" style="clear: both; text-align: center;"><img alt="OK, K.O.! Vamos ser Heróis - Episódio na Praia" height="225" src="https://lh3.googleusercontent.com/-EqEGR8oRA-o/XdXYjmCmBMI/AAAAAAAADBs/gLCtwajSPjIvlEUwiH3eWm8KgQ9KcO9kQCLcBGAsYHQ/s1000/vlcsnap-2019-11-20-21h16m27s840.png" width="400" /></div>
    <a name='more'></a>
    <br />Idioma: Português / Inglês
    <br />Legendas: Sem legendas
    <br />Formato: MKV
    <br />Qualidade: WEB-DL
    <br />Release: CTOON
    <br />Ripador: BombA
    <br />Encoder / Uploader: BombA
    <br />
    <br /><b><span style="font-size: x-large;">DOWNLOAD</span></b>
    <br /><span style="font-size: large;"><a href="https://mega.nz/#!W2wXxIqR!MSNhW_zCpHvDvZpj-oQCXCnN6ojem5actFa64idgtH4" rel="nofollow" target="_blank">Opção 1 (MEGA)</a></span>
    <br /><span style="font-size: large;"><a href="https://drive.google.com/open?id=1MNMQ6yPr5scQs5EGi64F_-8WX6l2rzBS" rel="nofollow" target="_blank">Opção 2 (Google Drive)</a></span>
    <br />
    <br /><span style="font-size: x-large;"><b>ASSISTA ONLINE</b></span>
    <br />
    <video poster="https://lh3.googleusercontent.com/-EqEGR8oRA-o/XdXYjmCmBMI/AAAAAAAADBs/gLCtwajSPjIvlEUwiH3eWm8KgQ9KcO9kQCLcBGAsYHQ/s1000/vlcsnap-2019-11-20-21h16m27s840.png" id="video-player" class="video-js vjs-default-skin" controls data-setup='{"fluid": true}'>
        <source src="https://lh3.googleusercontent.com/-rCr89oMQoBg/XdXhQO6rpfI/AAAAAAAADCI/nUGnRErqKPs6wlxG9t7Nh0NWJjOmRgcxQCEwYBhgL/m37/" type="video/mp4" label="1080p" res="1080" />
        <source src="https://lh3.googleusercontent.com/-rCr89oMQoBg/XdXhQO6rpfI/AAAAAAAADCI/nUGnRErqKPs6wlxG9t7Nh0NWJjOmRgcxQCEwYBhgL/m22/" type="video/mp4" label="720p" res="720" />
        <source src="https://lh3.googleusercontent.com/-rCr89oMQoBg/XdXhQO6rpfI/AAAAAAAADCI/nUGnRErqKPs6wlxG9t7Nh0NWJjOmRgcxQCEwYBhgL/m18/" type="video/mp4" label="360p" res="360" />
    </video>
    <script>
        videojs('video-player').videoJsResolutionSwitcher()
    </script>
</div>
'''
POST_ENTRY = {
    'published': '7 de dezembro de 2019',
    'tags': ['CN ao vivo'],
    'title': 'Cartoon Network Brasil ao vivo',
    'display_url': DISPLAY_URL,
    'slug': hashlib.md5(DISPLAY_URL.encode('ascii')).hexdigest(),
    'html': HTML,
    'author': 'BombA',
    'high_thumbnail': IMAGE,
    'low_thumbnail': IMAGE,
    'description': 'Assista ao Cartoon Network ao vivo em HD.'
}
'''
POST_ENTRY = {
    'published': '07 de novembro de 2019',
    'tags': ['Trem Infinito'],
    'title': 'Trem Infinito - O Motor (S01E10) (WEB-DL) [1080p]',
    'display_url': DISPLAY_URL,
    'slug': hashlib.md5(DISPLAY_URL.encode('ascii')).hexdigest(),
    'html': HTML,
    'author': 'BombA',
    'high_thumbnail': 'https://lh3.googleusercontent.com/-TSnzKOE65Ek/XcCtQ-2qXvI/AAAAAAAAC0c/m-Fswv6xKSgV-EqEot1TJ6WVgSTLlpSugCLcBGAsYHQ/s1920/vlcsnap-2019-11-04-19h51m31s132.png',
    'low_thumbnail': 'https://lh3.googleusercontent.com/-TSnzKOE65Ek/XcCtQ-2qXvI/AAAAAAAAC0c/m-Fswv6xKSgV-EqEot1TJ6WVgSTLlpSugCLcBGAsYHQ/s300/vlcsnap-2019-11-04-19h51m31s132.png',
    'description': POST_DESCRIPTION.format('O Motor', 'Trem Infinito')
}
'''
# PARTE 2
'''
<div style="text-align: center;">
    <div class="separator" style="clear: both; text-align: center;"><img alt="Steven Universo: O Filme" height="225" src="https://3.bp.blogspot.com/-qIdQ20PM_ow/XZu4z_-sLEI/AAAAAAAACgY/_3OkyTeCfII83WrvnMRvKRG_6ITdbOTJgCLcBGAsYHQ/s1600/FILME.jpg" width="400" /></div>
    <a name='more'></a>
    <br />Idioma: Português / Inglês
    <br />Legendas: Sem legendas
    <br />Formato: MKV
    <br />Qualidade: WEB-DL (1080p)
    <br />Release: RCVR
    <br />Ripador: MattplusBC
    <br />Remasterizador: BombA
    <br />Encoder / Uploader: BombA
    <br />
    <br /><b><span style="font-size: x-large;">DOWNLOAD</span></b>
    <br /><span style="font-size: large;"><a href="https://drive.google.com/open?id=1qf5u9_MmSb4bY3XE1tgpYAFRSnbd21rJ" rel="nofollow" target="_blank">Opção 1 (Google Drive)</a></span>
    <br /><span style="font-size: large;"><a href="https://www.mediafire.com/file/166c2gq6lfvqinl/Steven.Universo.O.Filme.2019.1080p.WEB-DL.Dual.ToonCiTY.V2.mkv/file" rel="nofollow" target="_blank">Opção 2 (MediaFire)</a></span>
    <br /><span style="font-size: large;"><a href="https://mega.nz/#!D6ZGVaDY!WayHFbRN_rdfVx6DIfTTdbguZ9WH0gryqj4krpu5njw" rel="nofollow" target="_blank">Opção 3 (MEGA)</a></span>
    <br /><span style="font-size: large;"><a href="https://1drv.ms/u/s!AjLTRq1wPpIVggckD4cgvFRreYvJ?e=0C72ck" rel="nofollow" target="_blank">Opção 4 (OneDrive)</a></span>
    <br />
    <br /><span style="font-size: x-large;"><b>ASSISTA ONLINE</b></span>
    <br />
    <!-- Download: <a href="https://drive.google.com/open?id=11c_watNLuNr1UG1q8qYupEC1cUWTdfDu" rel="nofollow" target="_blank">Google Drive</a> | <a class="assistir-online_1-01" href="#!">Assistir Online</a><br /><div style="display: none;" id="player_1-01"><br /><video poster="https://3.bp.blogspot.com/-JGjwmX7kB8g/XU81wROLL1I/AAAAAAAATos/r_FeTu_mEusSkOXDs-ujvbPejlO38KIZgCLcBGAs/s1920/vlcsnap-2019-08-10-18h22m16s094.png" id="video-player_1-01" class="video-js vjs-default-skin" preload="none" controls data-setup='{"fluid": true}'><source src="https://3.bp.blogspot.com/-ueffocZmKE8/XU9EU8tc7bI/AAAAAAAACec/is2yAmhYImQAZH3ZHbx_gt28WI8BEQMowCKgBGAs/m37/" type="video/mp4" label="1080p" res="1080" /><source src="https://3.bp.blogspot.com/-ueffocZmKE8/XU9EU8tc7bI/AAAAAAAACec/is2yAmhYImQAZH3ZHbx_gt28WI8BEQMowCKgBGAs/m22/" type="video/mp4" label="720p" res="720" /><source src="https://3.bp.blogspot.com/-ueffocZmKE8/XU9EU8tc7bI/AAAAAAAACec/is2yAmhYImQAZH3ZHbx_gt28WI8BEQMowCKgBGAs/m18/" type="video/mp4" label="360p" res="360" /><script>videojs('video-player_1-01').videoJsResolutionSwitcher();  $(document).ready(function(){     $(".assistir-online_1-01").click(function(){         $("#player_1-01").slideToggle("slow");     }); }); </script></video></div>-->
    <video poster="https://3.bp.blogspot.com/-qIdQ20PM_ow/XZu4z_-sLEI/AAAAAAAACgY/_3OkyTeCfII83WrvnMRvKRG_6ITdbOTJgCLcBGAsYHQ/s1600/FILME.jpg" id="video-player" class="video-js vjs-default-skin" controls data-setup='{"fluid": true}'>
        <source src="https://2.bp.blogspot.com/-P1doRl7SfRg/XaOfXsRqDbI/AAAAAAAACqk/r3sWQj95ZwwZYdZZjMpXGJ9f_D0dUz3-QCEwYBhgL/m37/" type="video/mp4" label="1080p" res="1080" />
        <source src="https://2.bp.blogspot.com/-P1doRl7SfRg/XaOfXsRqDbI/AAAAAAAACqk/r3sWQj95ZwwZYdZZjMpXGJ9f_D0dUz3-QCEwYBhgL/m22/" type="video/mp4" label="720p" res="720" />
        <source src="https://2.bp.blogspot.com/-P1doRl7SfRg/XaOfXsRqDbI/AAAAAAAACqk/r3sWQj95ZwwZYdZZjMpXGJ9f_D0dUz3-QCEwYBhgL/m18/" type="video/mp4" label="360p" res="360" />
    </video>
    <script>
        videojs('video-player').videoJsResolutionSwitcher()
    </script>
</div>
'''
# FIM
'''
<div style="text-align: center;">
    <div class="separator" style="clear: both; text-align: center;"><img alt="Steven Universo: O Filme" height="225" src="https://3.bp.blogspot.com/-qIdQ20PM_ow/XZu4z_-sLEI/AAAAAAAACgY/_3OkyTeCfII83WrvnMRvKRG_6ITdbOTJgCLcBGAsYHQ/s1600/FILME.jpg" width="400" /></div>
    <a name='more'></a>
    <br />Idioma: Português / Inglês
    <br />Legendas: Sem legendas
    <br />Formato: MKV
    <br />Qualidade: WEB-DL (1080p)
    <br />Release: RCVR
    <br />Ripador: BombA
    <br />Remasterizador: BombA
    <br />Encoder / Uploader: BombA
    <br />
    <br /><b><span style="font-size: x-large;">DOWNLOAD</span></b>
    <br /><span style="font-size: large;"><a href="https://drive.google.com/open?id=1qf5u9_MmSb4bY3XE1tgpYAFRSnbd21rJ" rel="nofollow" target="_blank">Opção 1 (Google Drive)</a></span>
    <br /><span style="font-size: large;"><a href="https://www.mediafire.com/file/166c2gq6lfvqinl/Steven.Universo.O.Filme.2019.1080p.WEB-DL.Dual.ToonCiTY.V2.mkv/file" rel="nofollow" target="_blank">Opção 2 (MediaFire)</a></span>
    <br /><span style="font-size: large;"><a href="https://mega.nz/#!D6ZGVaDY!WayHFbRN_rdfVx6DIfTTdbguZ9WH0gryqj4krpu5njw" rel="nofollow" target="_blank">Opção 3 (MEGA)</a></span>
    <br /><span style="font-size: large;"><a href="https://1drv.ms/u/s!AjLTRq1wPpIVggckD4cgvFRreYvJ?e=0C72ck" rel="nofollow" target="_blank">Opção 4 (OneDrive)</a></span>
    <br />
    <br /><span style="font-size: x-large;"><b>ASSISTA ONLINE</b></span>
    <br />
    <!-- Download: <a href="https://drive.google.com/open?id=11c_watNLuNr1UG1q8qYupEC1cUWTdfDu" rel="nofollow" target="_blank">Google Drive</a> | <a class="assistir-online_1-01" href="#!">Assistir Online</a><br /><div style="display: none;" id="player_1-01"><br /><video poster="https://3.bp.blogspot.com/-JGjwmX7kB8g/XU81wROLL1I/AAAAAAAATos/r_FeTu_mEusSkOXDs-ujvbPejlO38KIZgCLcBGAs/s1920/vlcsnap-2019-08-10-18h22m16s094.png" id="video-player_1-01" class="video-js vjs-default-skin" preload="none" controls data-setup='{"fluid": true}'><source src="https://3.bp.blogspot.com/-ueffocZmKE8/XU9EU8tc7bI/AAAAAAAACec/is2yAmhYImQAZH3ZHbx_gt28WI8BEQMowCKgBGAs/m37/" type="video/mp4" label="1080p" res="1080" /><source src="https://3.bp.blogspot.com/-ueffocZmKE8/XU9EU8tc7bI/AAAAAAAACec/is2yAmhYImQAZH3ZHbx_gt28WI8BEQMowCKgBGAs/m22/" type="video/mp4" label="720p" res="720" /><source src="https://3.bp.blogspot.com/-ueffocZmKE8/XU9EU8tc7bI/AAAAAAAACec/is2yAmhYImQAZH3ZHbx_gt28WI8BEQMowCKgBGAs/m18/" type="video/mp4" label="360p" res="360" /><script>videojs('video-player_1-01').videoJsResolutionSwitcher();  $(document).ready(function(){     $(".assistir-online_1-01").click(function(){         $("#player_1-01").slideToggle("slow");     }); }); </script></video></div>-->
    <video poster="https://3.bp.blogspot.com/-qIdQ20PM_ow/XZu4z_-sLEI/AAAAAAAACgY/_3OkyTeCfII83WrvnMRvKRG_6ITdbOTJgCLcBGAsYHQ/s1600/FILME.jpg" id="video-player" class="video-js vjs-default-skin" controls data-setup='{"fluid": true}'>
        <source src="https://2.bp.blogspot.com/-P1doRl7SfRg/XaOfXsRqDbI/AAAAAAAACqk/r3sWQj95ZwwZYdZZjMpXGJ9f_D0dUz3-QCEwYBhgL/m37/" type="video/mp4" label="1080p" res="1080" />
        <source src="https://2.bp.blogspot.com/-P1doRl7SfRg/XaOfXsRqDbI/AAAAAAAACqk/r3sWQj95ZwwZYdZZjMpXGJ9f_D0dUz3-QCEwYBhgL/m22/" type="video/mp4" label="720p" res="720" />
        <source src="https://2.bp.blogspot.com/-P1doRl7SfRg/XaOfXsRqDbI/AAAAAAAACqk/r3sWQj95ZwwZYdZZjMpXGJ9f_D0dUz3-QCEwYBhgL/m18/" type="video/mp4" label="360p" res="360" />
    </video>
    <script>
        videojs('video-player').videoJsResolutionSwitcher()
    </script>
</div>
'''

EDIT = {
    'published': None,
    'tags': None,
    'title': None,
    'display_url': None,
    'slug': None,
    'html': HTML,
    'author': None,
    'high_thumbnail': None,
    'low_thumbnail': None,
    'description': None
}

'''
Tipos:

add_description
add_post
limit_entries
gen_entries
sitemap
'''
TYPE = 'add_post'

if TYPE == 'add_description':
    file = 'posts_all.json'
    file_base64 = 'posts_all_base64.json'
    
    with open(file, 'r') as f:
        posts = json.loads(f.read())
    
    for idx, val in enumerate(posts):
        if val['title'] != 'Cine Cartoon Apresenta: Especial Oswaldo (2019) (HDCAM) [720p]':
            if not 'Temporada' in val['title']:
                title = re.search('<img alt="(.*?)"', val['html']).group(1).split(' - ')
                
                if len(title) == 2:
                    print(POST_DESCRIPTION.format(title[1], title[0]))
                    posts[idx]['description'] = POST_DESCRIPTION.format(title[1], title[0])
            
            elif 'Temporada' in val['title']:
                title = val['title'].replace(' (Dublado)', '').split(' - ')
                print(SEASON_DESCRIPTION.format(title[1], title[0]))
                posts[idx]['description'] = SEASON_DESCRIPTION.format(title[1], title[0])
    
    with open(file, 'w') as f, open(file_base64, 'w') as e:
        f.write(json.dumps(posts))
        e.write(json.dumps({
            'data': base64.b64encode(json.dumps(posts).encode('ascii')).decode()
        }))

elif TYPE == 'limit_entries':
    cwd = os.getcwd() + '\\postagens'
    file = 'posts_all.json'
    
    with open(file, 'r') as f:
        posts = json.loads(f.read())
    
    numbers = limit_entries(posts)
    
    subprocess.Popen('git add *', cwd=cwd, shell=True).wait()
    subprocess.Popen(f'git commit -m "limit_entries - {file}"', cwd=cwd, shell=True).wait()
    subprocess.Popen('git push origin master', cwd=cwd, shell=True).wait()

elif TYPE == 'gen_entries':
    cwd = os.getcwd() + '\\postagens'
    file = 'posts_all.json'
    
    with open(file, 'r') as f:
        posts = json.loads(f.read())
    
    gen_entries('post', posts)
    
    subprocess.Popen('git add *', cwd=cwd, shell=True).wait()
    subprocess.Popen(f'git commit -m "gen_entries - {file}"', cwd=cwd, shell=True).wait()
    subprocess.Popen('git push origin master', cwd=cwd, shell=True).wait()

elif TYPE == 'add_post':
    pos = 0
    cwd = os.getcwd() + '\\postagens'
    file = 'posts_all.json'
    
    with open(file, 'r') as f:
        posts = json.loads(f.read())
    
    posts.insert(pos, POST_ENTRY)
    gen_entries('post', [POST_ENTRY])
    limit_entries(posts)
    
    with open(file, 'w') as f:
        f.write(json.dumps(posts))
    
    subprocess.Popen('git add *', cwd=cwd, shell=True).wait()
    subprocess.Popen(f'git commit -m "add_post - {file}"', cwd=cwd, shell=True).wait()
    subprocess.Popen('git push origin master', cwd=cwd, shell=True).wait()

elif TYPE == 'edit_post':
    pos = 0
    cwd = os.getcwd() + '\\postagens'
    file = 'posts_all.json'
    
    with open(file, 'r') as f:
        posts = json.loads(f.read())
    
    for i in EDIT.keys():
        if EDIT[i] is not None:
            posts[pos][i] = EDIT[i]
    
    gen_entries('post', [posts[pos]])
    limit_entries(posts)
    
    with open(file, 'w') as f:
        f.write(json.dumps(posts))
    
    subprocess.Popen('git add *', cwd=cwd, shell=True).wait()
    subprocess.Popen(f'git commit -m "edit_post - {file}"', cwd=cwd, shell=True).wait()
    subprocess.Popen('git push origin master', cwd=cwd, shell=True).wait()

# elif TYPE == 'sitemap':