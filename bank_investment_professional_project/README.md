# Private Bank Investment Professional Simulation

## Project Overview

This project is a synthetic U.S. Private Bank Investment Professional workflow built to demonstrate practical readiness for an **Investment Professional Associate** role supporting Investors and Client Advisors.

The project models the daily analytical and control responsibilities of a private-bank investment support role: portfolio review, mandate monitoring, what-if scenario analysis, trade/blotter reconciliation, exception identification, fee billing review, and alternatives document tracking.

> **Important disclaimer:** This is a synthetic professional portfolio project. It is not investment advice, not a securities recommendation, not client work, and not evidence of executed brokerage trades, discretionary authority, registered investment-advisory activity, or private-bank employment.

## Why This Project Exists

The target role values:
- portfolio and client relationship support
- brokerage trade review and exception follow-up
- discretionary mandate support
- scenario-based analysis
- risk metric monitoring
- fee schedule and billing oversight
- alternatives document administration
- strong Excel, PowerPoint, accuracy, follow-through, and confidentiality

This project is designed to show those skills through a realistic but fully synthetic workflow.

## Project Deliverables

| File / Folder | Description |
|---|---|
| `Private_Bank_Investment_Professional_Simulation.xlsx` | Excel workbook with dashboard, portfolio summary, scenario analysis, trade controls, alternatives tracker, fee billing, and source notes |
| `Private_Bank_Investment_Professional_Executive_Deck.pptx` | Executive presentation summarizing the project in a private-bank style |
| `data/` | Synthetic client profiles, holdings, paper blotter, trade blotter, alternatives documentation, fee schedules, and scenario assumptions |
| `analysis/private_bank_workflow_analysis.py` | Python script that rebuilds the analytical outputs from the synthetic datasets |
| `output/` | Computed portfolio summary, scenario impact, trade reconciliation, dashboard preview, Excel model, and executive deck |
| `docs/` | Resume bullets, methodology, and GitHub publishing guide |

## Capabilities Demonstrated

### 1. Portfolio Review & Mandate Monitoring
The workbook evaluates synthetic client portfolios by:
- AUM
- asset-class allocation
- expected return
- income yield
- weighted volatility
- unrealized gain/loss
- mandate drift flags

### 2. Scenario and “What-If” Analysis
The model tests each portfolio against:
- Base Case
- Equity Drawdown
- Rates Up / Duration Shock
- Recession Stress
- Soft Landing

Outputs estimate modeled return, portfolio value, and estimated gain/loss by client and scenario.

### 3. Trade Control and Blotter Reconciliation
The project compares a synthetic paper blotter to a synthetic trade blotter to identify:
- matched trades
- price variances
- quantity mismatches
- missing trades
- unmatched trades
- approval exceptions
- cancel/correct review items

### 4. Alternatives Documentation Tracker
The project tracks synthetic private markets subscription-document status across:
- investor eligibility
- KYC/AML
- tax documents
- subscription agreements
- capital-call instructions
- pending client corrections

### 5. Fee Schedule and Billing Oversight
The model evaluates quarterly fees, billing status, and review flags by account.

## How to Run the Analysis

From the project root:

```bash
python analysis/private_bank_workflow_analysis.py
```

The script reads the synthetic CSV files in `data/` and recreates the analytical CSV outputs in `output/`.

## Suggested Resume Entry

**Private Bank Investment Professional Simulation | Excel, Python, PowerPoint**  
Built a synthetic private-bank portfolio support workflow evaluating client allocations, risk/return profiles, scenario outcomes, trade/blotter exceptions, fee schedules, and alternatives documentation; produced an executive-ready Excel dashboard and PowerPoint presentation simulating support for Investors and Client Advisors.

## Interview Talking Point

“I built this project to close the gap between my financial analysis and transaction-control background and the specific day-to-day responsibilities of a Private Bank Investment Professional. The workflow is synthetic, but it shows how I think through portfolio support, client mandates, scenario analysis, trade controls, billing reviews, alternatives documentation, accuracy, and follow-through.”
