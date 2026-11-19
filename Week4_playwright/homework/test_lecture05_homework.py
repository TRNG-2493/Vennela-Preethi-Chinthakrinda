from datetime import date, datetime, timedelta
from pathlib import Path

import pytest
from playwright.sync_api import Locator, Page, expect

PRACTICE_PAGE = Path(__file__).parent / "widgets_practice.html"


@pytest.fixture
def store(page: Page) -> Page:
    page.goto(PRACTICE_PAGE.as_uri())
    return page


# ---------- Helpers (already done) ----------

def column_index(table: Locator, header: str) -> int:
    headers = [h.strip() for h in table.get_by_role("columnheader").all_text_contents()]
    return headers.index(header)


def column_values(table: Locator, header: str) -> list[str]:
    index = column_index(table, header)
    return [row.get_by_role("cell").nth(index).text_content()
            for row in table.locator("tbody tr").all()]


def to_number(money: str) -> int:
    """'$95,000' -> 95000"""
    return float(money.replace("$", "").replace(",", ""))


def go_to_next_page(page: Page) -> None:
    page_info = page.locator("#page-info")
    before = page_info.text_content()
    page.get_by_role("button", name="Next", exact=True).click()
    expect(page_info).not_to_have_text(before)


def pick_calendar_date(page: Page, target: date) -> None:
    page.get_by_label("Delivery date").click()
    header = page.locator("#month-year")
    target_month = target.replace(day=1)
    while True:
        shown = datetime.strptime(header.text_content(), "%B %Y").date()
        if shown == target_month:
            break
        if shown < target_month:
            page.get_by_role("button", name="Next month").click()
        else:
            page.get_by_role("button", name="Previous month").click()
    page.get_by_role("button", name=f"{target:%B} {target.day}, {target.year}", exact=True).click()


# ================= PART 1: Tables (Employees) =================

def test_01_fatima_department(store: Page):
    # TODO: Fatima Khan's Department is "HR"
    row = store.locator("tbody tr").filter(has_text="Fatima Khan")
    department = row.locator("td").nth(2)
    expect(department).to_have_text("HR")

def test_02_ethan_start_date(store: Page):
    # TODO: Ethan Brown's Start date is "2023-05-22"
    row = store.locator("tbody tr").filter(has_text="Ethan Brown")
    start_date = row.locator("td").nth(4)
    expect(start_date).to_have_text("2023-05-22")

def test_03_sales_count(store: Page):
    # TODO: exactly 2 employees are in Sales
    row = store.locator("tbody tr").filter(has = store.get_by_role("cell", name = "Sales"))
    expect(row).to_have_count(2)


def test_04_total_salary(store: Page):
    # TODO: the total of all salaries is 458000
    # Hint: column_values + to_number + sum()
    row = column_values(store, "Salary")
    total = sum(to_number(salary) for salary in row)
    assert total == 458125.0
    
def test_05_started_before_2021(store: Page):
    # TODO: the employees who started before 2021-01-01 are
    #       ["Ben Carter", "Chen Wei", "Fatima Khan"]
    pass


def test_06_delete_all_sales(store: Page):
    # TODO: delete EVERY Sales employee (don't hard-code their names)
    # TODO: 4 rows remain and #employee-count says "4 employees"
    # Hint: read the "delete-loop" warning in the notes
    pass


def test_07_sort_salary_descending(store: Page):
    # TODO: click the Salary header TWICE (ascending, then descending)
    # TODO: the first row is now Chen Wei
    # TODO: the salaries are in descending order
    salary_header = store.get_by_role("columnheader", name="Salary")
    salary_header.click()
    salary_header.click()
    print(store.locator("tbody tr").all_text_contents())


# ================= PART 2: Pagination (Orders) =================

def test_08_find_order_2008(store: Page):
    # TODO: find order 2008 (it's not on page 1)
    # TODO: its cells are ["2008", "Ben", "Cancelled", "$62.50"]
    # TODO: we're on "Page 2 of 3"
    store.get_by_role("button", name="Next").click()
    row = store.locator("tbody tr").filter(has_text="2008")
    expect(row.locator("td")).to_have_text(["2008", "Ben", "Cancelled", "$62.50"])
    expect(store.locator("#page-info")).to_have_text("Page 2 of 3")

def test_09_count_pending_orders(store: Page):
    # TODO: count the "Pending" orders across ALL pages; there are 3
    pass


def test_10_previous_button(store: Page):
    # TODO: go to page 3, then click Previous
    # TODO: we're on "Page 2 of 3" and Next is enabled
    next_button = store.get_by_role("button", name="Next")
    previous_button = store.get_by_role("button", name="Previous")
    next_button.click()
    next_button.click()
    previous_button.click()
    expect(store.locator("#page-info")).to_have_text("Page 2 of 3")
    expect(next_button).to_be_enabled()

# ================= PART 3: Date pickers =================

def test_11_native_birthday(store: Page):
    # TODO: set Birthday to 31 January 2001 using a Python date object
    # TODO: #birthday-summary says "Birthday: 2001-01-31"
    pass


def test_12_new_years_eve(store: Page):
    # TODO: pick 31 December 2026 in the Delivery date calendar
    # TODO: the input says "12/31/2026"
    pass


def test_13_one_week_from_today(store: Page):
    # TODO: pick the date 7 days from today
    # TODO: #delivery-summary says "Delivery: <Month> <day>, <year>"
    #       e.g. "Delivery: November 6, 2026" (no leading zero on the day)
    pass


def test_14_first_of_next_month(store: Page):
    # TODO: pick the 1st day of NEXT month
    # TODO: check the input's value (MM/DD/YYYY)
    # Hint: this must also work when you run it in December!
    pass