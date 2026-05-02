#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: link-hermes-adapters.sh [--mode plan|apply] [--replace-existing]

Links this repo's hermes/<skill-name> adapter directories into
${HERMES_HOME:-$HOME/.hermes}/skills/software-development.

Options:
  --mode plan         Print intended changes without mutating.
  --mode apply        Apply symlink changes.
  --replace-existing  Move an existing non-symlink skill directory outside the
                      live skill tree before linking.
USAGE
}

mode="plan"
replace_existing=0

while [ "$#" -gt 0 ]; do
  case "$1" in
    --mode)
      mode="${2:-}"
      shift 2
      ;;
    --mode=*)
      mode="${1#--mode=}"
      shift
      ;;
    --replace-existing)
      replace_existing=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf 'Unknown argument: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [ "$mode" != "plan" ] && [ "$mode" != "apply" ]; then
  printf 'mode must be plan or apply\n' >&2
  exit 2
fi

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_dir="$repo_root/hermes"
hermes_home="${HERMES_HOME:-$HOME/.hermes}"
target_dir="$hermes_home/skills/software-development"
backup_root="$hermes_home/skills-legacy-backups/software-development"

if [ ! -d "$source_dir" ]; then
  printf 'Missing adapter root: %s\n' "$source_dir" >&2
  exit 1
fi

printf 'repo_root=%s\n' "$repo_root"
printf 'source_dir=%s\n' "$source_dir"
printf 'target_dir=%s\n' "$target_dir"
printf 'backup_root=%s\n' "$backup_root"
printf 'mode=%s\n' "$mode"
printf 'replace_existing=%s\n' "$replace_existing"

if [ -e "$target_dir" ] && [ ! -d "$target_dir" ]; then
  printf 'blocked=target exists but is not a directory: %s\n' "$target_dir" >&2
  exit 1
fi

if [ "$mode" = "apply" ]; then
  mkdir -p "$target_dir"
  mkdir -p "$backup_root"
fi

link_one() {
  local source_path="$1"
  local name
  local dest
  name="$(basename "$source_path")"
  dest="$target_dir/$name"

  if [ -L "$dest" ]; then
    if [ "$(readlink -f "$dest")" = "$(readlink -f "$source_path")" ]; then
      printf 'ok=%s already linked\n' "$name"
      return 0
    fi
    printf 'replace_symlink=%s old=%s new=%s\n' "$name" "$(readlink -f "$dest")" "$(readlink -f "$source_path")"
    if [ "$mode" = "apply" ]; then
      rm "$dest"
      ln -s "$source_path" "$dest"
    fi
    return 0
  fi

  if [ -e "$dest" ]; then
    if [ "$replace_existing" -ne 1 ]; then
      printf 'blocked=%s exists and is not a symlink\n' "$dest" >&2
      exit 1
    fi
    backup="$backup_root/${name}.legacy-dir-$(date -u +%Y%m%dT%H%M%SZ)"
    printf 'move_existing=%s -> %s\n' "$dest" "$backup"
    printf 'link=%s -> %s\n' "$dest" "$source_path"
    if [ "$mode" = "apply" ]; then
      mv "$dest" "$backup"
      ln -s "$source_path" "$dest"
    fi
    return 0
  fi

  printf 'link=%s -> %s\n' "$dest" "$source_path"
  if [ "$mode" = "apply" ]; then
    ln -s "$source_path" "$dest"
  fi
}

shopt -s nullglob
for skill_path in "$source_dir"/*; do
  if [ -d "$skill_path" ] && [ -f "$skill_path/SKILL.md" ]; then
    link_one "$skill_path"
  fi
done
shopt -u nullglob

if [ "$mode" = "apply" ]; then
  find "$target_dir" -maxdepth 1 -xtype l -print -quit | grep -q . && {
    printf 'blocked=broken symlink under %s\n' "$target_dir" >&2
    find "$target_dir" -maxdepth 1 -xtype l -print >&2
    exit 1
  }
fi

printf 'done\n'
