---
name: insta-viral
description: >-
  Find the reels actually working in the account's niche, rank them by how far
  each beat its own account's median (not raw views), name the hook formula,
  and turn the winners into hooks this account can shoot. Also breaks down a
  single viral reel or trend and reframes it for the account. Use for "what's
  working in my niche", "find viral reels", "swipe file", "reverse engineer
  this account", "why did this reel blow up", "trend ko apne niche mein
  convert karo", or when the user pastes a reel link or transcript.
---

# insta-viral

The research skill. Everything else writes; this one looks.

```bash
python3 swipe.py captured.tsv --out ~/.claude/instagram/<slug>/swipe.md
```

## The one idea

**Raw views are not evidence.** A 2M-follower account doing 4 lakh views had
a slow day. A 4,000-follower account doing 4 lakh views found something
copyable. Rank everything on the **outlier multiple**: views ÷ that account's
own recent median. Above 3x is a signal. Below 1.5x teaches nothing.

## Mode A: niche research (monthly)

**1. Pick 6-12 accounts** (propose them, get approval):
- 4 direct: same niche, slightly ahead (within ~10x of this account's size)
- 4 adjacent: different niche, same audience. Formats get borrowed from here
  before the niche has them.
- 2-4 outsized: for format only, never for tone or cadence.
Also ask the user to open their own **Saved** collection. It's the most
relevant corpus there is.

**2. Look, don't scrape.** Use whatever browser tool this session has, with
the user present in their own logged-in browser, or have them paste.
- Never log in to Instagram for the user and never ask for a password.
- Human speed, ~12 reels per account. No crawler, no scraping service, no
  background loop. Automated collection breaks Instagram's terms and gets
  accounts action-blocked.
- Copy the formula, never the video. Attribute every row.

Capture per reel (tab-separated, header row):
```
account	followers	median	views	hook
@someone	48000	11000	412000	nobody tells you your first 30 reels flop
```
`median` = the middle view count of their last ~12 reels. Without it you're
back to ranking by follower count.

**3. Run `swipe.py`.** It computes multiples, names the formula (all 31,
including the Hinglish ones), scores each hook, and compares top third vs
bottom third.

**4. Report three things only:** which formulas over-index in the top third
(with counts), what the top third share structurally, and the unclassified
hooks (read those by hand; they're new formulas or noise). State the sample
size. 40 reels across 6 accounts supports a claim; 12 reels doesn't.

**5. Write this account's version** of the top three formulas: their story,
their number, in the shape that works. Hand each to `insta-reel` with the
formula already chosen.

## Mode B: one reel or trend

When the user shares a viral reel, a competitor script, or a trending format:

1. Break it down: core idea, emotional trigger, hook formula, retention
   mechanism (open loop, pattern break, payoff timing), CTA, and why it
   worked for that account.
2. Find the problem in **this account's** audience the format can carry.
   The trend is the vehicle, never the starting point.
3. Deliver 5 rewritten hooks (scored) and one finished script via
   `insta-reel`, same energy, original wording. Never reuse the original's
   lines.

## Output

```
SWIPE  ·  Account: <name>  ·  38 reels  ·  7 accounts
OUTLIERS (3x+)
  38.4x  hook 86  #3  Nobody Tells You   @acct_a  412,000 (median 10,700)
OVER-INDEXING
  #28 Asli Wajah  x5 top third, 0 bottom
UNCLASSIFIED (6)  -> read by hand
YOUR VERSION
  #28 "Aapka ad budget waste nahi hua, aapke form ne karwaya."
```

Save to `~/.claude/instagram/<slug>/swipe.md`. `insta-reel` and `insta-plan`
read it. Nothing is posted, followed, liked or messaged by this skill.
