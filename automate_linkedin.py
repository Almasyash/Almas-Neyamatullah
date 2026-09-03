#!/usr/bin/env python3
"""
LinkedIn Portfolio Showcase Automation
-------------------------------------
Automates the updating of LinkedIn profile sections (Headline, About, Featured Portfolio Link)
using Playwright and data from `linkedin-data.json`.

Usage:
    pip install -r requirements.txt
    playwright install chromium
    python automate_linkedin.py
"""

import json
import os
import sys
import time
import argparse
from pathlib import Path

# Ensure UTF-8 output encoding across all terminals
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

DATA_FILE = Path(__file__).parent / "linkedin-data.json"
USER_DATA_DIR = Path(__file__).parent / ".browser_session"


def load_data(filepath=DATA_FILE):
    if not filepath.exists():
        print(f"[ERROR] Could not find data file at {filepath}")
        sys.exit(1)
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def wait_for_login(page):
    """Ensure user is logged in to LinkedIn before proceeding."""
    print("[INFO] Checking LinkedIn login status...")
    page.goto("https://www.linkedin.com/feed/", wait_until="domcontentloaded")
    time.sleep(3)

    if "login" in page.url or "checkpoint" in page.url or "authwall" in page.url or page.locator("input#username").count() > 0:
        print("\n=======================================================")
        print(">> ACTION REQUIRED: Please log in to LinkedIn in the browser window.")
        print(">> Complete any 2FA or CAPTCHA verification if prompted.")
        print(">> The script will automatically continue once logged in.")
        print("=======================================================\n")
        
        # Wait up to 5 minutes for user to log in
        for _ in range(60):
            time.sleep(5)
            if "feed" in page.url or page.locator("nav.global-nav").count() > 0 or "in/" in page.url:
                print("[SUCCESS] Login detected!")
                break
        else:
            print("[ERROR] Login timeout reached. Please run the script again.")
            sys.exit(1)
    else:
        print("[SUCCESS] Active LinkedIn session restored!")


def update_headline_and_about(page, profile_data):
    """Navigate to user profile and update headline and summary."""
    print("\n[INFO] Navigating to profile edit...")
    page.goto("https://www.linkedin.com/in/", wait_until="domcontentloaded")
    time.sleep(4)

    headline = profile_data.get("headline", "")
    about = profile_data.get("about", "")

    # 1. Update Intro / Headline
    try:
        print(f"[INFO] Setting Headline: '{headline}'")
        # Click top edit button on intro card
        edit_intro_btn = page.locator("button[aria-label*='Edit intro'], button.artdeco-button[aria-label*='intro']").first
        if edit_intro_btn.is_visible(timeout=5000):
            edit_intro_btn.click()
            time.sleep(2)

            # Headline input field
            headline_input = page.locator("input#single-line-text-input, input[id*='headline']").first
            if headline_input.is_visible(timeout=5000):
                headline_input.fill("")
                headline_input.type(headline, delay=20)
                time.sleep(1)

                # Save intro
                save_btn = page.locator("button.artdeco-button--primary:has-text('Save')").first
                if save_btn.is_visible():
                    save_btn.click()
                    print("[SUCCESS] Headline updated successfully!")
                    time.sleep(3)
        else:
            print("[NOTICE] Intro edit button not directly located. Please verify manually.")
    except Exception as e:
        print(f"[WARNING] Could not auto-update headline: {e}")

    # 2. Update About Section
    try:
        print(f"\n[INFO] Setting About section (~{len(about)} characters)...")
        page.goto("https://www.linkedin.com/in/", wait_until="domcontentloaded")
        time.sleep(3)

        edit_about_btn = page.locator("section:has(#about) button[aria-label*='Edit about'], button[aria-label*='Edit about']").first
        if edit_about_btn.is_visible(timeout=5000):
            edit_about_btn.click()
            time.sleep(2)

            about_textarea = page.locator("textarea#multiline-text-input, textarea[id*='summary']").first
            if about_textarea.is_visible(timeout=5000):
                about_textarea.fill("")
                about_textarea.type(about, delay=15)
                time.sleep(1)

                save_btn = page.locator("button.artdeco-button--primary:has-text('Save')").first
                if save_btn.is_visible():
                    save_btn.click()
                    print("[SUCCESS] About section updated successfully!")
                    time.sleep(3)
        else:
            print("[NOTICE] About section edit button not found or already up-to-date.")
    except Exception as e:
        print(f"[WARNING] Could not auto-update About section: {e}")


def add_featured_link(page, featured_item):
    """Add portfolio link to LinkedIn Featured section."""
    print("\n[INFO] Updating Featured section with Portfolio link...")
    page.goto("https://www.linkedin.com/in/", wait_until="domcontentloaded")
    time.sleep(4)

    url = featured_item.get("url", "")
    title = featured_item.get("title", "")
    desc = featured_item.get("description", "")

    try:
        # Check for '+ button' in Featured section
        add_featured_btn = page.locator("section:has(#featured) button[aria-label*='Add featured'], button[aria-label*='Add a featured']").first
        if add_featured_btn.is_visible(timeout=5000):
            add_featured_btn.click()
            time.sleep(2)

            # Click 'Add a link'
            add_link_option = page.locator("span:has-text('Add a link'), button:has-text('Add a link')").first
            if add_link_option.is_visible(timeout=3000):
                add_link_option.click()
                time.sleep(2)

                # Enter URL
                url_input = page.locator("input[placeholder*='http'], input#custom-url").first
                if url_input.is_visible(timeout=3000):
                    url_input.fill(url)
                    time.sleep(1)
                    add_url_btn = page.locator("button:has-text('Add')").first
                    add_url_btn.click()
                    time.sleep(3)

                    # Update title and description
                    title_input = page.locator("input#custom-title").first
                    if title_input.is_visible(timeout=3000):
                        title_input.fill(title)

                    desc_input = page.locator("textarea#custom-description").first
                    if desc_input.is_visible(timeout=3000):
                        desc_input.fill(desc)

                    save_btn = page.locator("button.artdeco-button--primary:has-text('Save')").first
                    if save_btn.is_visible():
                        save_btn.click()
                        print("[SUCCESS] Featured portfolio link added!")
                        time.sleep(3)
        else:
            print(f"[INFO] Portfolio link ready to be manually pinned to Featured: {url}")
    except Exception as e:
        print(f"[WARNING] Featured automation notice: {e}")


def display_summary(data):
    """Prints a clean, ready-to-copy summary of all profile elements."""
    p = data.get("profile", {})
    print("\n" + "=" * 65)
    print("       LINKEDIN PROFILE SHOWCASE CONTENT SUMMARY")
    print("=" * 65)
    print(f"\n👤 NAME:     {p.get('name')}")
    print(f"🎯 HEADLINE: {p.get('headline')}")
    print(f"📍 LOCATION: {p.get('location')}")
    print(f"🌐 URL:      {p.get('portfolio')}")
    print(f"\n📝 ABOUT SECTION (~{len(p.get('about', ''))} characters):")
    print("-" * 65)
    print(p.get("about"))
    print("-" * 65)

    print("\n💼 FEATURED PROJECTS TO SHOWCASE:")
    for i, proj in enumerate(data.get("projects", []), 1):
        print(f"\n  {i}. {proj.get('name')} ({', '.join(proj.get('tech', []))})")
        print(f"     Role: {proj.get('role', 'Developer')}")
        print(f"     Info: {proj.get('description')}")
        print(f"     Demo: {proj.get('url')}")

    print("\n⚡ SKILLS LIST:")
    print("  " + " • ".join(data.get("skills", [])))
    print("=" * 65 + "\n")


def main():
    parser = argparse.ArgumentParser(description="Automate LinkedIn portfolio updates.")
    parser.add_argument("--dry-run", action="store_true", help="Print content without launching browser")
    parser.add_argument("--data", default=str(DATA_FILE), help="Path to JSON data file")
    args = parser.parse_args()

    data = load_data(Path(args.data))
    display_summary(data)

    if args.dry_run:
        print("[INFO] Dry-run complete. Run without --dry-run to launch automation.")
        return

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("\n[ERROR] Playwright is not installed.")
        print("Please install requirements first:")
        print("    pip install -r requirements.txt")
        print("    playwright install chromium\n")
        sys.exit(1)

    print("[INFO] Launching Chromium browser with session persistence...")
    USER_DATA_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=False,
            viewport={"width": 1280, "height": 850},
            args=["--start-maximized", "--disable-blink-features=AutomationControlled"]
        )
        page = context.new_page()

        try:
            wait_for_login(page)
            update_headline_and_about(page, data.get("profile", {}))
            if data.get("featured"):
                add_featured_link(page, data.get("featured", [])[0])
            print("\n[ALL DONE] LinkedIn profile automation finished!")
            print("You can verify your profile live at: https://www.linkedin.com/in/\n")
            time.sleep(5)
        except KeyboardInterrupt:
            print("\n[INFO] Automation stopped by user.")
        finally:
            context.close()


if __name__ == "__main__":
    main()
