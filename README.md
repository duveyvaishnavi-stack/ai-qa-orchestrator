# AI QA Orchestration Pipeline

> Reads user stories → generates test cases → writes Playwright scripts → opens GitHub PRs. Automatically.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Playwright](https://img.shields.io/badge/Playwright-TypeScript-green)
![Claude](https://img.shields.io/badge/Powered%20by-Claude%20AI-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

Built by [Vaishnavi](https://www.linkedin.com/in/vaishnve-duvey-53b9a8143/?skipRedirect=true) · QA Engineer

---

## What it does

1. Reads a user story (acceptance criteria included)
2. Generates happy path + edge cases + negative test cases
3. Writes a ready-to-run Playwright TypeScript spec file
4. (Coming soon) Files a GitHub PR automatically via MCP

## Architecture

```
MCP Tools Layer    →   Jira · GitHub · TestRail · Slack
        ↓
AI Orchestrator    →   Claude reads stories, reasons, writes tests
        ↓
RAG Knowledge      →   Your codebase · standards · past incidents
```

## Quick start

```bash
# 1. Install
pip install anthropic

# 2. Set your API key
export ANTHROPIC_API_KEY=sk-ant-your-key-here

# 3. Run
python orchestrator.py

# Output: STORY-1042.spec.ts (ready-to-run Playwright file)
```

Get your API key at: https://console.anthropic.com

## Files

| File | Description |
|------|-------------|
| `orchestrator.py` | Main pipeline script |
| `README.md` | This file |

## Roadmap

- [x] Generate test cases from user stories
- [x] Write Playwright TypeScript spec files
- [ ] Jira MCP connector (auto-fetch stories)
- [ ] GitHub MCP connector (auto-open PRs)
- [ ] RAG layer (embed your codebase)
- [ ] Schedule via GitHub Actions

## Author

**Vaishnavi** — QA Engineer passionate about AI-powered testing

Connect on [LinkedIn](https://linkedin.com/in/your-profile)

---
⭐ Star this repo if it helped you!
