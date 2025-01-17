import jwt
import os

from flask import Blueprint, request, jsonify
from functools import wraps
from .models import User
from app import db


crumbl_blueprint = Blueprint("crumbl", __name__)


@crumbl_blueprint.route("/")
def home():
    return jsonify("Backend Online!")


# -------------------------------------------------------------#
# TODO: User Authentication With Sessions and Cookies: - SHANTANU , KYLE
# - User Login (SHANTANU) :  Implement user login functionality where
# a user can log in by providing credentials (username and
# password). Use sessions and cookies to track and maintain login states.
# - User Registration (KYLE): Allow new users to register by
# providing a username, password, and email.
# - Session Management (KYLE): Use Flask's session management to store user
# session data securely
# - Logout (SHANTANU): Implement logout functionality that clears the session and
# removes authentication cookies
# -------------------------------------------------------------#


# -------------------------------------------------------------#
# TODO: CRUD Operations for Inventory: - BETTY
# - Create Inventory Item: Allow the creation of new inventory
# items with fields like item name, description, quantity, and
# price. With auto creation of ID Read Inventory Items: Provide
# APIs to list all inventory items or fetch a single item based on
# its ID.
# - Update Inventory Item: Allow the modification of an inventory
# item's details (name, quantity, price, etc.).by id
# - Delete Inventory Item: Enable deletion of an inventory item by ID
# -------------------------------------------------------------#


# -------------------------------------------------------------#
# TODO: USER-Specific Inventory Management: - PHONG
# - Each Logged-in user will have their own inventory items, ensuring
# that users can only access and modify their own data.
# - Use sessions to ensure that only authenticated users can access
# inventory-related CRUD Operations
# -------------------------------------------------------------#


# -------------------------------------------------------------#
# TODO: Session and Cookie Security:
# - Secure user sessions with encryption (Flask Security key)
# - Implement proper session expiration handing to automatically
# log out.
# -------------------------------------------------------------#
