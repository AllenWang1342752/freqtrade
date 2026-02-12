# ![freqtrade](https://raw.githubusercontent.com/freqtrade/freqtrade/develop/docs/assets/freqtrade_poweredby.svg)

[![Freqtrade CI](https://github.com/freqtrade/freqtrade/actions/workflows/ci.yml/badge.svg?branch=develop)](https://github.com/freqtrade/freqtrade/actions/workflows/ci.yml)
[![DOI](https://joss.theoj.org/papers/10.21105/joss.04864/status.svg)](https://doi.org/10.21105/joss.04864)
[![Coverage Status](https://coveralls.io/repos/github/freqtrade/freqtrade/badge.svg?branch=develop&service=github)](https://coveralls.io/github/freqtrade/freqtrade?branch=develop)
[![Documentation](https://readthedocs.org/projects/freqtrade/badge/)](https://www.freqtrade.io)

Freqtrade 是一个用 Python 编写的免费开源加密货币交易机器人。它旨在支持所有主流交易所，并可通过 Telegram 或 WebUI 控制。它包含回测、绘图和资金管理工具，以及通过机器学习进行策略优化。

![freqtrade](https://raw.githubusercontent.com/freqtrade/freqtrade/develop/docs/assets/freqtrade-screenshot.png)

## 免责声明

本软件仅用于教育目的。请不要冒险投入你无法承受损失的资金。使用本软件风险自负。作者及所有关联方对你的交易结果不承担任何责任。

请始终先以 Dry-Run 方式运行交易机器人，在你理解其工作原理以及预期盈亏之前，不要投入真实资金。

我们强烈建议你具备编码和 Python 知识。请不要犹豫阅读源码并理解该机器人的机制。

## 支持的交易所市场

请阅读[交易所专用说明](docs/exchanges.md)，了解每个交易所可能需要的特殊配置。

### 支持的现货交易所

- [X] [Binance](https://www.binance.com/)
- [X] [BingX](https://bingx.com/invite/0EM9RX)
- [X] [Bitget](https://www.bitget.com/)
- [X] [Bitmart](https://bitmart.com/)
- [X] [Bybit](https://bybit.com/)
- [X] [Gate.io](https://www.gate.io/ref/6266643)
- [X] [HTX](https://www.htx.com/)
- [X] [Hyperliquid](https://hyperliquid.xyz/)（去中心化交易所，DEX）
- [X] [Kraken](https://kraken.com/)
- [X] [OKX](https://okx.com/)
- [X] [MyOKX](https://okx.com/)（OKX EEA）
- [ ] [可能还有更多](https://github.com/ccxt/ccxt/)。（_我们无法保证它们都能正常工作_）

### 支持的期货交易所

- [X] [Binance](https://www.binance.com/)
- [X] [Bitget](https://www.bitget.com/)
- [X] [Gate.io](https://www.gate.io/ref/6266643)
- [X] [Hyperliquid](https://hyperliquid.xyz/)（去中心化交易所，DEX）
- [X] [OKX](https://okx.com/)
- [X] [Bybit](https://bybit.com/)

在开始之前，请务必阅读[交易所专用说明](docs/exchanges.md)以及[杠杆交易](docs/leverage.md)相关文档。

### 社区测试

以下交易所已由社区确认可用：

- [X] [Bitvavo](https://bitvavo.com/)
- [X] [Kucoin](https://www.kucoin.com/)

## 文档

我们建议你阅读机器人文档，以确保你理解其工作方式。

完整文档请见 [freqtrade 网站](https://www.freqtrade.io)。

## 功能

- [x] **基于 Python 3.11+**：可在 Windows、macOS 和 Linux 上运行。
- [x] **持久化**：使用 sqlite 实现持久化。
- [x] **Dry-run**：无需真实资金即可运行机器人。
- [x] **回测**：对你的买卖策略进行模拟。
- [x] **机器学习策略优化**：使用机器学习基于真实交易所数据优化你的买卖参数。
- [X] **自适应预测建模**：使用 FreqAI 构建可通过自适应机器学习方法自我训练的智能策略。[了解更多](https://www.freqtrade.io/en/stable/freqai/)
- [x] **白名单加密货币**：选择你想交易的币种，或使用动态白名单。
- [x] **黑名单加密货币**：选择你想避免交易的币种。
- [x] **内置 WebUI**：内置 Web UI 管理机器人。
- [x] **可通过 Telegram 管理**：使用 Telegram 管理机器人。
- [x] **以法币显示盈亏**：以法币显示盈亏。
- [x] **性能状态报告**：提供当前交易的性能状态报告。

## 快速开始

请参考 [Docker 快速开始文档](https://www.freqtrade.io/en/stable/docker_quickstart/) 以快速上手。

如需更多（原生）安装方式，请参考[安装文档](https://www.freqtrade.io/en/stable/installation/)。

## 基本用法

### 机器人命令

```text
usage: freqtrade [-h] [-V]
                 {trade,create-userdir,new-config,show-config,new-strategy,download-data,convert-data,convert-trade-data,trades-to-ohlcv,list-data,backtesting,backtesting-show,backtesting-analysis,edge,hyperopt,hyperopt-list,hyperopt-show,list-exchanges,list-markets,list-pairs,list-strategies,list-hyperoptloss,list-freqaimodels,list-timeframes,show-trades,test-pairlist,convert-db,install-ui,plot-dataframe,plot-profit,webserver,strategy-updater,lookahead-analysis,recursive-analysis}
                 ...

Free, open source crypto trading bot

positional arguments:
  {trade,create-userdir,new-config,show-config,new-strategy,download-data,convert-data,convert-trade-data,trades-to-ohlcv,list-data,backtesting,backtesting-show,backtesting-analysis,edge,hyperopt,hyperopt-list,hyperopt-show,list-exchanges,list-markets,list-pairs,list-strategies,list-hyperoptloss,list-freqaimodels,list-timeframes,show-trades,test-pairlist,convert-db,install-ui,plot-dataframe,plot-profit,webserver,strategy-updater,lookahead-analysis,recursive-analysis}
    trade               Trade module.
    create-userdir      Create user-data directory.
    new-config          Create new config
    show-config         Show resolved config
    new-strategy        Create new strategy
    download-data       Download backtesting data.
    convert-data        Convert candle (OHLCV) data from one format to
                        another.
    convert-trade-data  Convert trade data from one format to another.
    trades-to-ohlcv     Convert trade data to OHLCV data.
    list-data           List downloaded data.
    backtesting         Backtesting module.
    backtesting-show    Show past Backtest results
    backtesting-analysis
                        Backtest Analysis module.
    hyperopt            Hyperopt module.
    hyperopt-list       List Hyperopt results
    hyperopt-show       Show details of Hyperopt results
    list-exchanges      Print available exchanges.
    list-markets        Print markets on exchange.
    list-pairs          Print pairs on exchange.
    list-strategies     Print available strategies.
    list-hyperoptloss   Print available hyperopt loss functions.
    list-freqaimodels   Print available freqAI models.
    list-timeframes     Print available timeframes for the exchange.
    show-trades         Show trades.
    test-pairlist       Test your pairlist configuration.
    convert-db          Migrate database to different system
    install-ui          Install FreqUI
    plot-dataframe      Plot candles with indicators.
    plot-profit         Generate plot showing profits.
    webserver           Webserver module.
    strategy-updater    updates outdated strategy files to the current version
    lookahead-analysis  Check for potential look ahead bias.
    recursive-analysis  Check for potential recursive formula issue.

options:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
```

### Telegram RPC 命令

Telegram 不是必需的，但它是控制机器人非常好的方式。更多细节与完整命令列表请见[文档](https://www.freqtrade.io/en/latest/telegram-usage/)。

- `/start`: 启动交易器。
- `/stop`: 停止交易器。
- `/stopentry`: 停止进入新交易。
- `/status <trade_id>|[table]`: 列出所有或指定的未平仓交易。
- `/profit [<n>]`: 列出过去 n 天内所有已完成交易的累计利润。
- `/profit_long [<n>]`: 列出过去 n 天内所有已完成多头交易的累计利润。
- `/profit_short [<n>]`: 列出过去 n 天内所有已完成空头交易的累计利润。
- `/forceexit <trade_id>|all`: 立即退出指定交易（忽略 `minimum_roi`）。
- `/fx <trade_id>|all`: `/forceexit` 的别名。
- `/performance`: 按交易对分组显示已完成交易的表现。
- `/balance`: 显示各币种账户余额。
- `/daily <n>`: 显示过去 n 天内按天计算的盈亏。
- `/help`: 显示帮助信息。
- `/version`: 显示版本。


## 开发分支

该项目当前设置了两个主要分支：

- `develop` - 该分支经常包含新功能，但也可能包含破坏性变更。我们努力保持该分支尽可能稳定。
- `stable` - 该分支包含最新稳定版本，通常经过良好测试。
- `feat/*` - 这些是正在积极开发的功能分支。除非你想测试特定功能，否则请不要使用这些分支。

## 支持

### 帮助 / Discord

如需任何文档未覆盖的问题或进一步了解机器人，或与志同道合的人交流，欢迎加入 Freqtrade [discord 服务器](https://discord.gg/p7nuUNVfP7)。

### [Bug / Issue](https://github.com/freqtrade/freqtrade/issues?q=is%3Aissue)

如果你发现机器人中的 bug，请先
[搜索 issue 列表](https://github.com/freqtrade/freqtrade/issues?q=is%3Aissue)。
如果未被报告，请
[创建新的 issue](https://github.com/freqtrade/freqtrade/issues/new/choose)，并确保遵循模板指南，以便团队能尽快协助你。

对每一个创建的 [issue](https://github.com/freqtrade/freqtrade/issues/new/choose)，请在问题解决并达到平衡点时，跟进并标记满意或提醒关闭。

--遵守 GitHub 的[社区政策](https://docs.github.com/en/site-policy/github-terms/github-community-code-of-conduct)--

### [功能请求](https://github.com/freqtrade/freqtrade/labels/enhancement)

你有很棒的想法想要改进机器人吗？请先搜索该功能是否已被[讨论过](https://github.com/freqtrade/freqtrade/labels/enhancement)。
如果还未被请求，请
[创建新的请求](https://github.com/freqtrade/freqtrade/issues/new/choose)
并确保遵循模板指南，以免被淹没在 bug 报告中。

### [Pull Requests](https://github.com/freqtrade/freqtrade/pulls)

觉得机器人缺少功能吗？欢迎提交 Pull Request！

在提交 PR 之前，请阅读
[贡献指南](https://github.com/freqtrade/freqtrade/blob/develop/CONTRIBUTING.md)
以了解相关要求。

贡献不一定需要写代码——也许可以从改进文档开始？标记为 [good first issue](https://github.com/freqtrade/freqtrade/labels/good%20first%20issue) 的问题适合作为首次贡献，并能帮助你熟悉代码库。

**注意**：在开始任何重大新功能开发之前，_请先提交一个 issue 描述你计划做的事情_ 或在 [discord](https://discord.gg/p7nuUNVfP7) 上与我们交流（请使用 #dev 频道）。这将确保相关方能对该功能提供宝贵反馈，并让他人知道你正在处理该功能。

**重要：** 请始终针对 `develop` 分支创建 PR，而不是 `stable`。

## 要求

### 时间同步

系统时间必须准确，并非常频繁地与 NTP 服务器同步，以避免与交易所通信问题。

### 最低硬件要求

运行此机器人，我们建议使用至少以下配置的云主机：

- 最低（建议）系统要求：2GB RAM、1GB 磁盘空间、2vCPU

### 软件要求

- [Python >= 3.11](http://docs.python-guide.org/en/latest/starting/installation/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [TA-Lib](https://ta-lib.github.io/ta-lib-python/)
- [virtualenv](https://virtualenv.pypa.io/en/stable/installation.html)（推荐）
- [Docker](https://www.docker.com/products/docker)（推荐）
