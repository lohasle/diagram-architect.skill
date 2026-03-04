#!/usr/bin/env python3
"""
Diagram Generator - Safely fills the HTML template with diagram content.

This script reads the template INTO MEMORY, replaces placeholders, and writes
to a NEW output file. It NEVER modifies the original template.

Usage:
    # Basic usage with inline source
    python3 generate.py --title "My Diagram" --output output.html \\
        --source "flowchart LR\\n    A --> B"

    # Read diagram source from a file
    python3 generate.py --title "API Flow" --subtitle "v2.0" \\
        --source-file diagram.mmd --output api-flow.html

    # Use a custom template
    python3 generate.py --title "My Diagram" --source-file diagram.mmd \\
        --template /path/to/custom-template.html --output output.html

Icon Support (D2 diagrams):
    Use @azure:ALIAS to embed Azure icons as base64 data URIs:

        vm: My Server {
          icon: "@azure:vm"
        }

    Available aliases: vm, kubernetes, app-service, function, storage,
    sql, cosmos-db, redis, vnet, load-balancer, app-gateway, firewall,
    key-vault, api-management, service-bus, event-hub, openai, and more.
    See references/azure-icons.md for the full catalog.
"""

import argparse
import base64
import os
import re
import sys

# Default template location (relative to this script)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_TEMPLATE = os.path.join(SCRIPT_DIR, '..', 'assets', 'templates', 'diagram.html')
DEFAULT_TEMPLATE = os.path.normpath(DEFAULT_TEMPLATE)

ICONS_DIR = os.path.join(SCRIPT_DIR, '..', 'assets', 'icons', 'azure')
ICONS_DIR = os.path.normpath(ICONS_DIR)


def build_icon_cache(icons_dir: str) -> dict:
    """Build a mapping of alias -> base64 data URI from the icons directory."""
    cache = {}
    if not os.path.isdir(icons_dir):
        return cache
    for fname in os.listdir(icons_dir):
        if fname.endswith('.svg'):
            alias = fname[:-4]  # strip .svg
            fpath = os.path.join(icons_dir, fname)
            with open(fpath, 'rb') as f:
                data = f.read()
            b64 = base64.b64encode(data).decode('ascii')
            cache[alias] = f'data:image/svg+xml;base64,{b64}'
    return cache


def resolve_icons(source: str, icons_dir: str) -> tuple[str, int]:
    """
    Replace @azure:ALIAS references in diagram source with base64 data URIs.
    Returns (processed_source, count_of_replacements).
    """
    cache = build_icon_cache(icons_dir)
    if not cache:
        return source, 0

    count = 0
    # Match: "@azure:alias" (with or without surrounding quotes in D2 source)
    pattern = re.compile(r'"@azure:([^"]+)"')

    def replacer(m):
        nonlocal count
        alias = m.group(1)
        if alias in cache:
            count += 1
            return f'"{cache[alias]}"'
        else:
            available = sorted(cache.keys())
            print(
                f"Warning: Icon '@azure:{alias}' not found. "
                f"Available: {', '.join(available[:10])}{'...' if len(available) > 10 else ''}",
                file=sys.stderr
            )
            return m.group(0)  # leave unchanged

    processed = pattern.sub(replacer, source)
    return processed, count


def generate(title: str, subtitle: str, source: str, template_path: str, output_path: str) -> None:
    """
    Read template, replace placeholders in memory, write to output file.
    Never modifies the original template.
    """
    # Pre-process: resolve @azure:alias icon references
    if '@azure:' in source:
        source, icon_count = resolve_icons(source, ICONS_DIR)
        if icon_count:
            print(f"  Icons: resolved {icon_count} @azure: reference(s) to base64 data URIs")

    # Read template
    if not os.path.exists(template_path):
        print(f"Error: Template not found: {template_path}", file=sys.stderr)
        sys.exit(1)

    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Verify template has expected placeholders
    missing = []
    for placeholder in ['DIAGRAM_TITLE', 'DIAGRAM_SOURCE']:
        if placeholder not in content:
            missing.append(placeholder)
    if missing:
        print(f"Warning: Template is missing placeholders: {', '.join(missing)}", file=sys.stderr)
        print(f"Template may have been previously modified. Using it as-is.", file=sys.stderr)

    # Replace placeholders IN MEMORY
    content = content.replace('DIAGRAM_TITLE', title)
    content = content.replace('DIAGRAM_SUBTITLE', subtitle)
    content = content.replace('DIAGRAM_SOURCE', source)

    # Verify all placeholders replaced
    remaining = []
    for placeholder in ['DIAGRAM_TITLE', 'DIAGRAM_SUBTITLE', 'DIAGRAM_SOURCE']:
        if placeholder in content:
            remaining.append(placeholder)
    if remaining:
        print(f"Warning: Unreplaced placeholders in output: {', '.join(remaining)}", file=sys.stderr)

    # Write to output (create parent dirs if needed)
    output_dir = os.path.dirname(os.path.abspath(output_path))
    os.makedirs(output_dir, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    size_kb = len(content) / 1024
    print(f"Generated: {output_path} ({size_kb:.1f} KB)")
    print(f"  Title: {title}")
    if subtitle:
        print(f"  Subtitle: {subtitle}")
    print(f"  Source: {len(source.splitlines())} lines of diagram code")


def main():
    parser = argparse.ArgumentParser(
        description='Generate diagram HTML from template',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('--title', required=True, help='Diagram title (replaces DIAGRAM_TITLE)')
    parser.add_argument('--subtitle', default='', help='Diagram subtitle (replaces DIAGRAM_SUBTITLE)')
    parser.add_argument('--source', help='Diagram source code inline (replaces DIAGRAM_SOURCE)')
    parser.add_argument('--source-file', help='File containing diagram source code')
    parser.add_argument('--template', default=DEFAULT_TEMPLATE, help=f'Template path (default: {DEFAULT_TEMPLATE})')
    parser.add_argument('--output', required=True, help='Output HTML file path')

    args = parser.parse_args()

    # Get diagram source
    if args.source_file:
        if not os.path.exists(args.source_file):
            print(f"Error: Source file not found: {args.source_file}", file=sys.stderr)
            sys.exit(1)
        with open(args.source_file, 'r', encoding='utf-8') as f:
            source = f.read().strip()
    elif args.source:
        source = args.source.replace('\\n', '\n')
    else:
        print("Error: Provide either --source or --source-file", file=sys.stderr)
        sys.exit(1)

    generate(
        title=args.title,
        subtitle=args.subtitle,
        source=source,
        template_path=args.template,
        output_path=args.output
    )


if __name__ == '__main__':
    main()
