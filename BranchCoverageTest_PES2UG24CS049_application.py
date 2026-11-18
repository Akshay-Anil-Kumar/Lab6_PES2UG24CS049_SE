import pytest
from mobile_data_plan import overage_charge, recharge_allowed, validity_status


# overage_charge(): invalid inputs and every decision outcome

def test_unknown_plan_branch():
    with pytest.raises(ValueError, match="unknown plan"):
        overage_charge("gold", 1, False, False)


def test_negative_usage_branch():
    with pytest.raises(ValueError, match="invalid data usage"):
        overage_charge("basic", -1, False, False)


@pytest.mark.parametrize("plan, usage, loyal", [
    ("basic", 3, True),       # loyalty condition true
    ("basic", 2, False),      # loyalty condition false
    ("premium", 10, True),    # premium exception
    ("standard", 6, True),    # loyalty-adjusted included amount
])
def test_loyalty_and_no_overage_branches(plan, usage, loyal):
    assert overage_charge(plan, usage, False, loyal) == 0


def test_extra_data_not_roaming_and_not_over_ten():
    assert overage_charge("standard", 7, False, False) == 30


def test_extra_data_roaming_and_not_over_ten():
    assert overage_charge("basic", 3, True, False) == 40


def test_extra_data_over_ten_not_roaming():
    assert overage_charge("premium", 21, False, False) == 275


def test_extra_data_over_ten_roaming_nested_branch():
    assert overage_charge("standard", 16, True, False) == 605


def test_exactly_ten_extra_gb():
    assert overage_charge("basic", 12, False, False) == 150


# recharge_allowed(): KYC, amount, and pending recharge branches

def test_kyc_pending_amount_at_limit():
    assert recharge_allowed(200, 99, True) is True


def test_kyc_pending_amount_above_limit():
    assert recharge_allowed(201, 0, True) is False


def test_non_kyc_amount_above_2000():
    assert recharge_allowed(2001, 0, False) is False


def test_non_kyc_amount_within_limit_and_pending_at_two():
    assert recharge_allowed(2000, 2, False) is True


def test_non_kyc_pending_above_two():
    assert recharge_allowed(500, 3, False) is False


def test_non_kyc_no_pending_recharges():
    assert recharge_allowed(500, 0, False) is True


# validity_status(): prepaid/postpaid, add-on, active/grace/expired

@pytest.mark.parametrize("days, prepaid, addon, expected", [
    (0, True, False, "active"),
    (-1, True, False, "grace"),
    (-15, True, False, "grace"),
    (-16, True, False, "expired"),
    (3, False, False, "active"),
    (2, False, False, "grace"),
    (-12, False, False, "grace"),
    (-13, False, False, "expired"),
    (2, True, True, "active"),
    (1, True, True, "grace"),
    (-13, True, True, "grace"),
    (-14, True, True, "expired"),
    (5, False, True, "active"),
    (4, False, True, "grace"),
    (-10, False, True, "grace"),
    (-11, False, True, "expired"),
])
def test_validity_all_decision_paths(days, prepaid, addon, expected):
    assert validity_status(days, prepaid, addon) == expected
