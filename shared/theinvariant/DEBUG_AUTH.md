# Debugging Admin Panel 401 Error

*Created: 2024-12-14*

---

## 🐛 Issue

Getting `401 (Unauthorized)` when accessing `/api/admin/agents-souls`

---

## ✅ Backend Works

Testing with curl shows the backend is working:
```bash
TOKEN=$(curl -s -X POST .../login | ...)
curl -H "Authorization: Bearer $TOKEN" .../agents-souls
# Returns: [{"state":{...}, ...}] ✅
```

---

## 🔍 Frontend Issues

### Possible Causes:

1. **Token not being sent**
   - Check browser console for token value
   - Verify `localStorage.getItem(TOKEN_KEY)` returns token
   - Check Network tab to see if `Authorization` header is present

2. **Token cleared before request**
   - Race condition in `verifyToken` or `fetchAgents`
   - localStorage access issues

3. **CORS/Header issues**
   - Browser blocking headers
   - Caddy not forwarding headers correctly

---

## 🛠️ Debug Steps Added

Added console.log statements to track:
- Token storage/retrieval
- Token verification
- Agent fetching
- Error details

**Check browser console** for these logs to see where it's failing.

---

## 🔧 Quick Fixes Applied

1. Added error handling for localStorage
2. Added logging for token operations
3. Improved error messages
4. Better state management

---

**Check browser console for detailed logs!** 🔍
