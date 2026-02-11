---
title: "Convert time in seconds to HH:MM:SS"
date: 2012-01-18
categories: 
  - "python"
slug: "convert-time-seconds-hhmmss"
---

```
## Convert time in seconds to hours:minutes:seconds
# @param sec Time in seconds
# @return The time in hh:mm:ss format
def SecToTime(Sec): 
  H = int(Sec / 3600)
  M = int(Sec / 60 - H * 60)
  S = int(Sec - (H * 3600 + M * 60))

  if len(str(H)) == 1: time = "0" + str(H) + ":"
  else: time = str(H) + ":"
 
  if len(str(M)) == 1: time = time + "0" + str(M) + ":"
  else: time = time + str(M) + ":"

  if len(str(S)) == 1: time = time + "0" + str(S) 
  else: time = time + str(S) 
  
  return time
  pass

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20python/general/convert%20time%20seconds%20hhmmss](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20python/general/convert%20time%20seconds%20hhmmss)
