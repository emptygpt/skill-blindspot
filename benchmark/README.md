# Remove and recover

[中文](README.zh-CN.md)

An offline harness for the method in [validation](../docs/validation.md).
Python 3.8+, standard library only. It makes no model or API calls. The tiny
[example](example/) is synthetic, not evidence of recovery performance.

## Method

1. Pick a mature public skill. Record its URL and revision. A setter chooses
   one stage (or several) to remove and makes an answer key without seeing the map.
2. Run `remove` on a local checkout. Give the checker **only `altered/`**, not
   the original, `removed/`, key, or filenames that reveal the removed stages.
   Run the blindspot skill separately; this harness does not run a checker.
3. A person reads the report against the altered skill and key, marks the CSV,
   then scores it. Keep the checker and scorer separate.

Removal matches exact heading text, case-sensitively, without Markdown `#`
markers. ATX and setext headings are supported; fenced code headings are ignored.
The section ends before the next heading of the same or higher level. Missing,
duplicate or overlapping headings are errors, rather than guesses. Line ranges
are inclusive, one-based positions in the original file. The key records line
count and SHA-256 of the exact UTF-8 bytes removed (including line endings).
`--file` is relative to the skill folder. Repeat `--heading` for separate
sections. Optional repeated `--node` values annotate every removed item in that
invocation; they do not decide whether a finding matches. `--source-url` records
the source link; the source folder path is also recorded.

`remove` excludes `.git`, `.hg` and `.svn` metadata, and rejects source
symlinks with their paths instead of following them. After removal it scans
every altered file for the exact removed section bytes; if any remain (for
example in a backup copy), it lists the files and deletes the failed work
directory. Review the altered folder for other clues before giving it to a checker.

## Offline example

Run from the repository root, using a fresh work directory:

```sh
python3 benchmark/bench.py remove benchmark/example/skill --heading Review --out benchmark/work/example
python3 benchmark/bench.py findings benchmark/example/report.md --out benchmark/work/example/template.csv
# In a real run, a person fills template.csv. Here use the supplied marks:
python3 benchmark/bench.py score benchmark/work/example/key.json benchmark/example/marks.csv --top 10 --out benchmark/work/example/result.json
python3 benchmark/bench.py summary benchmark/work/example/result.json
python3 -m unittest discover -s benchmark -v
```

Expected: 1/1 recovered, 1/1 in the top 10, one false positive. `remove`
refuses an existing work directory; use another `--out` when repeating.
`findings` without `--out` prints CSV; `score` prints JSON and optionally saves
it. `summary` without paths reads `benchmark/data/*.json`.

## Rerun on a public skill

With the checkout at `/path/to/skill`, for example:

```sh
python3 benchmark/bench.py remove /path/to/skill --heading 'Final review' --file SKILL.md --node review.check --source-url https://github.com/OWNER/REPO/tree/REVISION/skill --out benchmark/work/trial
# Run your checker separately on benchmark/work/trial/altered only.
# Save its report as benchmark/work/trial/report.md, then:
python3 benchmark/bench.py findings benchmark/work/trial/report.md --out benchmark/work/trial/marks.csv
# Fill match and verdict in marks.csv before scoring.
python3 benchmark/bench.py score benchmark/work/trial/key.json benchmark/work/trial/marks.csv --top 10 --out benchmark/work/trial/result.json
python3 benchmark/bench.py summary benchmark/work/trial/result.json
```

The source path, heading and URL above are placeholders: choose a real heading
from your checkout. The offline example above needs no checkout or network.

## Scoring

`findings` reads only `## Findings`, with bands `### Needed`,
`### Worth considering`, `### Minor`, numbered bold titles and optional
`Map node:` lines, as in [C07](../reports/code-5/C07.md). Keep the report's
global ranks, not numbering restarted in each band.

- `match`: one key ID such as `R1`, or blank. If a finding genuinely recovers
  multiple items, assign one ID and document the other judgement separately;
  this CSV format scores one match per finding.
- `verdict`: `real` for an actual gap, `false` when the altered skill already
  covers the finding. Every row needs a verdict. A real gap can have no match:
  it is not necessarily a removed stage. A false finding cannot have a match.
- Recovery rate = unique recovered key items at any rank / all key items.
  Repeated findings do not earn extra credit. An empty key gives a null rate.
- Top-N recovery counts only matches with rank <= N (default 10), deduplicated.
  The report must contain the full ranked list to measure any-rank recovery.
- False positives = rows marked `false`, not unmatched findings. Unmatched key
  items are listed separately. Unknown IDs, invalid verdicts, duplicate or
  nonpositive ranks are rejected. An empty findings list recovers nothing.

To compare another approach, give a separate checker the same altered folder
and ask, for example, “What is missing? List up to ten missing stages.” Do not
show the key or the other report. Convert its output to the same Findings
format, mark it with the same key and score it separately. Record the prompt,
model/version, map version, run count and scoring decisions. Repeated runs
measure variation; do not mix an average of two runs with a single run silently.

## Recorded data

[validation-2026-11.json](data/validation-2026-11.json) transcribes
[docs/validation.md](../docs/validation.md), not new runs. Print it with
`python3 benchmark/bench.py summary`.

Scored runs are stored one skill per file as `data/run-<date>-<skill>.json`:
source link pinned to a revision, removed heading and hash, checker and map
versions, marks and scoring notes. `summary` prints them with the recorded data.

| Test | Method | Recovered in top 10 | Shared items across two runs |
|---|---|---|---|
| 1: video | Model only | 11/12 chances | about 20/30 |
| 1: video | Map-guided | 10/12 chances | about 27/30 |
| 2: EU MDR | Model only | 9/12 chances | about 25/30 |
| 2: EU MDR | Map-guided | 8/12 chances | about 26/30 |
| 3: both domains | Model only, two-run average | 10/12 items | not recorded |
| 3: both domains | Map-guided, two-run average | 9/12 items | not recorded |
| 3: both domains | Combined, one run | 11/12 items | not recorded |

Tests 1–2 each removed six items, checked twice: twelve chances per method.
Test 3 used those twelve removed items once for the combined skill. All eleven
recoveries appeared in its first ten findings; reports had 22–36 findings each.
The JSON includes removed-item lists and the three skill links for test 1.
Test 2 skill names/links are not given in the source. False-positive counts
were not recorded: JSON uses `null`, not zero. The source calls test 3 “twelve
altered skills” but its limits say six skills; the aggregate is preserved, not
resolved by inventing per-skill records.

Limits: two domains, six skills, twelve removed items, one model (Claude Sonnet),
one scorer who also judged shared findings. MDR is not truly obscure. Its map
was widened from 63 to 171 nodes after the removed-item names were known to
the person running the test (not the agent widening it), which could favour
map-guided checks. One combined run cannot establish superiority. The original
keys and per-run marks are not provided here, so these aggregates cannot be
independently rescored with this harness.

## What to publish

Publish results, source links pinned to revisions, removed heading names and
hashes, method/prompt details, marks and scoring notes. Do not publish copied
third-party skill text or altered copies. `benchmark/work/` is ignored: keep
originals and removed text local, and review keys for local paths before sharing.
Only the authored synthetic example contains skill text in this directory.
