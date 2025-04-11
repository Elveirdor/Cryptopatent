def generate_readme(project_name, description, author, year, license_type, copyright_holder, copyright_number, installation_steps=None, usage_instructions=None, contributing_guidelines=None, contact_info=None):
    """Generates a basic README.md content as a string."""

    readme_content = f"""# {project_name}

{description}

## Table of Contents
- [License](#license)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Author](#author)
- [Copyright](#copyright)
- [Contact](#contact)

## License

This project is licensed under the **{license_type}** License - see the [LICENSE](LICENSE) file for details.

"""

    if installation_steps:
        readme_content += """## Installation

```
"""
        readme_content += installation_steps.strip()
        readme_content += """
```

"""

    if usage_instructions:
        readme_content += """## Usage

```
"""
        readme_content += usage_instructions.strip()
        readme_content += """
```

"""

    if contributing_guidelines:
        readme_content += """## Contributing

"""
        readme_content += contributing_guidelines.strip()
        readme_content += """

"""

    readme_content += f"""## Author

**{author}** - *{year}*

"""

    readme_content += f"""## Copyright

Copyright (c) {year} **{copyright_holder}**. All rights reserved.
Elveirdor is a copyrighted work, registration number {copyright_number}.

"""

    if contact_info:
        readme_content += """## Contact

"""
        readme_content += contact_info.strip()
        readme_content += """

"""

    return readme_content

if __name__ == "__main__":
    project = input("Enter the project name: ")
    desc = input("Enter a brief description of the project: ")
    name = input("Enter your full name (Author): ")
    year_input = input("Enter the copyright year: ")
    license_name = input("Enter the license type (e.g., MIT): ")
    copyright_name = input("Enter the copyright holder name: ")
    copyright_num = input("Enter your Elveirdor copyright number: ")

    install = input("Enter installation steps (leave blank if none): ")
    usage = input("Enter usage instructions (leave blank if none): ")
    contribute = input("Enter contributing guidelines (leave blank if none): ")
    contact = input("Enter contact information (leave blank if none): ")

    readme_content = generate_readme(
        project_name=project,
        description=desc,
        author=name,
        year=year_input,
        license_type=license_name,
        copyright_holder=copyright_name,
        copyright_number=copyright_num,
        installation_steps=install,
        usage_instructions=usage,
        contributing_guidelines=contribute,
        contact_info=contact
    )

    filename = "README.md"
    with open(filename, "w") as f:
        f.write(readme_content)
    print(f"\nREADME.md file generated successfully.")
