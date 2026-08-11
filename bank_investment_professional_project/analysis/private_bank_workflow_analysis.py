"""
Private Bank Investment Professional Simulation

This script rebuilds the analytical outputs from synthetic private-bank datasets.
It is for portfolio demonstration only and does not constitute investment advice,
securities recommendations, client work, brokerage execution, or registered advisory experience.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, List, Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUT = ROOT / "output"


def read_csv_dict(name: str) -> List[Dict[str, Any]]:
    with open(DATA / name, newline="") as f:
        return list(csv.DictReader(f))


def write_csv(name: str, rows: List[List[Any]], headers: List[str]) -> None:
    OUTPUT.mkdir(exist_ok=True)
    with open(OUTPUT / name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def to_float(value: Any) -> float:
    if value in ("", None):
        return 0.0
    return float(value)


def build_portfolio_summary() -> None:
    clients = read_csv_dict("client_profiles.csv")
    holdings = read_csv_dict("portfolio_holdings.csv")

    rows = []
    for client in clients:
        client_id = client["Client_ID"]
        client_holdings = [h for h in holdings if h["Client_ID"] == client_id]
        total_aum = sum(to_float(h["Market_Value"]) for h in client_holdings)

        by_class: Dict[str, float] = {}
        for h in client_holdings:
            by_class[h["Asset_Class"]] = by_class.get(h["Asset_Class"], 0.0) + to_float(h["Market_Value"])

        equity_pct = by_class.get("Equity", 0.0) / total_aum
        fixed_income_pct = by_class.get("Fixed Income", 0.0) / total_aum
        alternatives_pct = by_class.get("Alternatives", 0.0) / total_aum
        cash_pct = by_class.get("Cash", 0.0) / total_aum

        expected_return = sum(to_float(h["Market_Value"]) * to_float(h["Expected_Return"]) for h in client_holdings) / total_aum
        income_yield = sum(to_float(h["Market_Value"]) * to_float(h["Income_Yield"]) for h in client_holdings) / total_aum
        weighted_volatility = sum((to_float(h["Market_Value"]) / total_aum) * to_float(h["Volatility"]) for h in client_holdings)
        unrealized_gain_loss = sum(to_float(h["Market_Value"]) - to_float(h["Cost_Basis"]) for h in client_holdings)

        drift_flags = []
        if equity_pct > to_float(client["Max_Equity"]):
            drift_flags.append("Equity over max")
        if fixed_income_pct < to_float(client["Min_Fixed_Income"]):
            drift_flags.append("Fixed income below min")
        if alternatives_pct > to_float(client["Max_Alternatives"]):
            drift_flags.append("Alternatives over max")

        rows.append([
            client_id,
            client["Client_Profile"],
            client["Risk_Profile"],
            round(total_aum, 2),
            round(equity_pct, 4),
            round(fixed_income_pct, 4),
            round(alternatives_pct, 4),
            round(cash_pct, 4),
            round(expected_return, 4),
            round(income_yield, 4),
            round(weighted_volatility, 4),
            round(unrealized_gain_loss, 2),
            "; ".join(drift_flags) if drift_flags else "Within mandate",
        ])

    write_csv(
        "portfolio_summary.csv",
        rows,
        [
            "Client_ID", "Client_Profile", "Risk_Profile", "Total_AUM",
            "Equity_%", "Fixed_Income_%", "Alternatives_%", "Cash_%",
            "Expected_Return", "Income_Yield", "Weighted_Volatility",
            "Unrealized_Gain_Loss", "Mandate_Status",
        ],
    )


def build_scenario_analysis() -> None:
    scenarios = read_csv_dict("scenario_assumptions.csv")
    summary = read_csv_dict("portfolio_summary.csv")

    rows = []
    for client in summary:
        total_aum = to_float(client["Total_AUM"])
        equity_pct = to_float(client["Equity_%"])
        fixed_income_pct = to_float(client["Fixed_Income_%"])
        alternatives_pct = to_float(client["Alternatives_%"])
        cash_pct = to_float(client["Cash_%"])

        for scenario in scenarios:
            modeled_return = (
                equity_pct * to_float(scenario["Equity_Return"])
                + fixed_income_pct * to_float(scenario["Fixed_Income_Return"])
                + alternatives_pct * to_float(scenario["Alternatives_Return"])
                + cash_pct * to_float(scenario["Cash_Return"])
            )
            modeled_value = total_aum * (1 + modeled_return)
            rows.append([
                client["Client_ID"],
                scenario["Scenario"],
                round(modeled_return, 4),
                round(modeled_value, 2),
                round(modeled_value - total_aum, 2),
            ])

    write_csv(
        "scenario_impact.csv",
        rows,
        ["Client_ID", "Scenario", "Modeled_Return", "Modeled_Portfolio_Value", "Estimated_Gain_Loss"],
    )


def build_trade_reconciliation() -> None:
    paper = {row["Trade_ID"]: row for row in read_csv_dict("paper_blotter.csv")}
    trades = {row["Trade_ID"]: row for row in read_csv_dict("trade_blotter.csv")}
    all_trade_ids = sorted(set(paper) | set(trades))

    rows = []
    for trade_id in all_trade_ids:
        p = paper.get(trade_id)
        t = trades.get(trade_id)

        if p and t:
            paper_qty = to_float(p["Quantity"])
            trade_qty = to_float(t["Quantity"])
            expected_price = to_float(p["Limit_or_Expected_Price"])
            execution_price = to_float(t["Execution_Price"])
            notional_diff = to_float(t["Execution_Notional"]) - to_float(p["Notional"])
            price_variance_pct = abs(execution_price - expected_price) / expected_price if expected_price else 0

            if paper_qty != trade_qty:
                status = "Exception - quantity mismatch"
            elif p["Advisor_Approval"] != "Y":
                status = "Exception - approval missing"
            elif price_variance_pct > 0.002:
                status = "Review - price variance"
            elif t["Status"] != "Executed":
                status = "Review - not executed"
            else:
                status = "Matched"

            rows.append([
                trade_id, p["Account_ID"], p["Action"], p["Ticker"], paper_qty,
                trade_qty, expected_price, execution_price, round(notional_diff, 2), status,
            ])

        elif p and not t:
            rows.append([
                trade_id, p["Account_ID"], p["Action"], p["Ticker"], to_float(p["Quantity"]),
                "", to_float(p["Limit_or_Expected_Price"]), "", -to_float(p["Notional"]),
                "Exception - missing from trade blotter",
            ])

        elif t and not p:
            rows.append([
                trade_id, t["Account_ID"], t["Action"], t["Ticker"], "",
                to_float(t["Quantity"]), "", to_float(t["Execution_Price"]),
                to_float(t["Execution_Notional"]), "Exception - unmatched trade",
            ])

    write_csv(
        "trade_blotter_reconciliation.csv",
        rows,
        [
            "Trade_ID", "Account_ID", "Action", "Ticker", "Paper_Qty", "Trade_Qty",
            "Expected_Price", "Execution_Price", "Notional_Difference", "Control_Status",
        ],
    )


def main() -> None:
    build_portfolio_summary()
    build_scenario_analysis()
    build_trade_reconciliation()
    print("Private bank workflow outputs rebuilt in output/.")


if __name__ == "__main__":
    main()
