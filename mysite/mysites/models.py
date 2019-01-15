# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TAcceptOverdue(models.Model):
    id = models.BigAutoField(primary_key=True)
    org_id = models.BigIntegerField(blank=True, null=True)
    accept_min_day = models.SmallIntegerField(blank=True, null=True)
    accept_max_day = models.SmallIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    last_update_user = models.BigIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_accept_overdue'


class TApiAccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=32, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    org_id = models.BigIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_api_account'


class TApplyRelieve(models.Model):
    id = models.BigAutoField(primary_key=True)
    record_debt_id = models.BigIntegerField(blank=True, null=True)
    settlement_amount = models.IntegerField(blank=True, null=True)
    reject_reason = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_apply_relieve'


class TArea(models.Model):
    id = models.BigAutoField(primary_key=True)
    adcode = models.CharField(max_length=16, blank=True, null=True)
    parent_code = models.CharField(max_length=16, blank=True, null=True)
    name = models.CharField(max_length=16, blank=True, null=True)
    create_time = models.DateTimeField()
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_area'


class TArrearDebt(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_code = models.CharField(max_length=32, blank=True, null=True)
    creditor_id = models.BigIntegerField(blank=True, null=True)
    debtor_id = models.BigIntegerField(blank=True, null=True)
    should_refund_principal = models.IntegerField(blank=True, null=True)
    should_refund_interest = models.IntegerField(blank=True, null=True)
    should_refund_compensation = models.IntegerField(blank=True, null=True)
    should_refund_total = models.IntegerField(blank=True, null=True)
    relieve_amount = models.IntegerField(blank=True, null=True)
    already_refund_amount = models.IntegerField(blank=True, null=True)
    borrow_date = models.DateField(blank=True, null=True)
    should_refund_date = models.DateField(blank=True, null=True)
    overdue_day = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    last_sync_time = models.DateTimeField(blank=True, null=True)
    loan_business_department = models.CharField(max_length=32, blank=True, null=True)
    customer_manager = models.CharField(max_length=32, blank=True, null=True)
    customer_manager_mobile = models.CharField(max_length=16, blank=True, null=True)
    poundage = models.IntegerField(blank=True, null=True)
    poundage_compensation = models.IntegerField(blank=True, null=True)
    creditor_entrust_expire_time = models.DateTimeField(blank=True, null=True)
    funds_provider = models.CharField(max_length=32, blank=True, null=True)
    product_name = models.CharField(max_length=32, blank=True, null=True)
    product_code = models.CharField(max_length=32, blank=True, null=True)
    bill_no = models.CharField(max_length=256, blank=True, null=True)
    data_source = models.CharField(max_length=32, blank=True, null=True)
    pub_time = models.DateTimeField(blank=True, null=True)
    loan_agreement_url = models.CharField(max_length=128, blank=True, null=True)
    task_code_remark = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_arrear_debt'
        unique_together = (('task_code', 'creditor_id'),)


class TBlackDebtor(models.Model):
    id = models.BigAutoField(primary_key=True)
    card_type = models.IntegerField(blank=True, null=True)
    card_no = models.CharField(unique=True, max_length=32, blank=True, null=True)
    real_name = models.CharField(max_length=64, blank=True, null=True)
    reason = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_black_debtor'


class TBusinessDepartment(models.Model):
    id = models.BigAutoField(primary_key=True)
    business_city = models.CharField(max_length=32, blank=True, null=True)
    business_dept_name = models.CharField(unique=True, max_length=32, blank=True, null=True)
    business_dept_code = models.CharField(max_length=32, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_business_department'


class TClickRepairInfoCount(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    desc = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_click_repair_info_count'


class TCollectionAgencyDailyReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    org_id = models.BigIntegerField(blank=True, null=True)
    dept_id = models.BigIntegerField(blank=True, null=True)
    refund_total = models.BigIntegerField(blank=True, null=True)
    refund_record_count = models.IntegerField(blank=True, null=True)
    refund_debt_count = models.IntegerField(blank=True, null=True)
    refund_date = models.DateField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_collection_agency_daily_report'


class TCollectionEntrust(models.Model):
    id = models.BigAutoField(primary_key=True)
    debtor_id = models.BigIntegerField(blank=True, null=True)
    dept_id = models.BigIntegerField(blank=True, null=True)
    org_id = models.BigIntegerField(blank=True, null=True)
    dispatcher_id = models.BigIntegerField(blank=True, null=True)
    entrust_begin_time = models.DateTimeField(blank=True, null=True)
    entrust_expire_time = models.DateTimeField(blank=True, null=True)
    entrust_end_time = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    address_type = models.IntegerField(blank=True, null=True)
    already_refund_amount = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    abandon_reason = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    compete_address_longitude = models.FloatField(blank=True, null=True)
    compete_address_latitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_collection_entrust'


class TCollectionEntrustDebt(models.Model):
    id = models.BigAutoField(primary_key=True)
    debt_id = models.BigIntegerField(blank=True, null=True)
    entrust_id = models.BigIntegerField(blank=True, null=True)
    entrust_begin_time = models.DateTimeField(blank=True, null=True)
    entrust_expire_time = models.DateTimeField(blank=True, null=True)
    entrust_end_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_collection_entrust_debt'


class TCollectionRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    entrust_id = models.BigIntegerField(blank=True, null=True)
    recorder_id = models.BigIntegerField(blank=True, null=True)
    collection_way = models.IntegerField(blank=True, null=True)
    negotiater = models.IntegerField(blank=True, null=True)
    address_type = models.IntegerField(blank=True, null=True)
    current_place = models.CharField(max_length=128, blank=True, null=True)
    current_longitude = models.CharField(max_length=32, blank=True, null=True)
    current_latitude = models.CharField(max_length=32, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_collection_record'


class TCollectionRecordDebt(models.Model):
    id = models.BigAutoField(primary_key=True)
    record_id = models.BigIntegerField(blank=True, null=True)
    debt_id = models.BigIntegerField(blank=True, null=True)
    result = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_collection_record_debt'


class TCollectionRecordImg(models.Model):
    id = models.BigAutoField(primary_key=True)
    record_id = models.BigIntegerField(blank=True, null=True)
    img = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_collection_record_img'


class TCommissionDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    creditor_id = models.BigIntegerField(blank=True, null=True)
    org_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    dept_id = models.BigIntegerField(blank=True, null=True)
    refund_id = models.BigIntegerField(blank=True, null=True)
    overdue_day = models.SmallIntegerField(blank=True, null=True)
    commission_amout = models.IntegerField(blank=True, null=True)
    principal_commission = models.IntegerField(blank=True, null=True)
    interest_commission = models.IntegerField(blank=True, null=True)
    compensation_commission = models.IntegerField(blank=True, null=True)
    poundage_commission = models.IntegerField(blank=True, null=True)
    poundage_compensation_commission = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_commission_detail'


class TCommissionMonth(models.Model):
    id = models.BigAutoField(primary_key=True)
    creditor_id = models.BigIntegerField(blank=True, null=True)
    org_id = models.BigIntegerField(blank=True, null=True)
    settle_month = models.IntegerField(blank=True, null=True)
    sum_amout = models.BigIntegerField(blank=True, null=True)
    refund_principal = models.BigIntegerField(blank=True, null=True)
    refund_interest = models.BigIntegerField(blank=True, null=True)
    refund_compensation = models.BigIntegerField(blank=True, null=True)
    refund_poundage = models.BigIntegerField(blank=True, null=True)
    refund_poundage_compensation = models.BigIntegerField(blank=True, null=True)
    principal_commission = models.BigIntegerField(blank=True, null=True)
    interest_commission = models.BigIntegerField(blank=True, null=True)
    compensation_commission = models.BigIntegerField(blank=True, null=True)
    poundage_commission = models.BigIntegerField(blank=True, null=True)
    poundage_compensation_commission = models.BigIntegerField(blank=True, null=True)
    min_overdue_day = models.SmallIntegerField(blank=True, null=True)
    max_overdue_day = models.SmallIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_commission_month'


class TCommissionPay(models.Model):
    id = models.BigAutoField(primary_key=True)
    creditor_id = models.BigIntegerField(blank=True, null=True)
    settle_month = models.IntegerField(blank=True, null=True)
    pay_amout = models.IntegerField(blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    img = models.CharField(max_length=256, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_commission_pay'


class TCommissionRate(models.Model):
    id = models.BigAutoField(primary_key=True)
    org_id = models.BigIntegerField(blank=True, null=True)
    min_overdue_day = models.SmallIntegerField(blank=True, null=True)
    max_overdue_day = models.SmallIntegerField(blank=True, null=True)
    principal_rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    interest_rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    compensation_rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    poundage_rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    poundage_compensation_rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    last_update_user = models.BigIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_commission_rate'


class TContactInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    debtor_id = models.BigIntegerField(blank=True, null=True)
    real_name = models.CharField(max_length=64, blank=True, null=True)
    relationship = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_contact_info'


class TContactInfoDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    info = models.CharField(max_length=128, blank=True, null=True)
    info_type = models.IntegerField(blank=True, null=True)
    contact_info_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_contact_info_detail'


class TCreditInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    debtor_id = models.BigIntegerField(blank=True, null=True)
    org_id = models.BigIntegerField(blank=True, null=True)
    total_amount = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    business_department_city = models.CharField(max_length=32, blank=True, null=True)
    loan_business_department = models.CharField(max_length=32, blank=True, null=True)
    loan_business_dept_code = models.CharField(max_length=32, blank=True, null=True)
    bank_card = models.CharField(max_length=32, blank=True, null=True)
    business_apply_img = models.CharField(max_length=5120, blank=True, null=True)
    entrust_start_time = models.DateTimeField(blank=True, null=True)
    entrust_end_time = models.DateTimeField(blank=True, null=True)
    separate_hand = models.CharField(max_length=16, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    outer_debtor_id = models.CharField(max_length=64, blank=True, null=True)
    entrust_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_credit_info'
        unique_together = (('debtor_id', 'org_id'),)


class TCreditorBankInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    org_id = models.BigIntegerField(blank=True, null=True)
    pay_bank = models.CharField(max_length=32, blank=True, null=True)
    account_name = models.CharField(max_length=64, blank=True, null=True)
    account_no = models.CharField(max_length=32, blank=True, null=True)
    alipay_url = models.CharField(max_length=256, blank=True, null=True)
    alipay_name = models.CharField(max_length=16, blank=True, null=True)
    weipay_url = models.CharField(max_length=256, blank=True, null=True)
    weipay_name = models.CharField(max_length=16, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_creditor_bank_info'


class TCreditorRefundDailyReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    creditor_id = models.BigIntegerField(blank=True, null=True)
    refund_total = models.BigIntegerField(blank=True, null=True)
    refund_date = models.DateField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_creditor_refund_daily_report'


class TDebtor(models.Model):
    id = models.BigAutoField(primary_key=True)
    card_type = models.IntegerField(blank=True, null=True)
    card_no = models.CharField(unique=True, max_length=32, blank=True, null=True)
    real_name = models.CharField(max_length=64, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    marital_status = models.IntegerField(blank=True, null=True)
    children_status = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    mobile_status = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    qq = models.CharField(db_column='QQ', max_length=32, blank=True, null=True)  # Field name made lowercase.
    web_chat = models.CharField(max_length=32, blank=True, null=True)
    residence_province = models.CharField(max_length=16, blank=True, null=True)
    residence_city = models.CharField(max_length=16, blank=True, null=True)
    residence_area = models.CharField(max_length=16, blank=True, null=True)
    residence_address = models.CharField(max_length=128, blank=True, null=True)
    residence_longitude = models.FloatField(blank=True, null=True)
    residence_latitude = models.FloatField(blank=True, null=True)
    residence_status = models.IntegerField(blank=True, null=True)
    company_province = models.CharField(max_length=16, blank=True, null=True)
    company_city = models.CharField(max_length=16, blank=True, null=True)
    company_area = models.CharField(max_length=16, blank=True, null=True)
    company_address = models.CharField(max_length=128, blank=True, null=True)
    company_longitude = models.FloatField(blank=True, null=True)
    company_latitude = models.FloatField(blank=True, null=True)
    company_address_status = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=64, blank=True, null=True)
    present_province = models.CharField(max_length=16, blank=True, null=True)
    present_city = models.CharField(max_length=16, blank=True, null=True)
    present_area = models.CharField(max_length=16, blank=True, null=True)
    present_longitude = models.FloatField(blank=True, null=True)
    present_latitude = models.FloatField(blank=True, null=True)
    present_address = models.CharField(max_length=128, blank=True, null=True)
    present_address_status = models.IntegerField(blank=True, null=True)
    identity_img = models.CharField(max_length=2048, blank=True, null=True)
    debtor_img = models.CharField(max_length=2560, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    abandon_reason = models.CharField(max_length=128, blank=True, null=True)
    update_time = models.DateTimeField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_debtor'


class TDebtorInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    debtor_id = models.BigIntegerField(blank=True, null=True)
    residence_province = models.CharField(max_length=16, blank=True, null=True)
    residence_city = models.CharField(max_length=16, blank=True, null=True)
    residence_area = models.CharField(max_length=16, blank=True, null=True)
    residence_address = models.CharField(max_length=128, blank=True, null=True)
    residence_longitude = models.FloatField(blank=True, null=True)
    residence_latitude = models.FloatField(blank=True, null=True)
    residence_status = models.IntegerField(blank=True, null=True)
    company_province = models.CharField(max_length=16, blank=True, null=True)
    company_city = models.CharField(max_length=16, blank=True, null=True)
    company_area = models.CharField(max_length=16, blank=True, null=True)
    company_address = models.CharField(max_length=128, blank=True, null=True)
    company_longitude = models.FloatField(blank=True, null=True)
    company_latitude = models.FloatField(blank=True, null=True)
    company_address_status = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=64, blank=True, null=True)
    present_province = models.CharField(max_length=16, blank=True, null=True)
    present_city = models.CharField(max_length=16, blank=True, null=True)
    present_area = models.CharField(max_length=16, blank=True, null=True)
    present_longitude = models.FloatField(blank=True, null=True)
    present_latitude = models.FloatField(blank=True, null=True)
    present_address = models.CharField(max_length=128, blank=True, null=True)
    present_address_status = models.IntegerField(blank=True, null=True)
    real_name = models.CharField(max_length=64, blank=True, null=True)
    card_no = models.CharField(max_length=32, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    marital_status = models.IntegerField(blank=True, null=True)
    children_status = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    mobile_status = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    qq = models.CharField(db_column='QQ', max_length=32, blank=True, null=True)  # Field name made lowercase.
    web_chat = models.CharField(max_length=32, blank=True, null=True)
    identity_img = models.CharField(max_length=2048, blank=True, null=True)
    debtor_img = models.CharField(max_length=2560, blank=True, null=True)
    creditor_id = models.BigIntegerField(blank=True, null=True)
    update_time = models.DateTimeField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_debtor_info'
        unique_together = (('debtor_id', 'creditor_id'),)


class TDebtorUrgentContactor(models.Model):
    id = models.BigAutoField(primary_key=True)
    debtor_id = models.BigIntegerField(blank=True, null=True)
    debt_id = models.BigIntegerField(blank=True, null=True)
    real_name = models.CharField(max_length=64, blank=True, null=True)
    relationship = models.CharField(max_length=16, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    mobile_status = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_debtor_urgent_contactor'


class TDeptWithdraw(models.Model):
    id = models.BigAutoField(primary_key=True)
    debt_id = models.BigIntegerField(blank=True, null=True)
    withdrawer = models.BigIntegerField(blank=True, null=True)
    withdrawer_mobile = models.CharField(max_length=16, blank=True, null=True)
    reason = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_dept_withdraw'


class TEntrustArgsSetting(models.Model):
    id = models.BigAutoField(primary_key=True)
    org_id = models.BigIntegerField(blank=True, null=True)
    expire_day = models.SmallIntegerField(blank=True, null=True)
    fin_remain_max_money = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    last_update_user = models.BigIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_entrust_args_setting'


class TFeedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=120, blank=True, null=True)
    submitter = models.BigIntegerField(blank=True, null=True)
    submit_time = models.DateTimeField(blank=True, null=True)
    reply = models.CharField(max_length=120, blank=True, null=True)
    respondent = models.BigIntegerField(blank=True, null=True)
    reply_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_feedback'


class TFinDebtRepayRate(models.Model):
    id = models.BigAutoField(primary_key=True)
    org_id = models.BigIntegerField(blank=True, null=True)
    start_money = models.IntegerField(blank=True, null=True)
    end_money = models.IntegerField(blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    last_update_user = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_fin_debt_repay_rate'


class TFirstpartyOutsourceRelation(models.Model):
    id = models.BigAutoField(primary_key=True)
    creditor_id = models.BigIntegerField()
    org_id = models.BigIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_firstparty_outsource_relation'


class TFrozedUserRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    mobile = models.CharField(max_length=32, blank=True, null=True)
    real_name = models.CharField(max_length=64, blank=True, null=True)
    frozed_time = models.DateTimeField(blank=True, null=True)
    unlock_time = models.DateTimeField()
    belong_district = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_frozed_user_record'


class TGuarantor(models.Model):
    id = models.BigAutoField(primary_key=True)
    debt_id = models.BigIntegerField(blank=True, null=True)
    card_img = models.CharField(max_length=256, blank=True, null=True)
    card_type = models.IntegerField(blank=True, null=True)
    card_no = models.CharField(max_length=32, blank=True, null=True)
    real_name = models.CharField(max_length=64, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    mobile_status = models.IntegerField(blank=True, null=True)
    company_province = models.CharField(max_length=16, blank=True, null=True)
    company_city = models.CharField(max_length=16, blank=True, null=True)
    company_area = models.CharField(max_length=16, blank=True, null=True)
    company_address = models.CharField(max_length=128, blank=True, null=True)
    company_longitude = models.FloatField(blank=True, null=True)
    company_latitude = models.FloatField(blank=True, null=True)
    company_address_status = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=16, blank=True, null=True)
    present_province = models.CharField(max_length=16, blank=True, null=True)
    present_city = models.CharField(max_length=16, blank=True, null=True)
    present_area = models.CharField(max_length=16, blank=True, null=True)
    present_longitude = models.FloatField(blank=True, null=True)
    present_latitude = models.FloatField(blank=True, null=True)
    present_address = models.CharField(max_length=128, blank=True, null=True)
    present_address_status = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_guarantor'


class TMenuConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent_id = models.BigIntegerField(blank=True, null=True)
    value = models.CharField(max_length=128, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    desc = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_menu_config'


class TNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_code = models.CharField(max_length=16, blank=True, null=True)
    product_code = models.CharField(max_length=32, blank=True, null=True)
    product_name = models.CharField(max_length=32, blank=True, null=True)
    data_source = models.CharField(max_length=32, blank=True, null=True)
    bill_no = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_new'


class TNoProgress(models.Model):
    id = models.BigAutoField(primary_key=True)
    record_debt_id = models.BigIntegerField(blank=True, null=True)
    debtor_id = models.BigIntegerField(blank=True, null=True)
    dial_mobile = models.CharField(max_length=50, blank=True, null=True)
    dial_mobile_condition = models.CharField(max_length=20, blank=True, null=True)
    visit_address = models.CharField(max_length=128, blank=True, null=True)
    visit_address_condition = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_no_progress'


class TNotice(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=16)
    content = models.CharField(max_length=512, blank=True, null=True)
    sender_mobile = models.CharField(max_length=16, blank=True, null=True)
    sender_name = models.CharField(max_length=16, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_notice'


class TOperationLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    req_ip = models.CharField(max_length=16, blank=True, null=True)
    req_url = models.CharField(max_length=256, blank=True, null=True)
    req_args = models.CharField(max_length=512, blank=True, null=True)
    opr_time = models.DateTimeField(blank=True, null=True)
    opr_result = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=512, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_operation_log'


class TOrganizationDepartment(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    org_id = models.BigIntegerField()
    parent_id = models.BigIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_organization_department'
        unique_together = (('name', 'org_id'),)


class TPlatformBankInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    pay_bank = models.CharField(max_length=32, blank=True, null=True)
    account_name = models.CharField(max_length=64, blank=True, null=True)
    account_no = models.CharField(max_length=32, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_platform_bank_info'


class TPromiseRefund(models.Model):
    id = models.BigAutoField(primary_key=True)
    record_debt_id = models.BigIntegerField(blank=True, null=True)
    promise_refund_date = models.DateTimeField(blank=True, null=True)
    promise_refund_amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_promise_refund'


class TRefund(models.Model):
    id = models.BigAutoField(primary_key=True)
    serial_num = models.CharField(max_length=128, blank=True, null=True)
    creditor_id = models.BigIntegerField(blank=True, null=True)
    debt_id = models.BigIntegerField(blank=True, null=True)
    refund_total = models.IntegerField(blank=True, null=True)
    refund_principal = models.IntegerField(blank=True, null=True)
    refund_interest = models.IntegerField(blank=True, null=True)
    refund_compensation = models.IntegerField(blank=True, null=True)
    refund_poundage = models.IntegerField(blank=True, null=True)
    refund_poundage_compensation = models.IntegerField(blank=True, null=True)
    refund_way = models.IntegerField(blank=True, null=True)
    refund_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    actual_refund_total = models.IntegerField(blank=True, null=True)
    is_clear = models.IntegerField(db_column='IS_CLEAR', blank=True, null=True)  # Field name made lowercase.
    push_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_refund'


class TRefundRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    record_debt_id = models.BigIntegerField(blank=True, null=True)
    refund_amount = models.IntegerField(blank=True, null=True)
    refund_way = models.IntegerField(blank=True, null=True)
    refund_id = models.BigIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    bank_card = models.CharField(max_length=30, blank=True, null=True)
    refund_time = models.DateTimeField(blank=True, null=True)
    pay_money_way = models.IntegerField(blank=True, null=True)
    pay_money_name = models.CharField(max_length=20, blank=True, null=True)
    pay_money_bank = models.CharField(max_length=50, blank=True, null=True)
    update_time = models.DateTimeField()
    reason = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_refund_record'


class TRelievableRate(models.Model):
    id = models.BigAutoField(primary_key=True)
    org_id = models.BigIntegerField(blank=True, null=True)
    min_overdue_day = models.SmallIntegerField(blank=True, null=True)
    max_overdue_day = models.SmallIntegerField(blank=True, null=True)
    principal_rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    interest_rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    compensation_rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    last_update_user = models.BigIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_relievable_rate'


class TRepairDebtorActiveAddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    debtor_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()
    address = models.CharField(max_length=128, blank=True, null=True)
    address_status = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    repair_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    type = models.IntegerField(blank=True, null=True)
    longitude = models.CharField(max_length=32, blank=True, null=True)
    latitude = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_repair_debtor_active_address'
        unique_together = (('debtor_id', 'type'),)


class TRepairDebtorInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    debtor_id = models.BigIntegerField(unique=True, blank=True, null=True)
    user_id = models.BigIntegerField()
    mobile = models.CharField(max_length=16, blank=True, null=True)
    mobile_status = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    address_status = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=128, blank=True, null=True)
    company_name_status = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    repair_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_repair_debtor_info'


class TResource(models.Model):
    id = models.BigIntegerField(primary_key=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    status = models.IntegerField()
    code = models.CharField(max_length=255, blank=True, null=True)
    depth = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    seq = models.BigIntegerField(blank=True, null=True)
    sup_id = models.BigIntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    drop_down = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_resource'


class TRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField()
    parent_id = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    org_id = models.BigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_role'


class TRoleResource(models.Model):
    id = models.BigAutoField(primary_key=True)
    role_id = models.BigIntegerField()
    res_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 't_role_resource'


class TSms(models.Model):
    id = models.BigAutoField(primary_key=True)
    biz_no = models.CharField(max_length=10)
    sp_id = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    content = models.CharField(max_length=256, blank=True, null=True)
    send_status = models.IntegerField(blank=True, null=True)
    req_time = models.DateTimeField(blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_sms'


class TSysMessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=32, blank=True, null=True)
    content = models.CharField(max_length=1024, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    event_id = models.BigIntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_sys_message'


class TSysMessageUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    msg_id = models.BigIntegerField(blank=True, null=True)
    read_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_sys_message_user'


class TSysOrganization(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    contact_name = models.CharField(max_length=32, blank=True, null=True)
    contact_mobile = models.CharField(max_length=16, blank=True, null=True)
    contact_email = models.CharField(max_length=64, blank=True, null=True)
    org_type = models.SmallIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_sys_organization'


class TSysUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    account = models.CharField(max_length=32, blank=True, null=True)
    card_type = models.IntegerField(blank=True, null=True)
    card_no = models.CharField(max_length=32, blank=True, null=True)
    real_name = models.CharField(max_length=64, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    head_img = models.CharField(max_length=256, blank=True, null=True)
    mobile = models.CharField(unique=True, max_length=16, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    pwd = models.CharField(max_length=128, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    push_status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    org_id = models.BigIntegerField(blank=True, null=True)
    dept_id = models.BigIntegerField(blank=True, null=True)
    belong_district = models.CharField(max_length=200, blank=True, null=True)
    city_manager = models.IntegerField(blank=True, null=True)
    adcode = models.CharField(max_length=16, blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_sys_user'


class TTemp(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    time = models.DateTimeField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_temp'


class TTemp2(models.Model):
    id = models.BigAutoField(primary_key=True)
    debtor_id = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 't_temp2'


class TTempCard(models.Model):
    id = models.BigAutoField(primary_key=True)
    card_no = models.CharField(max_length=32)

    class Meta:
        managed = True
        db_table = 't_temp_card'


class TTempMobile(models.Model):
    mobile = models.CharField(max_length=16)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_temp_mobile'


class TTempMobile2(models.Model):
    mobile = models.CharField(max_length=16)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_temp_mobile2'


class TTempTaskCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_code = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_temp_task_code'


class TTempTaskCode2(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_code = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_temp_task_code2'


class TTempTaskCode3(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_code = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_temp_task_code3'


class TUserRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    role_id = models.BigIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_user_role'


class TValidAddressCount(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    desc = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    debtor_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_valid_address_count'


class TValidAddressInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    debtor_info_id = models.BigIntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    debtor_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_valid_address_info'


class TValidAddressRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    debtor_id = models.BigIntegerField(blank=True, null=True)
    result = models.CharField(max_length=500, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_valid_address_record'








