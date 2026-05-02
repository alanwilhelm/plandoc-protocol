#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: link-codex-adapters.sh [--mode plan|apply] [--convert-skills-symlink]

Links this repo's codex/<skill-name> adapter directories into
${CODEX_HOME:-$HOME/.codex}/skills.

Options:
  --mode plan                 Print intended changes without mutating.
  --mode apply                Apply symlink changes.
  --convert-skills-symlink    If ~/.codex/skills is currently a symlink, move
                              that symlink aside, create a real directory, and
                              preserve existing skills from the old target as
                              individual legacy symlinks.
USAGE
}

mode="plan"
convert_skills_symlink=0

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
    --convert-skills-symlink)
      convert_skills_symlink=1
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
source_dir="$repo_root/codex"
codex_home="${CODEX_HOME:-$HOME/.codex}"
target_dir="$codex_home/skills"

if [ ! -d "$source_dir" ]; then
  printf 'Missing adapter root: %s\n' "$source_dir" >&2
  exit 1
fi

printf 'repo_root=%s\n' "$repo_root"
printf 'source_dir=%s\n' "$source_dir"
printf 'target_dir=%s\n' "$target_dir"
printf 'mode=%s\n' "$mode"

legacy_target=""
planning_converted_target=0
if [ -L "$target_dir" ]; then
  legacy_target="$(readlink -f "$target_dir")"
  printf 'target_status=symlink legacy_target=%s\n' "$legacy_target"
  if [ "$convert_skills_symlink" -ne 1 ]; then
    printf 'blocked=target is a symlink; rerun with --convert-skills-symlink to replace it with a real directory\n'
    exit 1
  fi
  if [ "$mode" = "apply" ]; then
    backup="${target_dir}.legacy-link-$(date -u +%Y%m%dT%H%M%SZ)"
    mv "$target_dir" "$backup"
    mkdir -p "$target_dir"
    printf 'moved_legacy_symlink=%s\n' "$backup"
  else
    planning_converted_target=1
  fi
elif [ -e "$target_dir" ] && [ ! -d "$target_dir" ]; then
  printf 'blocked=target exists but is not a directory: %s\n' "$target_dir" >&2
  exit 1
else
  if [ "$mode" = "apply" ]; then
    mkdir -p "$target_dir"
  fi
fi

link_one() {
  local source_path="$1"
  local name
  local dest
  name="$(basename "$source_path")"
  dest="$target_dir/$name"

  if [ "$planning_converted_target" -eq 1 ]; then
    printf 'link_after_convert=%s -> %s\n' "$dest" "$source_path"
    return 0
  fi

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
    printf 'blocked=%s exists and is not a symlink\n' "$dest" >&2
    exit 1
  fi

  printf 'link=%s -> %s\n' "$dest" "$source_path"
  if [ "$mode" = "apply" ]; then
    ln -s "$source_path" "$dest"
  fi
}

if [ -n "$legacy_target" ] && [ -d "$legacy_target" ]; then
  shopt -s nullglob dotglob
  for legacy_path in "$legacy_target"/*; do
    name="$(basename "$legacy_path")"
    if [ "$name" = ".git" ] || [ "$name" = "." ] || [ "$name" = ".." ]; then
      continue
    fi
    if [ -d "$source_dir/$name" ] && [ -f "$source_dir/$name/SKILL.md" ]; then
      continue
    fi
    if [ "$name" != ".system" ] && [ ! -f "$legacy_path/SKILL.md" ]; then
      continue
    fi
    if [ "$planning_converted_target" -ne 1 ] && { [ -e "$target_dir/$name" ] || [ -L "$target_dir/$name" ]; }; then
      continue
    fi
    printf 'preserve_legacy=%s -> %s\n' "$target_dir/$name" "$legacy_path"
    if [ "$mode" = "apply" ]; then
      ln -s "$legacy_path" "$target_dir/$name"
    fi
  done
  shopt -u nullglob dotglob
fi

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
