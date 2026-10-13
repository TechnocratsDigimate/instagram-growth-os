---
name: insta-dm
description: >-
  Build the comment-keyword → DM lead flow behind a Reel: the keyword, the
  auto-reply that delivers the lead magnet, the qualifying question, the
  hand-off to WhatsApp or a call, and two follow-ups, in English or Hinglish.
  Also writes replies to comments and first DMs to warm leads. Use for "DM
  automation", "comment keyword", "lead magnet delivery", "ManyChat flow",
  "comment karo aur DM mein milega", "reply to my comments", or "follow up".
---

# insta-dm

Turns attention into a lead without the user typing 200 DMs.

## Step 0: load the account

See `insta-account`: offer, lead magnet, keyword, where leads go, compliance.

## The legal line (read first)

- **Allowed:** Instagram's own automated responses, and Meta-approved
  messaging partners (ManyChat, WATI, Interakt and similar) that reply
  **after the person comments or messages first**.
- **Not allowed:** browser bots, auto-DM-ing people who didn't message,
  auto-follow / auto-like tools, scraped lists. They break Instagram's terms
  and get accounts restricted.
- This skill writes the flow and the copy. The user configures it in their
  tool. Nothing is sent from here.

## The flow (one per lead magnet)

```
REEL CTA      "Comment AUDIT, I'll DM you the checklist."
              One keyword. Short, uppercase, impossible to misspell.
PUBLIC REPLY  Auto-reply to the comment (vary 3-5 versions so it doesn't
              look like a bot): "Bhej diya, DM check karo"
DM 1          Deliver immediately. Link first, one line of context.
              End with ONE qualifying question with tap buttons.
DM 2          Based on the answer: qualified → book a call / WhatsApp
              hand-off. Not yet → one useful resource, no pitch.
FOLLOW-UP 1   24h later, only if they engaged: one question about the
              resource ("Kaunsa point aapke case mein sabse relevant laga?")
FOLLOW-UP 2   3 days later: case-specific offer, one CTA. Then stop.
```

Two follow-ups. Not five.

## Qualifying questions that filter

Pick one that splits serious from curious, from the profile's audience:
- Agency: "Monthly ad spend? <₹50k / ₹50k-2L / ₹2L+"
- Study abroad: "Kab tak jaana hai? This intake / Next year / Just exploring"
- Clinic: "Treatment kab tak chahiye? This month / 3 months / Researching"

Route the top answer to a human fast. Speed-to-lead beats copy.

## Writing rules

- Lead magnet first, pitch never in DM 1.
- One question per message, with buttons where the tool supports them.
- Match the account's language. Hinglish accounts get Hinglish DMs.
- No guarantees, no fake scarcity, nothing the compliance list bans.
- Personalisation tokens (`{first_name}`) only where the tool fills them.

## Comment replies (manual, on the account's own posts)

Sort comments: keyword → let automation handle · lead signal ("price?",
"kaise contact karein") → reply + invite to DM · substantive question → a
real answer that adds a detail · praise → short, human, ask a follow-up ·
noise/spam → ignore or hide. Write the replies; the user posts them.

## Output

The full flow as a table (trigger, message, buttons, wait, branch), every
message copy-ready, plus a setup checklist for the user's tool and a test
step: comment the keyword from a second account before the Reel goes live.
