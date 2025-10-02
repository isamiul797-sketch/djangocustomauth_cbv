# utils/mixins.py
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

# Styled HTML for Access Denied
ACCESS_DENIED_HTML = """
<html>
<head>
    <style>
        body {
            background-color: #f8f9fa;
            font-family: Arial, sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        .error-box {
            background: white;
            border: 2px solid #dc3545;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        h1 {
            color: #dc3545;
            font-size: 28px;
            margin-bottom: 10px;
        }
        p {
            color: #333;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div class="error-box">
        <h1>Access Denied</h1>
        <p>You are not authorized to access this page.</p>
        <a href="/">Go Home</a>
    </div>
</body>
</html>
"""

# Customer Mixin
class IsCustomerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and getattr(self.request.user, 'is_customer', False)

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return HttpResponseForbidden(ACCESS_DENIED_HTML)
        return redirect('login')

# Seller Mixin
class IsSellerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and getattr(self.request.user, 'is_seller', False)

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return HttpResponseForbidden(ACCESS_DENIED_HTML)
        return redirect('login')
