import pytest
from mobile_data_plan import overage_charge, recharge_allowed, validity_status


def test_overage_charge_valid_plan():
    assert overage_charge("standard", 7, False, False) == 30


def test_overage_charge_unknown_plan():
    with pytest.raises(ValueError, match="unknown plan"):
        overage_charge("gold", 2, False, False)


def test_overage_charge_negative_usage():
    with pytest.raises(ValueError, match="invalid data usage"):
        overage_charge("basic", -1, False, False)


def test_overage_charge_loyalty():
    assert overage_charge("basic", 3, False, True) == 0


def test_overage_charge_roaming():
    assert overage_charge("basic", 3, True, False) == 40


def test_overage_charge_high_usage():
    assert overage_charge("premium", 21, False, False) == 275


def test_recharge_allowed():
    assert recharge_allowed(500, 1, False) is True


def test_recharge_kyc_pending():
    assert recharge_allowed(200, 0, True) is True


def test_recharge_amount_too_high():
    assert recharge_allowed(2001, 0, False) is False


def test_recharge_pending_limit():
    assert recharge_allowed(500, 3, False) is False


def test_validity_active():
    assert validity_status(5, True, False) == "active"


def test_validity_grace():
    assert validity_status(-1, True, False) == "grace"


def test_validity_expired():
    assert validity_status(-16, True, False) == "expired"


def test_validity_addon():
    assert validity_status(2, True, True) == "active"
