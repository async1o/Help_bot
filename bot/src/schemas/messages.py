from pydantic import BaseModel

class MsgSchema(BaseModel):
    message_id: int
    text: str
    operator_id: str
    sender_id: str