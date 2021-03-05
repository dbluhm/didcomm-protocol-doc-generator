Documentation Generator for DID Communication Protocols
=======================================================

I got tired of writing Protocol and Message documentation by hand so I created
this tool to remove a portion of the work.

This tool accepts a JSON or YAML structure and generates a Markdown Document.

The JSON/YAML should look like:
```json
{
	"protocols": [
		{
			"title": "Protocol Title",
			"name": "my-protocol",
			"version": "0.1",
			"identifier": "https://example.com/my-protocol/0.1",
			"description": "Description of the protocol.",
			"messages": [
				{
					"type": "https://example.com/my-protocol/1.0/message-type",
					"name": "message-type",
					"description": "description of the message",
					"example": "{\"example\": \"message structure\"}",
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
			]
		}
	]
}
```
