from pydantic import BaseModel


class EchoBody(BaseModel):
    content: str
    sender_com_id: str
    receiver_com_id: str
