# API Documentation

## Endpoints

### 1. Consultant Endpoint
`POST /v1/consultant`

Handles contract consultation and generates detailed Islamic finance contract reports.

#### Request Schema
```json
{
  "query": "string",
  "chat_history": [
    {
      "role": "string",
      "content": "string"
    }
  ]
}
```

#### Response Schema
```json
{
  "response": "string",
  "detailed_summary": "string"
}
```

### 2. Contractor Endpoint
`POST /v1/contractor`

Generates structured contract documents following Islamic finance standards.

#### Request Schema
Uses the same schema as the Consultant's detailed summary response.

#### Response Schema
```json
{
  "title": "string",
  "preamble": "string",
  "applicable_standards": ["string"],
  "chapters": [
    {
      "title": "string",
      "sections": [
        {
          "title": "string",
          "content": "string",
          "subsections": [
            {
              "title": "string",
              "content": "string",
              "subsections": null
            }
          ]
        }
      ]
    }
  ],
  "closing": "string"
}
```

### 3. Classifier Endpoint
`POST /v1/classifier`

Classifies Islamic finance transactions into specific categories.

#### Request Schema
- Content-Type: `multipart/form-data`
- Body: File upload containing transaction details

#### Response Schema
```json
{
  "classifier_decision": "Ijarah" | "Ijarah Muntahia Bittamleek",
  "explanation": "string"
}
```

### 4. Banking Department Endpoint
`POST /v1/banking_department`

Handles banking department queries (Phase 2 feature).

#### Request Schema
```json
{
  "files": [
    {
      "filename": "string",
      "content": "binary"
    }
  ]
}
```

#### Response Schema
```json
{
  "response": "string",
  "source": "string"
}
```

## Error Responses

All endpoints may return the following error responses:

### 500 Internal Server Error
```json
{
  "detail": "string"
}
```

## Notes

1. All endpoints are prefixed with `/v1/`
2. The banking department endpoint is currently in development (Phase 2)
3. File uploads should be properly formatted and contain valid Islamic finance transaction data
4. All responses are in JSON format
5. Authentication and authorization details will be added in future updates