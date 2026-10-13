---
name: insta-profile
description: >-
  Score an Instagram profile out of 100 on a 12-part rubric (name field, bio,
  pinned posts, link, highlights, grid, photo, handle, category, activity,
  stories) and rewrite whatever lost points, fix-first. Use for "audit my
  profile", "bio likh do", "optimise my Instagram profile", "rate my page",
  or before running ads or a lead magnet to the profile.
---

# insta-profile

The profile is the landing page every Reel sends people to. A viewer who
taps through decides in about three seconds.

## Step 0: load the account

See `insta-account`. The rewrite has to match the account's audience, offer
and language.

## Step 1: see the profile

Ask for a screenshot of the profile page (top of the grid visible), or have
the user open it in their own browser. Never log in for them. Also get: the
link destination, highlight names, and the date of the last post.

## Step 2: score it honestly

Score each item in `rubric.json` (12 items, 100 points). Most first-pass
profiles land in the 30s and 40s. A generous score helps nobody. Give each
item: points, what's there now, why it lost points.

The three that matter most: **name field** (it's indexed by Instagram
search; put the searchable keyword there, e.g. "Gautam Punj | Meta Ads"),
**bio first line** (who it's for and what changes for them), and **pinned
three** (proof, offer explainer, introduction, each doing a different job).

## Step 3: rewrite, fix-first

In order of points lost, give the copy-ready replacement:
- name field (30 characters max)
- bio (150 characters max, count them), one CTA that matches the link
- the three posts to pin, and why
- highlight names (4-6, named for buyer questions: Results, Process, Fees,
  About)
- link: one destination that matches the bio's promise

For Hinglish accounts the bio can be Hinglish, but the **name field stays
in the words people type in search**, usually English.

## Output

```
PROFILE SCORE  ·  Account: <name>  ·  41/100
name_field       4/12   "TD Official" -> "Technocrats | Meta Ads Agency"
bio_first_line   3/12   ...
...
REWRITE (paste-ready)
```

No fabricated proof in the bio. Follower counts, client counts and results
come from the profile's proof bank or the user.
