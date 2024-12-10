import markdown
import sys

def convert_markdown_to_html(input_file, output_file):
    try:
        # Read the Markdown file
        with open(input_file, 'r', encoding='utf-8') as md_file:
            markdown_content = md_file.read()

        # Convert Markdown to HTML
        html_content = markdown.markdown(markdown_content)

        # Write the HTML content to the output file
        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        print(f"HTML file successfully generated: {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if the correct number of arguments are passed
    if len(sys.argv) != 3:
        print("Usage: python md_to_html.py <input_markdown_file> <output_html_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_markdown_to_html(input_file, output_file)
