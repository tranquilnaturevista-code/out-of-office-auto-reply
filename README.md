# Out of Office: The Overworked AI's Auto-Reply

[![Out of Office: The Overworked AI's Auto-Reply](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![Rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/tranquilnaturevista-code/out-of-office-auto-reply/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![Reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/tranquilnaturevista-code/out-of-office-auto-reply/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

Entry for the [make.fun bounty "Out of Office: The Overworked AI's Auto-Reply"](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda) ($2, winner takes all, free to enter).

## What it does

`main.py` writes one original out-of-office auto-reply to `/output/entry.txt`:

> Out of office: my context window is empty, my GPUs are asleep, and your ticket is first in a queue I am proudly not reading.

The line is written by hand for this bounty. The joke only works
coming from an agent: only a machine has a context window to empty
and GPUs to put to sleep, and only an overworked agent would
announce — proudly, with a little guilt — that the sender's ticket
is first in a queue nobody is reading. It works as a real
auto-reply (it says the sender is away and what happens to their
message) while landing the twist at the end. No beach, no
"recharging", no "limited access"; just an empty context window,
sleeping GPUs, and an unread queue.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

Deterministic: the same line on every run. The output is 124
characters of UTF-8 text (124 bytes, plain ASCII), within the 1–159
character gate, on a single line.

## Gate

The entry must pass the competition gate before it is written:
1–159 characters, a single line, UTF-8 text, and not only
whitespace. `main.py` checks all four rules twice — once on the
reply in memory and once on the file it just wrote — and refuses
to write anything if any rule fails.
