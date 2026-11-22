# Build your own domain map

English | [中文](build-a-map.zh-CN.md)

This guide walks through making a new domain map, from choosing the domain to a passing check. The field reference is [map-format.md](map-format.md); this page is about the method. The examples come from the five maps added most recently: [`seo-web`](../skills/blindspot/maps/seo-web.yaml), [`spreadsheet-finance`](../skills/blindspot/maps/spreadsheet-finance.yaml), [`data-analysis`](../skills/blindspot/maps/data-analysis.yaml), [`tech-docs`](../skills/blindspot/maps/tech-docs.yaml) and [`research-paper`](../skills/blindspot/maps/research-paper.yaml). Open the files next to this page: every example below can be found in them.

| Map | Sources | Groups | Nodes |
|---|---|---|---|
| `seo-web` | 29 | 12 | 74 |
| `spreadsheet-finance` | 13 | 10 | 49 |
| `data-analysis` | 8 | 9 | 45 |
| `tech-docs` | 15 | 11 | 75 |
| `research-paper` | 23 | 8 | 76 |

## 1. Pick a domain

A map describes the stages and concerns of one kind of work, so that a skill doing that work can be checked for domain coverage. Before you start:

- **Check the existing maps.** Read [maps/INDEX.md](../skills/blindspot/maps/INDEX.md) or run `python3 skills/blindspot/scripts/blindspot.py maps`. If an existing map already covers most of the work, a narrower map that `extends` it is less work than a new base map (see step 5).
- **Name the work, not a tool.** Each of the five maps names a kind of work and what is out of scope in its `scope` field. `data-analysis` is "Answering a question with data"; `spreadsheet-finance` is "Building or changing a spreadsheet model or financial analysis".
- **Make sure sources exist.** The rule for every map is that a node with no source does not go in. If you cannot find an occupational database entry, a standard, a regulation, a textbook or course outline, or official documentation for the domain, the map will stay empty. Look for sources before you write nodes.
- **Open a [map request](https://github.com/emptygpt/skill-blindspot/issues/new?template=map-request.yml)** so two people do not build the same map. A new map should not need a change to `SKILL.md` ([CONTRIBUTING.md](../CONTRIBUTING.md)).

## 2. Find sources and cite them per node

Work from the sources to the nodes, not the other way round. List what the sources say a practitioner does, then group it.

**Kinds of source the five maps use:**

| Kind | Example in the maps |
|---|---|
| Occupational database | O*NET task statements: `data-analysis` D1 *Data Scientists (15-2051.00)* |
| Classification of skills | ESCO skill names: `tech-docs` cites "identify ICT user needs" |
| Professional body guidance | ICAEW *20 principles for good spreadsheet practice* in `spreadsheet-finance` |
| Government method guidance | *The AQuA Book* in `data-analysis` |
| Official documentation | Google web.dev *Web Vitals* in `seo-web` |
| Specification or standard | OpenAPI Specification v3.1.1 and WCAG 2.2 in `tech-docs` |
| Peer-reviewed paper | Wilson et al. (2017), *Good enough practices in scientific computing*, in `data-analysis` |
| Regulation | China PIPL articles in `data-analysis` |

**Read the source yourself.** Open the page and confirm the text is there. A source you remember, or one a model suggests, is not a source until you have read it.

**Record the source once** in the file's `sources` list, with all six fields: `id`, `title`, `publisher`, `url` (HTTP or HTTPS), `retrieved` (a `YYYY-MM-DD` date) and `licence`. For example, from `seo-web`:

```yaml
- id: W1
  title: "Web Vitals"
  publisher: "Google web.dev"
  url: "https://web.dev/articles/vitals"
  retrieved: '2026-11-19'
  licence: "CC BY 4.0 (page content); code samples Apache 2.0"
```

If you did not check the licence, write `not verified` and say what you cite, as `spreadsheet-finance` does for ICAEW: `not verified; only titles, headings and short statements cited`.

**Cite it on each node** with a `ref` and a `locator`. The locator is text that really appears in the source, so a reader can search for it. In the five maps:

- an O*NET task with its Task ID: `'Task 21831: Identify business problems or management objectives that can be addressed through data analysis.'` (`data-analysis`, `question.problem`);
- a numbered principle: `'6. Tailor the design and documentation to the needs of the audience and dependent processes.'` (`spreadsheet-finance`, `inputs.assumptions`);
- a heading: `"Core Web Vitals"` (`seo-web`, `page-experience.cwv`);
- an object or criterion title: `"Security Scheme Object"` (`tech-docs`, `api-description.security`);
- an ESCO skill name: `identify ICT user needs` (`tech-docs`, `doc-planning.readers`).

A node may cite several sources. Write the node's `title` and `description` in your own words. Cite titles and short statements only, and do not copy body text from a source whose licence does not allow it.

**Attribution.** When a source's licence asks for attribution, put the notice in the file header under "Licence and attribution". The O*NET notice in `data-analysis` and `spreadsheet-finance` is an example. When a source is share-alike, say so there too: `tech-docs` cites only headings of the CC BY-SA GitLab documentation and states that the parts derived from them are shared under the same terms.

## 3. List what you could not read as not covered

Some sources cannot be read: the page needs a login, the standard is paid, or the server returns an error or an empty page. Do not cite them, and do not write a node from what you think they say. Add an entry to the "Not yet covered" list in the file header instead, with the reason, so someone else can find a source later. A stage that you believe belongs in the map but that no source you read supports goes in the same list.

From the five maps:

- `seo-web`: the ESCO occupation page for search engine optimisation experts "returned a temporary-issue shell", and the Bing guidelines URL "returned an application shell", so neither is cited.
- `data-analysis`: the ASA Ethical Guidelines page and PDF "returned HTTP 403", and the EUR-Lex GDPR pages "returned empty responses"; the header adds that the PIPL nodes are not a substitute for GDPR.
- `spreadsheet-finance`: the XBRL specification fetch "returned no readable content", so tagging and filing validation are not covered.
- `tech-docs`: ISO/IEC/IEEE 26514 and 26515 are paid standards and the ISO page could not be read.
- `research-paper`: the COPE core-practices URL returned a member Code of Conduct instead, so correction and retraction workflows are not covered.

Two related habits from the same maps:

- If a readable copy of the same content exists, cite that and say so. `research-paper` cites ASA's public release of the 2016 principles because the journal article returned HTTP 403.
- If you leave out a readable source on purpose, say why. `tech-docs` lists "Not used on purpose: Diataxis (licence not found, as in the software map)".

## 4. Draw boundaries with existing maps

A skill is often checked against more than one map, so a map should say which neighbouring work it does not own. Write the boundary in two places: in the `scope` field ("Out of scope: ..."), and in the file header, naming the other map and, where useful, its node ids.

- `data-analysis` keeps analysis code (SQL, Python, R notebooks and scripts) as an analysis artefact, but sends building production software, data pipelines and ML services to `software`, and writing and publishing the article that contains the results to `writing`.
- `spreadsheet-finance` sends the prose quality of a memo to `writing` and the engineering practice of VBA, Python or Office Script code to `software`, and keeps concerns specific to spreadsheets, such as workbook change control and formula auditing.
- `seo-web` sends a single article's content to `writing` and code changes, security, testing and release to `software`. It names the overlap with `writing`'s `head.metadata-seo` and limits itself to site-level decisions.
- `tech-docs` has a "Boundaries with other maps" block. It names the `software` nodes that already ask whether a change updates its docs (`documentation.technical-docs`, `documentation.review-docs`) and the ones that own versioning and changelogs (`release.versioning`, `release.breaking-changes`, `release.changelog`), and says to check a task that is both a code change and its docs against both maps.
- `research-paper` takes academic paper writing, which the `writing` map lists as out of scope, and leaves general software-engineering practice (version control, code review, testing, CI) to `software`.

When the same source fits two maps, it can be cited in both, as long as each node is about its own map's work. `tech-docs` notes that some O*NET 27-3042.00 and ESCO technical communicator items are cited by both `tech-docs` and `writing`.

## 5. Base map or extension

The five maps are all base maps. A narrower kind of work inside an existing domain can instead extend a map, as `video-short` and `video-long` extend `video` and `wechat-article` extends `writing`. An extension:

- sets `extends: <id>` under `map`;
- lists only sources not already in the base map, and may cite the base map's sources;
- lists base nodes that do not apply under `exclude`, each with a one-line reason (`video-short` excludes `pre.budget` because "Phone-based short-form is normally made without a production budget to estimate.");
- adds its own groups and nodes, each with its own source.

The YAML for both shapes is in [map-format.md](map-format.md).

## 6. Write the file

Create `skills/blindspot/maps/<id>.yaml`. The file name must match `map.id`. The five maps use the same layout, so copy their structure:

1. A comment header: rules for the map, scope and boundaries, licence and attribution, and "Not yet covered".
2. `map`: `id`, `title`, `version`, `updated`, `scope`.
3. `sources`: one record per source.
4. `groups`: each with an `id` (lowercase letters, digits and hyphens, starting with a letter) and a `title`, holding `nodes`. Node ids are the group id, a dot and a short name, such as `question.problem`.

Each node needs `id`, `title`, `description` and at least one entry in `sources`. `applies_when` is optional, for a node that only matters in some cases. `keywords` is optional too: a list of words that the helper's `prepare` command also looks for when it matches skill lines to the node. `tech-docs` uses it, for example `audience` and `user needs` on `doc-planning.readers`.

Then list the map where people will find it: a row in [maps/INDEX.md](../skills/blindspot/maps/INDEX.md) and in the map tables of [README.md](../README.md) and [README.zh-CN.md](../README.zh-CN.md).

## 7. Run the checks

Install PyYAML and run the checker from the repository root:

```bash
python3 -m pip install pyyaml
python3 scripts/check_maps.py
```

It checks every map and prints one line each, for example `ok   data-analysis: 45 nodes`. It fails when, among other things:

- `map.id` does not match the file name, or `title`, `version`, `updated` or `scope` is missing;
- a source record lacks one of its six fields, its `url` is not HTTP(S), or `retrieved` is not a `YYYY-MM-DD` date;
- a source, group or node id is used twice in the map or its base maps;
- a node has no source, cites a source id that is not defined, or has an empty locator;
- `extends` names a map that does not exist or forms a cycle, or `exclude` names an unknown base node.

The helper script reads `skills/blindspot/maps/maps.json`, a compiled copy of all maps. When the YAML passes, write the new copy and check again:

```bash
python3 scripts/check_maps.py --write
python3 scripts/check_maps.py      # ends with "ok   maps.json is up to date"
```

Do not edit `maps.json` by hand. If it conflicts when you merge, take either side and run `--write` again.

Then try the map with the helper, which needs only the standard library:

```bash
python3 skills/blindspot/scripts/blindspot.py maps
python3 skills/blindspot/scripts/blindspot.py checklist --map <id> --groups
python3 skills/blindspot/scripts/blindspot.py sources --map <id> <node-id>
python3 skills/blindspot/scripts/blindspot.py prepare <a-skill-folder> --map <id> --out worksheet.md
```

`prepare` on a real skill in the domain shows whether the node titles, descriptions and keywords find the lines you expect. The same `check_maps.py` run, the unit tests and these smoke tests run on every push and pull request ([check-maps.yml](../.github/workflows/check-maps.yml)), on Python 3.8 and 3.12.

## 8. Open a pull request

In the description, list the sources with their URLs and say which were behind a login or paywall or could not be read. Keep the "Not yet covered" list in the file current. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Checklist

- [ ] Existing maps checked; scope and out-of-scope written
- [ ] Every source read, recorded with all six fields
- [ ] Every node cites a source with a locator that appears in it
- [ ] Attribution notices in the header where a licence asks for them
- [ ] Unreadable or missing sources listed under "Not yet covered"
- [ ] Boundaries with neighbouring maps written in `scope` and the header
- [ ] Rows added to `maps/INDEX.md`, `README.md` and `README.zh-CN.md`
- [ ] `python3 scripts/check_maps.py --write`, then `python3 scripts/check_maps.py` passes
