# Blindspot report: wechat-skill-article-workflow

Skill under audit: [just-ye/wechat-AI-technology-article-skill](https://github.com/just-ye/wechat-AI-technology-article-skill/tree/ae6d749d914065bb9a055c90dbcf0b370d03a08e).

Map: wechat-article 0.1.0 extends writing 0.1.0    Profile: none    Date: 2026-11-23

## Scope
- Writes or reviews practical articles about research Skills for graduate students from explicitly supplied source material, using references for structure and style.
- Includes outline approval, drafting, and editorial review. Ends at one reviewed Markdown file; does not format for upload, set account fields, submit or send.
- Separately extracts a named WeChat article or imports a reference into the local workspace. These are input routes, not publication or automatic rewriting. The map table evaluates the authored article.

## Step 2 list (before opening the map nodes)

- Looked for headline review: outline approval sets a title direction but the final reviewer does not explicitly compare the resulting title to the article.
- Looked for release/version/date, install tests and unsupported results: the workflow preserves supplied facts but does not establish that commands still apply, and prohibits running them itself.
- Looked for examples, first-person voice and disclosure: the structure asks for practical demonstrations and a collective voice, but does not explicitly label untested or hypothetical demonstrations or generated copy.
- Looked for permission, credit and sponsorship: reference use is constrained, but final review does not check source credit, artifact reuse rights or promotional disclosures.
- Looked for Markdown render, screenshots and alt text: a screenshot occurs in a reference example, but the reviewer does not check referenced assets or render the delivered file.

## Findings

### Needed

None after independent re-check.

### Worth considering

1. **Flag AI-generated prose to the operator at handoff** [model+map]

   Map nodes: `comp.ai-disclosure`, `wx.ai-label`.
   Source: [BBC Editorial Guidelines](https://www.bbc.co.uk/editorialguidelines/guidelines) — transparency about AI; [WeChat Official Platform Operating Rules](https://mp.weixin.qq.com/mp/opshowpage?action=newoplaw) — prominent labelling of generated or synthesized content.
   Why: The independent re-check confirmed that there is no AI or AIGC disclosure step at revision `ae6d749`. The skill stops at a Markdown file, so scope rule 3 puts the upload-time AI label outside its scope. Whether the Markdown itself should carry a disclosure is disputed, so scope rule 5 puts this finding in Worth considering rather than Needed.
   Fix: At final delivery, remind the operator to tick the AI creation declaration on upload and optionally add a disclosure line to the body.
2. **Check the provenance, version and limits of practical demonstrations** [model+map]

   Map nodes: `research.online-third-party`, `fact.verify`, `fact.corroborate`, `fact.authenticity`, `fact.not-misleading`, `draft.first-hand`, `draft.opinion-labelled`, `wx.false-info`, `wx.overmarketing`.
   Source: [BBC Editorial Guidelines, §3](https://www.bbc.co.uk/editorialguidelines/guidelines) — online material, corroboration and avoiding misleading audiences; [Google’s people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) — demonstrate first-hand expertise; [SPJ Code of Ethics](https://www.spj.org/spj-code-of-ethics/) — label opinion and analysis; [WeChat Official Platform Operating Rules](https://mp.weixin.qq.com/mp/opshowpage?action=newoplaw) — §§4.8–4.9.
   Why: Guard and reviewer preserve evidence anchors and prohibit invented results. That checks fidelity, not whether the supplied material still applies or whether the reader can distinguish a documented result, a hypothetical example and an endorsement. The writing structure calls for positive evaluation, which can omit material limitations even without introducing new facts.
   Fix: Ask the contributor for release or revision context and evidence for significant claims, flag unverified behavior, and distinguish demonstrated limitations and editorial judgments from factual instructions; do not install or execute the subject Skill.
3. **Validate the final headline, not just the outline direction** [model+map+trace]

   Map nodes: `head.headline`, `wx.title-length`, `wx.title-accurate`, `wx.title-no-bait`.
   Source: [Google’s people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) — descriptive, non-exaggerated headings; [WeChat Official Platform Operating Rules](https://mp.weixin.qq.com/mp/opshowpage?action=newoplaw) — §§4.11 and 4.21; [WeChat draft API](https://developers.weixin.qq.com/doc/subscription/api/draftbox/draftmanage/api_draft_add.html) — title limit for that route.
   Why: The outline gets a title direction and the reviewer removes exaggeration generally. The file-name guard sanitizes names, but it neither compares the article’s final heading with the reviewed body nor checks a platform headline limit.
   Fix: Before writing the file, compare its headline to the reviewed body, remove unsupported hooks and flag titles that exceed a known target-route limit.
4. **Carry source attribution and reuse choices through to the final copy** [model+map]

   Map nodes: `fact.cite-sources`, `rights.permissions`, `rights.attribution`, `head.byline`, `comp.honest-authorship`.
   Source: [SPJ Code of Ethics](https://www.spj.org/spj-code-of-ethics/) — identify sources and credit material; [O*NET Database](https://www.onetcenter.org/database.html) — 27-3041.00, arrange for copyright permissions; [Google’s people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) — byline and author information.
   Why: Keeping URLs and separating reference structures from factual sources prevents some copying. It does not say how to attribute a borrowed code example or screenshot, confirm that reuse is allowed, or identify the actual author when using the prescribed collective voice.
   Fix: Check what the user has permission to reproduce, attach source credit at the point of reuse, and ask for a byline or author context rather than assuming it.
5. **Have the operator review the finished article before publication** [map]

   Map nodes: `publish.approval`, `edit.second-reader`, `wx.no-templated-or-automated`.
   Source: [O*NET Database](https://www.onetcenter.org/database.html) — 27-3043.00, submit work for approval; [Purdue OWL](https://owl.purdue.edu/owl/general_writing/the_writing_process/proofreading/index.html) — ask someone else to read the draft; [WeChat Official Platform Operating Rules](https://mp.weixin.qq.com/mp/opshowpage?action=newoplaw) — §§3.27–3.28.
   Why: The operator approves the outline and the agent reviews the draft. Neither amounts to a human reviewing or contributing to the finished piece. A reusable article structure is not itself a violation, and the Skill does not post repeatedly.
   Fix: Recommend a human editorial pass at handoff for original contributions and release approval, without adding a platform publishing step.
6. **Ask about commercial relationships before presenting recommendations** [model+map]

   Map nodes: `comp.conflicts`, `comp.sponsored-disclosure`, `wx.ad-label`.
   Source: [SPJ Code of Ethics](https://www.spj.org/spj-code-of-ethics/) — disclose conflicts and label sponsorship; [WeChat Official Platform Operating Rules](https://mp.weixin.qq.com/mp/opshowpage?action=newoplaw) — §4.20, third-party commercial marketing.
   Why: The normal case is an instructional piece, not an ad; neither the draft route nor the five review rules distinguishes an independent article from a paid recommendation.
   Fix: Ask for any relevant relationships and carry the applicable plain-language or advertising disclosure into the Markdown.
7. **Review screenshots and linked assets before handoff** [model+map+trace]

   Map nodes: `visual.select`, `visual.captions`, `visual.layout`, `comp.privacy`, `wx.personal-data`, `wx.sensitive-images`.
   Source: [O*NET Database](https://www.onetcenter.org/database.html) — 27-3042.00, select illustrations and lay out material; [ESCO](https://esco.ec.europa.eu) — write captions; [SPJ Code of Ethics](https://www.spj.org/spj-code-of-ethics/) — weigh consequences of amplifying personal information; [WeChat Official Platform Operating Rules](https://mp.weixin.qq.com/mp/opshowpage?action=newoplaw) — §§4.16 and 4.26 and the private-information rule.
   Why: A reference example proposes an image, but there is no route from that placeholder to checking that an asset exists, illustrates the step, has a caption or alt text, and does not expose private material. This is conditional on an article using supplied evidence images, not a request to upload them.
   Fix: If the Markdown uses images, check the referenced assets, captions and redactions and resolve missing references before delivery.
8. **Keep the tutorial usable without funneling readers to another account** [map]

   Map nodes: `wx.read-original-link`, `wx.no-external-diversion`.
   Source: [WeChat draft API](https://developers.weixin.qq.com/doc/subscription/api/draftbox/draftmanage/api_draft_add.html) — original source URL; [WeChat Official Platform Operating Rules](https://mp.weixin.qq.com/mp/opshowpage?action=newoplaw) — withholding content to direct readers elsewhere.
   Why: The structure calls for practical steps and the guard preserves source URLs. Neither distinguishes legitimate dependency links from a call to leave the article for an otherwise missing explanation. The platform original-link field remains outside the local-file route.
   Fix: Check that linked project files are supplemental and the in-body explanation is complete.

### Minor

1. **Add a separate final prose and cohesion read** [map]

   Map nodes: `revise.structure-cohesion`, `edit.copyedit`, `edit.proofread-method`.
   Source: [Purdue OWL: The Writing Process](https://owl.purdue.edu/owl/general_writing/the_writing_process/index.html) — developing an outline, proofreading and revising; [ESCO](https://esco.ec.europa.eu) — proofread text.
   Why: There is a full reread, but it checks the five style rules and fidelity; they do not explicitly cover broken section transitions or general spelling, punctuation and grammar.
2. **Carry unresolved source questions forward without saving more draft files** [map]

   Map node: `research.notes`.
   Source: [BBC Editorial Guidelines, §3](https://www.bbc.co.uk/editorialguidelines/guidelines) — note-taking.
   Why: The reference loader can surface missing information and the guard records input identity, but there is no durable link from ambiguous claims in the final handoff to source questions or their disposition.

## Unsourced findings

None.

## Evidence limitations

Instructions, delegated rules and references, and the guard’s validation code were read at the pinned revision. No target code, scraper, installation command, example or WeChat account was used. The guard’s semantic review attestation is not evidence of an actual independent review.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Route request and read inputs | Explicit facts and separate style references | Outline or standalone review | Root SKILL.md:30–38 and 75–94 define the boundary; the guard records declared input hashes. |
| Prepare and approve outline | Approved angle and section plan | In-context draft | wechat-rewriter/SKILL.md:51–74 blocks drafting before approval. |
| Draft and review | Revised Markdown body and review attestation | Validation and final write | wechat-reviewer/SKILL.md:27–62 rereads for rule and fact preservation but does not render or explicitly revalidate the title against the body. |
| Validate, write, hand off | Single final file and outcome | User | workflow_guard.py:871–948 checks required URLs, code and terms before writing; no final human review is requested. |
| Standalone capture or import | Local source or reference | Explicitly requested future work only | Root SKILL.md:12–28 separates import from writing; no automatic edit or publishing handoff. |

## Map table

| Node | State | Evidence |
|---|---|---|
| topic.ideas | not-applicable | User supplies the Skill to cover. |
| topic.purpose | covered | `references/规则结构说明.md:9` — "从痛点切入" defines how the draft establishes why it exists. |
| topic.subject-form | not-applicable | Submissions are preselected research Skills in a fixed how-to format. |
| topic.news-judgement | not-applicable | Not a current-events desk. |
| topic.brief | covered | `wechat-rewriter/SKILL.md:62` — "用户明确确认大纲后再继续" gates further work on agreement. |
| topic.people-first | covered | `references/规则结构说明.md:71` — "需要引入具体实操案例" requires a worked example tied to a reader task. |
| topic.plan-schedule | not-applicable | No commissioning calendar or release deadline. |
| audience.define | covered | `wechat-rewriter/SKILL.md:49` — "默认读者是正在使用 AI 的硕博生" identifies the audience and tells the writer what vocabulary to assume. |
| audience.tone-medium | covered | `wechat-rewriter/SKILL.md:49` — "可直接使用常见 AI、科研和 Skill 术语" ties level to the intended readers. |
| audience.research | not-applicable | Writes for an assigned audience; no readership research brief. |
| research.background | covered | `wechat-rewriter/SKILL.md:46` — "明确指定的 Skill 材料" is read in full to gather the supplied factual background before writing. |
| research.consult-sources | covered | `wechat-rewriter/SKILL.md:46–47` — "材料有链接时读取链接内容"; original facts and stylistic references are kept separate. |
| research.interviews | not-applicable | No interview reporting. |
| research.source-network | not-applicable | No contact or source development. |
| research.online-third-party | shallow | `wechat-rewriter/SKILL.md:46` — "材料有链接时读取链接内容" but does not assess who controls the material or its reliability. |
| research.notes | shallow | `references/SKILL.md:46` — "向用户说明的信息缺口"; flags questions early but does not preserve provenance notes through handoff. |
| research.anonymous-sources | not-applicable | No anonymous sourcing. |
| research.technical-subject | covered | `wechat-rewriter/SKILL.md:31` — technical details "必须来自用户提供的材料"; the agent reads the specifications and asks for missing details. |
| structure.outline | covered | `wechat-rewriter/SKILL.md:53` — "正文前必须先输出大纲". |
| structure.main-point | covered | `references/规则结构说明.md:9` — "两句话说清楚即可" makes the pain point explicit before the project explanation. |
| structure.select-material | covered | `references/SKILL.md:25` — "三至四个实操步骤" follow the order of the research workflow, with a single-step exception. |
| structure.length-format | covered | `references/SKILL.md:26` — "两段、四至五句话的结尾" sets length and structure alongside the intro and body guidance. |
| structure.context | covered | `references/SKILL.md:23–24` — "安装方法与兼容性说明" accompanies project purpose and use cases. |
| draft.first-draft | covered | `wechat-rewriter/SKILL.md:66` — "严格按照已确认大纲写作" directs drafting before review. |
| draft.complete-coverage | covered | `wechat-rewriter/SKILL.md:59` — "安装与实操步骤的安排" is required in the outline before drafting the full tutorial. |
| draft.first-hand | shallow | `wechat-rewriter/SKILL.md:71` — "不编造安装结果、运行结果" guards against invention but does not distinguish supplied observations from illustrative examples. |
| draft.opinion-labelled | shallow | `references/规则结构说明.md:73` — "从积极方面进行评价" tells the writer to evaluate but not to label opinions separately. |
| draft.blog-commentary | covered | `references/SKILL.md:22` — "两句话内完成的痛点开头" specifies the short, direct form for the account article. |
| draft.press-release | not-applicable | Not a press release. |
| revise.rewrite | covered | `wechat-reviewer/SKILL.md:42` — "非必要列举改为直接陈述" gives a concrete revision rule. |
| revise.requirements | covered | `wechat-reviewer/SKILL.md:40` — "按 `规则.md` 的顺序检查并直接修正". |
| revise.feedback | covered | `wechat-rewriter/SKILL.md:62` — "先更新大纲并再次确认" on user changes; prior user feedback is loaded. |
| revise.structure-cohesion | shallow | `wechat-rewriter/SKILL.md:66` — "严格按照已确认大纲写作"; no separate pass for final transitions or order. |
| revise.consistency | covered | `wechat-rewriter/SKILL.md:45` — "应用已有反馈" along with repeated rules for terminology and voice across articles. |
| fact.verify | shallow | `wechat-reviewer/SKILL.md:31` — "事实、数字和专有名词" must match supplied material, whose continuing applicability is not established. |
| fact.statistics | not-applicable | The tutorial does not commission research or require statistical reporting. |
| fact.corroborate | absent | Cites user material as the only factual source; no second-source check. |
| fact.authenticity | shallow | `workflow_guard.py:873–879` — "manifest = extract_fact_manifest(source)" in a validator that compares the output to a declared snapshot; it does not authenticate the upstream source. |
| fact.rumour | not-applicable | No rumor reporting. |
| fact.cite-sources | shallow | `wechat-reviewer/SKILL.md:54` — "URL、英文名称、命令、参数" are checked for preservation, but individual claims need not be credited. |
| fact.right-of-reply | not-applicable | No allegations or investigative reporting. |
| fact.not-misleading | shallow | `wechat-reviewer/SKILL.md:55` — "没有新增未经材料支持的事实"; no overall impression or omissions check. |
| fact.expert-review | not-applicable | Scope is a tutorial from user-supplied specifications, not independent expert validation. |
| edit.copyedit | shallow | `wechat-reviewer/SKILL.md:43` — "把中文“技能”改为 `skill`" is a terminology correction, not general copy editing. |
| edit.proofread-method | shallow | `wechat-reviewer/SKILL.md:52` — "重新读取完整终稿" specifies a second pass, but for the same narrow rules. |
| edit.second-reader | absent | The final text is reread by the workflow agent, not handed to a second reader. |
| edit.style-standards | covered | `wechat-reviewer/SKILL.md:23` — "五项规则不可跳过、放宽" governs the required review pass. |
| head.headline | shallow | `wechat-rewriter/SKILL.md:55` — "标题方向" enters the outline, but the headline is not separately checked after body revisions. |
| head.metadata-seo | not-applicable | No discoverability metadata is produced. |
| head.byline | absent | No author credit is written into the article. |
| visual.select | shallow | `references/规则结构说明.md:83` — "{这部分是图片展示}" models a screenshot slot without directing how to pick the asset. |
| visual.captions | absent | No caption or alternate-text step for evidence images. |
| visual.edit-integrity | not-applicable | No workflow to generate or retouch images. |
| visual.layout | shallow | `references/SKILL.md:32` — "段落长度" is an input to layout, but the final Markdown with optional images is not rendered for review. |
| rights.permissions | absent | Does not confirm permission to reproduce third-party assets or excerpts in the article. |
| rights.attribution | shallow | `references/SKILL.md:36` — "不得复制参考文章的句子" restricts reuse from style references, but does not require point-of-use credit for factual material or examples. |
| rights.own-copyright | not-applicable | No registration. |
| rights.commission-terms | not-applicable | No agreement or payments. |
| publish.format-upload | not-applicable | Markdown delivery precedes platform rendering and upload. |
| publish.stale-check | not-applicable | No deferred publication; accuracy before handoff is assessed separately. |
| publish.approval | not-applicable | The user approves the outline, not release; release is outside scope. |
| publish.schedule | not-applicable | No release schedule. |
| publish.promote | not-applicable | No distribution. |
| feedback.* | not-applicable | A local opt-in rewrite log is not management of published articles or reader feedback. |
| comp.minimize-harm | not-applicable | Software tutorials, not reporting on named people. |
| comp.privacy | absent | No check for personal information in screenshots or supplied examples. |
| comp.vulnerable-subjects | not-applicable | No reporting about vulnerable people. |
| comp.conflicts | absent | No inquiry about a relationship with the featured project. |
| comp.sponsored-disclosure | absent | No requirement to mark sponsored recommendations in the draft. |
| comp.stereotypes | not-applicable | How-to scope does not require reporting on groups. |
| comp.law | not-applicable | No general press-law or release workflow; asset rights and applicable platform content rules are assessed separately. |
| comp.ai-disclosure | absent | No instruction to disclose AI assistance in the article. |
| comp.ai-accuracy | covered | `wechat-reviewer/SKILL.md:54–55` — "没有新增未经材料支持的事实"; review compares generated copy with named inputs. |
| comp.honest-authorship | shallow | `wechat-reviewer/SKILL.md:45` — "无依据的作者身份自居" is disallowed, but the skill does not ask whose first-hand voice the prescribed collective narrator represents. |
| wx.title-length | absent | File-name normalization is not a platform title length check. |
| wx.title-accurate | shallow | `wechat-rewriter/SKILL.md:55` — "标题方向" is approved before the full text exists. |
| wx.title-no-bait | shallow | `wechat-reviewer/SKILL.md:42` — "删除比喻、拟人、夸张" limits exaggeration but has no explicit headline bait check. |
| wx.cover-set-crop | not-applicable | No cover delivered or configured. |
| wx.cover-quality | not-applicable | No cover delivered or configured. |
| wx.summary-author-fields | not-applicable | No WeChat summary or account author field. |
| wx.read-original-link | shallow | `wechat-rewriter/SKILL.md:70` — "保留材料中的事实、URL" preserves body URLs but does not distinguish legitimate sources from incomplete content leading off-platform; the metadata field itself is out of scope. |
| wx.topic-tags | not-applicable | No platform topic tag. |
| wx.body-limits | not-applicable | Markdown text only; actual WeChat HTML payload is not produced. |
| wx.body-images | not-applicable | No platform image upload or draft packaging. |
| wx.layout-readability | not-applicable | No platform-specific typesetting promised; Markdown readability assessed separately. |
| wx.no-hidden-or-stuffed-text | not-applicable | No platform HTML or search-optimized text; the Markdown workflow does not insert hidden elements. |
| wx.sensitive-images | absent | Optional article illustrations have no sensitive-image review. |
| wx.original-eligibility | not-applicable | No original declaration. |
| wx.original-precheck | not-applicable | No send-time check. |
| wx.reprint-official-path | not-applicable | Extraction and reference import do not reprint a public article. |
| wx.reprint-whitelist | not-applicable | No account settings. |
| wx.no-washing | covered | `references/SKILL.md:36` — "不得复制参考文章的句子、事实、数据" separates style from the source of article facts; the drafting route requires explicit factual inputs. |
| wx.complaint-response | not-applicable | No post-release operations. |
| wx.ad-label | absent | No instruction to label promotional copy if it is sponsored. |
| wx.overmarketing | shallow | `wechat-reviewer/SKILL.md:36` — "没有的功能、结果或判断" cannot be added; no check for a one-sided promotional result built from supplied material. |
| wx.finance-claims | not-applicable | No investment advice or promotion in this tutorial brief. |
| wx.source-labelling | not-applicable | No current-affairs content. |
| wx.ai-label | absent | No reader-facing label for generated prose. |
| wx.no-templated-or-automated | shallow | `SKILL.md:39` — "等待明确确认" gives a human outline gate but does not require a final human contribution or review. |
| wx.no-induced-share-follow | not-applicable | The prescribed article ending summarizes the tool and practical caveats, not an engagement gate. |
| wx.no-external-diversion | shallow | `references/规则结构说明.md:71` — "具体实操案例" encourages in-body substance but does not check if links are used to withhold essential instructions. |
| wx.false-info | shallow | `wechat-rewriter/SKILL.md:71` — "不编造安装结果、运行结果" protects against fabricated results, not stale or unsupported upstream claims. |
| wx.personal-data | absent | No check for personal data in final copy or referenced example images. |
| wx.legal-red-lines | not-applicable | Subject is a technical how-to, not material on topics such as public maps or prohibited speech; privacy and advertising rules assessed separately. |
| wx-send.* | not-applicable | No platform account, transmitted draft, send or post-release operations. |

counts: covered 23, shallow 23, absent 14, not-applicable 58, undetermined 0

## Excluded by profile

None.
