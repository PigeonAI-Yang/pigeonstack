# PigeonStack：Codex 工作流

首先致敬并感谢 [Lauren Tan（poteto）](https://github.com/poteto)，[pstack](https://github.com/cursor/plugins/tree/99b609a72323b70204eab407c622f436e858e112/pstack) 的原作者。PigeonStack 基于她的工作，为这套 Codex 协作流程做了定制适配。

[English](README.md) | 简体中文

[文档](https://pigeonai-yang.github.io/pigeonstack/zh/) | [快速开始](https://pigeonai-yang.github.io/pigeonstack/zh/getting-started/) | [常见问题](#faq) | [问题反馈](https://github.com/PigeonAI-Yang/pigeonstack/issues)

<p align="center">
  <a href="https://github.com/PigeonAI-Yang/pigeonstack/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/PigeonAI-Yang/pigeonstack?style=flat-square&amp;logo=github" /></a>
  <a href="https://github.com/PigeonAI-Yang/pigeonstack/forks"><img alt="GitHub forks" src="https://img.shields.io/github/forks/PigeonAI-Yang/pigeonstack?style=flat-square&amp;logo=github" /></a>
  <a href="https://github.com/PigeonAI-Yang/pigeonstack/watchers"><img alt="GitHub watchers" src="https://img.shields.io/github/watchers/PigeonAI-Yang/pigeonstack?style=flat-square&amp;logo=github" /></a>
  <a href="#上游来源与许可"><img alt="Upstream MIT licenses" src="https://img.shields.io/badge/Upstream%20licenses-MIT-blue?style=flat-square" /></a>
</p>
<p align="center">
  <a href="https://pigeonai-yang.github.io/pigeonstack/zh/"><img alt="Website PigeonStack" src="https://img.shields.io/badge/Website-PigeonStack-7c3aed?style=flat-square" /></a>
  <a href="#一个任务如何完成"><img alt="Workflow Browse" src="https://img.shields.io/badge/Workflow-Browse-f59e0b?style=flat-square" /></a>
  <a href="https://github.com/PigeonAI-Yang/pigeonstack/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/PigeonAI-Yang/pigeonstack?style=flat-square&amp;logo=github" /></a>
  <a href="https://github.com/PigeonAI-Yang"><img alt="GitHub followers" src="https://img.shields.io/github/followers/PigeonAI-Yang?style=flat-square&amp;logo=github&amp;label=Follow%20author" /></a>
  <a href="https://x.com/KimbomArtist"><img alt="X KimbomArtist" src="https://img.shields.io/badge/X-KimbomArtist-000000?style=flat-square&amp;logo=x&amp;logoColor=white" /></a>
  <a href="https://www.xiaohongshu.com/user/profile/689af6b90000000019016082"><img alt="小红书 Dibo" src="https://img.shields.io/badge/%E5%B0%8F%E7%BA%A2%E4%B9%A6-Dibo-ff2442?style=flat-square&amp;logo=xiaohongshu&amp;logoColor=white" /></a>
</p>

**一套 Codex 工作配置：主代理默认亲自调查、实现和验证；只有用户明确要求时才调用子代理。**

PigeonStack 是 PigeonYang 维护的一套 Codex 工作配置，包含全局指令、Lauren Tan 的 pstack 定制版、Agent 角色定义、宿主配置和本地同步脚本。一个源码仓库让这些职责和已安装指令都能被一并审查。

工程注意事项保留在开发者对话或文档中。只有用户明确要求时，Agent 才会在交付的界面或面向客户的后端响应中添加免责声明。实际状态、错误和功能限制都要具体说明。

当前 Primary 默认亲自完成诊断、方案选择、实现、验证和最终验收，保留正在使用的模型与推理强度。子代理、咨询、审查和失败接管都需要用户在当前任务中明确要求。选择技能、任务复杂、失败或上下文压力都不会自动授权派发。获明确授权后，普通工作使用 Sol `medium`，Luna `max` 仅做简单重复的机械任务，关键设计和符合条件的接管保留 Astra 路径。

仓库交付的是指令、打包好的 Codex 插件和部署工具，不提供 MCP 服务或独立的自动调度器，也不会启动后台定时任务、常驻 Agent 或远程服务。仓库包含一个范围受限的 `SessionStart` 钩子；是否激活由宿主配置和信任状态决定。

## SessionStart 上下文钩子

只有当宿主事件中的会话和工作区与记录绑定一致时，`SessionStart` 钩子才会返回已保存任务记录的当前区域。它只加载已保存的任务上下文，不会排队或延迟消息。

源码还包含 `pstack/hooks/task_context.py`，供现有记录负责人读取并原位更新同一区域。更新使用整份记录的 SHA-256，保留区域外的字节，并归档完整旧正文。当前检查点建议保持简洁，以 4–8 KiB 为软目标。工具不会总结历史，也无法判断内容是否语义完整；它不会创建或验证 SessionStart 绑定。

当前正文上限仍为 16 KiB。Windows 包装器通过 `systemMessage` 报告读取故障。

2026-10-09 的检查点维护是版本 `0.15.13+codex.20261009checkpoint` 的历史证据。本地部署和安装文件核对均已通过，真实任务记录的读取、更新、归档和读回流程也已通过。该流程将当前区域从 29,370 字节缩减至 8,158 字节，并保留目标、权限、阻塞项及区域外历史。详见[历史检查点维护证据](pstack/ADAPTATION.md#current-checkpoint-maintenance-2026-10-09)。

当前源码版本为 `0.15.32+codex.20261026optin`；本次仅修改源码，部署需另行授权。2026-10-11 钩子验证时安装的版本为 `0.15.13+codex.20261011copy`。native reader 返回了完全一致的绑定当前正文，包括现有 `Pending` 状态。新的 Desktop 聊天运行了一次 `SessionStart`，失败次数为 0；它报告 index 无效诊断后继续。native 测试验证了临时记录绑定；Desktop 观察验证了启动，但未建立 `oneirloom` 的任务绑定。历史 Desktop `exit 1` 的原因仍未查明。详见[产品文案规则及 SessionStart 验证](pstack/ADAPTATION.md#product-copy-rules-and-sessionstart-verification-2026-10-11)。

钩子不会监控后续业务状态、拦截 Agent 派发或强制执行协调者提醒。详见[钩子契约](pstack/hooks/README.md)和[Codex 宿主适配](pstack/CODEX.md)。

## 从这里开始

PigeonStack 将 Codex 全局规则、Agent 角色、配置和适配后的 pstack 插件保存在 Git 中，再同步到 Codex 宿主。

首次检查时，先看[独立目录预览](#在独立目录中预览)，或阅读[快速开始指南](https://pigeonai-yang.github.io/pigeonstack/zh/getting-started/)。

不确定当前任务适合哪个 pstack 技能？可以询问 `/poteto-help`。它会阅读已打包的指南，推荐相关技能，也可以提供一条示例提示词。单纯询问帮助不会开始执行推荐的工作。Codex 的模型选择和权限遵循本仓库的 GPT 配置。

已验证的宿主是 Windows 与 PowerShell，同步脚本要求 Python 3.11 或更高版本。真正安装插件还需要兼容的 Codex CLI，以及已有的、能解析 `pstack@personal` 的本地插件市场注册。

- 在 Git 中维护 Codex 全局规则，并与源码一起审查改动。
- 默认由主代理直接执行；仅在用户明确要求代理协作时使用既有 Sol、Luna、Astra 分工。
- 保持维护中的源码、运行时文件和带版本的插件缓存同步。

## 为什么这样分工

如果每个子 Agent 都重新研究问题、自行决定修复方案，或者再找一个模型重复评审，多 Agent 协作就容易增加成本。如果把构建通过当成用户流程成功，交付结果也会失真。

PigeonStack 让一个主控默认亲自诊断、实现、验证，并对决策和最终验收负责。用户明确要求后，子 Agent 获取完成当前任务所需的上下文，执行边界明确的工作，再带回证据。独立任务可以并行，存在依赖或共用资源的操作则保留单一负责人。目标是用必要的最少改动交付完整、可验证的结果。

### 协调多个工作流

以下角色和协调规则仅适用于用户明确要求的代理协作或已指定团队，不要求普通任务使用子代理。

用户要求总控组织开发团队后，同一任务内的派工、回报、纠正和交接不再逐个代理、逐条消息请示。总控负责维护回报地址并随交接更新，Main 主动报告实质结果、阻塞和待决事项，省掉确认往返。不给其他代理发确认，不等于不给用户汇报：代理仍应简短说明处理了什么、当前进展和下一步，不能输出空回复；相关交流合并成一次有内容的汇报。版本 `0.15.13+codex.20261009team` 已部署到本地并核对安装文件，新会话中的实际行为仍待验证。详见[通信改动与验证边界](pstack/ADAPTATION.md#team-communication-and-user-visible-reports-2026-10-09)。

每个 Main 对完整任务负责到底，包括实现和真实验证，普通失败由它在自己的修复循环内解决。总控不反复检查中间补丁、不指定每条测试命令，也不逐次转发修复结果。Main 在任务完成，或遇到自己范围内无法解决的阻塞与决策时回报；总控审查最终证据，将具体验收差异交回同一个 Main 负责修正。用户指令、真实资源冲突和必须立即纠正的问题仍优先处理。用户持续获得有内容的进展汇报，不会收到空白最终回复。详见[COORDINATOR.md](pstack/COORDINATOR.md)；这些内容是行为指引，不是运行时强制能力。

| 角色 | 职责 | 建议的角色模型与推理强度 |
| --- | --- | --- |
| Primary 主控 | 默认亲自负责诊断、实现、验证、决策和最终验收。 | 建议默认值：`gpt-6.1-sol`，`high` |
| Luna 机械助手 | 仅处理输入、步骤固定且结果可直接核对的简单重复任务。 | `gpt-6-luna`，`max` |
| Sol 执行者 | 默认负责范围内的普通诊断、实现、重构、集成、检查、操作与文案；单独派发的咨询保持只读。 | `gpt-6.1-sol`，先用 `medium` |
| Astra 专家 | 关键架构、接口与数据契约、重大取舍，Sol `xhigh` 实际无法解决的问题，或当前任务明确选择。进展正常时继续，耗时本身不触发交接。 | `gpt-6-astra`，先用 `high` |

关键设计问题、Sol `xhigh` 实际报告无法解决的问题，或用户针对当前任务明确选择 Astra 模型时，可以进行 Astra 只读咨询。普通咨询从 Sol `medium` 开始，返回判断结果和执行说明，不负责应用实现。所有咨询和子 Agent 均由主控派发；接管任务使用明确指定模型和强度的通用执行角色。

这些名称表达的是本项目的模型使用策略和本机配置。实际可用模型、模型 ID、推理强度与费用取决于账号和 Codex 客户端。仓库没有提供速度提升、成本节省或跑分领先的实测承诺。

[MODELS.md](pstack/MODELS.md) 建议 Primary 角色默认使用 `gpt-6.1-sol`、`high`。仓库提交的[配置文件](config/workflow.toml)保留了当前显式选择的 `gpt-6-astra`、`high`。两者用途不同：修改任一文件都不会切换已运行的会话，模型标签也不能证明服务端内部的模型映射。当前任务明确指定的模型和强度优先于角色默认值。Sol 高级执行者是独立子 Agent，从 `medium` 开始；同一个未解决问题可依次进入 Sol `high`、`xhigh`，再到 Astra `high`、`xhigh`。

## 一个任务如何完成

主代理直接阅读相关证据、选择方案、实现修改，并验证约定结果，保留当前模型和推理强度。用户没有明确要求代理协作时，不创建探索、执行、审查或失败接管子代理。

```mermaid
flowchart TD
    P["当前 Primary"] --> D["直接调查、实现、验证并交付"]
    P -->|"用户明确要求代理协作"| G["范围明确的代理任务"]
    G --> S["普通工作使用 Sol medium"]
    G --> L["简单重复步骤使用 Luna max"]
    G --> A["关键设计或符合条件的接管使用 Astra high"]
    S --> R["成果和证据交回 Primary"]
    L --> R
    A --> R
```

获明确授权的代理遵循 [MODELS.md](pstack/MODELS.md)、单一资源负责人、新建子代理及既有证据驱动升级规则。升级顺序本身不会授权增加代理。咨询保持只读，ComputerUse 仍由主代理操作，图像工作继续串行。

例如报表导出出错时，主代理亲自诊断、修复和验证。用户明确要求 Sol 子代理后，才向其交付失败证据、预期行为、允许范围和检查。已确认字面替换的固定清单可交给 Luna，但同样需要明确的委派要求。

## 仓库里有什么

| 源码位置 | 用途 |
| --- | --- |
| [AGENTS.md](AGENTS.md) | 全局范围、授权、委派、调度与验收规则。 |
| [pstack/CODEX.md](pstack/CODEX.md) | Codex 工作流入口、工具转换、执行说明与部署约定。 |
| [pstack/MODELS.md](pstack/MODELS.md) | 模型 ID、推理强度与子 Agent 创建约定。 |
| [pstack/](pstack/) | 打包的 pstack 插件、选定技能、操作流程、上游资料和本地适配。 |
| [agents/](agents/) | `worker`、`poteto-agent` 与供可选咨询使用的只读 `astra-advisor` 兼容角色。 |
| [prompts/](prompts/) | 部署配置所引用的基础指令文件。 |
| [config/workflow.toml](config/workflow.toml) | PigeonStack 管理的配置白名单。 |
| [scripts/sync.py](scripts/sync.py) | 只读差异检查，以及带备份和回读验证的单向部署。 |

规则的归属明确：全局 `AGENTS.md` 管政策，`CODEX.md` 管宿主机制，`MODELS.md` 管模型 ID 和推理强度。随附技能为选中的步骤提供做法。上游技能的触发条件和角色默认值不能覆盖 Codex 宿主规则。

只加载当前决策需要的技能与参考资料。已知的局部修复不必重新做架构研究，闲聊和直接事实问答也不必启动完整流程。保留的部分上游内容仍使用 Cursor 工具名，或依赖可选的外部集成。[CODEX.md](pstack/CODEX.md) 说明宿主转换方式，[ADAPTATION.md](pstack/ADAPTATION.md) 记录适配边界。仓库保留的自动化示例仅作参考，未启用。

## 检查并适配源码

在你选择的目录中克隆仓库：

```powershell
git clone https://github.com/PigeonAI-Yang/pigeonstack.git
Set-Location pigeonstack
```

当前验证过的宿主环境是 Windows 与 PowerShell。同步脚本要求 Python 3.11 或更高版本。真正安装插件需要兼容的 Codex CLI，以及已经存在、能够解析 `pstack@personal` 的本地插件市场注册。多 Agent 执行还需要 Codex 环境提供原生子 Agent 工具，并且账号可以使用所选模型。

这是从个人实际使用环境整理出来的仓库，换机器时需要适配路径。将目标指向真实 Codex 目录之前，先检查这些位置：

- [scripts/sync.py](scripts/sync.py) 中的 `DEFAULT_HOME` 当前固定为 `J:/Users/yangda01/.codex`。
- [AGENTS.md](AGENTS.md)、[CODEX.md](pstack/CODEX.md) 和 [poteto-agent.toml](agents/poteto-agent.toml) 含有维护者机器上的源码或运行时路径。
- [config/workflow.toml](config/workflow.toml) 保留此仓库当前显式选择的 `gpt-6-astra`、`high`，以及 Agent 设置、角色文件和插件启用项。部署前确认需要采用的设置；修改源码文件不会切换已运行的会话。

脚本不会自动注册插件市场，也不是零配置安装器。`--codex-home` 参数不会重写指令中嵌入的所有路径。在其他位置正式安装前，需要修改维护中的源码，并适配已有的本地插件市场注册。

### 在独立目录中预览

在克隆后的仓库目录中，使用一个新的同级目录查看同步结果，避免直接指向日常使用的 `.codex`：

```powershell
python scripts/sync.py check --codex-home ../pigeonstack-preview-codex --skip-plugin-install
python scripts/sync.py deploy --codex-home ../pigeonstack-preview-codex --skip-plugin-install
python scripts/sync.py check --codex-home ../pigeonstack-preview-codex --skip-plugin-install
```

首次检查通常会报告差异，因为目标目录为空。部署会将受管理的文件和配置写入预览目录，最后一次检查在内容一致时返回 `status: ok`。非默认目标必须带 `--skip-plugin-install`，源码目录与目标目录不能重叠。

这个预览会跳过插件安装和已安装缓存检查。它验证的是文件副本和配置合并，不能证明插件已激活或模型协作行为已经生效。尚未适配的宿主路径仍会保留在复制后的指令里。

### 在已配置的宿主上部署

在维护者当前机器上，审查目标改动和已有的 `pstack@personal` 注册后，使用：

```powershell
Set-Location J:/PigeonYang/pigeonstack
python scripts/sync.py check
python scripts/sync.py deploy
python scripts/sync.py check
```

这些命令指向配置中的真实 Codex 目录，会更新全局指令和模型设置。在其他机器上采用同样的命令顺序前，先完成上面的路径与配置检查。

存在改动时，脚本复制受管理文件、合并白名单配置项，并将 `model_instructions_file` 指向目标目录里的基础提示文件。如果运行时或已安装缓存存在差异，还会调用：

```powershell
codex plugin add pstack@personal --json
```

随后脚本回读运行时文件和配置，并将安装后的插件文件与源码比较。插件安装可能在运行时文件已经写入后失败；需要查看错误与备份路径，不能将失败理解为自动回滚。

`check` 在内容一致时返回 `0`，存在差异时返回 `1`。参数无效或操作出错时返回 `2`。安装成功、文件一致只能证明磁盘状态；要确认完整协作行为在自己的宿主上成立，还需要在新的 Codex 会话中验证指令加载和实际模型路由。

## 只维护一份源码

维护者机器上的部署方向为：

```text
J:/PigeonYang/pigeonstack
    -> J:/Users/yangda01/.codex 中的受管理文件和 local-plugins/pstack
    -> 已安装的 pstack 插件缓存
```

修改源码仓库，运行时文件与安装缓存都作为部署副本。首次导入是一次快照，之后仍是单向同步。如果改动了运行时副本，需要先审查并明确带回源码，再做部署。

日常维护按以下顺序进行：

1. 修改维护中的源码，验证受影响的文件。
2. 涉及插件改动时，按照 `CODEX.md` 更新插件版本和已有插件市场的缓存版本标记。
3. 运行 `python scripts/sync.py check`，审查预期差异。
4. 部署已授权的改动。被覆盖的现有文件会备份到 `<codex-home>/backups/pigeonstack/`。
5. 再次运行 `check`，审查最终差异和相关行为证据，获得当前任务授权后提交。

内容未变化时，部署不会写入受管理文件，也不会新增备份。部署保留无关的已解析配置值，不删除运行时目录中的额外文件。已安装插件检查会报告缓存里的额外文件。受管理配置中不支持的多行值或复杂值会在写入运行时之前报错。

源码不包含实际凭据、对话历史或运行时状态。本地备份、认证信息、会话记录和生成的缓存应留在仓库之外。配置合并只管理明确列出的白名单，以及根据目标目录生成的 `model_instructions_file` 路径。

## 交付边界

规则要求保留用户改动和来源不明的文件，不自动暂存、重置或清理工作区。问题与诊断默认只读。技能不会扩大授权，发布、部署、提交、破坏性操作和向外部发送消息，都需要当前任务中的授权。

验收证据必须支持承诺的结果。构建通过、模拟测试、命令回执或子 Agent 报告，单独都不能证明实际业务流程成功。要声称某项行为成立，应通过现有 UI、CLI 或业务入口验证。服务不可用或访问被拒绝时，说明受影响的证据缺口，继续完成不依赖它的已授权工作。

优先通过现有入口推进已授权的正常业务流程。实际遇到或收到 BUG 报告时，保留足够的证据，在授权范围内定位并修复原因，再重跑受影响的真实业务流程并完成针对性回归。遇到问题就处理，不必等整个流程结束。仅阻塞受影响的操作及其依赖操作，继续推进独立且有效的工作。真实流程不可用时，明确说明尚未验证的结果。针对性回归不代表获准运行全量测试。

日常任务中，优先复用现有脚本、CLI 和业务入口。只有观察到已授权的实际需要，才为可重复的确定性工作增加最小工具。让负责该项工作的 Agent 能检查真实结果。升级模型前，先区分工具、反馈或环境缺口与推理失败。任务结束时，利用已收集的证据找出反复出现的问题，并以范围内最小的相关改动改进代码、工具、技能或规则。无关发现记入现有项目记录。这些习惯不会额外要求必须扫描项目、提交报告、新建技能或 harness、添加验证门，或自动复盘。

校验门是操作继续前必须通过的强制检查。只有问题已被证据确认，或存在明确的当前要求时，才可新增校验门。不得将未经证实的猜测或假设的未来失败转化为新的校验门或前置条件。确认 BUG 也不意味着必须加门。确有需要时，将校验门限定在受影响的操作和边界内，验证它能捕获该问题或落实当前要求，且不无故阻断有效工作。现有必需检查、明确的当前要求，以及安全、权限和数据完整性边界，均在 BUG 发生前就适用。

这些机制是 Agent 指令和配置约定，不是运行时强制钩子。磁盘同步、插件安装验证、当前任务已读取的指令，以及新会话实际表现，需要分别说明。

## 更新日志

### 2026-10-26 | `0.15.32+codex.20261026optin`

- 合入上游 pstack 0.15.32，固定到提交 `99b609a72323b70204eab407c622f436e858e112`，新增七个技能。
- 默认主代理直接执行；子代理、咨询、审查和替换代理需用户明确要求。保留既有模型和推理强度。
- 本次为源码整合，部署和新会话行为验证单独处理。

### 2026-10-16 | `0.15.13+codex.20261016solfirst`

- 普通开发、排错、集成、验证、操作和文案默认使用 Sol `medium`。Luna `max` 仅处理简单、高度重复、步骤固定且结果可直接核对的机械任务。
- 同步修改全局规则、宿主角色映射、基础指令、worker 角色和源码默认子代理配置；咨询结束后不再自动交回 Luna 实现。
- 默认子代理配置为 `gpt-6.1-sol`、`medium`，部署保留 Primary 和 Astra 设置。配置与安装文件读回，不等于已验证新会话的实际模型路由。

### 2026-10-11 | `0.15.13+codex.20261011mainownership`

- 专项 Main 缺席、归档或不可用时，总控不能用自己的实施子代理顶替。已有 Main 直接复用；缺席专项的接续任务整批准备，其他可执行的协调工作继续推进。
- 总控内部子代理仅辅助有界协调和最终验收。专项诊断、实现、修复及内部派工由对应 Main 负责。交接保留已有修改和证据，不重做已完成步骤。
- 新建独立聊天仍遵守宿主要求的用户创建指令。本次修改指令，尚未实测新总控的行为。

### 2026-10-11 | `0.15.13+codex.20261011noreplay`

- 启动、恢复或压缩上下文后，都从当前检查点继续。不要重放已完成的工作，也不要把被引用或已撤销的历史指令当作当前指令。之后明确的用户恢复指令在其范围内取代较早的 `Stop`。真正的新 `Stop` 仍立即生效。
- Main 之间不互发消息。只有总控路由跨工作流通信。Main 只报告已核验且下一负责人可用的阶段交付、已完成结果或真实异常。不发送零碎进展或确认循环。复用任务已有授权，不重复请求。
- SessionStart 提醒覆盖启动、恢复和上下文压缩。现有 101 项定向上下文生成检查全部通过，其中包括引用旧 `Stop` 并收到当前 `resume`，以及恢复后出现真正的新 `Stop`。这些检查不证明模型实机遵守规则，也不证明消息拦截。详见[上下文续接与协调规则](pstack/ADAPTATION.md#session-pickup-and-coordination-rules-2026-10-11)。

### 2026-10-11 | `0.15.13+codex.20261011productcopy`

- 将产品文案规则加入 `AGENTS.md` 和 `prompts/codex-event-driven-base.md`。工程注意事项保留在开发者对话或文档中。只有用户明确要求时，Agent 才会在交付的界面或面向客户的后端响应中添加免责声明。实际状态、错误和功能限制要具体说明。
- 已安装版本 `0.15.13+codex.20261011copy` 的 native engine 在 1,204 毫秒内完成 `SessionStart`。它使用真实事件中的会话 ID 选择临时测试绑定，并返回完全一致的当前正文，保留原有 `Pending` 状态。新的 Desktop 聊天运行了一次 `SessionStart`（`runs=1`、`failed=0`），输出 index 无效诊断后继续。
- 历史 Desktop `exit 1` 的原因仍未查明。本次没有修复钩子源码。详见[产品文案规则及 SessionStart 验证](pstack/ADAPTATION.md#product-copy-rules-and-sessionstart-verification-2026-10-11)。

### 2026-10-10 | `0.15.13+codex.20261010acceptance`

- 将用户原始目标和完成条件与 Main 的范围分开。每次 Main 交付后，接受证据支持的部分，并通过负责的 Main 推进仍可执行的授权工作。若只有已派发任务在运行，则使用现有可中断等待并处理结果，不以最终回复代替等待。
- 只有证据满足用户完成条件、用户停止或改变范围，或团队无法提供的外部输入或批准使所有授权工作都无法继续时，才结束任务。源码检查不能证明 Agent 行为；SessionStart 不会拦截轮次结束。

### 2026-10-10 | `0.15.13+codex.20261010gates`

- 按实际作用识别前置门槛，不能通过改称调查、证据补齐、兼容核对或验收来规避。
- 新增必做项必须有任务要求、已有强制规则，或具体证据证明的必要依赖或故障；不确定本身不构成依据。
- 适配默认复用已有能力与可信证据，总控撤销无依据的前提，不自行扩大目标或提高验收标准。
- 全局规则与基础指令保持同文，宿主与总控指南统一引用。源码检查通过，新会话行为尚未实测。

### 2026-10-10 | `0.15.13+codex.20261010brief`

- 专项 Main 派工统一为四项：目标、可检查的完成条件、验收证据、必要约束。
- 全局规则、总控指南和基础指令统一引用 CODEX.md 中的唯一模板；负责人和返回地址属于交接信息，不增加前置条件。
- 内部执行简报和模型路由保持不变。源码检查通过，新会话行为尚未实测。

### 2026-10-10 | `0.15.13+codex.20261010outcome`

- 总控主动撤销自身过时的方法限制，在同一轮把未完成目标交回负责的 Main 执行。
- 按验收需求处理证据缺口：安排必要调查或采集，可暂缺的未知项不阻塞已有证据支持的工作。
- 来源缺口、当前方法耗尽或记录部分交付，不能单独作为结束理由；外部依赖必须明确缺少的具体输入，且没有其他可推进工作。
- 源码与配置检查已通过；新会话行为尚未实测。

### 2026-10-10 | `0.15.13+codex.20261010progress`

- 30 分钟改为进展检查点，不再是任务完成期限。有实质进展且下一步明确时，原代理、原模型继续执行，Astra xhigh 同样适用。
- 只有证据表明确实无法继续推进时才升级。外部阻塞由对应负责人处理；近期没有聊天输出不等于停滞。
- 同步修正全局规则、模型路由、总控指南、基础提示词和运行配置。保留自动升级档位上限，不再把它当作执行时限。

### 2026-10-10 | `0.15.13+codex.20261010continuation`

- Main 用 commentary 回答临时插问后继续原任务；子代理运行时使用原生等待，返回后先处理结果，避免以“还有工作待完成”提前结束回合。
- 总控在 30 分钟内检查未完成的 Main 任务。正常执行者不受打扰；确认提前结束时，沿用原任务和已有结果，每个已结束回合只发送一次续办指令。
- 两项受控 Desktop 实测通过：插问后继续处理，以及通过一次续办消息恢复空闲 Main。恢复测试使用 15 秒检查期限，未跑满 30 分钟；这些规则不是运行时强制机制。

### 2026-10-09 | `0.15.13+codex.20261009wait`

- 总控没有独立工作、只等 Main 汇报时，改用可中断的 30 分钟 `clock.sleep`，避免两分钟一次的 `wait_threads` 循环；可执行工作和更早的操作期限优先。
- 已实测独立 Desktop 聊天消息让 180 秒等待在第 41.223 秒提前结束。Main 必须主动发送完成或阻塞报告，仅结束自身聊天不会通知总控。30 分钟参数在工具允许范围内，本次实测采用的是 180 秒。

### 2026-10-09 | `0.15.13+codex.20261009lean`

- 按下一步实际需要读取上下文并开工，复用已确定的结论和已有证据，不再要求先备齐完整计划及后续步骤的条件。
- 共享资源在相关操作开始前安排好，独立工作可以先推进。派工明确验收标准，完成证据在执行过程中取得。
- 三份规则总量减少约 30%，总控指南缩减约一半；合并重复的准备与收尾要求，保留必要权限、资源独占和最终验收；尚未重新验证代理实机表现。

### 2026-10-09 | `0.15.13+codex.20261009outcome`

- 总控一次交付完整目标，Main 自主负责诊断、实现、集成、验证与修复；总控在最终交付时验收，不再逐阶段批准。
- 共享资源操作者直接向负责该目标的 Main 返回结果。普通失败留在 Main 内部修复；总控只介入真实外部阻塞、跨负责人冲突、必须立即纠正的问题和用户新指令。
- 保留面向用户的实质进展汇报，避免确认循环、零碎指挥和空回复。用户停止联系团队的指令继续有效，本版尚未重新验证团队实机表现。

### 2026-10-09 | `0.15.13+codex.20261009checkpoint`

- 新增读取和更新现有标记区域的命令行工具。更新会比较整份记录的 SHA-256、保留区域外的所有字节、归档完整旧正文，并核对替换后的记录。
- 钩子的当前正文上限仍为 16 KiB。建议以 4–8 KiB 作为维护软目标，不增加强制门禁；工具不会总结内容，也无法判断语义是否完整。
- 版本 `0.15.13+codex.20261009checkpoint` 的 plugin-only 部署和已安装缓存检查均返回 `ok`，243 个托管文件无漂移。
- 对真实任务记录的更新将当前检查点从 29,370 字节缩减至 8,158 字节。完整旧正文已归档并核验；目标、权限和阻塞项得到保留，区域外历史保持不变。自然 `SessionStart` 行为仍未验证。
- 负责人先阅读简短的当前检查点，再按需查看相关任务和证据引用。


## 参与改进

围绕已观察到的问题或当前需求修改。复用已有源码与验证入口，保留无关改动，并说明支持修改的证据。中英文介绍应保持一致。

全局指令、角色定义和规则更新保持英文，中文 README 属于公开项目介绍。按任务内容选择角色：Sol 负责普通执行，Luna 仅做简单重复的机械任务。单独派发的咨询保持只读，接管保留其范围并持续负责到验证完成。主架构、系统架构、关键接口和数据契约设计及重大取舍交给 Astra。保留上游署名，在 [ADAPTATION.md](pstack/ADAPTATION.md) 中记录适配变更。

<a id="faq"></a>

## 常见问题

### PigeonStack 是 MCP 服务、Skill 还是 Agent？

它是包含 Codex 插件及配套指令、工具的仓库。插件打包选定的 pstack 技能和 Codex 适配层；全局规则、角色定义、配置与同步脚本则在仓库中与插件分别维护。它不运行 MCP 服务或自主调度器。

### PigeonStack 与 pstack 有什么区别？

PigeonStack 将 Lauren Tan 的 pstack 适配到 Codex，增加 Codex 专用全局规则、宿主适配器，以及面向运行时文件和插件缓存的版本化同步。仓库保留对 Lauren Tan 的作者署名与致谢。详见[上游来源与许可](#上游来源与许可)。

### 可以在不改动 `.codex` 目录的情况下预览吗？

可以。按照上面的独立目录预览步骤，指定 `.codex` 目录之外的新 `--codex-home` 路径，并加上 `--skip-plugin-install`。脚本只会在该目标中写入受管理文件和合并后的配置，不会安装插件或更改日常使用的 Codex 宿主；因此这次检查不能证明模型协作行为已经生效。

### PigeonStack 能让 Codex 更快或更省钱吗？

目前没有发布速度或成本基准测试。以更节省成本的方式协作是设计目标，不是实测结论。可用模型和原生子 Agent 工具取决于 Codex 宿主与账号。

## 上游来源与许可

PigeonStack 由 PigeonYang 维护，底层 pstack 工作流来自 Lauren Tan。仓库基于 pstack `0.15.32` 的[固定上游版本](https://github.com/cursor/plugins/tree/99b609a72323b70204eab407c622f436e858e112/pstack)适配，对应提交 `99b609a72323b70204eab407c622f436e858e112`。选入的控制与代码清理技能来自同一版本中的 Cursor Team Kit。

基于 pstack 0.15.32，包含用于处理反复出现的 Agent 错误的 `/correct`、用于提供性能证据的 `/benchmark-checklist`，以及用于解释测量数据的 `/principle-explain-the-number`。上游工作流已适配到 Codex；模型选择和升级路径遵循本项目的 GPT 配置。

[provenance.json](pstack/provenance.json) 记录导入文件及其源文件哈希，[ADAPTATION.md](pstack/ADAPTATION.md) 记录 Codex 适配及变更历史。原有许可声明保留在 [pstack/LICENSE](pstack/LICENSE) 和 [pstack/CURSOR-TEAM-KIT-LICENSE](pstack/CURSOR-TEAM-KIT-LICENSE)。

这些 MIT 声明适用于各自的上游材料。仓库目前没有单独的根目录许可证，将相同许可统一授予所有 PigeonStack 原创内容。
