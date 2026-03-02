#!/usr/bin/env python3
"""
Diagram Renderer - Renders D2 or PlantUML diagrams using kroki.io API

Usage:
    python render.py input.d2 output.svg
    python render.py input.puml output.svg --engine plantuml
    python render.py input.d2 output.png --format png
"""

import argparse
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: requests module not installed. Run: pip install requests")
    sys.exit(1)


KROKI_BASE_URL = "https://kroki.io"

ENGINES = {
    'd2': 'd2',
    'plantuml': 'plantuml',
    'puml': 'plantuml',
}

FORMATS = ['svg', 'png', 'pdf', 'txt', 'jpeg', 'base64']


def render_diagram(source: str, engine: str, output_format: str) -> tuple[int, str, bytes]:
    """
    Render diagram using kroki.io API

    Returns: (status_code, content_type, data)
    """
    url = f"{KROKI_BASE_URL}/{engine}/{output_format}"
    headers = {
        'Content-Type': 'text/plain; charset=utf-8',
    }

    try:
        response = requests.post(url, data=source.encode('utf-8'), headers=headers, timeout=30)
        return response.status_code, response.headers.get('Content-Type', ''), response.content
    except requests.RequestException as e:
        return 0, '', f"Request failed: {e}".encode()


def main():
    parser = argparse.ArgumentParser(
        description='Render diagrams using kroki.io API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s diagram.d2 output.svg
  %(prog)s diagram.puml output.svg --engine plantuml
  %(prog)s diagram.d2 output.png --format png
        """
    )

    parser.add_argument('input', type=str, help='Input diagram file path')
    parser.add_argument('output', type=str, help='Output file path')
    parser.add_argument('--engine', type=str, choices=list(ENGINES.keys()),
                        help='Diagram engine (default: auto-detect from extension)')
    parser.add_argument('--format', type=str, choices=FORMATS, default='svg',
                        help='Output format (default: svg)')

    args = parser.parse_args()

    # Read input file
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {args.input}")
        sys.exit(1)

    source = input_path.read_text(encoding='utf-8')

    # Auto-detect engine from extension if not specified
    if args.engine is None:
        ext = input_path.suffix.lower().lstrip('.')
        if ext in ENGINES:
            engine = ENGINES[ext]
        else:
            print(f"Error: Unknown file extension .{ext}")
            print(f"Supported engines: {', '.join(ENGINES.keys())}")
            sys.exit(1)
    else:
        engine = ENGINES[args.engine]

    # Render diagram
    print(f"Rendering {args.input} using {engine} engine...")

    status_code, content_type, data = render_diagram(source, engine, args.format)

    if status_code != 200:
        print(f"Error: kroki.io returned status {status_code}")
        if data:
            print(f"Response: {data.decode('utf-8', errors='ignore')[:500]}")
        sys.exit(1)

    # Write output file
    output_path = Path(args.output)
    output_path.write_bytes(data)

    print(f"Output written to: {args.output}")
    print(f"Format: {args.format}, Content-Type: {content_type}")


if __name__ == '__main__':
    main()
