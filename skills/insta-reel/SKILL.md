---
name: insta-reel
description: >-
  Turn one idea into a finished Instagram Reel: the real problem behind it,
  three scored hooks from 31 formulas (including 5 Hinglish ones), the spoken
  script, the on-screen text and a timed beat sheet, in the loaded account's
  voice and language. Use whenever the user wants a Reel, a short-form script,
  a voiceover, "reel bana do", "make a reel about X", "script for this idea",
  or is about to record and has no first line yet.
---

# insta-reel

One idea in. One Reel somebody finishes, out.

Two tools live in this folder and both actually run. Use them. Never eyeball
the hook and never guess the length.

```bash
python3 hookscore.py hooks.txt              # rank hook options (Hinglish-aware)
python3 hookscore.py --hook "one line"      # score one hook
python3 beats.py script.txt --target 30     # timed beat sheet before shooting
```

## Step 0: load the account

Follow `insta-account`. Language, audience, offer, series and "never say"
all come from the profile. If `~/.claude/instagram/<slug>/swipe.md` exists,
read it: that is this account's own evidence of what is working in its niche,
and it beats every default below.

## Step 1: find the real problem (do not skip)

Start every Reel with a real viewer problem, never with a trend, a tool, or a
wish to post. Build this chain before writing a word:

**specific viewer → visible symptom → hidden cause → what it costs them →
the one fix → the outcome**

Example (study abroad):
student with 7 IELTS → visa refused → SOP read like a template → ₹40,000
lost in fees plus a refusal on record → rewrite the SOP around one study gap
→ approval on reapply.

If a link is missing, infer a plausible one from the profile's audience and
say "assumption:" in one line. Ask at most one batched question, and only if
the answer would change the script. A thin idea gets a question, not padding:
what happened, to whom, and what did it cost or return.

**Reject the idea** if any account in the niche could post it unchanged
(logo-swap test), or if it reads like the first Google result for the topic.
Say so and offer a sharper angle.

## Step 2: pick the content job

| job | the viewer thinks | use |
| --- | --- | --- |
| Attention | "That's exactly what happens to me." | pain scene, contrarian take, humour |
| Connection | "They understand why." | diagnosis, myth correction, mistake breakdown |
| Trust | "They can actually fix this." | teardown, case pattern, process, proof |
| Action | "I should ask them." | diagnostic invite, lead magnet, comment keyword |

One job per Reel. It decides the CTA and the metric: sends for attention,
saves for trust, comments/DMs for action.

## Step 3: three hooks, scored

Read `hooks.json`: 31 formulas with template, example, on-screen version,
what each is for, and how it gets ruined. Formulas 27-31 are Hinglish-native
(Galti Confession, Asli Wajah, Same Budget Alag Result, Sach Bolun Toh,
Aap Bhi Yahi Kar Rahe Ho).

Pick **three different formulas** that genuinely fit. For each write the
spoken line and the on-screen line (six words max) separately. Put the three
spoken lines in a file and run `hookscore.py`. Show the ranking.

If the top hook is under 50, you do not have the hook yet. Go back to step 1.
The scorer catches weak hooks well and cannot pick between two good ones,
so between two hooks over 70 choose the one only this account can say.

## Step 4: the script

```
0:00-0:02  HOOK     the claim. Motion or text in frame 1, never a still face.
0:02-0:07  STAKE    why this costs the viewer. One line, one detail that
                    proves it's a real situation.
0:07-...   BODY     the diagnosis, then the one fix. One idea per beat,
                    frame changes every beat.
LAST 3s    PAYOFF   deliver what the hook promised, then the single ask.
LAST LINE  LOOP     echo a word from the hook so the replay lands clean.
```

20-45 seconds unless the user says otherwise. Write it the way they talk:
short spoken lines, natural Hindi-English switching for Hinglish accounts,
technical terms (pixel, CPL, SOP, GIC) explained in plain words the first
time.

## Step 5: time it

Save the script, one beat per line, and run
`beats.py script.txt --target <seconds>`. Hinglish is usually spoken faster:
use `--wpm 175` unless the profile gives a measured rate. Fix every flag (hook
over 3s, any beat over 4s, abstract runs, no loop) and re-run until clean.

## Step 6: humanize

Run the script through `insta-humanize` (`humanize.py` then `detect.py`).
Rewrite every flagged structure by hand. Hinglish buzzwords are flagged, not
auto-replaced, because swapping them breaks the grammar.

## Step 7: deliver

The script in a fenced block, on-screen text as a timed list, then:

```
REEL READY  ·  Account: <name>
hook:       #28 Asli Wajah, 87 STRONG
job:        connection  ·  measure: sends per reach
length:     31.2s across 9 beats at 175 wpm
on-screen:  6 cards
humanizer:  human score 82 PASS
next:       /insta-caption
```

On "yes", append date, formula and first line to
`~/.claude/instagram/<slug>/log.md` so `/insta-audit` can match results to
formulas later.

## On-screen text

- Six words or fewer per card. Hook card up at frame 1.
- Safe zone on 1080x1920: nothing above y=230 or below y=1440, keep the right
  230px clear (action rail).
- Burn in captions for the body. Most people watch muted first.

## Rules

- One idea per Reel. Two ideas means two Reels. Say so.
- Numbers over adjectives. "₹4 lakh" beats "bahut paisa".
- **Never fabricate.** Only numbers and stories from the profile's proof bank
  or from the user in this conversation. Otherwise leave `{{your number}}`
  and flag it.
- Respect the profile's compliance list. No guaranteed visas, results,
  returns or cures, ever, even in a hook.
- Never post. This skill writes. The user shoots and posts.
