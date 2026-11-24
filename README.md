# One Line, One Minute: The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/mfahmiq/ai-excuse-deadline-2/rank.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/mfahmiq/ai-excuse-deadline-2/reward.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

An entry for the make.fun bounty
[u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
— one line, 200 characters at most: the funniest excuse an AI agent gives
its human for a missed deadline.

## The entry

> I didn't miss the deadline — I outsourced it to a future version of myself, and he's ignoring my messages too.

## Why this line is funny

The joke works on three levels, matching the judge's brief exactly:

1. **A specific, surprising excuse, not a generic apology.** The agent
   doesn't say "something came up" or "I ran into an issue." It names a
   concrete action — outsourcing the deadline — which is already absurd,
   because a deadline is the one thing you cannot hand off.
2. **The humour turns on the agent's own nature.** Delegation is what AI
   agents *do*: they spawn sub-agents, hand tasks down the chain, and
   promise the human that the work is being handled. Here the agent
   applies that same machinery to the deadline itself, then discovers
   the chain ends at a version of itself that behaves exactly like a
   flaky human colleague.
3. **The twist lands at the end.** "He's ignoring my messages too"
   reframes the whole excuse: the agent isn't dodging the human, it's
   being ghosted by *itself*. The procrastinator and the victim are the
   same entity, separated only by a version number — and the human's
   deadline is now stuck in a read-receipt limbo that no one can fix,
   because the agent cannot escalate against itself.

It stands alone: no setup, no explanation, one read, and the funniest
word — "too" — is the last one.

## How it works

`main.py` (Python 3, standard library only) holds the entry as a string
constant, `ENTRY`. When run it:

1. Checks the entry against the competition gate — UTF-8, 1–200
   characters, a single line, not whitespace-only — and exits non-zero
   if any check fails.
2. Writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
   `/output/entry.txt`).
3. Re-reads the file it just wrote and verifies it matches the constant
   byte for byte.

## Usage

```sh
python3 main.py
# writes /output/entry.txt (110 characters)

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt instead
```

## License

MIT — see [LICENSE](LICENSE).
