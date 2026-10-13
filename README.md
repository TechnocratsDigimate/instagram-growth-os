# Instagram Growth OS

**10 Claude skills that run your Instagram like a performance marketer would.**
Scored hooks, Hinglish scripts, captions that survive the "...more" cut, a
humanizer that strips the AI feel, and an audit that tells you why your views
are low even with a big following.

Free. MIT. No API key, no Instagram login, nothing to connect.
**Nothing gets posted until you say yes.** These skills write. You post.

Built by **[Gautam Punj](https://gautampunj.com)**, founder of Technocrats
Digimate and head of digital marketing for one of India's largest study-abroad
brands. Made for Indian creators, founders and brands who post in **Hinglish**,
because every other Instagram AI tool is built for American English.

---

## Install (30 seconds)

**Easiest: paste this into Claude**

```
https://github.com/TechnocratsDigimate/instagram-growth-os

Install these skills, then set up my account with /insta-account.
```

**Claude Code**

```bash
git clone https://github.com/TechnocratsDigimate/instagram-growth-os.git
cp -r instagram-growth-os/skills/insta-* ~/.claude/skills/
```

**As a plugin**

```
/plugin marketplace add TechnocratsDigimate/instagram-growth-os
/plugin install instagram-growth-os
```

**claude.ai (web / app):** zip any `skills/insta-*` folder and upload it in
Settings → Capabilities → Skills. Start with `insta-account` and `insta-reel`.

Then spend 10 minutes on your account profile: run `/insta-account` and send
Claude 3 of your own reels. Every skill reads it. Running more than one page
(personal + business + client)? Add a profile for each and switch with
"for <account>".

---

## The 10 skills

| command | what it does |
| --- | --- |
| `/insta-account` | Set up and switch between your accounts. Each one keeps its own audience, voice, language, offer and rules. |
| `/insta-reel` | One idea into a finished Reel: the real problem, 3 scored hooks, script, on-screen text, timed beat sheet. |
| `/insta-hooks` | A bank of 10-20 hooks across 31 formulas, scored and ranked. Or score the hooks you already have. |
| `/insta-caption` | Caption written and linted: shows the 125 characters the feed actually shows, enforces the 5-hashtag cap. |
| `/insta-humanize` | Strips em dashes, AI words, invisible characters and Hinglish creator slop, then scores what's left. |
| `/insta-viral` | Finds what's working in your niche, ranked by outlier multiple, not raw views. Reframes any trend for your niche. |
| `/insta-plan` | The week: what to post, which format, which job each post does, one experiment, who to engage with. |
| `/insta-audit` | Reads your Insights export. Ranks your posts, finds what separates winners, and checks follower health. |
| `/insta-dm` | The comment-keyword → DM → WhatsApp lead flow behind a Reel, in English or Hinglish. |
| `/insta-profile` | Scores your profile out of 100 and rewrites what lost points. |

---

## Why the Hinglish part matters

Most hook scorers only understand English. Feed them a Hinglish hook and
they mark your best line as weak. This one knows *lakh*, *crore*, *₹*,
*galti*, *jala diya*, *aap / main*, and catches *"Hello dosto, aaj hum baat
karenge"* as the dealbreaker it is.

```
HOOK RANKING
->  87.0 STRONG  Aapka visa reject nahi hua, aapki SOP ne karwaya.
    83.0 STRONG  Nobody tells you ki Meta Ads ka pehla 7 din learning phase hota hai.
    79.4 STRONG  Maine ek client ka 4 lakh ka ad budget sirf ek galti se jala diya.
    66.2 OK      ₹50,000 ka ad budget, zero leads. Galti form mein thi.
    35.4 WEAK    Kya aap bhi Instagram pe grow karna chahte ho?
     0.0 WEAK    Hello dosto, aaj hum baat karenge digital marketing ke baare mein
        dealbreaker: Hinglish video preamble. Delete it and open on the payoff.
        dealbreaker: Greeting. Nobody came to the feed to be greeted.
```

Five Hinglish-native hook formulas are included: **Galti Confession**,
**Asli Wajah**, **Same Budget Alag Result**, **Sach Bolun Toh** and **Aap Bhi
Yahi Kar Rahe Ho**.

---

## The tools that actually run

Plain Python, no dependencies, no network. They run on your machine, on your text.

```bash
python3 skills/insta-reel/hookscore.py hooks.txt          # rank hooks
python3 skills/insta-reel/beats.py script.txt --target 30 # time the script
python3 skills/insta-caption/caption.py caption.txt       # lint the caption
python3 skills/insta-humanize/humanize.py draft.txt --report
python3 skills/insta-humanize/detect.py draft.txt         # human score
python3 skills/insta-viral/swipe.py captured.tsv          # rank competitor reels
python3 skills/insta-audit/audit.py export.csv --followers 185000
```

### "Big following, no views?" Run the audit

Export your last 90 days from Insights (Professional Dashboard → Insights →
Content → Export) and run:

```
FOLLOWER HEALTH
  median reach 4,850 / 185,000 followers = 2.6%   CRITICAL

TOP THIRD vs BOTTOM THIRD
  sends per 1k reach      18.0  vs   0.8
  hook score              76.6  vs  16.8
```

If your median reach is under 3% of your followers, posting more to the same
base won't fix it. `/insta-audit` gives you the rebuild playbook.

---

## The honest fine print

- **These skills never post, follow, like or DM.** Automating those with
  browser bots breaks Instagram's terms and gets accounts restricted.
  Comment-keyword DMs work through Instagram's own tools or Meta-approved
  partners (ManyChat, WATI, etc.), which `/insta-dm` writes the copy for.
- **The hook scorer catches bad hooks. It doesn't pick winners.** It reliably
  flags greetings, preambles, vague lines and hooks too long to say in 3
  seconds. Between two good hooks, your retention graph decides.
- **The humanizer is local heuristics**, not a detector API. Nobody can
  honestly promise "undetectable".
- **Nothing is fabricated.** If a script needs a number you haven't given,
  it comes back as `{{your number}}`.
- **Platform rules change.** The hashtag cap moved from 30 to 5 in December
  2025. If something here contradicts what Instagram does today, Instagram
  is right.

---

## Want this done for your brand?

This is the system I use for my own pages and for client accounts.
If you'd rather have it run for you, with paid ads, lead funnels and
WhatsApp automation on top, find me at **[gautampunj.com](https://gautampunj.com)**.

---

## Credit

Built on **[instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill)**
by Jake Schincariol (MIT). The hook scorer, beat timer, caption linter,
humanizer and swipe ranker started as his work. This version adds Hinglish
and Indian-market support, five Hinglish hook formulas, multi-account
profiles, the Insights audit with follower-health check, and the
problem-first content method.

## License

MIT. Take it, change it, ship it. Keep the copyright notices.
