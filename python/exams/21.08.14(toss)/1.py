import math

def solution(orderAmount, taxFreeAmount, serviceFee):
    # orderAmount : 주문금액
    # taxFreeAmount : 비과세금액
    # serviceFee : 봉사료
    # 부가가치세를 구하기

    supplyAmount = getSupplyAmount(orderAmount, taxFreeAmount, serviceFee)

    pureSupplyAmount = supplyAmount - taxFreeAmount

    if pureSupplyAmount == 1:
        return 0

    return math.ceil(pureSupplyAmount/10)


def getSupplyAmount(orderAmount, taxFreeAmount, serviceFee):
    orderAmountexceptServiceFee = orderAmount - serviceFee
    supplyAmount = ((10 * orderAmountexceptServiceFee) + taxFreeAmount)/11
    return supplyAmount

