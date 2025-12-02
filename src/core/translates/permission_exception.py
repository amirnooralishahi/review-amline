from dataclasses import dataclass


@dataclass
class PermExcTrans :
    insufficient_credit = "موجودی کیف پول کافی نیست"
    access_denied='عدم دسترسی '
    request_already_submitted = 'درخواست قبلا ثبت شده'
    user_doe_not_have_enough_permission="کاربر دسترسی کافی برای انجام این عملیات را ندارد"
    deposit_amount_not_set = "مبلغ رهن قرارداد مشخص نشده"
    rent_amount_not_set="مبلغ اجاره قرارداد مشخص نشده"
    contract_second_side_not_set="طرف دوم قرارداد مشخص نشده"
    contract_dates_not_set = "تاریخ شروع و پایان قرارداد مشخص نشده"
    invoice_already_paid = 'این فاکتور قبلا پرداخت شده است'
    settlement_already_sttleted = ' تسویه در وضعیت در انتظار تایید نیست '
    forbidden_action= 'عملیات غیرمجاز'
    promo_code_already_user = 'کدتخفیف قبلا استفاده شده'
    invalid_promo_code = "کد تخفیف نامعتبر است "
    only_one_promo_code_per_invoice = 'هر فاکتور می تواند یک کد تخفیف داشته باشد'
    party_is_not_contract_owner = "کاربر شروع کننده قرارداد نیست"
    user_is_not_contract_party="کاربر طرف قرار داد نیست"
    user_cannot_sign_contract='کاربر نمیتواند قرارداد را امضا کند'
    contract_is_not_editable = "قرارداد غیر قابل ویرایش است"
    contract_steps_incomplete_for_tenant_approval= "مراحل قرار داد برا تایید مستاجر کامل نشده است   "
    contract_status_must_be_admin_approved='ادمین باید قررارداد را تایید کرده باشد'
    tracking_code_status_cannot_be_changed = 'وضعیت کدرهگیری قابل تغییر نیست'
    contract_clause_is_read_only='این بنبد قرارداد غیرقابل ویرایش است'
    tenant_should_e_contract_owner_to_approve= 'مستاجر باید صاحب قرارداد باشد تا بتواند قرارداد را تایید کند '
    landlord_cant_sign_contract = 'مالک نمیتواند قرارداد را امضا کند'
    party_cannot_pay_commission='طرف قرارداد نمی تواند کمیسیونپرداخت کند'
    contract_steps_is_not_completed_for_admin_approval="هوز نوبت تایید کارشناس حقوقی نرسیده"
    contract_should_be_approved_by_admin_first = 'قرارداد باید ابتدا وسط کارشناس حقوقی تایید شود'
    contract_steps_is_not_completed_for_requesting_tracking_code='مراحل قرارداد برای درخواست کد رهگیری کامل نشده است'
    contract_owner_cannot_reject_contract='صاحب قرارداد نمیتواند قرارداد را رد کند'
    rejected_contract_cannot_changes= "قرارداد رد شده قابل تغییر نیست"
    party_is_not_tenant="طرف قرار داد مستاجر نیست"
    party_is_not_landlord='طرف قرارداد مالک نیست'
    missing_required_steps="عدم تکمیل مراحل مورد نیاز"
    user_is_not_payment_payer = "شما پرداخت کننده این پرداخت نیستید"
    user_is_not_payment_payee='شما دریافت کننده این پرداخت نیستید'
    rent_payment_already_finalized=" پرداخت های رهن قبلا نهایی شده است"
    deposit_payment_already_finalized = 'پرداخت های رهن قبلا نهایی شده اتس'
    contract_owner_cannot_edit_request = 'صاحب قرار داد نمیتواند درخواست ورایش قرار داد دهد '
    commission_payment_cannot_be_deleted_directly = 'پرداخت کمیسیون نمیتواند مستقیما حذف شود'
    only__rend_and_deposit_payment_types_are_allowed='در حال حاضر فقط پرداخت های اجاره و رهن مجاز هستند '
    you_are_not_allowed_to_perform_this_action = 'شما مجاز به انجا این عملیات نیستید'
    settlement_already_rejected= "درخواست قبلا رد شده و ااعتبار کاربر به کیف پولش بازگشته"
    