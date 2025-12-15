# Session-Based Authentication ✅

*Implemented: 2024-12-14*

---

## 🔐 Long-Lived Sessions

The admin panel now uses **JWT token-based sessions** that last for **30 days** (configurable).

### How It Works

1. **Login**: User enters 4-word password
2. **Token Creation**: Backend creates JWT token (valid 30 days)
3. **Storage**: Token stored in `localStorage` on frontend
4. **Auto-Login**: Token checked on page load - if valid, user stays logged in
5. **API Requests**: Token sent with every request in `Authorization: Bearer <token>` header

---

## 🚀 Features

- ✅ **30-day sessions** (configurable via `SESSION_DURATION_DAYS`)
- ✅ **Auto-login** on page load if token valid
- ✅ **Secure storage** - tokens hashed in database
- ✅ **Session tracking** - last used timestamp, IP, user agent
- ✅ **Logout** - revokes token immediately
- ✅ **Token verification** - `/api/admin/verify` endpoint

---

## 📋 API Endpoints

### `POST /api/admin/login`
Login with password, receive token.

**Request:**
```json
{
  "password": "the invariant editorial system"
}
```

**Response:**
```json
{
  "success": true,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expiresAt": "2026-01-13T21:45:38.683Z",
  "message": "Login successful"
}
```

### `POST /api/admin/logout`
Revoke current session token.

**Headers:**
```
Authorization: Bearer <token>
```

### `GET /api/admin/verify`
Verify token is still valid.

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
{
  "valid": true,
  "expiresAt": "2026-01-13T21:45:38.683Z",
  "message": "Token is valid"
}
```

---

## 🗄️ Database

Sessions stored in `admin_sessions` table:
- `token_hash` - SHA256 hash of JWT token
- `expires_at` - Token expiration timestamp
- `last_used_at` - Last API request timestamp
- `user_agent` - Browser/client info
- `ip_address` - Client IP

---

## ⚙️ Configuration

**Environment Variables:**
```bash
ADMIN_PASSWORD=the invariant editorial system
JWT_SECRET=your-secret-key-change-in-production
SESSION_DURATION_DAYS=30
```

---

## 🔄 User Experience

1. **First Visit**: Login form shown
2. **After Login**: Token stored, dashboard loads
3. **Return Visit**: Token checked automatically - if valid, dashboard loads immediately
4. **After 30 Days**: Token expires, login form shown again
5. **Logout**: Click logout button, token revoked, login form shown

---

## 🔒 Security Notes

- Tokens are **JWT signed** with secret key
- Tokens are **hashed** before storage (SHA256)
- Tokens **expire** after configured days
- Tokens can be **revoked** via logout
- All requests use **HTTPS** (encrypted in transit)
- Tokens stored in `localStorage` (accessible to JavaScript)

**For production**, consider:
- Rotating JWT secret periodically
- Adding refresh tokens
- Implementing rate limiting
- Adding CSRF protection

---

**Sessions last 30 days! 🎉**
