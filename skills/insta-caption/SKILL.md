---
name: insta-caption
description: >-
  Write an Instagram caption and lint it: shows exactly what the feed displays
  before "...more", enforces the 5-hashtag cap, checks search keywords, catches
  two-ask captions, and understands Hinglish CTAs ("comment karo", "save kar
  lo"). Use when the user asks for a caption, "caption likh do", hashtags,
  "fix my caption", or has a Reel/carousel ready to post.
---

# insta-caption

The tool runs. Use it on every caption before showing it.

```bash
python3 caption.py caption.txt
python3 caption.py caption.txt --keywords "uk study visa,ielts score"
```

## Step 0: load the account

See `insta-account`. Language, CTA keyword and compliance rules come from
the profile.

## Decide the caption's one job

- **Extend the hook** (attention / connection posts): first line adds the
  detail the video didn't have time for.
- **Make it searchable** (trust posts): the words someone would type into
  Instagram search, in the first two lines, said naturally.
- **Convert** (action posts): the keyword CTA, stated once, early enough to
  be seen.

## The shape

```
Line 1    The hook, rewritten for reading. Must make sense alone.
          This is all most people ever see (~125 characters).
Body      The one idea, short lines, white space. Real numbers.
Ask       ONE action: comment a keyword, save, share, or DM.
Tags      Up to 5 hashtags, specific to the topic. Optional.
```

## Rules

- **The first 125 characters are the caption.** Run the tool and read the box
  it prints. If the visible window ends mid-thought or has no concrete detail,
  rewrite line 1.
- **Five hashtags maximum.** Instagram's cap since 18 December 2025. No
  #viral, #explore, #reelsinstagram. Topic tags only.
- **Search terms beat hashtags.** Put 1-2 phrases the audience actually
  searches ("canada study visa", "meta ads lead quality") in plain sentences.
  Pass them with `--keywords` so the linter checks they're present.
- **One ask.** Two asks is zero asks. The tool counts English and Hinglish
  asks.
- **Comment-keyword CTAs need a delivery.** If the caption says "comment
  AUDIT", make sure `insta-dm` has the auto-reply set up first.
- No guarantees, no fake urgency, nothing the profile's compliance list bans.

## The loop

1. Write the caption.
2. Run `caption.py` (with `--keywords` if the post should rank in search).
3. Run `insta-humanize` on it.
4. Fix every WARN. Re-run until clean.
5. Deliver the caption in a fenced block, ready to paste, plus the tool's
   feed-preview box so the user sees what the scroll sees.
