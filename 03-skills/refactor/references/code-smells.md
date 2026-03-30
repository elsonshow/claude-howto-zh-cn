# Code Smells Catalog

这是一个用于识别代码异味的简明参考表。

## 常见 Code Smells

### Long Method

**Signs**

- 方法超过 30-50 行
- 多层嵌套
- 需要靠注释区分段落

**Refactorings**

- Extract Method
- Replace Temp with Query
- Introduce Parameter Object

### Large Class

**Signs**

- 字段过多
- 方法过多
- 职责明显混杂

**Refactorings**

- Extract Class
- Extract Subclass

### Primitive Obsession

**Signs**

- 用基础类型表示复杂领域概念
- 到处都是 magic strings / numbers

**Refactorings**

- Replace Primitive with Object
- Replace Type Code with Class

### Long Parameter List

**Signs**

- 参数 4 个以上
- 参数经常成组出现

**Refactorings**

- Introduce Parameter Object
- Preserve Whole Object

### Data Clumps

**Signs**

- 相同一组字段总是一起出现

**Refactorings**

- Extract Class
- Introduce Parameter Object
