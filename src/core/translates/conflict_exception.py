from dataclasses import dataclass


@dataclass
class ConflictExcTrans:
    another_user_with_same_national_code_already_exists: str = 'کاربر دیگری با این کد ملی وجود دارد '
    party_and_counter_party_are_same: str = 'طرف اول و دوم قرارداد نمیتوانند یکسان باشند '
    party_type_already_exists: str = "نوع طرف قراارداد قبلا تعیین شده است"
    contract_party_already_signed: str = 'طرف قرارداد قبلا امضا کرده است'
    otp_rate_limit_exceeded: str = "تعداد دخخوست های ارسالی بیش از حد مجاز است پس از مدی دوباه سعی کنید"
    role_already_exists: str = "نقش قبلا اضافه شده است"
    bank_account_already_exists: str = "حساب بانکی قبلا اضافه شده است"
