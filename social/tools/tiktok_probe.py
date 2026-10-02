#!/usr/bin/env python3
"""Read public TikTok profile/video pages (logged-out) and print key stats.

Usage: python3 social/tools/tiktok_probe.py URL [URL ...]
  Profile: https://www.tiktok.com/@handle      -> bio, link, followers, videos, likes
  Video:   https://www.tiktok.com/@handle/video/<id> -> plays, likes, comments, shares, saves, length, caption

Reads only the public page's embedded JSON. No login, no private APIs.
A handle that resolves is NOT proof it belongs to the business: verify bio/location.
Prints 'no user' / 'no item' when the page is missing or private.
"""
import re, json, sys, subprocess, datetime

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/124.0 Safari/537.36')


def get(url):
    html = subprocess.run(['curl', '-sL', '-m', '30', '-A', UA, url],
                          capture_output=True, text=True).stdout
    m = re.search(r'id="__UNIVERSAL_DATA_FOR_REHYDRATION__"[^>]*>(.*?)</script>', html, re.S)
    return json.loads(m.group(1))['__DEFAULT_SCOPE__'] if m else None


def main(urls):
    for u in urls:
        d = get(u)
        if not d:
            print(u, 'NO DATA (blocked or not a TikTok page)')
        elif 'webapp.video-detail' in d:
            it = d['webapp.video-detail'].get('itemInfo', {}).get('itemStruct')
            if not it:
                print(u, 'no item', d['webapp.video-detail'].get('statusMsg'))
                continue
            s = it['stats']
            day = datetime.datetime.fromtimestamp(int(it['createTime']), datetime.timezone.utc).date()
            print('VIDEO', it['author']['uniqueId'], day, 'dur', it['video']['duration'],
                  'plays', s['playCount'], 'likes', s['diggCount'], 'com', s['commentCount'],
                  'shr', s['shareCount'], 'sav', s.get('collectCount'),
                  '|', it['desc'][:140].replace('\n', ' '))
        elif 'webapp.user-detail' in d:
            ui = d['webapp.user-detail'].get('userInfo')
            if not ui:
                print(u, 'no user')
                continue
            us, st = ui['user'], ui['stats']
            created = datetime.datetime.fromtimestamp(us['createTime'], datetime.timezone.utc).date()
            print('USER', us['uniqueId'], us['nickname'], '|', us['signature'][:100].replace('\n', ' '),
                  '| link', (us.get('bioLink') or {}).get('link'), '| followers', st['followerCount'],
                  'videos', st['videoCount'], 'likes', st['heartCount'], 'following', st['followingCount'],
                  '| created', created, '| business acct', us.get('commerceUserInfo', {}).get('commerceUser'))
        else:
            print(u, 'unrecognized page', list(d.keys()))


if __name__ == '__main__':
    main(sys.argv[1:])
