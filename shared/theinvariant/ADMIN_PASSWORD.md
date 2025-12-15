# Admin Panel Password

*Last updated: 2024-12-14*

---

## 🔐 Password Protection Added

The admin panel is now protected with a simple 4-word password.

### Password

**`the invariant editorial system`**

(4 words, lowercase, spaces)

---

## 🚀 How It Works

1. **Frontend**: Login form at `/admin`
   - Enter password
   - Stored in component state
   - Sent with every API request

2. **Backend**: Password check middleware
   - Checks `X-Admin-Password` header
   - Or `Authorization: Bearer <password>` header
   - Returns 401 if incorrect

---

## 🔄 Update Password

To change the password:

1. **Update backend** (`backend/routes/admin.js`):
   ```javascript
   const ADMIN_PASSWORD = process.env.ADMIN_PASSWORD || 'your new password';
   ```

2. **Update frontend** (`app/admin/page.tsx`):
   ```typescript
   if (password === 'your new password') {
   ```

3. **Set environment variable** (optional):
   ```bash
   # In .env
   ADMIN_PASSWORD=your new password
   ```

4. **Deploy**:
   ```bash
   ./deploy.sh
   ```

---

## 🔒 Security Notes

- **Simple password** - For basic protection only
- **Not encrypted** - Sent in headers (HTTPS encrypts in transit)
- **No session** - Password sent with every request
- **For production** - Consider JWT tokens or proper auth

---

**Password: `the invariant editorial system` 🔐**
