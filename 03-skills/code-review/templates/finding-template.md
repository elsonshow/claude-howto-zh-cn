# Code Review Finding Template

## Issue: [TITLE]

### Severity

- [ ] Critical
- [ ] High
- [ ] Medium
- [ ] Low

### Category

- [ ] Security
- [ ] Performance
- [ ] Code Quality
- [ ] Maintainability
- [ ] Testing
- [ ] Design Pattern
- [ ] Documentation

### Location

**File:** `src/components/UserCard.tsx`  
**Lines:** 45-52  
**Function/Method:** `renderUserDetails()`

### Issue Description

- **What**
- **Why it matters**
- **Current behavior**
- **Expected behavior**

### Code Example

#### Current

```typescript
const users = fetchUsers();
users.forEach(user => {
  const posts = fetchUserPosts(user.id);
  renderUserPosts(posts);
});
```

#### Suggested Fix

```typescript
const usersWithPosts = fetchUsersWithPosts();
usersWithPosts.forEach(({ user, posts }) => {
  renderUserPosts(posts);
});
```

### Impact Analysis

| Aspect | Impact | Severity |
|--------|--------|----------|
| Performance | [describe] | High |
| User Experience | [describe] | High |
| Scalability | [describe] | Critical |
| Maintainability | [describe] | Medium |
