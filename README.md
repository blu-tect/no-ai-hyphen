# No AI Hyphen

A tiny, optional writing style rule for AI agents.

**Mission:** Keep generated prose free of em dashes and en dashes, without altering code, quoted material, or user supplied text.

## Agent instruction

> In prose written for this user, do not use em dashes or en dashes. Prefer commas, full stops, colons or parentheses. Preserve punctuation in verbatim quotations, code, URLs and source material. Do not change meaning to satisfy this style rule.

Copy the instruction into your agent's custom instructions or system prompt.

## CLI check

Requires Python 3.9 or newer. Run:

```sh
python3 no_ai_hyphen.py README.md
```

The checker flags prohibited dash characters in supplied files. It does not automatically rewrite files, because substitutions can change meaning.

## Tests

```sh
python3 -m unittest discover -s tests
```

## Licence

MIT. See LICENSE.
