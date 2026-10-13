---
name: insta-account
description: >-
  Set up, switch and list the Instagram accounts this pack writes for. Each
  account gets its own profile (audience, voice, language, offer, series, CTA
  rules), so one install can run a founder page, an agency page and a brand
  page without mixing them up. Use when the user says "set up my account",
  "add another account", "switch to <account>", "for <account>", "which
  account", or runs any insta-* skill and no account is loaded yet.
---

# insta-account

Every other `insta-*` skill starts here. A script in the wrong voice, language
or offer is unusable, so the account is loaded before anything is written.

## Where accounts live

```
~/.claude/instagram/
  active                 one line: the slug of the current account
  accounts/<slug>.md     the profile (copy of accounts/_template.md)
  <slug>/swipe.md        written by /insta-viral
  <slug>/log.md          written by /insta-reel and /insta-plan
  <slug>/audit.md        written by /insta-audit
```

Profiles are private. They hold positioning, offers and internal context, and
they never belong in a public repo. The repo ships only `_template.md` and
generic examples.

If this session has no persistent home folder (claude.ai chat, mobile), ask
the user to paste the profile once per conversation, or keep it as a file in
their Claude Project. Say so in one line, then carry on.

## Load an account (every insta-* skill does this first)

1. If the user names an account in the message ("for TD", "agency page ke liye",
   "on my personal page"), match it against the slugs and the `aliases:` line
   in each profile. Load that one and write its slug to `active`.
2. Otherwise read `active` and load that profile.
3. If there is no profile at all, run **Set up** below before writing anything.
4. If two accounts could match, ask which one. One short question.

State the loaded account in the first line of the output, e.g.
`Account: TD (@technocratsdigimate) · Hinglish · goal: audit enquiries`.
The user should never have to wonder which voice they are reading.

## Set up an account

Take the fastest path the user allows:

- **From their reels (best).** Ask for links or transcripts of 3 of their own
  reels that performed, plus their bio. Infer voice, language mix, sentence
  length, recurring phrases and what they never say. Fill the template.
- **From answers.** Ask the template's questions in one batch, not one by one.
- **From an existing doc.** A brand manual or positioning doc they paste.

Then show the filled profile and ask for corrections before saving. Mark
anything you inferred rather than were told with `(inferred)` so the user can
check it.

## The fields that change the output most

| field | why it matters |
| --- | --- |
| audience | Who is in the room. "Founders of ₹2-20 Cr service businesses" writes a different hook than "Class 12 students in Punjab". |
| language | Hinglish / English / Hindi / Punjabi, and the mix ratio. Decides every line. |
| job of the account | Leads, trust, personal brand, community. Decides the CTA and which metric counts. |
| offer + lead magnet | What a qualified viewer can ask for. One CTA keyword per offer. |
| series | 2-4 repeatable formats the audience can recognise. |
| never say | Banned claims, words, competitors, compliance lines. |
| proof bank | Real numbers and stories the user has approved for use. Nothing outside this list gets stated as fact. |
| compliance | Regulated claims (visa success, medical, returns, guarantees). Hard rules, not style. |

## Switching mid-conversation

"Now do the same for X" means: load X, then **rewrite**, don't translate.
Different audience means a different problem, a different hook and a
different ask. Re-run the scoring for the new version.

## List

`/insta-account list` prints each slug, handle, language and goal, and marks
the active one.
