Documentation Generator for DID Communication Protocols
=======================================================

I got tired of writing Protocol and Message documentation by hand so I created
this tool to remove a portion of the work.

This tool accepts a JSON structure and generates a Markdown Document.

The JSON should look like:
```json
{
	"https://example.com/my-protocol/1.0": {
		"description": "Description of the protocol.",
		"messages": {
			"https://example.com/my-protocol/1.0/message-type": {
				"name": "message-type",
				"description": "description of the message",
				"fields": [
					{
						"key": "field-key",
						"type": "String",
						"description": "field description",
						"example": "example value for field",
						"required": true
					}
				]
			}
		}
	}
}
```
