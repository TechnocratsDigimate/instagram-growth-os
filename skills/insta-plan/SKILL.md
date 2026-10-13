---
name: insta-plan
description: >-
  Plan the week (or month) for one Instagram account: what to post each day,
  which format and series, which content job each post does, the one
  experiment to run, and the accounts to engage with. Built from the account's
  own audit and swipe file when they exist. Use for "content plan", "week ka
  plan", "content calendar", "what should I post this week", or "30 day plan".
---

# insta-plan

## Step 0: load the account and its evidence

Load the profile (`insta-account`). Then read, if they exist:
- `~/.claude/instagram/<slug>/audit.md`: what worked on this account
- `~/.claude/instagram/<slug>/swipe.md`: what works in the niche
- `~/.claude/instagram/<slug>/log.md`: what was already posted (avoid repeats)

With no evidence, say the plan runs on defaults and recommend
`/insta-audit` first.

## The mix (default week: 5 posts)

| slot | job | format | measure |
| --- | --- | --- | --- |
| 2 | Attention | Reel, pain scene / contrarian | sends per reach |
| 1 | Connection | Reel, diagnosis or myth correction | sends + saves |
| 1 | Trust | Carousel or teardown Reel | saves per reach |
| 1 | Action | Reel with lead-magnet keyword | comments, DMs, leads |

Shift the mix by account health (from the audit):
- **Follower health WEAK/CRITICAL**: add more attention posts and publish
  them as **Trial Reels** (shown to non-followers first), so the inactive
  follower base stops dragging each test. No giveaways, no "follow for
  follow". They're what usually caused the problem.
- **Healthy reach, few leads**: move one attention slot to action.
- **Leads but low quality**: make action posts more diagnostic so they
  filter, not just attract.

## Rules

- **Series over one-offs.** Every post belongs to one of the profile's 2-4
  series where it fits. Recognisable formats compound.
- **Every post starts from a real viewer problem.** Write the
  symptom → hidden cause chain for each slot, not just a topic.
- **One experiment per week**, one variable only: hook type, length,
  talking-head vs B-roll, Hinglish vs English, posting time. Write down the
  hypothesis and the metric now so next week's audit can call it.
- **Stories daily, lightly**: one poll or question sticker tied to the
  week's topic. It feeds DMs and tells Instagram who your engaged followers are.
- **Engagement list**: 10 accounts to comment on this week (5 peers, 5 where
  the audience is). Real comments only, written by the user.

## Output

```
WEEK PLAN  ·  Account: <name>  ·  <dates>
Mon  Attention  Reel  [Series]  problem: ...  hook (scored): ...  CTA: share
Tue  Trust      Carousel ...
...
EXPERIMENT   Hinglish vs English hook on the two attention reels. Metric: sends/1k reach.
STORIES      Mon poll: "..." ...
ENGAGE       @... x10
```

Offer to write any slot as a finished Reel (`insta-reel`) or caption
(`insta-caption`). On approval, append the plan to `log.md`.
For a month, plan week 1 in full and weeks 2-4 as topics only. Week 2 should
be rewritten after week 1's audit.
