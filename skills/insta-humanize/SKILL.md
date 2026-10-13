---
name: insta-humanize
description: >-
  Strip the AI fingerprint out of a script or caption before it ships: invisible
  characters, em dashes, stock "AI" words, Instagram filler and Hinglish creator
  slop ("Hello dosto", "aaj hum baat karenge", "next level", "game changer"),
  then score what is left on five checks. Use on every draft other insta-*
  skills write, and when the user says "humanize this", "make it sound human",
  "sounds like AI", or "remove the AI feel".
---

# insta-humanize

Two scripts. Both run locally. Nothing is uploaded.

```bash
python3 humanize.py draft.txt --report     # clean it and show every change
python3 detect.py draft.txt                # score it, five checks
python3 detect.py before.txt after.txt     # prove the improvement
```

## What gets fixed automatically

- **Invisible characters**: zero-width spaces, joiners, soft hyphens, BOMs,
  tag characters. They survive copy-paste and nobody types them.
- **Typography**: em dash to comma, curly quotes to straight, ellipsis to
  three dots.
- **Stock words and phrases** from `slop.json`, including safe Hinglish
  deletions ("video ko end tak dekhna", "like share subscribe",
  "chaliye shuru karte hain").

## What gets flagged, not fixed

Rewriting these needs judgement, and Hinglish grammar breaks under
find-and-replace:

- "It's not just X, it's Y", rule-of-three lists, emoji bullets, shouted caps
- Hinglish greeting and preamble openers ("Hello dosto", "Aaj hum baat
  karenge", "Is video mein")
- "Kya aap bhi...?" question openers
- Creator buzzwords ("next level", "game changer", "No. 1 in India")
- Guarantee and hype claims ("100% guaranteed", "secret hack")
- Reflex follow bait

Rewrite every flagged line yourself, in the account's voice, then re-run
`detect.py` and show the before/after score.

## Order of operations

1. `humanize.py --report` on the draft.
2. Rewrite each flagged structure by hand.
3. `detect.py before after` to show the delta.
4. Ship only on PASS (70+). If it can't pass, the draft is the problem, not
   the words. Go back to the idea.

## Say this honestly

The five checks are local heuristics modelled on what AI detectors key on.
They are not GPTZero or Originality, they call no service, and nobody can
honestly promise "undetectable". The real goal is simpler: a line that sounds
like a person when it's said out loud.

`slop.json` is meant to be edited. Add the phrases your niche overuses.
