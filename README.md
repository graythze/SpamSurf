# Email Bomber

This tool allows continuous email spam without requiring registration/personal mail/enabling less secure app and other options

## How does it work?
Spam tool uses [EmoSurf.com](https://emosurf.com/) which doesn't require account activation after registration and solving captcha after multiple attempts to recover password. It makes possible to spam about 15-20 emails per second for unlimited time

## Privacy
While using this tool, emosurf.com will sending emails contain your IP address. Victim will have emails starting at `DD-MM-YY в HH:MM с IP-адреса [xxx.xxx.xxx.xxx] отослан запрос`

![img.png](img/img.png)

**USE VPN/PROXY  IF YOU'D LIKE TO HIDE YOUR REAL IP ADDRESS**

## Spamming prevention
To avoid spamming, add **info@emosurf.com** and **trash@emosurf.com** to blacklist

## Usage
Check arguments section below to see detailed information, or just run

    python bomb.py -t <amount of threads> <victim email>

## Arguments
* ***victim*** — Enter victim email
* ***-t*** ***[--threads]*** — OPTIONAL: Enter amount of threads (4 is set by default)
* ***-s*** ***[--silence]*** — OPTIONAL: Run threads silently
* ***-w*** ***[--webdriver]*** — OPTIONAL: Choose chrome or firefox webdriver (Chrome is set by default)
* ***-n*** ***[--name]*** — OPTIONAL: Set a name for account
