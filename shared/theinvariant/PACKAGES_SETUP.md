# The Invariant — Package Setup

*Last updated: 2024-12-14*

---

## ✅ Installed Packages

### Core UI Libraries

1. **shadcn/ui** — Component library built on Radix UI
   - ✅ Installed: `button`, `card`
   - ✅ Configured: `components.json`
   - ✅ Utils: `lib/utils.ts` with `cn()` helper

2. **@tailwindcss/typography** — Beautiful typography for article content
   - ✅ Installed and configured
   - Use `prose` classes for article content

3. **Radix UI Primitives** — Accessible component primitives
   - ✅ Installed via shadcn/ui

### Utility Packages

- `class-variance-authority` — Component variants
- `clsx` — Conditional classnames
- `tailwind-merge` — Merge Tailwind classes
- `lucide-react` — Icon library

---

## Usage Examples

### Using shadcn/ui Components

```tsx
import { Button } from "@/components/ui/button"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"

export default function Example() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Article Title</CardTitle>
      </CardHeader>
      <CardContent>
        <Button>Read More</Button>
      </CardContent>
    </Card>
  )
}
```

### Using Tailwind Typography for Articles

```tsx
<article className="prose prose-lg max-w-3xl mx-auto">
  <h1>Article Title</h1>
  <p>Beautiful typography automatically applied...</p>
</article>
```

### Custom Typography Styling

The `prose` plugin is configured with our custom colors. You can customize it in `tailwind.config.js`:

```js
typography: {
  DEFAULT: {
    css: {
      maxWidth: '720px',
      color: 'var(--color-text)',
      // ... custom styles
    }
  }
}
```

---

## Available shadcn/ui Components

To add more components:

```bash
npx shadcn@latest add [component-name]
```

Popular components for magazines:
- `card` ✅
- `button` ✅
- `input` (for newsletter forms)
- `separator` (for dividers)
- `badge` (for categories)
- `skeleton` (for loading states)
- `dialog` (for modals)
- `tabs` (for navigation)

---

## Best Practices

1. **Use shadcn/ui for UI elements only** — buttons, inputs, dialogs, etc.
2. **Keep custom styling for "vibe"** — hero sections, article layouts, magazine-specific design
3. **Use Tailwind Typography for article content** — ensures beautiful, readable prose
4. **Leverage `cn()` utility** — for conditional classes and merging

---

## Next Steps

1. ✅ shadcn/ui installed
2. ✅ Tailwind Typography configured
3. [ ] Refactor page components to use shadcn/ui where appropriate
4. [ ] Create article template with Typography plugin
5. [ ] Add more shadcn/ui components as needed

---

**These packages ensure the site looks professional and is hard to mess up! 🎨**
