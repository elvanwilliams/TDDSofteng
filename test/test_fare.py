import pytest
from src.fare import compute_food_delivery

def test_amount_under_10():
    assert compute_food_delivery(
        amount_orders=8,
        isPeakHours=True,
        isMembership=True,
        delivery_distance=10,
    ) == 11

def test_amount_under_10_2():
    assert compute_food_delivery(
        amount_orders=8,
        isPeakHours=True,
        isMembership=False,
        delivery_distance=10,
    ) == 13

def test_amount_under_10_3():
    assert compute_food_delivery(
        amount_orders=8,
        isPeakHours=True,
        isMembership=True,
        delivery_distance=21,
    ) == -1

def test_amount_under_10_4():
    assert compute_food_delivery(
        amount_orders=8,
        isPeakHours=True,
        isMembership=False,
        delivery_distance=21,
    ) == -1

#-----------------------------------------------------
#def test_amount_under_10_5():
def test_amount_under_10_5():
    assert compute_food_delivery(
        amount_orders=8,
        isPeakHours=False,
        isMembership=True,
        delivery_distance=10,
    ) == 11

#def test_amount_under_10_6():
def test_amount_under_10_6():
    assert compute_food_delivery(
        amount_orders=8,
        isPeakHours=False,
        isMembership=False,
        delivery_distance=10,
    ) == 11

#def test_amount_under_10_7():
def test_amount_under_10_7():
    assert compute_food_delivery(
        amount_orders=8,
        isPeakHours=False,
        isMembership=True,
        delivery_distance=21,
    ) == -1


#def test_amount_under_10_8():
def test_amount_under_10_8():
    assert compute_food_delivery(
        amount_orders=8,
        isPeakHours=False,
        isMembership=False,
        delivery_distance=21,
    ) == -1

#----------------------------------------

#def test_amount_between_10-50():
def test_amount_between_10_50():
    assert compute_food_delivery(
        amount_orders=10,
        isPeakHours=True,
        isMembership=True,
        delivery_distance=10,
    ) == 10

#def test_amount_between_10-50_2():
def test_amount_between_10_50_2():
    assert compute_food_delivery(
        amount_orders=10,
        isPeakHours=True,
        isMembership=False,
        delivery_distance=10,
    ) == 12


#def test_amount_between_10-50_3():
def test_amount_between_10_50_3():
    assert compute_food_delivery(
        amount_orders=10,
        isPeakHours=True,
        isMembership=True,
        delivery_distance=21,
    ) == -1

#def test_amount_between_10-50_4():
def test_amount_between_10_50_4():
    assert compute_food_delivery(
        amount_orders=10,
        isPeakHours=True,
        isMembership=False,
        delivery_distance=21,
    ) == -1

#def test_amount_between_10-50_5():
def test_amount_between_10_50_5():
    assert compute_food_delivery(
        amount_orders=10,
        isPeakHours=False,
        isMembership=True,
        delivery_distance=10,
    ) == 10

#def test_amount_between_10-50_6():
def test_amount_between_10_50_6():
    assert compute_food_delivery(
        amount_orders=10,
        isPeakHours=False,
        isMembership=False,
        delivery_distance=10,
    ) == 10

#def test_amount_between_10-50_7():
def test_amount_between_10_50_7():
    assert compute_food_delivery(
        amount_orders=10,
        isPeakHours=False,
        isMembership=True,
        delivery_distance=21,
    ) == -1

#def test_amount_between_10-50_8():
def test_amount_between_10_50_8():
    assert compute_food_delivery(
        amount_orders=10,
        isPeakHours=False,
        isMembership=False,
        delivery_distance=21,
    ) == -1

#----------------------------------------
#def test_amount_above_50():
def test_amount_above_50():
    assert compute_food_delivery(
        amount_orders=51,
        isPeakHours=True,
        isMembership=True,
        delivery_distance=10,
    ) == 51

#def test_amount_above_50_2():
def test_amount_above_50_2():
    assert compute_food_delivery(
        amount_orders=51,
        isPeakHours=True,
        isMembership=False,
        delivery_distance=10,
    ) == 51

#def test_amount_above_50_3():
def test_amount_above_50_3():
    assert compute_food_delivery(
        amount_orders=51,
        isPeakHours=True,
        isMembership=True,
        delivery_distance=21,
    ) == -1

#def test_amount_above_50_4():
def test_amount_above_50_4():
    assert compute_food_delivery(
        amount_orders=51,
        isPeakHours=True,
        isMembership=False,
        delivery_distance=21,
    ) == -1

#def test_amount_above_50_5():
def test_amount_above_50_5():
    assert compute_food_delivery(
        amount_orders=51,
        isPeakHours=False,
        isMembership=True,
        delivery_distance=10,
    ) == 51

#def test_amount_above_50_6():
def test_amount_above_50_6():
    assert compute_food_delivery(
        amount_orders=51,
        isPeakHours=False,
        isMembership=False,
        delivery_distance=10,
    ) == 51

#def test_amount_above_50_7():
def test_amount_above_50_7():
    assert compute_food_delivery(
        amount_orders=51,
        isPeakHours=False,
        isMembership=True,
        delivery_distance=21,
    ) == -1

#def test_amount_above_50_8():
def test_amount_above_50_8():
    assert compute_food_delivery(
        amount_orders=51,
        isPeakHours=False,
        isMembership=False,
        delivery_distance=21,
    ) == -1
#random test
def test_amount_under_10_9():
    assert compute_food_delivery(
        amount_orders=7,
        isPeakHours=False,
        isMembership=True,
        delivery_distance=10
    ) == 10

def test_amount_under_10_10():
    assert compute_food_delivery(
        amount_orders=1,
        isPeakHours=True,
        isMembership=True,
        delivery_distance=10
    ) == 4

def test_amount_between_10_50_9():
    assert compute_food_delivery(
        amount_orders=15,
        isPeakHours=False,
        isMembership=False,
        delivery_distance=10,
    ) == 15

def test_amount_between_10_50_10():
    assert compute_food_delivery(
        amount_orders=45,
        isPeakHours=True,
        isMembership=False,
        delivery_distance=15,
    ) == 47

def test_amount_above_50_9():
    assert compute_food_delivery(
        amount_orders=58,
        isPeakHours=False,
        isMembership=True,
        delivery_distance=10,
    ) == 58