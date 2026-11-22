# Map format

For the method (choosing sources, boundaries, what to leave out), see [Build your own domain map](build-a-map.md).

A map is one YAML file in `skills/blindspot/maps/`. It lists the stages and concerns of a domain. Every node cites where it comes from.

The [map licence and attribution notes](../skills/blindspot/maps/INDEX.md#licence-and-attribution) explain how source terms apply to map data and derived outputs.

## The rule

**A node with no source does not go in.** A model may merge duplicates, reword and regroup. It may not decide alone that something belongs. A source can be an occupational database, a standard, a regulation, a textbook or course outline, official platform documentation, or a documented industry consensus. The `locator` must be text that really appears in the source: a section title, a clause number, a task statement, a skill name.

Something the model believes is missing but has no source stays out of the map. Record it in the "not yet covered" list in the file header so someone can find a source.

## Base map

```yaml
map:
  id: video                 # lowercase, hyphens
  title: Video production
  version: 0.1.0
  updated: 2026-11-16
  scope: One or two sentences. Say what is out of scope.
sources:
  - id: S1
    title: Title in its original language
    publisher: Who published it
    url: https://...
    retrieved: 2026-11-16
    licence: Licence, or "not verified"
groups:
  - id: script
    title: Script
    nodes:
      - id: script.opening-hook        # group id, dot, short name
        title: Opening hook
        description: One plain sentence on what doing this means.
        applies_when: Optional. When this node is relevant.
        sources:
          - ref: S6
            locator: "hooks, pacing"
```

## A map that extends another

Use this for a narrower kind of work inside a domain, such as short-form video inside video, or a newsletter article inside writing.

```yaml
map:
  id: video-short
  extends: video
  title: Short-form video
  version: 0.1.0
  updated: 2026-11-17
  scope: ...
sources:            # only sources not already in the base map
  - id: T1
    ...
exclude:            # base nodes that do not apply to this kind of work
  - node: publish.playlists
    reason: One short reason.
groups:             # nodes to add. A node here needs its own source.
  - id: short
    title: Short-form specifics
    nodes: [...]
```

## Contributing a node

Run `python3 scripts/check_maps.py` to validate the YAML and check that the runtime cache is current. With `--write`, the checker updates the cache only after validation passes. Source records need all six fields shown above, with an HTTP(S) URL and a calendar date. Source, group and node IDs must be unique across a map and its ancestors; an extension can cite ancestral sources but cannot redeclare them. Extension chains must name existing maps and may not contain cycles.

Open a pull request that adds the node with its source. Give the URL and the exact locator. If the source is behind a login or paywall, say so. Cite titles and short statements only. Do not copy body text from sources whose licence does not allow it.
