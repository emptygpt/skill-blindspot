# Contributing

The most useful contributions are maps and sources. Code is a small part of this repository.

## Add or fix a node

1. Find a source: an occupational database, a standard, a regulation, a textbook or course outline, official platform documentation, or a documented industry consensus.
2. Add the node to the map in `skills/blindspot/maps/` with its `ref` and a `locator`: text that really appears in the source, such as a section title, clause number or task statement.
3. Run `python3 scripts/check_maps.py` (needs PyYAML). The same check runs on every pull request.
4. Open a pull request. Give the URL, and say if the source is behind a login or paywall.

**A node with no source does not go in.** If you believe a stage is missing but cannot find a source, add it to the "not yet covered" list in the map's header, or open a [node correction](https://github.com/emptygpt/skill-blindspot/issues/new?template=node-correction.yml) issue, so someone else can find one.

Cite titles and short statements only. Do not copy body text from sources whose licence does not allow it.

The full format, including how a narrower map extends a base map, is in [docs/map-format.md](docs/map-format.md).

## Add a map

Open a [map request](https://github.com/emptygpt/skill-blindspot/issues/new?template=map-request.yml) first, so two people do not build the same one. [Build your own domain map](docs/build-a-map.md) walks through the steps. A new map should not need any change to `SKILL.md`. If it does, say why in the issue.

## Share a report

If you ran blindspot on a public skill and the report taught you something, open an issue with a link. Reports on other people's skills should link to their repository and quote only short lines as evidence.

## Change the skill

Changes to `skills/blindspot/SKILL.md` should come with a before-and-after run on at least one skill, so the effect can be seen.
