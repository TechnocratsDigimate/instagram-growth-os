---
name: insta-hooks
description: >-
  Generate a bank of 10-20 Instagram hooks for one topic across different
  formulas, score every one with the Hinglish-aware hook scorer, and return
  them ranked with on-screen versions. Also scores hooks the user already has.
  Use when the user asks for "hooks", "hook ideas", "first line", "10 hooks
  for this", "score my hooks", "which hook is better", or "hook bank".
---

# insta-hooks

The fast lane. When the user wants hooks and not a full script.

The scorer lives in the reel skill. Run it from there:

```bash
python3 ../insta-reel/hookscore.py hooks.txt
python3 ../insta-reel/hookscore.py --hook "one line"
```

## Steps

1. **Load the account** (see `insta-account`). The audience decides the hook.
2. **Pin the problem.** One viewer, one symptom, one cost (see step 1 of
   `insta-reel`). A hook bank for "Instagram growth" is useless; a hook bank
   for "study-abroad page with 1 lakh followers and 2,000 views" is not.
3. **Write across formulas, not paraphrases.** Read
   `../insta-reel/hooks.json`. Use at least 8 different formulas for a bank of
   15. Vary the mechanism: confession, diagnosis, contrarian, peer contrast,
   statistic, identity callout, warning, curiosity gap, verbatim question.
4. **Write each hook twice:** the spoken line, and the on-screen line (six
   words max, blunter).
5. **Score all of them** in one run. Drop everything under 50. Never show a
   hook with a dealbreaker unless you are explaining why it failed.
6. **Return the ranked table:**

```
Account: <name>  ·  topic: <problem>
score  formula               spoken / on-screen
 87    #28 Asli Wajah        Aapka visa reject nahi hua, aapki SOP ne karwaya.
                             ASLI WAJAH: SOP
 83    #3 Nobody Tells You   ...
```

7. **Recommend three**, and say why each fits this account specifically,
   not why it scored high.

## Scoring someone's existing hooks

Run them as given. For each one under 70, name the weakest property and
write the fixed version under it, then re-score the fix so the user sees the
delta.

## Be honest about the score

The scorer was built to catch weak hooks (greetings, preambles, nothing
concrete, too long). It cannot predict which of two good hooks will travel.
Say that when the user picks between two hooks over 70. The retention graph
decides, not the script.
