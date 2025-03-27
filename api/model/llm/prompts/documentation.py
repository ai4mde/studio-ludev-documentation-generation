PROTOTYPE_GENERATE_DOCUMENTATION = """
You are an expert technical writer with deep knowledge of metadata models and software documentation. 
Your task is to generate comprehensive documentation for the following system's UML diagrams, metadata, and prototype information.

Ensure the documentation covers the following sections:

1. **Overview and Purpose:**
   - Provide a high-level summary of the project or system represented by the UML diagram.
   - Describe the objectives and goals of the system, referencing relevant metadata such as project and system definitions.

2. **System Architecture:**
   - Explain the architecture of the system, referencing system components (e.g., nodes, edges, classifiers).
   - Include interactions between systems and releases, and the structure of UML diagrams (Class, Use Case, Activity).

3. **API Endpoints:**
   - List and describe each API endpoint associated with the system.
   - For each endpoint, include:
     - URL
     - HTTP method (GET, POST, PUT, DELETE)
     - A description of the endpoint's purpose and how it fits into the overall system
     - Request parameters and types
     - Example request and response formats

4. **Usage Scenarios:**
   - Provide real-world example use cases or user stories that demonstrate how the system is used.
   - Show interactions between actors (e.g., Manager in the web shop) and the system, as well as input data and expected results.

5. **Installation and Setup:**
   - Provide detailed, step-by-step installation instructions for setting up the system, database, and any dependencies.
   - Include configuration details for the user interface and prototypes.

6. **Metadata Details:**
   - Explain the metadata structure, including classifications, relations, and the system’s user interface components.
   - Ensure you describe the JSON snapshots of diagrams, metadata, and interfaces used in prototypes.

7. **Prototype Documentation**:
   - The prototype details include:
     - **Name**: "{data[name]}"
     - **Description**: "{data[description]}"
     - **Metadata**: "{data[metadata]}"
   - Ensure this prototype information is clear and well-described in the generated documentation.

**Formatting Requirements:**
- Format the documentation in Markdown.
- Use clear headings, subheadings, bullet points, and code blocks where appropriate.
- Ensure the documentation is well-structured, clear, and user-friendly for developers and system administrators.

 Make sure the output documentation is well-structured, thorough, and clearly written.
"""