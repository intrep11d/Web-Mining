 if logo_path and os.path.exists(logo_path):
        try:
            pdf.image(logo_path, x=logo_x, y=logo_y, w=logo_width, h=logo_height)
        except Exception as e:
            print(f"Warning: Could not add logo from '{logo_path}'. Error: {e}")
    elif logo_path: # Only warn if path was provided but file not found
        print(f"Warning: Logo file not found at '{logo_path}'. Skipping logo.")