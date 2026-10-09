from datetime import datetime
from pydantic import BaseModel, field_validator

class PaymentRequest(BaseModel):
    card_holder: str
    card_number: str
    expiration_date: str
    cvv: str
    amount: float

    @field_validator("card_holder")
    @classmethod
    def validate_card_holder(cls, value: str) -> str:

        value = value.strip()

        if len(value) < 3:
            raise ValueError(
                "O nome do titular deve possuir pelo menos 3 caracteres."
            )

        return value

    @field_validator("card_number")
    @classmethod
    def validate_card_number(cls, value: str) -> str:
        if not value.isdigit():
            raise ValueError(
                "O número do cartão deve conter apenas números."
            )

        if len(value) != 16:
            raise ValueError(
                "O cartão deve possuir 16 dígitos"
            )

        return value

    @field_validator("cvv")
    @classmethod
    def validate_cvv(cls, value: str) -> str:
        if not value.isdigit():
            raise ValueError(
                "O CVV deve conter apenas números."
            )

        if len(value) != 3:
            raise ValueError(
                "O CVV deve possuir 3 dígitos."
            )

        return value

    @field_validator("expiration_date")
    @classmethod
    def validate_expiration_date(
        cls, value: str
    ) -> str:

        try:
            expiration = datetime.strptime(
                value, "%m/%Y"
            )
        except ValueError:
            raise ValueError(
                "Formato deve ser MM/YYYY."
            )

        current_date = datetime.now()

        current_reference = (
            current_date.year,
            current_date.month
        )

        expiration_reference = (
            expiration.year,
            expiration.month
        )

        if expiration_reference < current_reference:
            raise ValueError(
                "Cartão vencido."
            )

        return value

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, value: float) -> float:

        if value <= 0:
            raise ValueError(
                "O valor da compra deve ser maior que zero."
            )

        return value