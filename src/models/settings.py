from src.errors.custom import InvalidTypeError, InvalidLengthError


class Settings:
    """Модель настроек с кастомными ошибками."""
    __inn: str = ""
    __account: str = ""
    __correspondent_account: str = ""
    __bic: str = ""
    __name: str = ""
    __type_of_ownership: str = ""

    def __str__(self):
        return (f"INN: {self.__inn} \nACCOUNT: {self.__account} \n"
                f"CORRESPONDENT_ACCOUNT: {self.__correspondent_account} \n"
                f"BIC: {self.__bic} \nNAME: {self.__name} \n"
                f"TYPE_OF_OWNERSHIP: {self.__type_of_ownership}")

    @property
    def inn(self) -> str:
        return self.__inn

    @inn.setter
    def inn(self, new_inn) -> None:
        if not isinstance(new_inn, str):
            raise InvalidTypeError("INN must be a string")
        if len(new_inn) != 12:
            raise InvalidLengthError(f"INN must be exactly 12 characters long, not {len(new_inn)}")
        self.__inn = new_inn

    @property
    def account(self) -> str:
        return self.__account

    @account.setter
    def account(self, new_account) -> None:
        if not isinstance(new_account, str):
            raise InvalidTypeError("ACCOUNT must be a string")
        if len(new_account) != 11:
            raise InvalidLengthError(f"ACCOUNT must be exactly 11 characters long, not {len(new_account)}")
        self.__account = new_account

    @property
    def correspondent_account(self) -> str:
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, new_correspondent_account) -> None:
        if not isinstance(new_correspondent_account, str):
            raise InvalidTypeError("CORRESPONDENT_ACCOUNT must be a string")
        if len(new_correspondent_account) != 11:
            raise InvalidLengthError(f"CORRESPONDENT_ACCOUNT must be exactly 11 characters long, not {len(new_correspondent_account)}")
        self.__correspondent_account = new_correspondent_account

    @property
    def bic(self) -> str:
        return self.__bic

    @bic.setter
    def bic(self, new_bic) -> None:
        if not isinstance(new_bic, str):
            raise InvalidTypeError("BIC must be a string")
        if len(new_bic) != 9:
            raise InvalidLengthError(f"BIC must be exactly 9 characters long, not {len(new_bic)}")
        self.__bic = new_bic

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name) -> None:
        if not isinstance(new_name, str):
            raise InvalidTypeError("NAME must be a string")
        self.__name = new_name

    @property
    def type_of_ownership(self) -> str:
        return self.__type_of_ownership

    @type_of_ownership.setter
    def type_of_ownership(self, new_type_of_ownership) -> None:
        if not isinstance(new_type_of_ownership, str):
            raise InvalidTypeError("TYPE_OF_OWNERSHIP must be a string")
        if len(new_type_of_ownership) != 5:
            raise InvalidLengthError(f"TYPE_OF_OWNERSHIP must be exactly 5 characters long, not {len(new_type_of_ownership)}")
        self.__type_of_ownership = new_type_of_ownership
