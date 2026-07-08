from sqlalchemy import Column, Integer, String
from .database import Base


# ==========================================
# USERS TABLE
# ==========================================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15), nullable=False)
    password = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)


# ==========================================
# RESTAURANTS TABLE
# ==========================================
class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    owner = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15), nullable=False)
    address = Column(String(255), nullable=False)


# ==========================================
# CATEGORIES TABLE
# ==========================================
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(255), nullable=False)


# ==========================================
# FOOD ITEMS TABLE
# ==========================================
class FoodItem(Base):
    __tablename__ = "food_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    restaurant = Column(String(100), nullable=False)
    category = Column(String(100), nullable=False)


# ==========================================
# CART TABLE
# ==========================================
class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100), nullable=False)
    food_name = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Integer, nullable=False)


# ==========================================
# ORDERS TABLE
# ==========================================
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100), nullable=False)
    order_date = Column(String(50), nullable=False)
    total_amount = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False)


# ==========================================
# ORDER ITEMS TABLE
# ==========================================
class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, nullable=False)
    food_name = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)


# ==========================================
# PAYMENTS TABLE
# ==========================================
class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, nullable=False)
    payment_method = Column(String(50), nullable=False)
    payment_status = Column(String(50), nullable=False)
    amount = Column(Integer, nullable=False)


# ==========================================
# DELIVERIES TABLE
# ==========================================
class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, nullable=False)
    delivery_person = Column(String(100), nullable=False)
    delivery_status = Column(String(50), nullable=False)
    delivery_address = Column(String(255), nullable=False)


# ==========================================
# REVIEWS TABLE
# ==========================================
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100), nullable=False)
    restaurant_name = Column(String(100), nullable=False)
    rating = Column(Integer, nullable=False)
    review = Column(String(255), nullable=False)