import os
from urllib.parse import quote

SITES = {
    'Profile': 'https://www.sunithvs.com',
    'Blogs': 'https://www.sunithvs.com/blogs',
    'Projects': 'https://www.sunithvs.com/projects',
    'Contact': 'https://www.sunithvs.com/contact'
}


def generate_markdown_with_screenshots(sites=SITES, output_file='README.md'):
    """
    Generate a Markdown file with tightly packed website screenshots.

    :param sites: Dictionary of site names and URLs
    :param output_file: Name of the output Markdown file
    """
    with open(output_file, 'w') as f:
        for name, url in sites.items():
            encoded_url = quote(url)
            screenshot_url = f"https://api.microlink.io?url={encoded_url}&screenshot=true&embed=screenshot.url"

            markdown_entry = f"[![{name} Screenshot]({screenshot_url})]({url})\n"
            f.write(markdown_entry)

    print(f"Markdown file '{output_file}' generated successfully!")


if __name__ == '__main__':
    generate_markdown_with_screenshots()
