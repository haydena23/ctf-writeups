# geoguessr

ictf{xx.xxx,-yyy.yyy} [osint.png](./osint.png).

Author: eth007

50 Points

---
## Solution

This is a super simple OSINT problem! The first thing I did was plop the image into Google image search, and it pointed me to the Four Corners Monument in the United States. Looking at the flag format, I assumed it would be some GPS coordinates. Another quick Google search of the GPS coordinates of the Four Corners Monument lends us our position. Put that in flag format, and theres the answer!

---
## Flag
```
ictf{36.999,-109.045}
```