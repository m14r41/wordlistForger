# wordlistForger
Hello, Security Reseacher!
> This tool `wordlistForger` is designed to help and speed up situations where you need realistic test data for security testing and automation.
> It will help you to create things like API keys, UUIDs, tokens, order IDs, invoice numbers, transaction IDs, coupon codes, etc.
> This would be super useful for testing brute-force logic, IDOR cases, and any situation where you need structured and predictable identifiers.

# Install:
```python
pip install wordlistforger
```

 ##### Alternate with Git
```python
git clone https://github.com/m14r41/wordlistForger.git && cd wordlistForger && python wordlistForger.py -p ORD-2024-H2B7  --lock  ORD-  -l 20 --strict-case --live
```
 
## Tools Switches And Argument Options: 
| Option / Flag     | Description                                                         |
| ----------------- | ------------------------------------------------------------------- |
| `-p`, `--pattern` | **(Required)** Pattern used to generate strings. Give you word likewise have to generat (eg. `aA99xx`, `ORD-192` `api_keyxxxx`  |
| `-l`, `--limit`   | **(Required)** Number of unique outputs to generate                 |
| `--lock`          | Locks a fixed substring inside the pattern                          |
| `--lock-mask`     | Mask to control fixed positions (`x` = random, other chars = fixed) |
| `--strict-case`   | Enforces case sensitivity (lower stays lower, upper stays upper)    |
| `--match-pattern` | Uses specific placeholders: n (numbers), x (hex), a (lower), A (upper)                |
| `-s`, `--seed`    | Set seed for reproducible results                                   |
| `-o`, `--output`  | Output file name (default: `wordlist.txt`)                          |
| `--live`          | Print generate worlist live               |

## Pattern Behavior
### With vs Without --match-pattern

| Pattern | Without `--match-pattern` | With `--match-pattern`                   | Details                        |
| ------- | ------------------------- | ---------------------------------------- | ---------------------------------- |
| `xxxx`  | Random letters (a–Z)      | Hex chars (`0-9`, `a-f`)                 | `x` becomes hex only in match mode |
| `nnnn`  | Random letters (a–Z)      | Digits (`0-9`)                           | `n` works only in match mode       |
| `aaaa`  | Letters (mixed case)      | Lowercase only (`a-z`)                   | Match mode enforces lowercase      |
| `AAAA`  | Letters (mixed case)      | Uppercase only (`A-Z`)                   | Match mode enforces uppercase      |
| `aA9x`  | Mixed letters/digits      | Structured (lower + upper + digit + hex) | Precise control with match mode    |
| `1234`  | Digits only               | Digits only                              | Numbers behave same in both modes  |
| `ABCD`  | Random case letters       | Strict uppercase letters                 | Match mode respects pattern case   |


## In summary :

| Pattern | Without    | With `--match-pattern` |
| ------- | ---------- | ---------------------- |
| `xxxx`  | letters    | hex                    |
| `nnnn`  | letters    | digits                 |
| `aaaa`  | mixed case | lowercase              |
| `AAAA`  | mixed case | uppercase              |



## Example of usage 
| Use Case                      | Command                                                                             | What It Demonstrates                          |
| ----------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------- |
| Basic generation              | `-p aaaa -l 10`                                                                     | Simple lowercase generation                   |
| Mixed case (default)          | `-p aaaa -l 10`                                                                     | Generates both lower + upper (no strict mode) |
| Strict case enforcement       | `-p aaaa -l 10 --strict-case`                                                       | Forces only lowercase                         |
| Hex UUID-style                | `-p xxxxxxxx-xxxx -l 5 --match-pattern`                                             | Uses `x` as hex characters                    |
| Numeric only IDs              | `-p nnnnnn -l 20 --match-pattern`                                                   | Uses `n` for digits                           |
| Fixed prefix (lock)           | `-p xxxx-xxxx -l 10 --lock 2026`                                                    | Forces `2026` inside pattern                  |
| Position control (lock-mask)  | `-p AAAAAA -l 10 --lock-mask xxABxx`                                                | Forces specific positions (`A`, `B`)          |
| Lock + mask combined          | `-p xxxx-xxxx -l 10 --lock 99 --lock-mask xx99xxxx`                                 | Combines both locking methods                 |
| Reproducible results          | `-p aaaa -l 10 -s 1234`                                                             | Same output every run                         |
| Custom output file            | `-p aaaa -l 10 -o mylist.txt`                                                       | Saves to custom file                          |
| Live output mode              | `-p aaaa -l 10 --live`                                                              | Prints results instead of progress bar        |
| API key generator             | `-p xxxxxxxxxxxxxxxxxxxxxxxx -l 5 --match-pattern -o keys.txt`                      | Real-world API key format                     |
| MAC address                   | `-p xx:xx:xx:xx:xx:xx -l 10 --match-pattern`                                        | Structured hardware IDs                       |
| Invoice IDs (strict format)   | `-p INV-AAAA-nnnn -l 20 --match-pattern --strict-case`                              | Mixed structured format                       |
| Session tokens (reproducible) | `-p xxxx-xxxx -l 10 --match-pattern -s 42`                                          | Debug-friendly generation                     |
| High-volume generation        | `-p nnnnnnnn -l 100000`                                                             | Performance test                              |
| Live + output file            | `-p xxxx -l 10 --match-pattern --live -o live.txt`                                  | Console + file output                         |
| Complex enterprise ID         | `-p AAAA-xxxx-nnnn -l 50 --match-pattern --strict-case --seed 99 -o enterprise.txt` | Combines multiple switches                    |


# Basics use case example ( i.e withut --match-pattern)

## Generate API keys wordlist

```python
python wordlistForger.py -p api_key7m9xq2kpl4 -l 10   --strict-case
python wordlistForger.py -p api_key7m9xq2kpl4 -l 10   --lock api_key --live
```
<img width="1022" height="966" alt="1" src="https://github.com/user-attachments/assets/784fe21d-b746-4e88-9e80-cb53ccd308c4" />


## Generate Invoice ID

<img width="1348" height="936" alt="2" src="https://github.com/user-attachments/assets/afc675ec-662a-4f31-b2d6-4daa7195df2e" />

## Generate ORDER ID
```python
python wordlistForger.py -p ODER-ID-1943AC -l 10 --lock ODER-ID --live
python wordlistForger.py -p ODER-ID-1943AC -l 10 --lock ODER-ID --strict-case --live
```
<img width="1151" height="964" alt="3" src="https://github.com/user-attachments/assets/1a4630d2-d6ac-40b2-8dad-01dfceb38019" />



# Advance Use case: --match-pattern
> Generate advance and more controlled wordlist with real types of data for pentesting in real word with switch :  `--match-pattern` 

## 1. Simple wordlist

```bash id="u1"
python .\wordlistForger.py -p aaaa -l 5
```

```id="u1o"
aBcD
xYzA
mNoP
qRsT
uVwX
```

---

## 2. Lowercase words

```bash id="u2"
python .\wordlistForger.py -p aaaa -l 5 --match-pattern
```

```id="u2o"
abcd
wxyz
lmno
pqrs
tuvw
```

---

## 3. Numbers only

```bash id="u3"
wordlistForger -p nnnnnn -l 5 --match-pattern
```

```id="u3o"
482193
905321
118273
667200
902134
```

---

## 4. Hex strings

```bash id="u4"
wordlistForger  -p xxxxxxxx -l 5 --match-pattern
```

```id="u4o"
a3f9c1e2
9b2c4d6f
0f1e2d3c
abcdef12
1234abcd
```

---

## 5. UUID format

```bash id="u5"
wordlistForger  -p xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx -l 5 --match-pattern
```

```id="u5o"
a3f9c1e2-9b2c-4d6f-0f1e-2d3cabcdef12
1234abcd-5678-9abc-def0-1234567890ab
deadbeef-cafe-babe-face-001122334455
abcdef12-3456-7890-abcd-ef1234567890
0f1e2d3c-4b5a-6978-8899-aabbccddeeff
```

---

## 6. Order IDs

```bash id="u6"
wordlistForger -p ORD-nnnnnn -l 5 --match-pattern
```

```id="u6o"
ORD-482193
ORD-905321
ORD-118273
ORD-667200
ORD-902134
```

---

## 7. Invoice IDs

```bash id="u7"
wordlistForger  -p INV-AAAA-nnnn -l 5 --match-pattern
```

```id="u7o"
INV-ABCD-1234
INV-WXYZ-5678
INV-QWER-9087
INV-ASDF-1122
INV-ZXCV-3344
```

---

## 8. API keys (short)

```bash id="u8"
wordlistForger  -p xxxxxxxxxxxxxxxxxxxxxxxx -l 5 --match-pattern
```

```id="u8o"
a3f9c1e29b2c4d6f0f1e2d3c
abcdef1234567890deadbeef
1234abcd5678efab9abc0001
0f1e2d3c4b5a69788899aabb
ffeeddccbbaa998877665544
```

---

## 9. MAC addresses

```bash id="u9"
wordlistForger  -p xx:xx:xx:xx:xx:xx -l 5 --match-pattern
```

```id="u9o"
a3:1f:9c:e2:4d:6f
9b:2c:4d:6f:0f:1e
de:ad:be:ef:ca:fe
ab:cd:ef:12:34:56
0f:1e:2d:3c:4b:5a
```

---

## 10. Coupon codes

```bash id="u10"
wordlistForger -p SAVE-AAAA-nn -l 5 --match-pattern
```

```id="u10o"
SAVE-ABCD-12
SAVE-WXYZ-34
SAVE-QWER-56
SAVE-ASDF-78
SAVE-ZXCV-90
```

---

## 11. User IDs

```bash id="u11"
wordlistForger -p user_nnnnn -l 5 --match-pattern
```

```id="u11o"
user_48219
user_90532
user_11827
user_66720
user_90213
```

---

## 12. Transaction IDs

```bash id="u12"
wordlistForger -p TXN-xxxxxxxx -l 5 --match-pattern
```

```id="u12o"
TXN-a3f9c1e2
TXN-9b2c4d6f
TXN-deadbeef
TXN-abcdef12
TXN-1234abcd
```

---

## 13. License keys

```bash id="u13"
wordlistForger  -p AAAAA-AAAAA-AAAAA -l 5
```

```id="u13o"
AbCdE-FgHiJ-KlMnO
XyZaB-CdEfG-HiJkL
MnOpQ-RsTuV-WxYzA
QrStU-VwXyZ-AbCdE
FgHiJ-KlMnO-PqRsT
```

---

## 14. Employee IDs

```bash id="u14"
wordlistForger -p EMP-nnnn -l 5 --match-pattern
```

```id="u14o"
EMP-1023
EMP-4587
EMP-7765
EMP-9901
EMP-3342
```

---

## 15. Bank reference numbers

```bash id="u15"
wordlistForger -p REF-nnnnnnnn -l 5 --match-pattern
```

```id="u15o"
REF-48219384
REF-90532177
REF-11827366
REF-66720055
REF-90213411
```

---

## 16. Tracking numbers

```bash id="u16"
wordlistForger -p TRK-AAAA-nnnn -l 5 --match-pattern
```

```id="u16o"
TRK-ABCD-1234
TRK-WXYZ-5678
TRK-QWER-9087
TRK-ASDF-1122
TRK-ZXCV-3344
```

---

## 17. Serial numbers

```bash id="u17"
wordlistForger -p SN-xxxx-xxxx -l 5 --match-pattern
```

```id="u17o"
SN-a3f9-c1e2
SN-9b2c-4d6f
SN-dead-beef
SN-abcd-1234
SN-0f1e-2d3c
```

---

## 18. Database IDs

```bash id="u18"
wordlistForger -p ID-nnnnn -l 5 --match-pattern
```

```id="u18o"
ID-48219
ID-90532
ID-11827
ID-66720
ID-90213
```

---

## 19. Session tokens

```bash id="u19"
wordlistForger -p xxxxxxxxxxxxxxxx -l 5 --match-pattern
```

```id="u19o"
a3f9c1e29b2c4d6f
9b2c4d6f0f1e2d3c
abcdef1234567890
0f1e2d3c4b5a6978
ffeeddccbbaa9988
```

---

## 20. Temporary passwords

```bash id="u20"
wordlistForger -p Aaannn -l 5 --match-pattern
```

```id="u20o"
Abc123
Xyz456
Qwe789
Asd234
Zxc567
```

---

## 21. WiFi passwords

```bash id="u21"
wordlistForger -p WIFI-xxxx-nnnn -l 5 --match-pattern
```

```id="u21o"
WIFI-a3f9-1234
WIFI-9b2c-5678
WIFI-dead-9087
WIFI-abcd-1122
WIFI-0f1e-3344
```

---

## 22. API tokens (long)

```bash id="u22"
wordlistForger -p xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx -l 5 --match-pattern
```

```id="u22o"
a3f9c1e29b2c4d6f0f1e2d3cabcdef12
9b2c4d6f0f1e2d3c1234abcd5678ef90
abcdef1234567890deadbeefcafebabe
0f1e2d3c4b5a69788899aabbccddeeff
ffeeddccbbaa99887766554433221100
```

---

## 23. Discount codes

```bash id="u23"
wordlistForger -p SALE-AAAA-nn -l 5 --match-pattern
```

```id="u23o"
SALE-ABCD-12
SALE-WXYZ-34
SALE-QWER-56
SALE-ASDF-78
SALE-ZXCV-90
```

---

## 24. Gaming usernames

```bash id="u24"
wordlistForger -p gamerAAA -l 5
```

```id="u24o"
gamerAbC
gamerXyZ
gamerQwE
gamerTyU
gamerUiO
```

---

## 25. Log filenames

```bash id="u25"
wordlistForger -p log-2026-nnnn -l 5 --match-pattern
```

```id="u25o"
log-2026-1001
log-2026-2456
log-2026-7788
log-2026-9001
log-2026-3344
```

---

## 26. OTP codes

```bash id="u26"
wordlistForger -p nnnnnn -l 5 --match-pattern
```

```id="u26o"
482193
905321
118273
667200
902134
```

---

## 27. Device IDs

```bash id="u27"
wordlistForger -p DEV-xxxxxx -l 5 --match-pattern
```

```id="u27o"
DEV-a3f9c1
DEV-9b2c4d
DEV-deadbe
DEV-abcd12
DEV-0f1e2d
```

---

## 28. License plates

```bash id="u28"
wordlistForger -p AA-nnnn-AA -l 5 --match-pattern
```

```id="u28o"
AB-1234-CD
XY-5678-ZW
QR-9087-AS
DF-1122-GH
ZX-3344-CV
```

---

## 29. Fixed prefix (lock)

```bash id="u29"
wordlistForger -p xxxx-xxxx -l 5 --lock ACME
```

```id="u29o"
ACME-abcd
ACME-xYzA
ACME-qwer
ACME-lmno
ACME-uvwx
```

---

## 30. Mask control

```bash id="u30"
wordlistForger -p AAAAAA -l 5 --lock-mask xxHRxx
```

```id="u30o"
abHRcd
efHRgh
ijHRkl
mnHRop
qrHRst
```

---

## 31. Reproducible dataset

```bash id="u31"
wordlistForger -p nnnn -l 5 --match-pattern -s 42
```

```id="u31o"
1043
9275
6612
8801
3390
```

---

## 32. Live output

```bash id="u32"
wordlistForger -p xxxx -l 5 --match-pattern --live
```

```id="u32o"
a3f9
9b2c
4d6f
0f1e
2d3c
```

---

## 33. Customer IDs

```bash id="u33"
wordlistForger -p CUST-nnnnn -l 5 --match-pattern
```

```id="u33o"
CUST-48219
CUST-90532
CUST-11827
CUST-66720
CUST-90213
```

---

## 34. Subscription IDs

```bash id="u34"
wordlistForger -p SUB-xxxx-nnnn -l 5 --match-pattern
```

```id="u34o"
SUB-a3f9-1234
SUB-9b2c-5678
SUB-dead-9087
SUB-abcd-1122
SUB-0f1e-3344
```

---

## 35. OAuth tokens

```bash id="u35"
wordlistForger -p oauth_xxxxxxxxxx -l 5 --match-pattern
```

```id="u35o"
oauth_a3f9c1e2
oauth_9b2c4d6f
oauth_deadbeef
oauth_abcdef12
oauth_1234abcd
```

---

## 36. Cloud resource IDs

```bash id="u36"
wordlistForger -p aws-xxxx-xxxx -l 5 --match-pattern
```

```id="u36o"
aws-a3f9-c1e2
aws-9b2c-4d6f
aws-dead-beef
aws-abcd-1234
aws-0f1e-2d3c
```

---

## 37. IoT device keys

```bash id="u37"
wordlistForger -p iot-xxxxxxxx -l 5 --match-pattern
```

```id="u37o"
iot-a3f9c1e2
iot-9b2c4d6f
iot-deadbeef
iot-abcdef12
iot-1234abcd
```

---

## 38. Backup identifiers

```bash id="u38"
wordlistForger -p BAK-2026-nnnn -l 5 --match-pattern
```

```id="u38o"
BAK-2026-1001
BAK-2026-2456
BAK-2026-7788
BAK-2026-9001
BAK-2026-3344
```

---

## 39. Audit log references

```bash id="u39"
wordlistForger -p AUD-xxxx-nnnn -l 5 --match-pattern
```

```id="u39o"
AUD-a3f9-1234
AUD-9b2c-5678
AUD-dead-9087
AUD-abcd-1122
AUD-0f1e-3344
```

---

## 40. System session logs

```bash id="u40"
wordlistForger -p SYS-nnnnnnnn -l 5 --match-pattern
```

```id="u40o"
SYS-48219384
SYS-90532177
SYS-11827366
SYS-66720055
SYS-90213411
```


