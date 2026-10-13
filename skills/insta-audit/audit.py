#!/usr/bin/env python3
"""
audit.py - post-mortem on your own Instagram posts from an Insights export.

The point of this script is the same correction swipe.py makes for other
people's reels, applied to your own: raw views are not evidence. Every post is
ranked on its multiple over YOUR account's median, and judged on what the
algorithm actually rewards in 2026: sends (shares) per reach, saves per reach,
and follows per reach. Likes are printed and otherwise ignored.

It also runs one check most audits skip: FOLLOWER HEALTH. If your median reach
is a tiny fraction of your follower count, a large part of the follower base is
not seeing you or not engaging when it does. Instagram tests new posts on a
slice of your followers first, so a big inactive base drags every test. This
is a heuristic, not a bot detector. It tells you where to look.

Input: the CSV you export from Meta Business Suite / Professional Dashboard
(Insights > Content > Export), or any CSV/TSV with a header row. Column names
are matched loosely. Recognised columns (any one alias is enough):

    date      publish time, date, posted
    type      post type, type, format, media type
    text      description, caption, hook, title
    views     views, plays, video views
    reach     reach, accounts reached
    likes     likes
    comments  comments
    shares    shares, sends
    saves     saves
    follows   follows
    link      permalink, link, url

Usage
  python3 audit.py export.csv
  python3 audit.py export.csv --followers 185000
  python3 audit.py export.csv --followers 185000 --out audit.md
  python3 audit.py export.csv --json

Part of Instagram Growth OS. Built on Jake Schincariol's instagram-agent-skill
(MIT). No network, no dependencies, nothing uploaded.
"""

import argparse
import csv
import io
import json
import os
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

ALIASES = {
    "date": ["publish time", "date", "posted", "published", "timestamp"],
    "type": ["post type", "type", "format", "media type", "media_type"],
    "text": ["description", "caption", "hook", "title", "first line"],
    "views": ["views", "plays", "video views", "reel plays"],
    "reach": ["reach", "accounts reached"],
    "likes": ["likes"],
    "comments": ["comments"],
    "shares": ["shares", "sends"],
    "saves": ["saves"],
    "follows": ["follows", "follows from post"],
    "link": ["permalink", "link", "url"],
}
NUMERIC = ["views", "reach", "likes", "comments", "shares", "saves", "follows"]

try:  # optional: score the first line of each caption as a hook
    sys.path.insert(0, os.path.join(HERE, "..", "insta-reel"))
    import hookscore  # noqa: E402
except Exception:
    hookscore = None


def load(path):
    raw = sys.stdin.read() if path == "-" else open(path, encoding="utf-8-sig").read()
    sample = raw[:4096]
    delim = "\t" if sample.count("\t") > sample.count(",") else ","
    rows = list(csv.reader(io.StringIO(raw), delimiter=delim))
    if not rows:
        sys.exit("empty file")
    header = [h.strip().lower() for h in rows[0]]
    col = {}
    for key, names in ALIASES.items():
        for i, h in enumerate(header):
            if h in names:
                col[key] = i
                break
    if "views" not in col and "reach" not in col:
        sys.exit("need a 'Views' or 'Reach' column. Found: " + ", ".join(rows[0]))
    posts = []
    for r in rows[1:]:
        if not any(c.strip() for c in r):
            continue
        p = {}
        for key, i in col.items():
            v = r[i].strip() if i < len(r) else ""
            if key in NUMERIC:
                try:
                    p[key] = float(v.replace(",", "")) if v else None
                except ValueError:
                    p[key] = None
            else:
                p[key] = v
        posts.append(p)
    return posts, col


def per_k(n, d):
    if n is None or not d:
        return None
    return n / d * 1000


def fmt(x, nd=1):
    return "-" if x is None else (f"{x:,.0f}" if abs(x) >= 100 else f"{x:.{nd}f}")


def mean(xs):
    xs = [x for x in xs if x is not None]
    return statistics.mean(xs) if xs else None


def analyse(posts, followers=None):
    metric = "views" if any(p.get("views") for p in posts) else "reach"
    vals = [p[metric] for p in posts if p.get(metric)]
    if not vals:
        sys.exit(f"no numbers in the {metric} column")
    base = statistics.median(vals)
    for p in posts:
        v = p.get(metric)
        p["multiple"] = (v / base) if v and base else None
        reach = p.get("reach") or p.get("views")
        p["sends_k"] = per_k(p.get("shares"), reach)
        p["saves_k"] = per_k(p.get("saves"), reach)
        p["follows_k"] = per_k(p.get("follows"), reach)
        text = (p.get("text") or "").strip()
        p["first_line"] = text.splitlines()[0][:120] if text else ""
        p["hook_score"] = None
        if hookscore and p["first_line"]:
            try:
                p["hook_score"] = round(hookscore.run(p["first_line"])[1], 1)
            except Exception:
                pass
    ranked = sorted([p for p in posts if p["multiple"] is not None],
                    key=lambda p: -p["multiple"])
    third = max(1, len(ranked) // 3)
    top, bottom = ranked[:third], ranked[-third:]

    def band(group):
        return {
            "multiple": mean([p["multiple"] for p in group]),
            "sends_k": mean([p["sends_k"] for p in group]),
            "saves_k": mean([p["saves_k"] for p in group]),
            "follows_k": mean([p["follows_k"] for p in group]),
            "hook": mean([p["hook_score"] for p in group]),
        }

    by_type = {}
    for p in ranked:
        t = (p.get("type") or "unknown").strip() or "unknown"
        by_type.setdefault(t, []).append(p["multiple"])
    formats = {t: {"n": len(v), "median_multiple": statistics.median(v)}
               for t, v in by_type.items()}

    health = None
    reach_vals = [p["reach"] for p in posts if p.get("reach")]
    if followers and reach_vals:
        ratio = statistics.median(reach_vals) / followers
        if ratio >= 0.20:
            verdict, note = "HEALTHY", "Your followers are seeing you. Growth now comes from non-follower reach: sends and shares."
        elif ratio >= 0.08:
            verdict, note = "NORMAL", "Typical for an established account. Push sends per reach to break out of the follower bubble."
        elif ratio >= 0.03:
            verdict, note = "WEAK", ("A large share of followers is not seeing or not engaging. "
                                     "Likely causes: old giveaway/contest followers, bought followers, "
                                     "or an audience that followed for content you no longer make.")
        else:
            verdict, note = "CRITICAL", ("Median reach is under 3% of followers. The follower base is mostly "
                                         "inactive for this content. Check follower quality in Insights "
                                         "(top locations, age, 'Active times') against your real audience, and "
                                         "rebuild on non-follower reach rather than posting more to the same base.")
        health = {"followers": followers, "median_reach": statistics.median(reach_vals),
                  "ratio": ratio, "verdict": verdict, "note": note}

    return {"metric": metric, "baseline": base, "count": len(posts), "ranked": ranked,
            "top": band(top), "bottom": band(bottom), "formats": formats, "health": health}


def render(a, out=sys.stdout):
    w = lambda s="": print(s, file=out)
    w(f"INSTAGRAM AUDIT  ·  {a['count']} posts  ·  baseline: median {a['metric']} {fmt(a['baseline'])}")
    w("=" * 78)
    w(f"{'mult':>6} {a['metric']:>9} {'send/1k':>8} {'save/1k':>8} {'fol/1k':>7} {'hook':>5}  first line")
    for p in a["ranked"]:
        line = p["first_line"] or p.get("link", "")
        line = line if len(line) <= 34 else line[:31] + "..."
        w(f"{p['multiple']:5.1f}x {fmt(p.get(a['metric'])):>9} {fmt(p['sends_k']):>8} "
          f"{fmt(p['saves_k']):>8} {fmt(p['follows_k']):>7} {fmt(p['hook_score'], 0):>5}  {line}")
    w("-" * 78)
    t, b = a["top"], a["bottom"]
    w("TOP THIRD vs BOTTOM THIRD")
    for k, label in [("multiple", "multiple"), ("sends_k", "sends per 1k reach"),
                     ("saves_k", "saves per 1k reach"), ("follows_k", "follows per 1k reach"),
                     ("hook", "hook score (first caption line)")]:
        w(f"  {label:<32} {fmt(t[k]):>8}  vs  {fmt(b[k]):>8}")
    w("")
    if len(a["formats"]) > 1:
        w("BY FORMAT (median multiple)")
        for f, v in sorted(a["formats"].items(), key=lambda kv: -kv[1]["median_multiple"]):
            w(f"  {f:<24} {v['median_multiple']:4.2f}x   n={v['n']}")
        w("")
    h = a["health"]
    if h:
        w("FOLLOWER HEALTH")
        w(f"  median reach {fmt(h['median_reach'])} / {fmt(h['followers'])} followers = "
          f"{h['ratio']*100:.1f}%   {h['verdict']}")
        w(f"  {h['note']}")
        w("")
    w("Read the top third for what to repeat and the bottom third for what to stop.")
    w("Sends per reach is the number to grow. Views follow it.")


def main():
    ap = argparse.ArgumentParser(description="Audit your own Instagram posts from an Insights export.")
    ap.add_argument("input", help="CSV/TSV export, or - for stdin")
    ap.add_argument("--followers", type=float, help="current follower count, for the follower-health check")
    ap.add_argument("--out", help="also write the report to this file")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    posts, _ = load(args.input)
    a = analyse(posts, args.followers)
    if args.json:
        slim = dict(a)
        slim["ranked"] = [{k: v for k, v in p.items()} for p in a["ranked"]]
        print(json.dumps(slim, indent=2, ensure_ascii=False, default=str))
        return
    render(a)
    if args.out:
        path = os.path.expanduser(args.out)
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            render(a, out=f)
        print(f"\nwritten: {path}")


if __name__ == "__main__":
    main()
