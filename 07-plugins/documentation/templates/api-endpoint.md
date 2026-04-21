# API endpoint 模板：[METHOD] /api/v1/[endpoint]

## 说明

简要说明这个 endpoint 的作用。

## 鉴权

说明鉴权方式，例如 Bearer token。

## 参数

### 路径参数

| 名称 | 类型 | 是否必填 | 说明 |
|------|------|----------|-------------|
| id | string | Yes | 资源 ID |

### 查询参数

| 名称 | 类型 | 是否必填 | 说明 |
|------|------|----------|-------------|
| page | integer | No | 页码 |
| limit | integer | No | 每页条数 |

### 请求体

```json
{
  "field": "value"
}
```

## 响应

### 200 OK

```json
{
  "success": true,
  "data": {
    "id": "123",
    "name": "Example"
  }
}
```

## 示例

### cURL 示例

```bash
curl -X GET "https://api.example.com/api/v1/endpoint" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json"
```
