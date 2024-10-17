# FortiMail Intruder Wordlist Generate
This script takes in a list of usernames and a list of passwords and generates a corresponding file of base64 encoded, XOR encrypted login strings to be used with a Burp Intruder sniper attack against a FortiMail web interface.

Username/email and password list files should be newline delimited, as shown below:
```
test1
test2
test3
...
```

**Make sure to check for duplicate usernames before locking a user out!**
