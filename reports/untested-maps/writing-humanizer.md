# Blindspot report: humanizer

Skill under audit: [blader: humanizer](https://github.com/blader/humanizer/blob/3e5f816b5609c4002aebb69f12c6476fe3347d0a/SKILL.md).

Map: writing 0.1.0    Profile: none    Date: 2026-11-23

## Scope

- Takes existing prose and, when supplied, a writing sample. This audit covers edits to an online nonfiction article.
- Rewrites prose for voice and directness without changing supported claims. It can return text or edit prose in a named file.
- Ends at the rewritten text, not at reporting, image production, publication, or follow-up.

## Step 2 list (before opening the map nodes)

- The initial rewrite may introduce details. The draft check guards the original facts, but does not say how to verify a newly introduced detail before use.
- The process checks the first rewrite and then rewrites again. The final-version and file-output instructions do not repeat the factual check on the exact text delivered.

## Findings

### Needed

None.

### Worth considering

1. **Verify factual changes in the final rewrite, not just the intermediate draft** [model+map+trace]
   Map nodes: `fact.verify`, `fact.statistics`, `fact.cite-sources`, `fact.not-misleading`, `comp.ai-accuracy`.
   Sources: [O*NET 30.0](https://www.onetcenter.org/database.html) — 27-3041.00, verification of facts, dates and statistics; [BBC Editorial Guidelines 2025](https://www.bbc.co.uk/editorialguidelines/guidelines) — Accuracy: Reporting Statistics and Risk, Avoiding Misleading Audiences, and Use of Automated Technology and Artificial Intelligence; [SPJ Code of Ethics](https://www.spj.org/spj-code-of-ethics/) — access to relevant source material.
   Why: SKILL.md:37–39 checks the intermediate rewrite against the input, then allows another rewrite without specifying a repeat check. It also permits new specific details without requiring an evidence check for them. A changed number or qualifier may survive in the delivered text even though the checked draft was faithful.
   Fix: Compare the final version with the input for factual changes, and check any new detail against a supplied or reliable source; ask or omit it if it cannot be supported.

### Minor

1. **Add a separate mechanics check when a clean copy is expected** [map]
   Map nodes: `edit.copyedit`, `edit.proofread-method`.
   Sources: [O*NET 30.0](https://www.onetcenter.org/database.html) — 27-3041.00, reading copy or proof to detect and correct errors; [Purdue OWL: Proofreading](https://owl.purdue.edu/owl/general_writing/the_writing_process/proofreading/index.html) — General Strategies Before You Proofread.
   Why: SKILL.md:36–39 gives a targeted read-aloud pass for residual patterns, not a final check for spelling, punctuation and syntax introduced by the rewrite.

## Unsourced findings

None.

## Evidence limitations

Read the pinned SKILL.md including its examples. Other repository files are not called by this prose workflow. The Wikipedia and research links at the end credit the pattern list rather than delegate an editorial step. No target skill or example was executed.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Read the text and optional sample; mark patterns | Candidate changes and voice constraints | First rewrite | SKILL.md:36,43,47 gives contextual exceptions and a no-change branch. |
| Write the first pass | Revised prose | Draft check | SKILL.md:38 compares it against the input and rechecks patterns. |
| Make final edits | Delivered prose or updated file | Writer | SKILL.md:39,49–55 gives no second fact check after this pass. |

## Map table

| Node | State | Evidence |
|---|---|---|
| topic.* | not-applicable | Article topic and commission precede the prose edit. |
| audience.define | not-applicable | The reader is not selected in this editing pass. |
| audience.tone-medium | covered | SKILL.md:41–47 — "match the kind of text"; the sample or prose genre sets the register. |
| audience.research | not-applicable | No audience study; an existing sample is a style input. |
| research.* | not-applicable | No reporting or background research workflow. |
| structure.outline | not-applicable | A full text is the input. |
| structure.main-point | covered | SKILL.md:39 — "main point"; use it to rebuild an awkward paragraph. |
| structure.select-material | covered | SKILL.md:37 — "without losing information"; reorder or compress while keeping substance. |
| structure.length-format | not-applicable | No new article length or form is commissioned. |
| structure.context | not-applicable | Not tasked with gathering or adding article background. |
| drafting.* | not-applicable | Edits an existing article rather than drafting one from a topic. |
| revise.rewrite | covered | SKILL.md:39 — "rewrite the paragraph"; uses larger edits when local repairs are awkward. |
| revise.requirements | not-applicable | No publisher or client brief beyond the prose edit. |
| revise.feedback | not-applicable | Returns an edit; no editor-to-writer review cycle. |
| revise.structure-cohesion | covered | SKILL.md:36–37 — "Check paragraph shape"; inspect patterns across sentences and edit paragraph boundaries and order. |
| revise.consistency | not-applicable | No series or multiple authors to reconcile. |
| fact.verify | shallow | SKILL.md:38 — "did not drop or change"; checks fidelity to the supplied draft, not the factual basis of additions or the final pass. |
| fact.statistics | shallow | SKILL.md:38 — "number, date"; preserves figures during the intermediate check, but does not verify new ones or recheck final edits. |
| fact.corroborate | not-applicable | Not a reporting or independent investigation workflow. |
| fact.authenticity | not-applicable | Does not authenticate documentary evidence. |
| fact.rumour | covered | SKILL.md:422 — "what the source does not show"; state the limit or remove the guess. |
| fact.cite-sources | shallow | SKILL.md:327 — "name it"; replaces vague attribution when known, but gives no trace-back step for new details. |
| fact.right-of-reply | not-applicable | Does not solicit responses from subjects. |
| fact.not-misleading | shallow | SKILL.md:38–39 — "lost or changed claim"; catches changes before another rewrite, not after it. |
| fact.expert-review | not-applicable | No consultation or expert handoff. |
| edit.copyedit | shallow | SKILL.md:239 — "Use active voice"; gives targeted syntax improvements but not a full mechanics pass. |
| edit.proofread-method | shallow | SKILL.md:38 — "Read the draft aloud"; checks pattern recurrence, not general final-copy errors. |
| edit.second-reader | not-applicable | One editing pass, no external review or release. |
| edit.style-standards | not-applicable | No publisher style guide; author voice is checked separately. |
| packaging.* | not-applicable | No article headline, metadata or byline task. |
| visual.select | not-applicable | Does not select images. |
| visual.captions | not-applicable | Does not prepare images or captions. |
| visual.edit-integrity | not-applicable | Images are not edited. |
| visual.layout | covered | SKILL.md:359,377 — "Use sentence case"; improves text hierarchy and removes purely decorative formatting. |
| rights.permissions | not-applicable | No third-party material is commissioned or acquired. |
| rights.attribution | covered | SKILL.md:456 — "source credit the reader can follow"; preserves traceable credit during prose cleanup. |
| rights.own-copyright | not-applicable | No rights registration. |
| rights.commission-terms | not-applicable | No negotiation or commission. |
| publishing.* | not-applicable | Ends at returned or saved prose. |
| feedback.* | not-applicable | Does not handle post-publication work. |
| comp.minimize-harm | not-applicable | No editorial release decision about named subjects. |
| comp.privacy | not-applicable | No collection or publication of personal details. |
| comp.vulnerable-subjects | not-applicable | Does not conduct reporting on vulnerable subjects. |
| comp.conflicts | not-applicable | No commissioned or sponsored reporting. |
| comp.sponsored-disclosure | not-applicable | No sponsorship or brand handoff. |
| comp.stereotypes | not-applicable | Not a substantive review of the article's reporting about groups. |
| comp.law | not-applicable | No legal or release review. |
| comp.ai-disclosure | not-applicable | No publication or disclosure requirement specified for the edited text. |
| comp.ai-accuracy | shallow | SKILL.md:37–38 — "detail you know to be true"; no prescribed source check for a new detail or check after the final edits. |
| comp.honest-authorship | not-applicable | Does not create a byline, biography or credentials. |

counts: covered 8, shallow 7, absent 0, not-applicable 63, undetermined 0

## Excluded by profile

None.
