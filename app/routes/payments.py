from fastapi import APIRouter
from app.producer import send_payment_event
from app.schemas import PaymentRequest

# Rota - permite separar endpoints por responsabilidade
router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

# Equivalente ao POST /payments
@router.post("/")
def create_payment(payment: PaymentRequest):

    # O evento abaixo enviará apenas dados menos sensíveis para a fila
    event = {
        "card_holder": payment.card_holder,
        "card_last_digits": payment.card_number[-4:],
        "amount": payment.amount,
        "status": "RECEIVED"
    }

    # Publicação do evento
    send_payment_event(event)

    # Retorno ao usuário
    return {
        "message": "Pagamento enviado para processamento.",
        "event": event,
    }