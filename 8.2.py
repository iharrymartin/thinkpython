import sys
Prefixes = 'JKLMNOPQ'
Suffix = 'ack'
for char in Prefixes[0:4]:
 print char + Suffix
for char in Prefixes[5]:
 print char + 'o' + Suffix
for char in Prefixes[6]:
 print char + Suffix
for char in Prefixes[7]:
 print char + 'o' + Suffix
