from sqlalchemy.orm import relationship  
from .user import User
from .subscription import Subscription
from .payments import  Payment

User.subscription = relationship(
    "Subscription",
    back_populates="users",
    foreign_keys=[User.subscription_id]
)

Subscription.users = relationship(
    "User",
    back_populates="subscription",
    foreign_keys=[User.subscription_id]
)

User.payments = relationship(
    "Payment",
    back_populates="user",
    foreign_keys=[Payment.user_id]
)

Payment.user = relationship(
    "User",
    back_populates="payments",
    foreign_keys=[Payment.user_id]
)