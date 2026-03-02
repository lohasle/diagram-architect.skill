# Diagram Themes

## Theme Overview

Five professional themes for different contexts. Each theme defines:
- **Primary color** - Main elements (systems, containers)
- **Accent color** - Highlights and important elements
- **Background** - Canvas color
- **Text colors** - For readability and hierarchy

---

## Theme 1: Corporate

### Use Case
Enterprise architecture, technical documentation, professional presentations

### Color Palette
```css
:root[data-theme="corporate"] {
    /* Primary Colors */
    --primary-bg: #1e3a5a;
    --primary-border: #1e40af;
    --primary-text: #ffffff;

    /* Secondary Colors */
    --secondary-bg: #3b82f6;
    --secondary-border: #2563eb;
    --secondary-text: #ffffff;

    /* Accent Colors */
    --accent-bg: #0ea5e9;
    --accent-border: #0284c7;
    --accent-text: #ffffff;

    /* Neutral Colors */
    --background: #f8fafc;
    --surface: #ffffff;
    --border: #e2e8f0;
    --text-primary: #0f172a;
    --text-secondary: #64748b;

    /* Status Colors */
    --success: #10b981;
    --warning: #f59e0b;
    --error: #ef4444;
}
```

### Mermaid Configuration
```javascript
{
  theme: 'base',
  themeVariables: {
    primaryColor: '#1e3a5a',
    primaryTextColor: '#ffffff',
    primaryBorderColor: '#1e40af',
    lineColor: '#64748b',
    secondaryColor: '#3b82f6',
    tertiaryColor: '#e0e7ff',
    background: '#f8fafc',
    edgeLabelBackground: '#ffffff'
  }
}
```

---

## Theme 2: Dark Mode

### Use Case
Developer documentation, IDE-like interface, dark-themed dashboards

### Color Palette
```css
:root[data-theme="dark-mode"] {
    /* Primary Colors */
    --primary-bg: #1e293b;
    --primary-border: #334155;
    --primary-text: #f1f5f9;

    /* Secondary Colors */
    --secondary-bg: #0f172a;
    --secondary-border: #1e293b;
    --secondary-text: #e2e8f0;

    /* Accent Colors */
    --accent-bg: #38bdf8;
    --accent-border: #0ea5e9;
    --accent-text: #0f172a;

    /* Neutral Colors */
    --background: #0f172a;
    --surface: #1e293b;
    --border: #334155;
    --text-primary: #f1f5f9;
    --text-secondary: #94a3b8;

    /* Status Colors */
    --success: #22c55e;
    --warning: #eab308;
    --error: #f87171;
}
```

### Mermaid Configuration
```javascript
{
  theme: 'dark',
  themeVariables: {
    primaryColor: '#1e293b',
    primaryTextColor: '#f1f5f9',
    primaryBorderColor: '#334155',
    lineColor: '#64748b',
    secondaryColor: '#0f172a',
    tertiaryColor: '#334155',
    background: '#0f172a',
    edgeLabelBackground: '#1e293b'
  }
}
```

---

## Theme 3: Minimal

### Use Case
White papers, academic documents, clean publications

### Color Palette
```css
:root[data-theme="minimal"] {
    /* Primary Colors */
    --primary-bg: #374151;
    --primary-border: #1f2937;
    --primary-text: #ffffff;

    /* Secondary Colors */
    --secondary-bg: #6b7280;
    --secondary-border: #4b5563;
    --secondary-text: #ffffff;

    /* Accent Colors */
    --accent-bg: #9ca3af;
    --accent-border: #6b7280;
    --accent-text: #1f2937;

    /* Neutral Colors */
    --background: #ffffff;
    --surface: #f9fafb;
    --border: #e5e7eb;
    --text-primary: #111827;
    --text-secondary: #6b7280;

    /* Status Colors */
    --success: #059669;
    --warning: #d97706;
    --error: #dc2626;
}
```

### Mermaid Configuration
```javascript
{
  theme: 'base',
  themeVariables: {
    primaryColor: '#374151',
    primaryTextColor: '#ffffff',
    primaryBorderColor: '#1f2937',
    lineColor: '#9ca3af',
    secondaryColor: '#6b7280',
    tertiaryColor: '#f3f4f6',
    background: '#ffffff',
    edgeLabelBackground: '#ffffff'
  }
}
```

---

## Theme 4: Tech

### Use Case
Tech startups, AI/ML products, modern SaaS

### Color Palette
```css
:root[data-theme="tech"] {
    /* Primary Colors */
    --primary-bg: #7c3aed;
    --primary-border: #6d28d9;
    --primary-text: #ffffff;

    /* Secondary Colors */
    --secondary-bg: #0ea5e9;
    --secondary-border: #0284c7;
    --secondary-text: #ffffff;

    /* Accent Colors */
    --accent-bg: #10b981;
    --accent-border: #059669;
    --accent-text: #ffffff;

    /* Neutral Colors */
    --background: #f0f9ff;
    --surface: #e0f2fe;
    --border: #bae6fd;
    --text-primary: #0c4a6e;
    --text-secondary: #0369a1;

    /* Status Colors */
    --success: #22c55e;
    --warning: #eab308;
    --error: #ef4444;
}
```

### Mermaid Configuration
```javascript
{
  theme: 'base',
  themeVariables: {
    primaryColor: '#7c3aed',
    primaryTextColor: '#ffffff',
    primaryBorderColor: '#6d28d9',
    lineColor: '#0369a1',
    secondaryColor: '#0ea5e9',
    tertiaryColor: '#cffafe',
    background: '#f0f9ff',
    edgeLabelBackground: '#ffffff'
  }
}
```

---

## Theme 5: Warm

### Use Case
Educational content, tutorials, friendly documentation

### Color Palette
```css
:root[data-theme="warm"] {
    /* Primary Colors */
    --primary-bg: #92400e;
    --primary-border: #78350f;
    --primary-text: #fef3c7;

    /* Secondary Colors */
    --secondary-bg: #f59e0b;
    --secondary-border: #d97706;
    --secondary-text: #78350f;

    /* Accent Colors */
    --accent-bg: #fbbf24;
    --accent-border: #d97706;
    --accent-text: #78350f;

    /* Neutral Colors */
    --background: #fffbeb;
    --surface: #fef3c7;
    --border: #fcd34d;
    --text-primary: #451a03;
    --text-secondary: #92400e;

    /* Status Colors */
    --success: #16a34a;
    --warning: #ea580c;
    --error: #dc2626;
}
```

### Mermaid Configuration
```javascript
{
  theme: 'base',
  themeVariables: {
    primaryColor: '#92400e',
    primaryTextColor: '#fef3c7',
    primaryBorderColor: '#78350f',
    lineColor: '#b45309',
    secondaryColor: '#f59e0b',
    tertiaryColor: '#fef3c7',
    background: '#fffbeb',
    edgeLabelBackground: '#fef3c7'
  }
}
```

---

## Theme Selection Guide

| Context | Recommended Theme |
|----------|-------------------|
| Enterprise architecture, B2B | Corporate |
| Developer tools, API docs | Dark Mode |
| Academic, white paper | Minimal |
| Startup, SaaS, AI product | Tech |
| Tutorial, education | Warm |

---

## Custom Themes

When creating custom themes, follow these principles:

### Color Harmony
- Use analogous colors (adjacent on color wheel) for cohesion
- Limit to 2-3 main colors + neutrals
- Ensure sufficient contrast for text readability

### Accessibility
- Minimum 4.5:1 contrast ratio for text
- Test with color blindness simulators
- Provide visual distinction beyond color (patterns, shapes)

### Brand Alignment
- Use brand colors as primary/accent
- Keep neutral colors for background
- Ensure brand logo fits with the theme

---

## Applying Themes in Mermaid

### Method 1: Theme Variables (Recommended)
```javascript
mermaid.initialize({
  startOnLoad: true,
  theme: 'base',
  themeVariables: {
    primaryColor: '#1e3a5a',
    primaryTextColor: '#ffffff',
    // ... more variables
  }
});
```

### Method 2: Built-in Themes
```javascript
mermaid.initialize({
  startOnLoad: true,
  theme: 'default'  // or 'base', 'dark', 'forest', 'neutral'
});
```

### Method 3: CSS Override
```css
.mermaid .node rect {
  fill: #1e3a5a !important;
  stroke: #1e40af !important;
}
```

---

## Font Pairings

| Theme | Heading Font | Body Font |
|-------|--------------|-----------|
| Corporate | Inter Bold | Inter Regular |
| Dark Mode | JetBrains Mono | Inter |
| Minimal | Instrument Serif | Inter |
| Tech | Space Grotesk | Inter |
| Warm | Poppins | Lato |

---

## Typography Scale

```css
:root {
    --font-xs: 12px;
    --font-sm: 14px;
    --font-base: 16px;
    --font-lg: 18px;
    --font-xl: 20px;
    --font-2xl: 24px;
    --font-3xl: 30px;
    --font-4xl: 36px;
}
```
