#!/usr/bin/env python3
"""Automated macOS build and packaging script for sView.

Outputs:
  - dist/YYYYMMDD_HHMMSS_sview.app
  - dist/YYYYMMDD_HHMMSS_sview.zip (unless --no-zip is passed)
"""

from __future__ import annotations

import argparse
import datetime
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], cwd: Path | None = None, env: dict[str, str] | None = None) -> None:
    print(f"+ {' '.join(cmd)}")
    subprocess.run(cmd, cwd=cwd, env=env, check=True)


def check_macos_prerequisites() -> None:
    if platform.system() != "Darwin":
        raise SystemExit("Error: build_macos.py only supports macOS.")

    for tool in ("cmake", "clang++"):
        if shutil.which(tool) is None:
            raise SystemExit(f"Error: '{tool}' not found in PATH.")

    ibtool_check = subprocess.run(
        ["xcrun", "--find", "ibtool"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if ibtool_check.returncode != 0:
        raise SystemExit(
            "Error: 'ibtool' is unavailable (Xcode.app is required to compile MainMenu.xib).\n"
            "Install Xcode from the App Store and run:\n"
            "  sudo xcode-select -s /Applications/Xcode.app/Contents/Developer"
        )


def detect_brew_prefix(formula: str) -> Path | None:
    brew = shutil.which("brew")
    if not brew:
        return None
    res = subprocess.run(
        [brew, "--prefix", formula],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if res.returncode == 0:
        p = Path(res.stdout.strip())
        if p.exists():
            return p
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Build and package sView for macOS.")
    parser.add_argument(
        "--build-type",
        default="Release",
        choices=["Release", "Debug"],
        help="CMake build type (default: Release)",
    )
    parser.add_argument(
        "--arch",
        default=platform.machine(),
        choices=["arm64", "x86_64"],
        help="Target macOS architecture (default: host architecture)",
    )
    parser.add_argument(
        "--deployment-target",
        default="11.0",
        help="MACOSX_DEPLOYMENT_TARGET (default: 11.0)",
    )
    parser.add_argument(
        "-j", "--jobs",
        type=int,
        default=os.cpu_count() or 4,
        help="Parallel build jobs (default: CPU count)",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove build/ directory before configuring",
    )
    parser.add_argument(
        "--no-zip",
        action="store_true",
        help="Skip creating .zip archive",
    )
    parser.add_argument(
        "--dmg",
        action="store_true",
        help="Also create a .dmg disk image using hdiutil",
    )
    args = parser.parse_args()

    check_macos_prerequisites()

    repo_root = Path(__file__).resolve().parent
    build_dir = repo_root / "build"
    dist_dir = repo_root / "dist"

    if args.clean and build_dir.exists():
        print(f"Cleaning {build_dir}...")
        shutil.rmtree(build_dir)

    cmake_args = [
        "cmake",
        "-S", str(repo_root),
        "-B", str(build_dir),
        f"-DCMAKE_BUILD_TYPE={args.build_type}",
        f"-DCMAKE_OSX_ARCHITECTURES={args.arch}",
        f"-DCMAKE_OSX_DEPLOYMENT_TARGET={args.deployment_target}",
        "-DCMAKE_INSTALL_NAME_DIR=@executable_path/../Frameworks",
        "-DUSE_OPENVR=OFF",
        "-DUSE_UPDATER=OFF",
        "-DUSE_STCONFIG=OFF",
    ]

    if shutil.which("ninja"):
        cmake_args.extend(["-G", "Ninja"])

    openal_prefix = detect_brew_prefix("openal-soft")
    if openal_prefix is not None:
        cmake_args.append(f"-DCMAKE_PREFIX_PATH={openal_prefix}")

    run(cmake_args, cwd=repo_root)
    run(["cmake", "--build", str(build_dir), "--parallel", str(args.jobs)], cwd=repo_root)

    built_app = build_dir / f"{args.build_type}.app"
    if not built_app.exists():
        raise SystemExit(f"Error: Expected bundle not found at {built_app}")

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = f"{timestamp}_sview"
    dist_dir.mkdir(parents=True, exist_ok=True)

    out_app = dist_dir / f"{base_name}.app"
    if out_app.exists():
        shutil.rmtree(out_app)

    print(f"Copying {built_app} -> {out_app}")
    shutil.copytree(built_app, out_app, symlinks=True)

    outputs = [out_app]

    if not args.no_zip:
        out_zip = dist_dir / f"{base_name}.zip"
        run(["ditto", "-c", "-k", "--sequesterRsrc", "--keepParent", str(out_app), str(out_zip)])
        outputs.append(out_zip)

    if args.dmg:
        out_dmg = dist_dir / f"{base_name}.dmg"
        run([
            "hdiutil", "create",
            "-volname", "sView",
            "-srcfolder", str(out_app),
            "-ov",
            "-format", "UDZO",
            str(out_dmg),
        ])
        outputs.append(out_dmg)

    print("\nBuild & package completed successfully:")
    for item in outputs:
        print(f"  - {item}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

