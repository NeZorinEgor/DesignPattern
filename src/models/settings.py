class Settings:
    """ Модель настроек. """
    __INN: str = ""
    __ACCOUNT: str = ""
    __CORRESPONDENT_ACCOUNT: str = ""
    __BIC: str = ""
    __NAME: str = ""
    __TYPE_OF_OWNERSHIP: str = ""

    def __str__(self):
        return f"INN={self.__INN} \nACCOUNT={self.__ACCOUNT} \nCORRESPONDENT_ACCOUNT={self.__CORRESPONDENT_ACCOUNT} \nBIC={self.__BIC} \nNAME={self.__NAME} \nTYPE_OF_OWNERSHIP={self.__TYPE_OF_OWNERSHIP}"

    @property
    def INN(self) -> str:
        return self.__INN

    @INN.setter
    def INN(self, new_inn) -> None:
        if not isinstance(new_inn, str):
            raise TypeError("INN must be a string")
        if len(new_inn) != 12:
            raise ValueError(f"INN must be exactly 12 characters long, not {len(new_inn)}")

        self.__INN = new_inn

    @property
    def ACCOUNT(self) -> str:
        return self.__ACCOUNT

    @ACCOUNT.setter
    def ACCOUNT(self, new_account) -> None:
        if not isinstance(new_account, str):
            raise TypeError("ACCOUNT must be a string")
        if len(new_account) != 11:
            raise ValueError(f"ACCOUNT must be exactly 11 characters long, not {len(new_account)}")

        self.__ACCOUNT = new_account

    @property
    def CORRESPONDENT_ACCOUNT(self) -> str:
        return self.__CORRESPONDENT_ACCOUNT

    @CORRESPONDENT_ACCOUNT.setter
    def CORRESPONDENT_ACCOUNT(self, new_correspondent_account) -> None:
        if not isinstance(new_correspondent_account, str):
            raise TypeError("CORRESPONDENT_ACCOUNT must be a string")
        if len(new_correspondent_account) != 11:
            raise ValueError(f"CORRESPONDENT_ACCOUNT must be exactly 11 characters long, not {len(new_correspondent_account)}")

        self.__CORRESPONDENT_ACCOUNT = new_correspondent_account

    @property
    def BIC(self) -> str:
        return self.__BIC

    @BIC.setter
    def BIC(self, new_bic) -> None:
        if not isinstance(new_bic, str):
            raise TypeError("CORRESPONDENT_ACCOUNT must be a string")
        if len(new_bic) != 9:
            raise ValueError(f"BIC must be exactly 9 characters long, not {len(new_bic)}")

        self.__BIC = new_bic

    @property
    def NAME(self) -> str:
        return self.__NAME

    @NAME.setter
    def NAME(self, new_name) -> None:
        if not isinstance(new_name, str):
            raise TypeError("NAME must be a string")
        self.__NAME = new_name

    @property
    def TYPE_OF_OWNERSHIP(self) -> str:
        return self.__TYPE_OF_OWNERSHIP

    @TYPE_OF_OWNERSHIP.setter
    def TYPE_OF_OWNERSHIP(self, new_type_of_ownership) -> None:
        if not isinstance(new_type_of_ownership, str):
            raise TypeError("TYPE_OF_OWNERSHIP must be a string")
        if len(new_type_of_ownership) != 5:
            raise ValueError(f"TYPE_OF_OWNERSHIP must be exactly 5 characters long, not {len(new_type_of_ownership)}")
        self.__TYPE_OF_OWNERSHIP = new_type_of_ownership
