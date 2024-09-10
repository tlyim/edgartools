import marimo

__generated_with = "0.8.13"
app = marimo.App(width="medium")


@app.cell
def __():
    return


@app.cell
def __():
    from edgar import set_identity, Company
    return Company, set_identity


@app.cell
def __():
    dir()
    return


@app.cell
def __(set_identity):

    set_identity("Andrew Yim acdryim@gmail.com")
    return


@app.cell
def __(Company):
    apple = Company("AAPL")
    apple
    return apple,


@app.cell
def __(apple):
    apple.financials
    return


@app.cell
def __(apple):
    help(apple.financials)
    return


@app.cell
def __(apple):
    print(apple.financials.__dict__)
    return


@app.cell
def __(apple):
    filings = apple.get_filings(form="10-Q")
    filings
    return filings,


@app.cell
def __(filings):
    filings.to_pandas()
    return


@app.cell
def __():
    from edgar import get_filings
    filings2 = get_filings(form="10-K")
    filing2 = filings2[0]
    return filing2, filings2, get_filings


@app.cell
def __():
    from edgar.financials import Financials
    return Financials,


@app.cell
def __(Financials, filing2):
    financials = Financials(filing2.xbrl())
    financials
    return financials,


@app.cell
def __(financials):
    financials.get_income_statement()
    financials.get_cash_flow_statement()
    financials.get_balance_sheet()

    return


if __name__ == "__main__":
    app.run()
