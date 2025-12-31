# n8n Expression Syntax Patterns

**CRITICAL: Read this before creating/editing n8n function content.**

## Core Rule: Method Syntax, NOT Function Syntax

n8n uses **method syntax** where functions are called ON objects, not as standalone functions.

```javascript
// CORRECT - Method syntax (n8n style)
{{ $json.field.hasField('link') }}
{{ $json.name.toUpperCase() }}
{{ [1,2,3].every(n => n > 0) }}

// WRONG - Function syntax (NOT n8n style)
{{ hasField($json.field, 'link') }}
{{ toUpperCase($json.name) }}
{{ every([1,2,3], n => n > 0) }}
```

## Pattern by Data Type

### String Methods
```javascript
// String methods are called ON the string
{{ $json.email.extractDomain() }}
{{ $json.url.extractUrlPath() }}
{{ $json.text.isNumeric() }}
{{ $json.name.toLowerCase() }}
{{ $json.filename.endsWith('.pdf') }}
{{ $json.code.startsWith('ABC') }}
{{ $json.text.substring(0, 10) }}
{{ $json.input.replaceAll('old', 'new') }}
{{ $json.message.removeMarkdown() }}
{{ $json.value.quote() }}
```

### Object Methods
```javascript
// Object methods are called ON the object
{{ $json.data.hasField('email') }}
{{ $json.user.merge({timestamp: $now}) }}
{{ $json.config.isEmpty() }}
{{ $json.record.keys() }}
{{ $json.item.values() }}
```

### Array Methods
```javascript
// Array methods are called ON the array
{{ $json.items.every(item => item.isValid) }}
{{ $json.users.some(u => u.isAdmin) }}
{{ $json.list.filter(x => x > 0) }}
{{ $json.data.find(d => d.id === 123) }}
{{ $json.numbers.map(n => n * 2) }}
{{ $json.scores.sum() }}
{{ $json.values.average() }}
{{ $json.prices.max() }}
{{ $json.ages.min() }}
```

### Date Methods
```javascript
// Date methods - toDateTime() converts, then chain methods
{{ $json.dateString.toDateTime() }}
{{ $json.date.toDateTime().plus(1, 'day') }}
{{ $json.timestamp.toDateTime().format('yyyy-MM-dd') }}
{{ $now.minus(7, 'days') }}
```

## Example Patterns for JSON Content

### thepexcel_syntax_primary
```json
// CORRECT
"thepexcel_syntax_primary": "string.extractUrlPath()"
"thepexcel_syntax_primary": "object.hasField(fieldName)"
"thepexcel_syntax_primary": "array.every(callback)"

// WRONG
"thepexcel_syntax_primary": "extractUrlPath(url)"
"thepexcel_syntax_primary": "hasField(object, fieldName)"
"thepexcel_syntax_primary": "every(array, callback)"
```

### thepexcel_step_examples
```json
// CORRECT
{
  "example_formula": "{{ $json.website.extractUrlPath() }}",
  "example_result": "/products/item-123",
  "example_explanation": "..."
}

// WRONG
{
  "example_formula": "{{ extractUrlPath($json.website) }}",
  "example_result": "/products/item-123",
  "example_explanation": "..."
}
```

## n8n Built-in vs JavaScript Methods

### n8n Built-in Convenience Methods
These are n8n-specific additions (documented at docs.n8n.io):
- `extractUrlPath()`, `extractDomain()`, `extractEmail()`
- `isNumeric()`, `isEmail()`, `isUrl()`, `isEmpty()`
- `hasField()`, `merge()`, `removeField()`
- `toDateTime()`, `plus()`, `minus()`, `format()`
- `sum()`, `average()`, `min()`, `max()`, `first()`, `last()`

### Standard JavaScript Methods (also work in n8n)
These are standard JS methods usable in n8n expressions:
- `substring()`, `slice()`, `split()`, `join()`
- `toLowerCase()`, `toUpperCase()`
- `startsWith()`, `endsWith()`, `includes()`
- `every()`, `some()`, `filter()`, `find()`, `map()`
- `push()`, `pop()`, `shift()`, `unshift()`

**Both types use the same method syntax!**

## Quick Reference Table

| Category | Method | Correct Syntax |
|----------|--------|----------------|
| String | extractUrlPath | `$json.url.extractUrlPath()` |
| String | endsWith | `$json.file.endsWith('.pdf')` |
| String | substring | `$json.text.substring(0, 5)` |
| Object | hasField | `$json.data.hasField('key')` |
| Object | merge | `$json.base.merge($json.extra)` |
| Array | every | `$json.items.every(x => x.valid)` |
| Array | some | `$json.list.some(x => x > 0)` |
| Array | filter | `$json.users.filter(u => u.active)` |
| Date | toDateTime | `$json.date.toDateTime()` |
| Date | format | `$now.format('yyyy-MM-dd')` |

## Checklist Before Publishing n8n Content

1. [ ] All `example_formula` use method syntax (`object.method()`)
2. [ ] `syntax_primary` shows method on type (`string.method()`, not `method(string)`)
3. [ ] No standalone function calls like `{{ functionName(arg1, arg2) }}`
4. [ ] Examples use `$json.field.method()` pattern
5. [ ] Clarify if it's n8n built-in or standard JavaScript method
