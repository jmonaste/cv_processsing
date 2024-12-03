# AI-Powered Resume Processing with ChatGPT

## Summary

This project leverages the new **Structured Outputs** feature of the ChatGPT API to build a robust system for processing resumes. The Structured Outputs capability ensures that responses adhere to a pre-defined JSON Schema, making it ideal for extracting, structuring, and managing resume data.

Structured Outputs enhance the reliability of the ChatGPT API for production-level workflows, enabling robust and predictable data extraction from unstructured text.

---

## Key Features of Structured Outputs

1. **JSON Schema Enforcement**: Ensures the model generates responses that strictly follow the provided schema by setting the `strict: true` parameter in API calls.
   
2. **Applications**:
   - Populate databases with structured content from resumes.
   - Extract entities and relevant information for use in recruitment pipelines.
   - Display resume data in a user-friendly format for hiring teams.

3. **Example Use Cases**:
   - Extracting work experience, education, and skills into structured formats for applicant tracking systems.
   - Summarizing candidate profiles for quick reviews.
   - Matching candidate attributes to job descriptions using structured responses.

4. **Reliability**: The refusal mechanism guarantees that responses outside the defined schema are flagged, reducing errors in data parsing.

---

## API Features in Detail

- **Strict JSON Schema**: Previously, `response_format` allowed simple JSON output, but now schemas can define exact field names, data types, and structure.
- **Function Calls with Constraints**: Combine schema definitions with API function calls for tightly controlled workflows.
- **SDK Integration**: Simplified parsing and schema validation using Pydantic models for clean and error-free integration.

---

## Example Applications

### 1. Extracting Resume Details
The API can extract structured data like:
- Name
- Contact Information
- Work Experience
- Education
- Skills

Schema Example:
```json
{
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"},
        "work_experience": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "position": {"type": "string"},
                    "company": {"type": "string"},
                    "duration": {"type": "string"}
                },
                "required": ["position", "company", "duration"]
            }
        }
    },
    "required": ["name", "email", "work_experience"]
}
