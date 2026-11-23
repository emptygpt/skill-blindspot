# Blindspot report: baoyu-post-to-wechat

Skill under audit: [baoyu-post-to-wechat](https://github.com/JimLiu/baoyu-skills/tree/bf1ff076e25f8da4a339eb1c8cf03361fea5ea4c/skills/baoyu-post-to-wechat).

Map: wechat-article 0.1.0 extends writing 0.1.0    Profile: none    Date: 2026-11-23

## Scope
- Takes provided WeChat content; selects an account, packages the content, and stores a draft or submits where the route supports it.
- Includes platform-facing metadata, page rendering and supported submission settings.
- Does not originate or fact-check the supplied article, or manage post-release editorial results.

## Step 2 list (before opening the map nodes)

- Looked for originality/reprint handling, promotional disclosures, and a deliberate final preview; the workflow calls out metadata and browser checks but these platform-specific gates need scrutiny.

## Findings

### Needed

None.

### Worth considering

1. **Add a deliberate presubmit review for rendered pages** [model+map+trace]

   Map nodes: `head.headline`, `head.metadata-seo`, `visual.select`, `publish.approval`, `wx.title-length`, `wx.title-accurate`, `wx.title-no-bait`, `wx.cover-set-crop`, `wx.cover-quality`, `wx.topic-tags`, `wx.body-limits`, `wx.no-hidden-or-stuffed-text`, `wx.sensitive-images`.
   Source: [ESCO classification, skills of journalist, blogger, advertising copywriter, newspaper editor, web content manager, writer and technical communicator](https://esco.ec.europa.eu) — keywords in digital content; write headlines.
   Source: [O*NET 30.0 Database, task statements for writing-related occupations (27-3043.00, 27-3043.05, 27-3041.00, 27-3042.00, 27-3023.00, 27-3031.00)](https://www.onetcenter.org/database.html) — 27-3042.00 task: Select photographs, drawings, sketches, diagrams, and charts to illustrate material.; 27-3043.00 task: Edit or rewrite existing written material as necessary, and submit written material for approval by supervisor, editor, or publisher..
   Source: [新增草稿 (微信开放文档 / 公众号-服务端 / 草稿管理)](https://developers.weixin.qq.com/doc/subscription/api/draftbox/draftmanage/api_draft_add.html) — 图文消息的封面图片素材id（必须是永久MediaID）; 必须少于2万字符，小于1M，且此处会去除JS; 标题，总长度不超过32个字。.
   Source: [微信公众平台运营规范](https://mp.weixin.qq.com/mp/opshowpage?action=newoplaw) — 3.18 违规使用话题标签能力; 4.11 煽动、夸大、误导类内容; 4.26 不适宜直接展示内容; 关键词堆砌; 违规擦边（如低俗擦边、标题党擦边）、使用了生僻字/绕过字体形式对抗等的标题.
   Source: [微信公众号和服务号推荐运营规范](https://mp.weixin.qq.com/cgi-bin/announce?action=getannouncement&key=11697600328G0Tbo&version=1&lang=zh_CN&platform=2) — 封面图人物不完整、存在明显标记，或者画质不清等.
   Why: Draft handling and metadata fallbacks make a payload, but do not verify that title, crop, metadata and body look right on the target surface.
   Fix: Preview the package, check applicable title and body limits, and obtain confirmation before an actual send.
2. **Route reused content through a rights and originality check** [model+map]
   Map nodes: `rights.permissions`, `rights.attribution`, `wx.original-eligibility`, `wx.original-precheck`, `wx.reprint-official-path`, `wx.reprint-whitelist`, `wx.no-washing`, `wx.source-labelling`.
   Source: [O*NET 30.0 Database, task statements for writing-related occupations (27-3043.00, 27-3043.05, 27-3041.00, 27-3042.00, 27-3023.00, 27-3031.00)](https://www.onetcenter.org/database.html) — 27-3041.00 task: Arrange for copyright permissions..
   Source: [SPJ Code of Ethics (Society of Professional Journalists)](https://www.spj.org/spj-code-of-ethics/) — Never plagiarize. Always attribute..
   Source: [微信公众平台运营规范](https://mp.weixin.qq.com/mp/opshowpage?action=newoplaw) — 3.6.1 文章滥用原创声明; 4.1.3原创性存在争议; 4.24 信息资讯未标注信息来源.
   Source: [微信公众平台文章原创保护指引](https://mp.weixin.qq.com/cgi-bin/announce?action=getannouncement&key=11565151480ZCKVy&version=1&lang=zh_CN&platform=2) — 5.4.1 别的帐号想要转载我的文章，让我给开白，我要怎么操作呢？; 5.4.3 如何正确转载他人的原创文章; （事前）群发撞库流程.
   Why: The user can provide source links, but those do not establish permission or determine which reprint or originality option is appropriate.
   Fix: Ask about rights and prior publication; record attribution and direct only eligible content to the corresponding platform workflow.
3. **Review applicable platform rules before packaging or sending** [model+map]
   Map nodes: `comp.sponsored-disclosure`, `comp.ai-disclosure`, `wx.ad-label`, `wx.overmarketing`, `wx.finance-claims`, `wx.ai-label`, `wx.no-templated-or-automated`, `wx.no-induced-share-follow`, `wx.no-external-diversion`, `wx.false-info`, `wx.personal-data`, `wx.legal-red-lines`.
   Source: [SPJ Code of Ethics (Society of Professional Journalists)](https://www.spj.org/spj-code-of-ethics/) — Prominently label sponsored content and partnerships..
   Source: [BBC Editorial Guidelines 2025 (section index and Section 3: Accuracy, Guidelines)](https://www.bbc.co.uk/editorialguidelines/guidelines) — Any use of AI by the BBC must be transparent and clear to the audience..
   Source: [微信公众平台运营规范](https://mp.weixin.qq.com/mp/opshowpage?action=newoplaw) — 3.27 非真人自动化创作行为; 3.29.4 财经利诱类; 3.3.1 诱导分享; 4.12 违反国家法律法规禁止的内容; 4.20 第三方商业营销内容违规; 4.8 过度营销类内容; 4.9 不实信息类内容; 发布生成式人工智能生成合成内容时，必须依据法律法规进行显著标识; 发表不完整内容，并通过二维码、文字、链接、图标等形式，引导用户跳转至其他内容; 未经授权发送他人身份证号码、照片等个人隐私资料.
   Why: The link conversion covers one presentation concern, not a policy check for promotional, AI-assisted, or otherwise restricted content. Exact required checks depend on the content and selected route.
   Fix: Make the operator confirm applicable disclosures and red flags before save or send, and identify checks that must be done manually.
4. **Check final-send controls where the route can submit** [map]

   Map nodes: `wx.mass-send-limit`, `wx.recommendation-setting`.
   Source: [微信公众平台文章原创保护指引](https://mp.weixin.qq.com/cgi-bin/announce?action=getannouncement&key=11565151480ZCKVy&version=1&lang=zh_CN&platform=2) — 当天群发次数已经用完了，请第二天再群发.
   Source: [微信公众号和服务号推荐运营规范](https://mp.weixin.qq.com/cgi-bin/announce?action=getannouncement&key=11697600328G0Tbo&version=1&lang=zh_CN&platform=2) — 创作者可选择是否允许内容被推荐.
   Why: API runs end at a draft, but the image-text browser path exposes submission; the route does not explicitly surface account send limits or recommendation choices.
   Fix: For a route that submits, show the account's applicable send and recommendation settings before confirmation; leave draft-only paths alone.

### Minor

None.

## Unsourced findings

None.

## Evidence limitations

No account, preferences, credentials or supplied article were used. Bundled routes and scripts were read as evidence; no target code was run, and no draft or post was sent.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Select route and account | Explicit publishing context | Metadata and packaging | SKILL.md:91–162 and references/multi-account.md:44–62 resolve account and access. |
| Render and pack | Metadata and WeChat-ready content | Draft or submit path | SKILL.md:164–219 guards missing API covers but does not require a rendered editorial preview. |
| Save or submit | Draft ID or browser result | User handoff | SKILL.md:221–223 names API output as a draft, not a sent article. |

## Map table

| Node | State | Evidence |
|---|---|---|
| topic.* | not-applicable | The supplied copy is not commissioned, investigated, rewritten, or independently fact-checked by this publisher. |
| audience.* | not-applicable | The supplied copy is not commissioned, investigated, rewritten, or independently fact-checked by this publisher. |
| research.* | not-applicable | The supplied copy is not commissioned, investigated, rewritten, or independently fact-checked by this publisher. |
| structure.* | not-applicable | The supplied copy is not commissioned, investigated, rewritten, or independently fact-checked by this publisher. |
| drafting.* | not-applicable | The supplied copy is not commissioned, investigated, rewritten, or independently fact-checked by this publisher. |
| revision.* | not-applicable | The supplied copy is not commissioned, investigated, rewritten, or independently fact-checked by this publisher. |
| factcheck.* | not-applicable | The supplied copy is not commissioned, investigated, rewritten, or independently fact-checked by this publisher. |
| editing.* | not-applicable | The supplied copy is not commissioned, investigated, rewritten, or independently fact-checked by this publisher. |
| head.headline | shallow | SKILL.md:170–177 — provides or derives a title; does not compare a supplied title to the text or flag sensational labels. |
| head.metadata-seo | shallow | SKILL.md:168–177 — handles descriptive metadata, not SEO term selection. |
| head.byline | covered | SKILL.md:168–177,221–223 — resolves summary and author from supplied metadata or defined fallbacks. |
| visual.select | shallow | SKILL.md:179; scripts/wechat-api.ts:799–843 — selects a supported cover or first body image; does not review the resulting crop or image suitability. |
| visual.captions | not-applicable | Does not author captions or edit images editorially; conversion is technical. |
| visual.edit-integrity | not-applicable | Does not author captions or edit images editorially; conversion is technical. |
| visual.layout | covered | SKILL.md:164–167,181–187,212–219 — applies themes and renders and inserts content according to the route. |
| rights.permissions | absent | The publishing routes do not distinguish rights-cleared original work from authorized reprints or prevent misleading originality claims. |
| rights.attribution | shallow | SKILL.md:175,187,205–210 — carries ordinary links into citations and a source URL, but does not require source labels from the user for reused work. |
| rights.own-copyright | not-applicable | No registration or commercial agreement. |
| rights.commission-terms | not-applicable | No registration or commercial agreement. |
| publish.format-upload | covered | SKILL.md:113–122,181–223 — routes input to the correct uploader and identifies the API output as a saved draft. |
| publish.stale-check | not-applicable | Packages or submits current input; no publication schedule, delayed editorial cycle or promotion. |
| publish.approval | shallow | SKILL.md:221–223 and references/image-text-posting.md:5–30 — drafts and explicit submission are distinct; no stated final editorial preview gate. |
| publish.schedule | not-applicable | Packages or submits current input; no publication schedule, delayed editorial cycle or promotion. |
| publish.promote | not-applicable | Packages or submits current input; no publication schedule, delayed editorial cycle or promotion. |
| feedback.* | not-applicable | No post-release operations or monetization. |
| comp.minimize-harm | not-applicable | No substantive editorial or authorship verification; platform submission checks are accounted for separately. |
| comp.privacy | not-applicable | No substantive editorial or authorship verification; platform submission checks are accounted for separately. |
| comp.vulnerable-subjects | not-applicable | No substantive editorial or authorship verification; platform submission checks are accounted for separately. |
| comp.conflicts | not-applicable | No substantive editorial or authorship verification; platform submission checks are accounted for separately. |
| comp.sponsored-disclosure | absent | No decision point checks the supplied article against the applicable publication policies. |
| comp.stereotypes | not-applicable | No substantive editorial or authorship verification; platform submission checks are accounted for separately. |
| comp.law | not-applicable | No substantive editorial or authorship verification; platform submission checks are accounted for separately. |
| comp.ai-disclosure | absent | No decision point checks the supplied article against the applicable publication policies. |
| comp.ai-accuracy | not-applicable | No substantive editorial or authorship verification; platform submission checks are accounted for separately. |
| comp.honest-authorship | not-applicable | No substantive editorial or authorship verification; platform submission checks are accounted for separately. |
| wx.title-length | absent | Metadata validation does not ask the operator to check the title constraint or optional topic classification. |
| wx.title-accurate | shallow | SKILL.md:170–177 — provides or derives a title; does not compare a supplied title to the text or flag sensational labels. |
| wx.title-no-bait | shallow | SKILL.md:170–177 — provides or derives a title; does not compare a supplied title to the text or flag sensational labels. |
| wx.cover-set-crop | shallow | SKILL.md:179; scripts/wechat-api.ts:799–843 — selects a supported cover or first body image; does not review the resulting crop or image suitability. |
| wx.cover-quality | shallow | SKILL.md:179; scripts/wechat-api.ts:799–843 — selects a supported cover or first body image; does not review the resulting crop or image suitability. |
| wx.summary-author-fields | covered | SKILL.md:168–177,221–223 — resolves summary and author from supplied metadata or defined fallbacks. |
| wx.read-original-link | covered | SKILL.md:175,205–210 — accepts and passes the source link as WeChat metadata. |
| wx.topic-tags | absent | Metadata validation does not ask the operator to check the title constraint or optional topic classification. |
| wx.body-limits | shallow | SKILL.md:115,183–185; scripts/wechat-api.ts:759–763 — has image-count/format and digest checks, not a full article payload length check. |
| wx.body-images | covered | SKILL.md:113–122,181–187 — supports multiple images and instructs conversion of unsupported body images. |
| wx.layout-readability | covered | SKILL.md:164–167,181–187,212–219 — applies themes and renders and inserts content according to the route. |
| wx.no-hidden-or-stuffed-text | absent | No publication-time rendered check for problematic text or images. |
| wx.sensitive-images | absent | No publication-time rendered check for problematic text or images. |
| wx.original-eligibility | absent | The publishing routes do not distinguish rights-cleared original work from authorized reprints or prevent misleading originality claims. |
| wx.original-precheck | absent | The publishing routes do not distinguish rights-cleared original work from authorized reprints or prevent misleading originality claims. |
| wx.reprint-official-path | absent | The publishing routes do not distinguish rights-cleared original work from authorized reprints or prevent misleading originality claims. |
| wx.reprint-whitelist | absent | The publishing routes do not distinguish rights-cleared original work from authorized reprints or prevent misleading originality claims. |
| wx.no-washing | absent | The publishing routes do not distinguish rights-cleared original work from authorized reprints or prevent misleading originality claims. |
| wx.complaint-response | not-applicable | No post-release operations or monetization. |
| wx.ad-label | absent | No decision point checks the supplied article against the applicable publication policies. |
| wx.overmarketing | absent | No decision point checks the supplied article against the applicable publication policies. |
| wx.finance-claims | absent | No decision point checks the supplied article against the applicable publication policies. |
| wx.source-labelling | shallow | SKILL.md:175,187,205–210 — carries ordinary links into citations and a source URL, but does not require source labels from the user for reused work. |
| wx.ai-label | absent | No decision point checks the supplied article against the applicable publication policies. |
| wx.no-templated-or-automated | absent | No decision point checks the supplied article against the applicable publication policies. |
| wx.no-induced-share-follow | absent | No decision point checks the supplied article against the applicable publication policies. |
| wx.no-external-diversion | shallow | SKILL.md:187,205–210 — converts Markdown links in the default flow, but HTML and explicitly retained links are not reviewed for promotional diversion. |
| wx.false-info | absent | No decision point checks the supplied article against the applicable publication policies. |
| wx.personal-data | absent | No decision point checks the supplied article against the applicable publication policies. |
| wx.legal-red-lines | absent | No decision point checks the supplied article against the applicable publication policies. |
| wx.draft-first | covered | SKILL.md:113–122,181–223 — routes input to the correct uploader and identifies the API output as a saved draft. |
| wx.publish-status | covered | SKILL.md:113–122,181–223 — routes input to the correct uploader and identifies the API output as a saved draft. |
| wx.api-eligibility | covered | SKILL.md:150–163; references/api-setup.md:5–35 — requires account credentials and checks the route's access requirements. |
| wx.mass-send-limit | absent | No explicit final-send quota or recommendation setting review for a route that can submit. |
| wx.recommendation-setting | absent | No explicit final-send quota or recommendation setting review for a route that can submit. |
| wx.comments-setting | covered | SKILL.md:58–60,205–209,221–223 — sends comment and fan-only preferences on the API route. |
| wx.comment-curation | not-applicable | No post-release operations or monetization. |
| wx.monetisation-features | not-applicable | No post-release operations or monetization. |
| wx.no-fake-engagement | not-applicable | No post-release operations or monetization. |
| wx.notices-appeals | not-applicable | No post-release operations or monetization. |

counts: covered 11, shallow 12, absent 23, not-applicable 72, undetermined 0

## Excluded by profile

None.
