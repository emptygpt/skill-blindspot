# Blindspot report: wechat-typesetting

Skill under audit: [webzol/WXSKill](https://github.com/webzol/WXSKill/tree/964b3aa1c46a4119acbe6a0baf13e0e95feb6396).

Map: wechat-article 0.1.0 extends writing 0.1.0    Profile: none    Date: 2026-11-23

## Scope
- Takes existing copy, chooses a theme and template, and produces inline HTML intended for pasting into the WeChat official-account editor.
- Delivers HTML and an archive; can also generate a browser preview. Placement and legibility of text and images are in scope.
- Does not commission, write or fact-check the article, prepare the account’s article fields, create a platform draft, or send it.

## Step 2 list (before opening the map nodes)

- Looked for preview, mobile, paste and sanitization checks: the preview is optional and there is no explicit post-paste verification and adjustment loop.
- Looked for image URLs, alt text, captions and fallback: the component has fields for images but no step verifies loading or supplies a fallback for missing assets.
- Looked for buttons, links and follow prompts: templates supply them without a rule for when to omit them or how to check their destinations.
- Looked for preservation and omissions: the archive can note omissions, but the workflow does not compare the full output with the supplied copy.

## Findings

### Needed

None.

### Worth considering

1. **Verify image delivery and readable captions in the editor handoff** [model+map+trace]

   Map nodes: `wx.body-images`, `visual.captions`.
   Source: [WeChat draft API](https://developers.weixin.qq.com/doc/subscription/api/draftbox/draftmanage/api_draft_add.html) — `content`, external URLs are filtered in the API route; [WeChat article-image upload API](https://developers.weixin.qq.com/doc/subscription/api/material/permanent/api_uploadimage.html) — format and size for that route; [ESCO](https://esco.ec.europa.eu) — write captions.
   Why: The template can carry image descriptions and captions, but the formatter assumes public URLs and does not check whether meaningful images and their captions survive the paste. The API rules don't establish what the manual editor does; the browser preview doesn't establish that either.
   Fix: For image-bearing articles, provide an asset checklist and ask the operator to verify loading and matching captions after paste, with a manual upload fallback if an image fails.
2. **Review the final snippet for hidden, omitted, or overlong body content** [model+map+trace]

   Map nodes: `wx.body-limits`, `wx.no-hidden-or-stuffed-text`.
   Source: [WeChat draft API](https://developers.weixin.qq.com/doc/subscription/api/draftbox/draftmanage/api_draft_add.html) — `content` limits for the API route; [WeChat Official Platform Operating Rules](https://mp.weixin.qq.com/mp/opshowpage?action=newoplaw) — keyword stuffing, hidden text and §4.17.
   Why: An optional browser preview and a CSS checklist don't show whether source passages are missing, content is visually hidden in a selected theme, or a long article will fit the target route. The draft API limit is a reference, not a verified limit for manual paste.
   Fix: Compare text against the input, flag probable size and legibility problems, and give the operator an in-editor preview check before saving.
3. **Treat template buttons and footers as optional article content** [model+map]

   Map nodes: `wx.no-induced-share-follow`, `wx.no-external-diversion`.
   Source: [WeChat Official Platform Operating Rules](https://mp.weixin.qq.com/mp/opshowpage?action=newoplaw) — §§3.3.1, 3.3.2, 3.22 and the provision on incomplete posts directing readers elsewhere.
   Why: Reusable follow footers and outbound buttons are not inherently violations. There is no check that they belong in the source copy, that nobody must follow or share to read, or that the snippet contains the full article rather than routing readers elsewhere for it.
   Fix: Omit filler calls to action and validate any retained link and the completeness of the body before providing the snippet.
4. **Flag sensitive assets where the layout inserts them** [map]

   Map node: `wx.sensitive-images`.
   Source: [WeChat Official Platform Operating Rules](https://mp.weixin.qq.com/mp/opshowpage?action=newoplaw) — §4.26, images unsuitable for direct display.
   Why: The image component chooses placement and rendering but does not distinguish sensitive photos. Not every draft contains them, and the formatter need not alter user assets on its own.
   Fix: Flag affected images and ask for a cleared replacement or appropriately obscured version before including them.

### Minor

None.

## Unsourced findings

None.

## Evidence limitations

The audit read the pinned instructions, rendering guidance, templates, themes and examples. No target skill or installer was run, and neither a browser render nor a manual paste into WeChat was tested. API limits are not treated as confirmed manual-editor limits.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Read copy | Recognized body structure | Template selection and assembly | SKILL.md:45–52 identifies sections and blocks; it does not produce a completeness check for the finished body. |
| Lock template and theme | Block skeleton and palette | HTML generation | SKILL.md:49–59 names defaults and requires the corresponding files. |
| Assemble inline HTML | Pasteable snippet | Preview, delivery and archive | SKILL.md:148–161 prescribes a compatibility self-check and an optional local preview, not a post-paste check. |
| Deliver and archive | Snippet, input copy and handoff notes | Human operator | SKILL.md:65–94 records external assets and omissions but does not check the saved or rendered platform result. |

## Map table

| Node | State | Evidence |
|---|---|---|
| topic.* | not-applicable | Receives complete copy instead of choosing or commissioning a topic. |
| audience.* | not-applicable | Applies visual themes without defining the readership or writing to it. |
| research.* | not-applicable | No editorial research. |
| structure.* | not-applicable | Recognizes the supplied structure to style it; does not plan the article. |
| drafting.* | not-applicable | Does not author the article. |
| revision.* | not-applicable | Changes layout, not prose. |
| factcheck.* | not-applicable | Copy and claims are supplied; no editorial verification. |
| editing.* | not-applicable | No copy-edit or proofread of the source text. |
| packaging.* | not-applicable | Styles the existing heading; does not write headline copy or article metadata. |
| visual.select | not-applicable | Places supplied images rather than commissioning or selecting illustrations. |
| visual.captions | shallow | `references/components.md:117` — "{{图片说明}}" provides a caption slot but no instruction for a meaningful caption when the source lacks one. |
| visual.edit-integrity | not-applicable | Styles image placement; does not create or edit image content. |
| visual.layout | covered | `SKILL.md:59` — "把草稿内容塞进合适块里" after selecting the template and theme. |
| rights.* | not-applicable | No rights transaction or editorial selection of third-party material; styles supplied copy and assets. |
| publishing.* | not-applicable | Ends with the snippet and archive, not uploading, signing off or sending a post. |
| feedback.* | not-applicable | No post-release work. |
| compliance.* | not-applicable | Does not commission or assess the supplied prose; platform rules on the generated layout are considered below. |
| wx-meta.* | not-applicable | The HTML body is not a platform title, cover, author, summary, original-link or topic-tag field. |
| wx.body-limits | shallow | `SKILL.md:161` — "长文如需分段交付" describes splitting output but not validating the complete HTML payload size. |
| wx.body-images | shallow | `SKILL.md:110` — "微信外链图"; provides inline image placement but no test of pasted images or platform-upload fallback. |
| wx.layout-readability | covered | `references/wechat-compat.md:53` — "正文字号 16px、行高 1.8" sets body typography; the preceding line sets dark-theme contrast. |
| wx.no-hidden-or-stuffed-text | shallow | `references/wechat-compat.md:52` — "正文与背景对比度 ≥" mitigates unreadable text in dark themes; no check for intentionally hidden elements or keyword stuffing. |
| wx.sensitive-images | absent | Image markup and compatibility checks do not screen for sensitive images. |
| wx-original.* | not-applicable | Does not declare originality or rewrite other publishers' work; no reprint submission or complaint handling. |
| wx.ad-label | not-applicable | Does not author ad copy or edit disclosures in existing copy. |
| wx.overmarketing | not-applicable | Does not author or vet product claims. |
| wx.finance-claims | not-applicable | Does not author or vet financial claims. |
| wx.source-labelling | not-applicable | Does not write current-affairs copy or its source line. |
| wx.ai-label | not-applicable | Transforms formatting around supplied text; does not generate substantive copy or set platform labels. |
| wx.no-templated-or-automated | not-applicable | Reuses visual templates, not the main text; no automatic posts. |
| wx.no-induced-share-follow | absent | Templates can insert a follow prompt; no check for forced or rewarded engagement. |
| wx.no-external-diversion | absent | Supports buttons and external links but does not check that the user can read the full article in-app. |
| wx.false-info | not-applicable | Existing factual claims are outside formatting. |
| wx.personal-data | not-applicable | Does not add personal data or collect reader information. |
| wx.legal-red-lines | not-applicable | Editorial legal review of supplied copy is outside formatting. |
| wx-send.* | not-applicable | No platform draft, send, settings or post-release operations. |

counts: covered 2, shallow 4, absent 3, not-applicable 109, undetermined 0

## Excluded by profile

None.
