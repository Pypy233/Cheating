import random
import csv



break_rule = False
break_rate = 8
no_guarantee_rate = 20

load_avg = 50
year_rate_avg = 4.9
apply_avg = 7
year_avg = 1.5

credit_rate = ['AA', 'A', 'B', 'C']


data_cnt = 300




file_name = 'fake_generator.csv'
f = open(file_name, 'w')
f_writer = csv.writer(f)
f_writer.writerow(['违约', '信用贷款', '抵押物价值', '贷款金额',
                   '年利率', '信用评级', '等级取值', '申请次数', '成功次数', '还清次数'])

def prob(a):
    ret = random.choice(range(1, 101))

    if ret <= a:
        return True
    return False


for i in range(data_cnt//2):
    break_rule0 = 1 if prob(break_rate) else 0
    guarantee_val_r0 = 0 if prob(no_guarantee_rate) else 1

    guarantee_val0 = 0
    guarantee_val1 = 0

    break_rule1 = 1 if prob(break_rate) else 0
    guarantee_val_r1 = 0 if prob(no_guarantee_rate) else 1

    load_amt0 = round(random.uniform(2, 200), 2)
    load_amt1 = round(load_avg * 2 - load_amt0, 2)

    if load_amt1 < 0:
        load_amt1 = round(random.uniform(2, 4), 2)
        load_amt0 = round(load_amt0 - random.choice(range(10, 30)), 2)
    if guarantee_val_r0 != 0:
        guarantee_val0 = round(random.uniform(load_amt0, load_amt0 * 2), 2)

    if guarantee_val_r1 != 0:
        guarantee_val1 = round(random.uniform(load_amt1, load_amt1 * 2), 2)

    year_rate0 = round(random.uniform(4.35, 6), 2)
    year_rate1 = round(year_rate_avg * 2 - year_rate0, 2)

    apply_cnt0 = random.randint(1, 12)
    apply_cnt1 = apply_avg * 2 - apply_cnt0

    cre0 = random.choice(credit_rate)
    cre1 = random.choice(credit_rate)

    cre_val0 = 7 - credit_rate.index(cre0)
    cre_val1 = 7 - credit_rate.index(cre1)

    suc_cnt0 = cre_val0 - 7 + apply_cnt0
    suc_cnt1 = cre_val1 - 7 + apply_cnt1

    if suc_cnt0 < 0:
        suc_cnt0 = random.choice(range(0, 1))
    if suc_cnt1 < 0:
        suc_cnt1 = random.choice(range(0, 1))

    repay_cnt0 = suc_cnt0 - random.choice(range(0, 7 - cre_val0 + 1))
    repay_cnt1 = suc_cnt1 - random.choice(range(0, 7 - cre_val1 + 1))

    if repay_cnt0 < 0:
        repay_cnt0 = random.choice(range(0, 1))
    if repay_cnt1 < 0:
        repay_cnt1 = random.choice(range(0, 1))

    r0 = [break_rule0, guarantee_val_r0, guarantee_val0, load_amt0, year_rate0, cre0, cre_val0, apply_cnt0, suc_cnt0, repay_cnt0]

    r1 = [break_rule1, guarantee_val_r1, guarantee_val1, load_amt1, year_rate1, cre1, cre_val1, apply_cnt1, suc_cnt1, repay_cnt1]

    f_writer.writerow(r0)
    f_writer.writerow(r1)
