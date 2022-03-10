# scriptlibrary
 Library of General Scripts created for Work or Personal 

#### encode.py & decode.py 
---
Use case is to convert ascii to hex and then feed that hex string to these scripts for encoding. To leave notes at my job without it all being in plain text

***encode.py***
Feed it a hex string and it generates a random number from 1 - 15 and offsets each digit based on that seed. The seed is appended to the string of encoded digits for decoding

***decode.py***
Pulls the last 2 digit from the encoded string and offsets it back to the original value. Prints out the decoded hex string. 