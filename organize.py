from pathlib import Path
import argparse
import logging
import shutil

project_folder = Path(__file__).resolve().parent

parser = argparse.ArgumentParser(description="Sort files into folders.")
parser.add_argument(
    "folder",
    nargs="?",
    default=str(project_folder / "downloads"),
    help="Folder to organize. Defaults to the project's downloads folder.",
)
parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Preview moves without changing files.",
)
args = parser.parse_args()

folder = Path(args.folder).expanduser().resolve()

if not folder.is_dir():
    parser.error(f"Folder does not exist or is not a directory: {folder}")

log_file = project_folder / "organizer.log"

if not args.dry_run:
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        encoding="utf-8",
    )

categories = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".csv": "Spreadsheets",
    ".txt": "Text",
    ".docx": "Documents",
    ".zip": "Archives",
}

protected_files = {
    Path(__file__).resolve(),
    log_file.resolve(),
}

for file in sorted(folder.iterdir()):
    if file.is_symlink() or not file.is_file():
        continue

    if file.resolve() in protected_files:
        continue

    extension = file.suffix.lower()
    category = categories.get(extension, "Other")

    destination_folder = folder / category
    destination = destination_folder / file.name

    if destination.exists():
        message = f"Skipped: {file.name} — destination already exists"
        print(message)

        if not args.dry_run:
            logging.warning(message)

        continue

    if args.dry_run:
        print(f"[DRY RUN] Would move: {file.name} -> {category}")
        continue

    try:
        destination_folder.mkdir(exist_ok=True)
        shutil.move(str(file), str(destination))
    except (OSError, shutil.Error) as error:
        message = f"Failed: {file.name} — {error}"
        print(message)
        logging.error(message)
    else:
        print(f"Moved: {file.name} -> {category}")
        logging.info("Moved: %s -> %s", file, destination)