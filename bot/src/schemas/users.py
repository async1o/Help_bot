from pydantic import BaseModel

class UserSchema(BaseModel):
    user_id: str
    full_name: str = None
    is_operator: bool
    is_admin: bool
