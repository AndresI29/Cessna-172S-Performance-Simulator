## Baseline validation (untuned)

```
Quantity                           Model       POH   Error %
Stall speed, clean (kt)             53.7      51.0      +5.3
Max speed, sea level (kt)          138.7     126.0     +10.1
Max climb rate, SL (ft/min)       1312.7     730.0     +79.8
Service ceiling (ft)             23024.6   14000.0     +64.5
Max range w/ reserve (nm)          901.2     638.0     +41.3
```

#---------

0.55 is below what a real prop achieves at cruise (about 0.75-0.80), so treat it as an effective value that also absorbs the optimistic power lapse and installation losses.

Climb matches while max speed is 5% low. That tension is the limit of a constant efficiency, because a real fixed-pitch prop gets more efficient as speed rises. A speed-dependent efficiency would be the physically correct fix, and it’s a good “future improvements” item.

Range is proportional to prop_eff divided by BSFC. Since BSFC was a guess, the −2.9% is partly luck from errors cancelling. Say so rather than presenting it as a clean win

Validate again ---
Quantity                           Model       POH   Error %
Stall speed, clean (kt)             53.7      51.0      +5.3
Max speed, sea level (kt)          119.3     126.0      -5.3
Max climb rate, SL (ft/min)        730.3     730.0      +0.0
Service ceiling (ft)             15311.0   14000.0      +9.4
Max range w/ reserve (nm)          619.6     638.0      -2.9