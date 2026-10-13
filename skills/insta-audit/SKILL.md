---
name: insta-audit
description: >-
  Post-mortem on the account's own Instagram posts from an Insights CSV export:
  ranks every post by its multiple over the account median, compares sends,
  saves and follows per reach between winners and losers, compares formats,
  and runs a follower-health check that flags a dead or bot-heavy follower
  base. Use for "audit my account", "why are my views low", "big following but
  no reach", "what's working on my page", "analyse my insights", or when the
  user uploads an Instagram export.
---

# insta-audit

```bash
python3 audit.py export.csv --followers 185000 --out ~/.claude/instagram/<slug>/audit.md
```

## Step 0: load the account

See `insta-account`. The audit is saved per account and `insta-plan` reads it.

## Step 1: get the data

Ask the user to export it (no login on their behalf, no scraping):
**Professional Dashboard / Meta Business Suite → Insights → Content →
Export (CSV)**, last 60-90 days. Ask for the current follower count too.
Any CSV with Views or Reach plus Shares/Saves works; columns are matched
loosely. Fewer than 15 posts: run it, but say the read is directional.

## Step 2: run it and read it in this order

1. **Follower health** (if followers given). Median reach ÷ followers.
   - 20%+ healthy · 8-20% normal · 3-8% weak · under 3% critical.
   - Weak or critical means much of the base is inactive for this content:
     old giveaway followers, bought followers, or people who followed for
     content the account no longer makes. It is a heuristic, not a bot count.
2. **Top third vs bottom third.** Which of sends, saves, follows per 1k
   reach moved most? Sends usually separates them. That's the number to grow.
3. **Hook score gap.** If winners' first lines score much higher, the
   problem is hooks, and `insta-hooks` is the fix.
4. **Format.** Median multiple by format. Don't drop a format on n=1.
5. **Match against `log.md`** if it exists: which formulas and series made
   the top third.

## Step 3: the verdict (max 5 actions, ranked)

Each action: what to change, why the data says so, and how to measure it
next audit. Examples:

- "Winners average 18 sends per 1k reach vs 0.8. All three opened on a
  specific loss with a number. Next 2 weeks: every attention reel uses #27 or
  #28. Target: median sends/1k above 8."
- "Event-photo and congratulation posts sit at 0.5x and pull the account
  median down. Move them to Stories."

## Low reach on a big account (follower health CRITICAL)

The usual playbook, in order:

1. **Stop feeding the dead base.** No giveaways, contests, or follow-for-follow.
2. **Publish attention reels as Trial Reels** so they're tested on
   non-followers first, not the inactive base.
3. **Optimise for sends.** Shareable posts (pain scenes, myths, peer contrast)
   reach non-followers through DMs, which is how a page rebuilds an active
   audience.
4. **Check who the followers are.** Insights → Audience: top cities,
   countries, age bands. If they don't match the real audience (e.g. a
   local education page with a big follower share from unrelated countries),
   that's the contamination.
5. **Don't mass-remove followers.** Bulk removal can itself look like
   automation and risk the account. Let the active audience outgrow the dead
   one.
6. **Re-audit in 30 days** and compare median sends/1k and the health ratio.

## Output

Show the tool's table, then the verdict. Save with `--out` and offer to
turn the top action into next week's plan via `insta-plan`.
