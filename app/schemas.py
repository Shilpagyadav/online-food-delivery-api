from pydantic import BaseModel, EmailStr


# =====================================================
# USER SCHEMAS
# =====================================================

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str
    address: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    address: str

    class Config:
        from_attributes = True


# =====================================================
# RESTAURANT SCHEMAS
# =====================================================

class RestaurantCreate(BaseModel):
    name: str
    owner: str
    email: EmailStr
    phone: str
    address: str


class RestaurantResponse(BaseModel):
    id: int
    name: str
    owner: str
    email: EmailStr
    phone: str
    address: str

    class Config:
        from_attributes = True


# =====================================================
# CATEGORY SCHEMAS
# =====================================================

class CategoryCreate(BaseModel):
    name: str
    description: str


class CategoryResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True


# =====================================================
# FOOD ITEM SCHEMAS
# =====================================================

class FoodItemCreate(BaseModel):
    name: str
    description: str
    price: int
    restaurant: str
    category: str


class FoodItemResponse(BaseModel):
    id: int
    name: str
    description: str
    price: int
    restaurant: str
    category: str

    class Config:
        from_attributes = True


# =====================================================
# CART SCHEMAS
# =====================================================

class CartCreate(BaseModel):
    user_name: str
    food_name: str
    quantity: int
    total_price: int


class CartResponse(BaseModel):
    id: int
    user_name: str
    food_name: str
    quantity: int
    total_price: int

    class Config:
        from_attributes = True


# =====================================================
# ORDER SCHEMAS
# =====================================================

class OrderCreate(BaseModel):
    user_name: str
    order_date: str
    total_amount: int
    status: str


class OrderResponse(BaseModel):
    id: int
    user_name: str
    order_date: str
    total_amount: int
    status: str

    class Config:
        from_attributes = True


# =====================================================
# ORDER ITEM SCHEMAS
# =====================================================

class OrderItemCreate(BaseModel):
    order_id: int
    food_name: str
    quantity: int
    price: int


class OrderItemResponse(BaseModel):
    id: int
    order_id: int
    food_name: str
    quantity: int
    price: int

    class Config:
        from_attributes = True


# =====================================================
# PAYMENT SCHEMAS
# =====================================================

class PaymentCreate(BaseModel):
    order_id: int
    payment_method: str
    payment_status: str
    amount: int


class PaymentResponse(BaseModel):
    id: int
    order_id: int
    payment_method: str
    payment_status: str
    amount: int

    class Config:
        from_attributes = True


# =====================================================
# DELIVERY SCHEMAS
# =====================================================

class DeliveryCreate(BaseModel):
    order_id: int
    delivery_person: str
    delivery_status: str
    delivery_address: str


class DeliveryResponse(BaseModel):
    id: int
    order_id: int
    delivery_person: str
    delivery_status: str
    delivery_address: str

    class Config:
        from_attributes = True


# =====================================================
# REVIEW SCHEMAS
# =====================================================

class ReviewCreate(BaseModel):
    user_name: str
    restaurant_name: str
    rating: int
    review: str


class ReviewResponse(BaseModel):
    id: int
    user_name: str
    restaurant_name: str
    rating: int
    review: str

    class Config:
        from_attributes = True