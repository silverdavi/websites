# The Invariant — Quick Start Guide

*Last updated: 2024-12-14*

---

## ✅ What's Installed

### Professional UI Libraries

1. **shadcn/ui** — Battle-tested component library
   - Prevents ugly UI mistakes
   - Accessible by default
   - Fully customizable

2. **Tailwind Typography** — Beautiful article content
   - Automatic typography for prose
   - Magazine-quality reading experience
   - Customizable with your brand colors

3. **Radix UI** — Accessible primitives
   - Screen reader friendly
   - Keyboard navigation
   - ARIA compliant

---

## 🎨 How to Use

### For Article Content

```tsx
<article className="prose prose-lg max-w-3xl mx-auto">
  <h1>Your Article Title</h1>
  <p>Beautiful typography automatically applied...</p>
</article>
```

### For UI Components

```tsx
import { Button } from "@/components/ui/button"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"

<Card>
  <CardHeader>
    <CardTitle>Article Card</CardTitle>
  </CardHeader>
  <CardContent>
    <Button>Read More</Button>
  </CardContent>
</Card>
```

### Adding More Components

```bash
npx shadcn@latest add [component-name]
```

Popular choices:
- `input` — Newsletter forms
- `separator` — Dividers
- `badge` — Categories/tags
- `skeleton` — Loading states
- `dialog` — Modals
- `tabs` — Navigation

---

## 🚫 What NOT to Do

1. ❌ Don't override shadcn/ui styles with inline CSS
2. ❌ Don't mix CSS modules with Tailwind (use one approach)
3. ❌ Don't skip the `prose` class for article content
4. ❌ Don't build custom buttons/inputs when shadcn/ui has them

---

## ✅ What TO Do

1. ✅ Use `cn()` utility for conditional classes
2. ✅ Use `prose` for all article content
3. ✅ Use shadcn/ui for UI elements (buttons, inputs, cards)
4. ✅ Keep custom CSS for "vibe" (hero sections, unique layouts)
5. ✅ Follow the design tokens in `tailwind.config.js`

---

## 📚 Resources

- [shadcn/ui Docs](https://ui.shadcn.com)
- [Tailwind Typography](https://tailwindcss.com/docs/plugins/typography)
- [Radix UI](https://www.radix-ui.com)

---

**These packages make it hard to build something ugly! 🎨**
